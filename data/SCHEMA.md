# 字段说明

|字段|含义|
|---|---|
|id|稳定ID；P为主目录，U为独立遗忘专题参照|
|title / journal / year|原始题名、期刊和主统计年份|
|abstract_zh / abstract_type|中文摘要概述及其来源类型；Comment可能为导语概述|
|date / date_basis / issue_year|可核验日期、日期口径和卷期年；允许YYYY-MM或空值，不补造具体日|
|doi / url / source_urls|唯一DOI、原文及核验来源|
|category / topic|人工整理主题|
|catalog_group / scope_group / relevance|核心电网、交叉扩展、背景补充及关联边界|
|article_type|出版社文献类型，区分研究、综述、观点和评论|
|unlearning_class / unlearning_reason|遗忘筛查结果与依据，不等于全文不存在性证明|
|evidence_level / accessed_date / notes|核验层级、检索日期和例外说明|
|revision_added|1=旧版保留；2=本轮新增|

JSON为主数据；CSV使用UTF-8 BOM便于中文读取；Excel与JSON一致。BibTeX仅提供已核实基本字段，正式引用前应从DOI补全作者、页码与卷期。
