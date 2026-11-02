# 检索、筛查与局限

检索日期：2026年11月2日（Asia/Shanghai）。近三年按2024、2025、2026三个日历年处理，截止2026-11-02；不等于向前滚动36个月，也不覆盖尚未结束的2026全年。优先采用首次在线发表年份，个别Joule记录仅能核验卷期日/月，已逐条注明。

本报告是可复核的专题文献目录，不是WoS/Scopus全量检索的系统综述。实际使用公开网页检索、期刊官网、出版社摘要与必要的作者机构记录交叉核验；Crossref直连受网络限制，本次不声称完成其全库补检。

## 检索设计

电网词组：power grid, power system, smart grid, electricity, transmission, distribution, stability, blackout, load forecasting, demand response, energy storage, vehicle-to-grid。按期刊及2024/2025/2026拆分检索，沿相关论文补查。

遗忘词组：machine unlearning, federated unlearning, selective forgetting, concept erasure, knowledge removal, data deletion, client removal, right to be forgotten。使用单词与电网词交叉检索，并检查能源社会研究等假阳性。实际执行查询保存在data/search_log.json；上述词表是检索设计，不表示穷举执行了所有笛卡尔组合。

## 记录与质量控制

1. 候选记录依据原始期刊摘要判定电网关联；背景条目另标。
2. 按DOI去重，记录标题、期刊、年份、日期及日期依据；DOI中的年份不直接视为发表年。
3. 中文摘要由检索到的摘要或明确标注的文章概要改写，不是出版商英文摘要全文或逐字翻译。原始摘要通过链接读取。
4. 每条遗忘判定保留证据层级；多数仅完成题名与公开摘要筛查，不声称对所有订阅正文作全文排除。
5. 原创研究、Analysis、Review、Perspective、Commentary分开标注；同一论文的预印本不重复计数。
6. 日期、必填字段、DOI唯一性、数据与目录计数、内部链接及输出文件结构执行本地校验。

## 已知局限

- 网页检索排序与索引覆盖有限，未检索到不等于不存在；尤其不能把当前数量当成各刊发文普查。
- 2026年只到检索日；2023年的滚动窗口尾段未检索。
- 部分Joule条目在线首发精确日期未核验，保留卷期时间或月份并注明；Array专题参照未核验精确在线日，留空。
- 少数记录经出版商搜索索引或作者机构核验，证据来源与强度逐条注明。
- 未系统覆盖Nature Physics、Nature Electronics、主刊、PNAS或所有Cell Press刊；不能将名单外的零检索等同于零论文。
- 不分发论文PDF全文；链接的访问权限与版权由原出版方决定。

另有1篇Joule风电系统综述已核到2025卷期但首次在线年份可能为2024，暂放data/pending_candidates.json，避免混淆在线年与卷期年；另1篇IEEE电动车遗忘论文摘要尚未核实。两者不计入85条主目录及6篇专题参照。
