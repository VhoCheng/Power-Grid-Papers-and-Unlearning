"""Check data integrity and the inline-abstract GitHub presentation."""
from pathlib import Path
import csv,json,re
from collections import Counter

root=Path(__file__).resolve().parents[1]
papers=json.loads((root/'data/papers.json').read_text())
refs=json.loads((root/'data/unlearning_references.json').read_text())
summary=json.loads((root/'data/review_summary.json').read_text())
readme=(root/'README.md').read_text()
all_records=papers+refs
ids=[p['id'] for p in all_records];dois=[p['doi'].casefold() for p in all_records]
assert len(ids)==len(set(ids)),'Duplicate ID'
assert len(dois)==len(set(dois)),'Duplicate DOI'
for p in all_records:
    for k in ['id','title','abstract_zh','journal','year','doi','url','article_type','evidence_level','source_urls','abstract_type']:
        assert p.get(k),(p['id'],k)
    assert 2024<=p['year']<=2026,p['id']
    d=p.get('date')
    if d:
        assert re.fullmatch(r'\d{4}-\d{2}(?:-\d{2})?',d),(p['id'],d)
        assert d[:4]==str(p['year']),(p['id'],d,p['year'])
        assert '2024-01'<=d<='2026-11-02',(p['id'],d)
    assert readme.count(f'<a id="{p["id"]}"></a>')==1,p['id']
    assert readme.count(p['abstract_zh'])==1,('abstract not exactly once',p['id'])
    detail=root/'docs'/('CATALOG.md' if p['id'].startswith('P') else 'UNLEARNING.md')
    assert f'<a id="{p["id"]}"></a>' in detail.read_text(),p['id']
assert '<details' not in readme.lower(),'Abstracts must be expanded'
assert summary['total_records']==len(papers)
assert summary['unlearning_references']==len(refs)
assert summary['new_records']==sum(p.get('revision_added')==2 for p in papers)
assert summary['journals']==dict(Counter(p['journal'] for p in papers))
for name,rows in [('papers',papers),('unlearning_references',refs)]:
    with (root/f'data/{name}.csv').open(encoding='utf-8-sig',newline='') as f:csvrows=list(csv.DictReader(f))
    assert [p['id'] for p in csvrows]==[p['id'] for p in rows]
    for a,b in zip(csvrows,rows):
        for k in ['title','abstract_zh','journal','doi']:assert a[k]==b[k],(name,a['id'],k)
for f in root.rglob('*.md'):
    text=f.read_text()
    for dst in re.findall(r'\]\(([^)]+)\)',text):
        if dst.startswith(('http','mailto')):continue
        path,_,anchor=dst.partition('#')
        dest=(f.parent/path).resolve() if path else f
        assert dest.exists(),(f,dst)
        if anchor and re.fullmatch('[PU][0-9]+|topic-[0-9]+|journal-scope|paper-list|unlearning',anchor):
            assert f'id="{anchor}"' in dest.read_text(),(f,dst)
print(f'PASS: {len(papers)} main records + {len(refs)} references; unique DOI/ID, required fields, dates, counts, CSV, relative links, anchors and every inline abstract.')
