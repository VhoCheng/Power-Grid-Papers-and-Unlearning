# 近三年覆盖核查与局限

截至2026-11-02，主目录从85条补充为194条，新增109条。本轮合并保存221条实际网页查询记录（跨组可能重复）；逐条确认新条目的题目、日期依据与摘要或导语。**补检确实发现旧版遗漏，因此旧版不能视为完整清单；新版也不声称全库穷尽。**

## 逐刊逐年分布

下表是收录数量，不是检索召回率。0表示本目录没有收录，不能推断该刊该年未发表。

|期刊|2024|2025|2026截至11月2日|新增|
|---|---:|---:|---:|---:|
|Nature Energy|8|11|6|11|
|Nature Communications|25|32|29|58|
|Science Advances|1|2|0|0|
|Joule|8|6|6|12|
|Nature Sustainability|5|7|5|7|
|Nature Climate Change|5|4|3|5|
|Nature Machine Intelligence|0|0|0|0|
|Nature Computational Science|0|0|1|0|
|Nature Reviews Electrical Engineering|5|5|7|7|
|Communications Engineering|2|4|4|6|
|Nature Cities|0|1|2|3|

## 实际核查路径

1. 读取GitHub现有README及JSON，并确认与85条基线一致；保留旧ID。
2. 按期刊、年份和电网主题组合检索，补充近月论文，避免仅搜索“power grid”造成漏检。
3. 检查Nature官方能源网络、基础设施、供需、储能等主题目录，追查标题和DOI；主题目录只作发现入口，其标签本身不构成纳入证据。
4. 新候选优先回到出版社公开摘要；访问受限时使用作者机构存档或作者版本，保留证据等级和日期例外。
5. DOI去重，区分在线年与卷期年；同时区分原创研究、综述、观点、评论、背景材料。
6. 对机器遗忘同义词进行定向补检，审阅相关摘要和部分重点方法全文，记录直接、邻近与未见相关的区别。

## 各组审计记录

- [Nature Communications](../data/search_audits/nc.json)：实际查询、逐年覆盖、排除项与待核查项。
- [Nature Communications需求响应与市场补检](../data/search_audits/nc_supplement.json)：实际查询、逐年覆盖、排除项与待核查项。
- [Nature Energy / Joule](../data/search_audits/energy_joule.json)：实际查询、逐年覆盖、排除项与待核查项。
- [Science Advances / Nature Sustainability / Nature Climate Change / Nature Cities](../data/search_audits/science_climate.json)：实际查询、逐年覆盖、排除项与待核查项。
- [AI、工程扩展刊与遗忘同义词](../data/search_audits/extensions.json)：实际查询、逐年覆盖、排除项与待核查项。

## 仍存在的覆盖限制

- 未完成Web of Science、Scopus、Crossref或OpenAlex的全量导出与逐期枚举，无法计算可证明的召回率。
- 官方主题标签与搜索索引可能滞后；只出现在全文而不在标题/摘要中的电网案例或遗忘方法可能漏检。
- Science、Cell及IEEE部分页面存在403或机器人验证；已尽量用机构来源交叉核实，但有些候选仍保留待查。
- 2026仅覆盖截止日之前已经核实的发表记录；DOI或实验室“2026”列表不能单独证明正式发表日期。
- 本轮新增记录经过题目和公开摘要/导语核验；原85条沿用此前核验结果。本轮没有逐页重读全部原文。
- “未确认直接遗忘论文”是范围限定的发现，不能用于证明不存在或直接宣称“首次”。

## 未计入主目录的候选

- **Data centres asymmetrically exacerbate energy burdens through wholesale price increases and regressive grid cost shifting**：实验室2026清单发现，官网2026-11-02访问返回404，不能确认已在截止日前正式发表；未计入新增 [线索](https://www.peese.org/publications/)
- **Capturing the distribution of costs and benefits in electricity system planning and operations**：确认2026年Joule Commentary（卷期2026-04-15）；可见出版社文本主要为作者/项目说明，未取得足够正文/摘要以写可靠内容概述，故待补 [线索](https://www.sciencedirect.com/science/article/pii/S2542435126000711)
- **Can industrial overcapacity provide seasonal grid flexibility?**：发现近期Joule候选，未获得出版社摘要和出版日期核验；可能是NE原研究的评述 [线索](https://ouci.dntb.gov.ua/en/works/lRrbbkLK/)
- **Little to lose: The case for a robust European green hydrogen strategy**：发现综合能源系统候选，电网关联及正式摘要待进一步筛选 [线索](https://doi.org/10.1016/j.joule.2025.101974)
- **Science Advances 12, eaea1569 (2026)**：机构搜索结果出现文章编号但未取得题名与原文，机构页抓取超时；未纳入，不据此推断电网相关性。 [线索](https://www.monash.edu/energy-institute/research/publications)

已纳入但在线具体日待补的记录见[日期限定](../data/pending_candidates.json)。这些记录不重复计为未收录候选。

[返回首页](../README.md)
