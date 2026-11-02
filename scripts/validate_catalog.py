from pathlib import Path
import json,re
p=Path(__file__).resolve().parents[1]
a=json.loads((p/'data/papers.json').read_text());u=json.loads((p/'data/unlearning_references.json').read_text())
seen=set()
for x in a+u:
 for k in ['id','title','journal','year','abstract_zh','doi','url','evidence_level']:
  assert x.get(k), (x.get('id'),k)
 assert x['doi'].lower() not in seen,x['doi']
 seen.add(x['doi'].lower())
 assert 2024<=x['year']<=2026
 d=x.get('date')
 if d and re.fullmatch(r'\d{4}-\d{2}-\d{2}',d):assert d<='2026-11-02',d
 assert x['url'].startswith('https://')
text=(p/'docs/CATALOG.md').read_text()
for x in a:assert ('id="'+x['id']+'"') in text,x['id']
for f in p.rglob('*.md'):
 for dst in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if dst.startswith(('http','mailto','#')):continue
  dst=dst.split('#')[0]
  assert (f.parent/dst).exists(),(f,dst)
print(f'PASS: {len(a)} catalogue records, {len(u)} unlearning references; DOI, dates, fields, local links and anchors valid.')
