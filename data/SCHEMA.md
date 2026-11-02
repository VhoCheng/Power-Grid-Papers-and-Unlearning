# 字段说明

- `id`：编号。
- `title`：题目。
- `abstract_zh`：摘要_中文概述。
- `journal`：期刊。
- `year`：年份。
- `date`：发表日期。
- `date_basis`：日期依据。
- `issue_year`：卷期年份。
- `article_type`：文章类型。
- `catalog_group`：收录分组。
- `category`：主题分类。
- `relevance`：电网关联。
- `unlearning_class`：遗忘相关性。
- `unlearning_reason`：筛查依据。
- `doi`：DOI。
- `url`：原文链接。
- `evidence_level`：核验层级。
- `accessed_date`：检索日期。

`year`优先为在线年，未确认时按`date_basis`使用卷期年；`date`允许YYYY-MM或空值。`abstract_zh`为中文概述，非出版社原始全文。`source_urls`保留核验链接；`notes`记录更正和边界问题。BibTeX只提供已核验基本字段，未补全作者、页码，正式引用前请从DOI导出完整记录。
