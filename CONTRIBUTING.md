# 维护与上传

## 上传现有GitHub仓库

1. 解压仓库ZIP，打开`Power-Grid-Papers-and-Unlearning`目录。
2. 把该目录内的`README.md`、`docs/`、`data/`、`scripts/`等内容覆盖上传到仓库根目录；不要再套一层目录。
3. 提交后打开仓库首页，摘要应在每个条目下面直接显示。原P001—P085及其详情锚点保留。

## 新增论文

先核对DOI、出版社日期和摘要；在`data/papers.json`添加记录，分配未使用的P编号，保留来源与日期口径。摘要使用自行改写的中文概述，并按主题和遗忘关联分类。

运行`python3 scripts/render_readme.py`可从JSON重建首页。其他导出与审计表也应同步更新。运行`python3 scripts/validate_catalog.py`检查字段、重复、日期、首页摘要与本地链接。

原始论文与第三方内容的权利归原权利人；请不要把付费PDF或大段原文上传到此仓库。详细说明见[RIGHTS.md](RIGHTS.md)。
