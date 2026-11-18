#!/usr/bin/env python3
"""Mechanical check for numeric citations in Chinese/English plain-text or Markdown reviews."""
import argparse
import json
import re
from pathlib import Path

CITE = re.compile(r'\[\s*(\d+(?:\s*[-–—,，、]\s*\d+)*)\s*\]')
REF_HEADING = re.compile(r'^\s*#{0,6}\s*(?:参考文献|References|Bibliography)\s*[:：]?\s*$', re.M | re.I)
REF_ENTRY = re.compile(r'^\s*\[\s*(\d+)\s*\]', re.M)


def expand(value):
    nums = []
    for part in re.split(r'[,，、]', value):
        bounds = re.split(r'[-–—]', part)
        a = int(bounds[0])
        if len(bounds) == 1:
            nums.append(a)
        elif len(bounds) == 2:
            b = int(bounds[1])
            if b < a or b - a > 1000:
                raise ValueError(f'Invalid range: {part}')
            nums.extend(range(a, b + 1))
        else:
            raise ValueError(f'Invalid citation: {part}')
    return nums


def check(text):
    match = REF_HEADING.search(text)
    body = text[:match.start()] if match else text
    refs = text[match.end():] if match else ''
    order, invalid = [], []
    for m in CITE.finditer(body):
        try:
            for n in expand(m.group(1)):
                if n not in order:
                    order.append(n)
                if n < 1:
                    invalid.append(m.group(0))
        except ValueError:
            invalid.append(m.group(0))
    ref_ids = [int(n) for n in REF_ENTRY.findall(refs)]
    clean = CITE.sub('', body)
    clean = re.sub(r'^\s*#{1,6}\s+', '', clean, flags=re.M)
    han = len(re.findall(r'[\u3400-\u4dbf\u4e00-\u9fff]', clean))
    return {
        'reference_heading_found': bool(match),
        'first_appearance_order': order,
        'first_appearance_is_sequential': order == list(range(1, len(order)+1)),
        'reference_list_is_sequential': ref_ids == list(range(1, len(ref_ids)+1)),
        'missing_reference_entries': sorted(set(order)-set(ref_ids)),
        'uncited_reference_entries': sorted(set(ref_ids)-set(order)),
        'duplicate_reference_entries': sorted({n for n in ref_ids if ref_ids.count(n)>1}),
        'invalid_citations': invalid,
        'han_characters_excluding_citation_numbers': han,
        'non_whitespace_characters_excluding_citation_numbers': len(re.sub(r'\s+', '', clean)),
        'count_scope': 'All text before the reference heading, including title and abstract. Not equivalent to Word word count.',
        'limitations': 'Only checks numeric patterns; does not validate metadata, citation meaning, scientific evidence, or all citation styles.'
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('manuscript', type=Path, help='UTF-8 .md or .txt file')
    args = p.parse_args()
    result = check(args.manuscript.read_text(encoding='utf-8-sig'))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    ok = (result['reference_heading_found'] and result['first_appearance_is_sequential'] and result['reference_list_is_sequential'] and not any(result[k] for k in ('missing_reference_entries', 'uncited_reference_entries', 'duplicate_reference_entries', 'invalid_citations')))
    raise SystemExit(0 if ok else 1)

if __name__ == '__main__':
    main()
