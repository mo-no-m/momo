#!/usr/bin/env python3
"""Look up PubMed bibliographic metadata only; does not retrieve paper full text."""
import argparse, json, urllib.parse, urllib.request
BASE='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
def request(endpoint,params):
    url=BASE+endpoint+'?'+urllib.parse.urlencode(params)
    with urllib.request.urlopen(url,timeout=25) as r: return json.load(r)
def main():
    p=argparse.ArgumentParser();p.add_argument('query');p.add_argument('--limit',type=int,default=5)
    a=p.parse_args()
    term=a.query.strip()
    if term.lower().startswith('https://doi.org/'): term=term[16:]
    if term.upper().startswith('PMID:'): term=term[5:].strip()
    if term.isdigit(): term+='[uid]'
    elif term.startswith('10.') and '/' in term: term+='[aid]'
    elif term.upper().startswith('PMC'): term+='[pmcid]'
    ids=request('esearch.fcgi',{'db':'pubmed','term':term,'retmode':'json','retmax':min(max(a.limit,1),20)})['esearchresult']['idlist']
    result=request('esummary.fcgi',{'db':'pubmed','id':','.join(ids),'retmode':'json'})['result'] if ids else {}
    print(json.dumps([result[i] for i in ids],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
