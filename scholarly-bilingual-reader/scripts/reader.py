#!/usr/bin/env python3
"""Validate and render an annotated reading document. No model calls."""
import argparse, json, html, base64, subprocess
from pathlib import Path

KINDS = {'claim':'#fff09a','concept':'#ffd0d0','evidence':'#cce5ff','caveat':'#c9efcf','method':'#e5d4ff'}
def esc(x): return html.escape(str(x), quote=True)
def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))
def validate(d):
    errors=[]; seen=set()
    for k in ('title','authors','source','coverage','overview'):
        if not isinstance(d.get(k),str) or not d[k].strip(): errors.append('Missing '+k)
    if not isinstance(d.get('references'),list): errors.append('Missing references array')
    if not isinstance(d.get('sections'),list) or not d['sections']: return errors+['Missing sections']
    for s in d['sections']:
        if not s.get('title') or not s.get('paragraphs'): errors.append('Empty section')
        for p in s.get('paragraphs',[]):
            pid=p.get('id','')
            if not pid or pid in seen: errors.append('Missing or duplicate ID: '+pid)
            seen.add(pid)
            for key in ('page','en','zh','function','logic','analysis'):
                if not isinstance(p.get(key),str) or not p[key].strip(): errors.append(pid+': missing '+key)
            prev=0
            for h in sorted(p.get('highlights',[]),key=lambda h:h.get('start',-1)):
                a,b=h.get('start'),h.get('end')
                if not isinstance(a,int) or not isinstance(b,int) or not prev<=a<b<=len(p.get('en','')) or h.get('kind') not in KINDS:
                    errors.append(pid+': invalid highlight')
                else: prev=b
    for f in d.get('figures',[]):
        src=f.get('src','')
        if not any(src.startswith('data:image/'+t+';base64,') for t in ('png','jpeg','gif','webp')): errors.append('Figure must be embedded raster')
        if not f.get('alt') or not f.get('caption'): errors.append('Figure needs alt and caption')
    return errors
def marked(p):
    out=[]; prev=0; en=p['en']
    for h in sorted(p.get('highlights',[]),key=lambda x:x['start']):
        a,b=h['start'],h['end']
        out.extend([esc(en[prev:a]),'<mark style="background:'+KINDS[h['kind']]+'">'+esc(en[a:b])+'</mark>'])
        prev=b
    return ''.join(out)+esc(en[prev:])
def render(d,pdf=None):
    css='''*{box-sizing:border-box}body{font:16px/1.65 system-ui,sans-serif;color:#202c2a;margin:0;background:#f6f8f7}header,main{max-width:1350px;margin:auto;padding:22px}nav{position:sticky;top:0;background:white;padding:10px 22px;border-bottom:1px solid #ddd;z-index:2;display:flex;flex-wrap:wrap;gap:12px}nav a{color:#006b58}input{padding:8px;max-width:100%}.unit{background:white;border:1px solid #ddd;border-radius:10px;margin:16px 0;padding:18px;display:grid;grid-template-columns:1.25fr 1fr;gap:24px;scroll-margin-top:100px}.meta{grid-column:1/-1;font-size:13px;color:#526760}.en,.zh,.notes{white-space:pre-wrap;overflow-wrap:anywhere}.zh{border-top:1px solid #ddd;padding-top:12px}.notes{background:#eef5f1;padding:14px;border-radius:6px}h1,h2{color:#006b58}section{scroll-margin-top:100px}img{max-width:100%;height:auto}mark{color:#202020}[hidden]{display:none!important}@media(max-width:760px){.unit{grid-template-columns:1fr}nav{position:static}header,main{padding:12px}}'''
    out=['<!doctype html><html lang="zh"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(d['title'])+'</title><style>'+css+'</style></head><body><header><h1>'+esc(d['title'])+'</h1><p>'+esc(d['authors'])+' · '+esc(d['source'])+'</p><p>覆盖范围：'+esc(d['coverage'])+'</p><p>英文：'+ ' '.join('<mark style="background:'+v+'">'+k+'</mark>' for k,v in KINDS.items())+'</p></header><nav><input id="search" type="search" placeholder="搜索全文 / Search" aria-label="Search">']
    for i,s in enumerate(d['sections']): out.append('<a href="#s'+str(i)+'">'+esc(s['title'])+'</a>')
    out.append('<a href="#overview">论证概览</a><a href="#refs">参考文献</a></nav><main>')
    for i,s in enumerate(d['sections']):
        out.append('<section id="s'+str(i)+'"><h2>'+esc(s['title'])+'</h2>')
        for p in s['paragraphs']:
            out.append('<article class="unit" id="'+esc(p['id'])+'"><div class="meta">'+esc(p['id'])+' · '+esc(p['page'])+'</div><div><div class="en">'+marked(p)+'</div><p class="zh">'+esc(p['zh'])+'</p></div><aside class="notes"><b>段落功能</b> '+esc(p['function'])+'\n<b>逻辑位置</b> '+esc(p['logic'])+'\n<b>论证分析</b> '+esc(p['analysis'])+'</aside></article>')
        out.append('</section>')
    for f in d.get('figures',[]): out.append('<figure><a href="'+esc(f['src'])+'" target="_blank" rel="noopener"><img alt="'+esc(f['alt'])+'" src="'+esc(f['src'])+'"></a><figcaption>'+esc(f['caption'])+' '+esc(f.get('page',''))+'</figcaption></figure>')
    out.append('<h2 id="overview">论证概览</h2><p style="white-space:pre-wrap">'+esc(d['overview'])+'</p><h2 id="refs">参考文献</h2><ol>'+''.join('<li>'+esc(r)+'</li>' for r in d['references'])+'</ol>')
    if pdf: out.append('<a download="source.pdf" href="data:application/pdf;base64,'+base64.b64encode(Path(pdf).read_bytes()).decode()+'">授权原文 PDF</a>')
    out.append('</main><script>document.getElementById("search").addEventListener("input",function(){let q=this.value.toLowerCase();document.querySelectorAll(".unit").forEach(x=>x.hidden=!x.textContent.toLowerCase().includes(q));});</script></body></html>')
    return ''.join(out)
def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='cmd',required=True)
    for name in ('validate','render'):
        s=sub.add_parser(name);s.add_argument('--input',required=True);s.add_argument('--strict',action='store_true')
        if name=='render': s.add_argument('--output',required=True);s.add_argument('--pdf')
    s=sub.add_parser('inventory');s.add_argument('--pdf',required=True);s.add_argument('--out',required=True)
    a=p.parse_args()
    if a.cmd=='inventory':
        raw=subprocess.run(['pdftotext','-layout',a.pdf,'-'],check=True,capture_output=True).stdout.decode('utf-8',errors='replace')
        Path(a.out).write_text(json.dumps({'warning':'Layout text only; visually verify reading order.','pages':[{'page':i+1,'text':v} for i,v in enumerate(raw.rstrip('\f').split('\f'))]},ensure_ascii=False,indent=2),encoding='utf-8');return
    d=load(a.input); errors=validate(d)
    if errors: raise SystemExit('\n'.join(errors))
    if a.cmd=='render': Path(a.output).write_text(render(d,a.pdf),encoding='utf-8')
    print('Structural checks passed; source fidelity requires human review.')
if __name__=='__main__': main()
