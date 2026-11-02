# 电网 × 机器遗忘：专项筛查

在本次选定期刊、时间窗和已核验电网文献中，未检索到同时满足“电网应用”与“从已训练模型定向撤回数据、客户端或概念影响”的明确直接论文。这是有限公开检索的结果，不是不存在性证明，更不能据此宣称该交叉领域尚无人研究。

电力专业期刊已有直接研究，例如 [Task-Aware Machine Unlearning and Its Application in Load Forecasting](https://ieeexplore.ieee.org/abstract/document/10472091)（IEEE Transactions on Power Systems，2024）。因此更准确的选题定位是研究遗忘在特定电网场景中的新约束、机制与评价，而不是笼统宣称“首次用于电网”。

## 判定标准

- **machine unlearning / data deletion / certified removal**：有明确的待删除训练样本、用户或任务，目标是移除其对已训练模型的影响；理想参照是从未使用待删数据训练的模型。
- **federated unlearning / client removal**：从联邦全局模型中撤回某个客户端或其数据的历史训练贡献；仅不再参与后续训练不充分。
- **concept erasure / knowledge unlearning / selective forgetting**：定向移除模型中的指定概念、知识或能力，同时保持无关能力；需核对是参数/训练影响删除，还是仅推理时屏蔽。
- **相邻但不等同**：联邦学习、差分隐私、持续学习、概念漂移适应、避免灾难性遗忘、RAG知识库更新、图边物理切除、论文撤稿或社会规范的unlearning，均不能自动判作机器遗忘。

直接命中至少需要：明确的遗忘对象；清除已学习影响的训练/参数机制；删除有效性与保留能力评价。若仅包含联邦学习、隐私保护、分布漂移适应、RAG文档删除或一般在线更新，则标记为邻近，不自动视为遗忘。

## 已有邻近与范围外证据

<a id="U01"></a>
### U01 · Task-Aware Machine Unlearning and Its Application in Load Forecasting

**期刊：** IEEE Transactions on Power Systems ｜ **年份：** 2024 ｜ **日期：** 2024-03-13 ｜ **类型：** Article

**归类：** 范围外电力专业期刊 ｜ **电网关联：** 范围外电力专业期刊

**摘要（中文概述）：** 针对恶意数据或用户撤回需求，研究从已训练负荷预测器中删除指定数据影响。利用影响函数与样本重加权平衡遗忘和预测性能，并将调度、再调度成本纳入三层优化，在真实负荷数据及线性、CNN、MLP-Mixer模型上验证。

**遗忘筛查：** 直接相关。已训练负荷预测器；指定数据遗忘；下游电力调度成本评价。属于电网×机器遗忘，但不在本次大子刊名单。

**核验：** IEEE官网完整摘要、在线日期、DOI已核验。日期口径：在线发表日期。

[论文与原始摘要](https://ieeexplore.ieee.org/abstract/document/10472091) · [DOI](https://doi.org/10.1109/TPWRS.2024.3376828)

<a id="U02"></a>
### U02 · A SISA-based Machine Unlearning Framework for Power Transformer Inter-Turn Short-Circuit Fault Localization

**期刊：** 2026 IEEE Power & Energy Society General Meeting (PESGM) ｜ **年份：** 2026 ｜ **日期：** 2026-07-23 ｜ **类型：** Conference paper

**归类：** 范围外会议论文 ｜ **电网关联：** 范围外会议论文

**摘要（中文概述）：** 针对传感器故障导致的变压器诊断训练数据污染，采用分片、隔离、切片和聚合的SISA训练框架。检测到污染后只重训受影响子模型；在仿真匝间短路定位中，取得接近完整重训的准确率并减少重训时间。

**遗忘筛查：** 直接相关。删除污染诊断数据对模型的影响；是电力设备故障定位。会议论文，不属于目标期刊；arXiv初稿日期2026-03-07。

**核验：** 作者机构INL记录及arXiv作者论文摘要交叉核验。日期口径：在线发表日期。

[论文与原始摘要](https://inl.elsevierpure.com/en/publications/a-sisa-based-machine-unlearning-framework-for-power-transformer-i/) · [DOI](https://doi.org/10.1109/PESGM58988.2026.11693380)

<a id="U03"></a>
### U03 · A survey of machine unlearning for electric power systems: From privacy compliance to resilient grid operations

**期刊：** Array ｜ **年份：** 2026 ｜ **日期：** 精确日期未核验 ｜ **类型：** Survey

**归类：** 范围外期刊综述 ｜ **电网关联：** 范围外期刊综述

**摘要（中文概述）：** 面向电力系统整理精确和近似机器遗忘、验证指标及隐私扩展，讨论智能电表数据删除、SCADA/PMU污染数据清除、跨电力企业联邦遗忘和在线模型维护。提出速度与稳定性权衡、认证和审计需求；属于综述框架，不能当作四类场景均已工程验证。

**遗忘筛查：** 直接相关。综述对象明确是电力系统机器遗忘；Array不属于目标Nature/Science/Cell子刊。

**核验：** 出版商搜索索引提供题目、期刊、卷期、DOI和完整摘要；页面直接打开403。日期口径：官网检索记录为2026年9月卷31；精确在线发表日期未核验，不能以9月1日代填。。

[论文与原始摘要](https://www.sciencedirect.com/science/article/pii/S2590005626003103) · [DOI](https://doi.org/10.1016/j.array.2026.100987)

<a id="U04"></a>
### U04 · Rethinking machine unlearning for large language models

**期刊：** Nature Machine Intelligence ｜ **年份：** 2025 ｜ **日期：** 2025-02-17 ｜ **类型：** Review Article

**归类：** 目标交叉期刊，但非电网研究 ｜ **电网关联：** 目标交叉期刊，但非电网研究

**摘要（中文概述）：** 综述大语言模型遗忘的定义、方法、指标和应用，强调移除不希望保留的数据影响及相关能力，同时维护无关知识。讨论遗忘范围、数据与模型交互、多维评估，以及与模型编辑、影响函数、可解释性等领域的关系。

**遗忘筛查：** 直接相关。直接研究机器遗忘，但非电网应用；仅可作为方法论文参考，不能计入电网交叉命中。

**核验：** 期刊官网完整摘要与在线日期已核验。日期口径：在线发表日期。

[论文与原始摘要](https://www.nature.com/articles/s42256-025-00985-0) · [DOI](https://doi.org/10.1038/s42256-025-00985-0)

<a id="U05"></a>
### U05 · Mitigating algorithmic unfairness arising from forgetfulness of medical records in clinical artificial intelligence

**期刊：** Nature Communications ｜ **年份：** 2026 ｜ **日期：** 2026-05-04 ｜ **类型：** Article

**归类：** 核心期刊，但非电网研究 ｜ **电网关联：** 核心期刊，但非电网研究

**摘要（中文概述）：** 研究患者记录撤回后临床模型的公平性损失，提出以梯度正交协调遗忘与公平目标的方法。在多医院的感染筛查、死亡和休克预测数据上评估，考察删除有效性、预测能力和人群公平性的联合保持。

**遗忘筛查：** 直接相关。机器遗忘原创研究，但对象是医疗记录而非电网。

**核验：** 期刊官网搜索索引完整摘要与日期已核验。日期口径：在线发表日期。

[论文与原始摘要](https://www.nature.com/articles/s41467-026-72601-7) · [DOI](https://doi.org/10.1038/s41467-026-72601-7)

<a id="U06"></a>
### U06 · Superior resilience to poisoning and amenability to unlearning in quantum machine learning

**期刊：** Nature Communications ｜ **年份：** 2026 ｜ **日期：** 2026-03-09 ｜ **类型：** Article

**归类：** 核心期刊，但非电网研究 ｜ **电网关联：** 核心期刊，但非电网研究

**摘要（中文概述）：** 比较经典与量子神经网络对训练数据污染的响应，分析量子模型的抗噪性及近似遗忘能力。研究以污染样本为遗忘集、干净样本为保留集，对照完整重训，报告量子模型更易清除错误数据的影响。

**遗忘筛查：** 直接相关。直接研究机器遗忘，但不是电网问题；量子模型的能量等术语不能据此归为电网。

**核验：** 期刊官网完整摘要及方法已核验；2026-03-09早期在线，2026-04-23正式版本。日期口径：在线发表日期。

[论文与原始摘要](https://www.nature.com/articles/s41467-026-70420-4) · [DOI](https://doi.org/10.1038/s41467-026-70420-4)


## 待补查，不计入核验数

- [Learning and Unlearning to Operate Profitable Secure Electric Vehicle Charging](https://ieeexplore.ieee.org/document/10541863)（IEEE Transactions on Industrial Informatics，2024；DOI：10.1109/TII.2024.3396524）。作者实验室页面确认题目与刊期；IEEE页面机器人验证，未直接核验原始摘要与在线日期。仅留作补查线索，不用于严格核验文献数。

## 常见误命中

- [A conceptual analysis of gendered energy care work and epistemic injustice through a case study of Zanzibar’s Solar Mamas](https://www.nature.com/articles/s41560-024-01539-1)：Nature Energy 2024含unlearning，但指改变性别化社会规范，不是机器遗忘。
- [Federated asynchronous graph attention network with structural semantic embedding for multi-label graph classification](https://www.nature.com/articles/s41598-025-22500-6)：Scientific Reports；电网作者单位和参考文献中federated unlearning不足以证明本文研究电网遗忘。
- [Data-driven and privacy-preserving risk assessment method based on federated learning for smart grids](https://www.nature.com/articles/s44172-024-00300-6)：电网隐私保护联邦学习，但没有撤回已训练贡献的机制。

## 下一步研究方向（调研推论）

以下是本次文献交叉阅读形成的研究建议，尚不能视为已证实的新颖性：

1. **智能电表或联邦客户端撤回**：从预测模型中撤回客户历史贡献，同时约束负荷预测误差与下游调度成本；比较从头重训、SISA、影响函数或近似遗忘，并验证成员推断风险。
2. **受污染PMU/SCADA与设备诊断数据删除**：污染被发现后快速修复模型；除遗忘与保留集指标，还应评价暂态误报、漏报、约束违背及闭环稳定性。
3. **电网智能体的概念/知识撤回**：撤回过时规程、错误拓扑或危险操作知识，区分RAG库删文档与参数中知识擦除；测试提示改写后残留、重新学习、工具调用正确性及安全约束。

方法参照可从 [Rethinking machine unlearning for large language models](https://www.nature.com/articles/s42256-025-00985-0) 开始；电网应用评价应以已有IEEE负荷预测遗忘研究为基线，避免仅换数据集。

## 两篇Joule邻近论文的全文补核

电网基础模型与电力行业大语言模型两篇论文的作者全文版本已作词干搜索（unlearn / forget / delet / eras）及相关章节核对，未发现明确遗忘机制。其内容包括联邦学习、差分隐私、持续学习、RAG或训练前信息清理，均不能自动视为撤回既有学习影响。该核对不覆盖出版社最终版本全部内容及补充材料；细节、作者版本链接保存在data/unlearning_audit.json。
