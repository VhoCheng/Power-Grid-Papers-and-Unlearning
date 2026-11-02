"""Render the GitHub home page from the canonical JSON files (standard library only)."""
from pathlib import Path
import json
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
load=lambda f:json.loads((ROOT/'data'/f).read_text(encoding='utf-8'))
papers=load('papers.json');refs=load('unlearning_references.json');s=load('review_summary.json')
scope=load('journal_scope.json')
categories=['预测、建模与机器学习','储能、需求响应与车网互动','气候风险、韧性与可靠性','稳定性、安全与停电恢复','电网规划、互联与新能源融合','电力市场、政策与转型','可信AI、隐私与遗忘邻近','背景补充：资源、环境与转型']
counts=Counter(p['journal'] for p in papers)

text=f'''# ⚡ Power Grid Papers & Machine Unlearning

> 电网相关高水平子刊文献整理 · 2024—2026 · 更新至 {s['cutoff']} · v2 摘要直接展开版

![Records](https://img.shields.io/badge/catalogue-{len(papers)}-17324D) ![Period](https://img.shields.io/badge/years-2024--2026-167D8D) ![Unlearning](https://img.shields.io/badge/topic_references-{len(refs)}-9A6B28)

**本轮由85条补充到{len(papers)}条，新增{s['new_records']}条；每篇摘要均直接显示在条目下方，无需点击或展开。** 主目录包含{s['groups']['核心期刊电网文献']}条核心期刊电网文献、{s['groups']['交叉与扩展期刊']}条交叉与扩展期刊文献、{s['groups']['背景补充']}条背景补充；另列{len(refs)}条遗忘专题参照，独立计数。

**时间口径：** 2024-01-01—2026-11-02，按三个日历年处理，优先采用首次在线发表年；卷期年和例外单独保存。摘要为根据来源自行改写的中文概述，原始英文摘要见论文链接。无正式摘要的Comment标为“导语概述”。

**遗忘专项结论：** 在本次选定期刊、时间窗和已核验电网文献中，尚未确认“电网应用 × 定向撤回已学数据、客户端或概念影响”的直接研究。电力专业期刊已有明确研究，见下方专题参照；本次未检出不能证明不存在，也不能据此宣称“首次”。

**覆盖说明：** 第二轮通过官方主题目录、分年关键词和原文核验补齐多处遗漏，包含2026年10月新作；未完成全部数据库和逐期穷尽检索。具体范围、待核验项及访问限制见[覆盖核查](docs/COVERAGE_AUDIT.md)。

## 导航

- [和电网相关的“大子刊”](#journal-scope)
- [分类论文与逐篇摘要](#paper-list)
'''
for i,c in enumerate(categories,1):text+=f'  - [{c}](#topic-{i})\n'
text+='''- [遗忘学习、撤回学习与概念撤回](#unlearning)
- [本轮新增与更正](docs/UPDATE_2026-11-02.md) · [逐刊逐年覆盖](docs/COVERAGE_AUDIT.md) · [检索策略](docs/SEARCH_STRATEGY.md)
- 数据：[CSV](data/papers.csv) · [JSON](data/papers.json) · [Excel](data/papers.xlsx) · [BibTeX](data/references.bib)
- [逐条核验详情](docs/CATALOG.md) · [遗忘专题详情](docs/UNLEARNING.md) · [上传与维护](CONTRIBUTING.md)

<a id="journal-scope"></a>
## 和电网相关的“大子刊”

“大子刊”没有统一官方定义。优先关注 **Nature Energy、Nature Communications、Joule、Science Advances、Nature Sustainability、Nature Climate Change**；电网AI方法可交叉关注NMI与NCS，综述可关注NREE。以下“核心/扩展”是本次检索分组，不是官方期刊等级，扩展刊不默认与核心六刊处于同一层级。

|期刊|本次角色|相关方向|本目录条数|
|---|---|---|---:|
'''
for j in scope:text+=f'|[{j["journal"]}]({j["url"]})|{j["role"]}|{j["description"]}|{counts[j["journal"]]}|\n'
text+='''
条数含该刊背景补充；不是该刊全部电网发文量。NMI的非电网遗忘/知识编辑参照独立列示。Nature Cities为本轮定向扩展，其他潜在相关刊与排除边界见[期刊范围](docs/JOURNALS.md)。

<a id="paper-list"></a>
## 分类论文与逐篇摘要

组内按日期倒序。📘为研究/分析，📚为综述/观点/评论；类型以逐条标注为准。`邻近但非遗忘`表示广义AI、隐私或可信计算背景，不表示已提出遗忘算法。旧编号P001—P085保留，`本轮新增`从P086开始。

'''
def card(p,reference=False):
    kind=p.get('article_type','')
    icon='📚' if any(k in kind.lower() for k in ['review','survey','perspective','comment']) else '📘'
    q=f'<a id="{p["id"]}"></a>\n\n- {icon} **[{p["year"]} · {p["journal"]}] [{p["title"]}]({p["url"]})** · `{p["id"]}`'
    if p.get('revision_added')==2:q+=' · `本轮新增`'
    q+='\n\n'
    q+=f'  **发表：** {p.get("date") or "精确日期未核验"}（{p.get("date_basis","见核验详情")}） · **类型：** {kind} · **范围：** {p.get("catalog_group",p.get("scope",""))}\n\n'
    at=p.get('abstract_type','')
    label='内容概述（出版社导语，无正式摘要）' if '无正式摘要' in at else '内容概述（作者机构说明）' if '作者机构内容说明' in at else '内容概述（导语或机构摘要）' if '内容概述' in at else '摘要（中文概述）'
    q+=f'  **{label}：** {p["abstract_zh"]}\n\n'
    if reference or p.get('unlearning_class')=='邻近但非遗忘':q+=f'  **遗忘筛查：** {p["unlearning_class"]}。{p.get("unlearning_reason",p.get("reason",""))}\n\n'
    if p.get('notes') and p['notes']!='第二轮补检新增。':q+=f'  **备注：** {p["notes"].removeprefix("第二轮补检新增。 ")}\n\n'
    dest='UNLEARNING' if reference else 'CATALOG'
    q+=f'  [DOI](https://doi.org/{p["doi"]}) · [核验与筛查依据](docs/{dest}.md#{p["id"]})\n\n'
    return q
for i,c in enumerate(categories,1):
    group=sorted([p for p in papers if p['category']==c],key=lambda p:(p.get('date') or str(p['year']),p['title']),reverse=True)
    text+=f'<a id="topic-{i}"></a>\n### {c}（{len(group)}条）\n\n'
    text+=''.join(card(p) for p in group)
    text+='[返回导航](#导航)\n\n'
text+='''<a id="unlearning"></a>
## 遗忘学习、撤回学习与概念撤回

这里按研究目标判断，而不只看术语：是否有明确待撤回的样本、客户端、任务、知识或概念；是否移除其对已训练模型的影响；是否评估删除有效性及其他能力的保留。

- **可算直接相关：** 机器遗忘、联邦遗忘、认证删除、定向概念或知识移除，且符合上述目标。
- **不能自动等同：** 联邦学习、差分隐私、在线更新、概念漂移、避免灾难性遗忘、推理时屏蔽、RAG文档删除、物理线路切除、论文撤稿。
- **本次结论：** 主目录尚未确认直接交叉命中；下面前三条说明电力系统领域已有专业期刊/会议研究。U04—U06是目标刊中的非电网遗忘参照，U07是非电网知识编辑邻近参照。

### 已有直接电力研究与综述（范围外）

'''
for p in refs[:3]:text+=card(p,True)
text+='### 非电网遗忘方法参照\n\n'
for p in refs[3:6]:text+=card(p,True)
text+='### 非电网知识编辑邻近方向\n\n'
for p in refs[6:]:text+=card(p,True)
text+='''### 尚待核验

IEEE TII的[Learning and Unlearning to Operate Profitable Secure Electric Vehicle Charging](https://doi.org/10.1109/TII.2024.3396524)已确认题名与刊期，但一手摘要仍受访问限制；2026年“Sequential Federated Unlearning for Distributed Electricity Load Forecasting”目前只核实到[软件复现包](https://zenodo.org/records/21992940)，不能冒充正式期刊论文。两者不计入已核验论文数，详见[待核验记录](data/pending_candidates.json)。

## 数据与使用

全文元数据在`data/papers.json`，每条含题目、摘要、期刊、年份、DOI、来源和筛查理由。可使用页面搜索按年份、期刊、主题或ID定位。新旧数量、日期例外及检索边界见[更新记录](docs/UPDATE_2026-11-02.md)和[覆盖核查](docs/COVERAGE_AUDIT.md)。

解压仓库包后，将内部文件直接上传到GitHub仓库根目录即可，操作见[维护说明](CONTRIBUTING.md)。本仓库不打包论文PDF；原论文权利归原权利人，中文概述仅供文献导航。正式引用前请阅读原文并核对完整书目信息。
'''
(ROOT/'README.md').write_text(text,encoding='utf-8')
print(f'README rendered: {len(papers)} main entries + {len(refs)} references; {len(text.encode("utf-8")):,} bytes')
