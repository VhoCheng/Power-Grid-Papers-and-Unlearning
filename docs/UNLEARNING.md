# 电网 × 机器遗忘：专项筛查

在本次选定期刊、时间窗和已核验电网文献中，未检索到同时满足“电网应用”与“从已训练模型定向撤回数据、客户端或概念影响”的明确直接论文。这是有限公开检索的结果，不是不存在性证明，更不能据此宣称该交叉领域尚无人研究。

电力专业期刊已有直接研究，例如 [Task-Aware Machine Unlearning and Its Application in Load Forecasting](https://ieeexplore.ieee.org/abstract/document/10472091)（IEEE Transactions on Power Systems，2024）。因此更准确的选题定位是研究遗忘在特定电网场景中的新约束、机制与评价，而不是笼统宣称“首次用于电网”。

## 判定标准

- **machine unlearning / data deletion / certified removal**：有明确的待删除训练样本、用户或任务，目标是移除其对已训练模型的影响；理想参照是从未使用待删数据训练的模型。
- **federated unlearning / client removal**：从联邦全局模型中撤回某个客户端或其数据的历史训练贡献；仅不再参与后续训练不充分。
- **concept erasure / knowledge unlearning / selective forgetting**：定向移除模型中的指定概念、知识或能力，同时保持无关能力；需核对是参数/训练影响删除，还是仅推理时屏蔽。
- **相邻但不等同**：联邦学习、差分隐私、持续学习、概念漂移适应、避免灾难性遗忘、RAG知识库更新、图边物理切除、论文撤稿或社会规范的unlearning，均不能自动判作机器遗忘。

直接命中至少需要：明确的遗忘对象；清除已学习影响的训练/参数机制；删除有效性与保留能力评价。若仅包含联邦学习、隐私保护、分布漂移适应、RAG文档删除或一般在线更新，则标记为邻近，不自动视为遗忘。

## 本轮补检说明

新增条目继续按题目、公开摘要或导语筛查。智能电表联邦拆分学习、边缘充电协同、图强化学习恢复、虚假数据攻击反制均未在所读文本中定义定向删除已学习影响的目标。2026年新增NMI知识编辑观点仅属邻近方法参照，不作为电网遗忘命中。

**准确的结论是“本次范围内尚未确认”，而非“这些期刊绝对没有”。** 并未逐页通读全部全文；未公开的算法细节、不同术语以及索引滞后仍会影响检出。IEEE TII充电论文的一手摘要尚受访问限制，2026年Zenodo负荷预测联邦遗忘线索仅确认为软件复现包，均保留待核验。

## 已有直接研究与邻近参照

以下7条独立于电网主目录计数；其中含专业期刊、会议及非电网方法文献。

<a id="U01"></a>
### U01 · Task-Aware Machine Unlearning and Its Application in Load Forecasting

**期刊：** IEEE Transactions on Power Systems ｜ **年份：** 2024 ｜ **日期：** 2024-03-13 ｜ **类型：** Article

**归类：** 范围外电力专业期刊 ｜ **电网关联：** 范围外电力专业期刊

**摘要（中文概述）：** 针对恶意数据或用户撤回需求，研究从已训练负荷预测器中删除指定数据影响。利用影响函数与样本重加权平衡遗忘和预测性能，并将调度、再调度成本纳入三层优化，在真实负荷数据及线性、CNN、MLP-Mixer模型上验证。

**遗忘筛查：** 直接相关。已训练负荷预测器；指定数据遗忘；下游电力调度成本评价。属于电网×机器遗忘，但不在本次大子刊名单。

**核验：** IEEE官网完整摘要、在线日期、DOI已核验。日期口径：在线发表日期；卷期年份：2024。

[论文与来源](https://ieeexplore.ieee.org/abstract/document/10472091) · [DOI](https://doi.org/10.1109/TPWRS.2024.3376828) · [补充来源1](https://arxiv.org/abs/2308.14412) · [补充来源2](https://github.com/xuwkk/task_aware_machine_unlearning)

<a id="U02"></a>
### U02 · A SISA-based Machine Unlearning Framework for Power Transformer Inter-Turn Short-Circuit Fault Localization

**期刊：** 2026 IEEE Power & Energy Society General Meeting (PESGM) ｜ **年份：** 2026 ｜ **日期：** 2026-07-23 ｜ **类型：** Conference paper

**归类：** 范围外会议论文 ｜ **电网关联：** 范围外会议论文

**摘要（中文概述）：** 针对传感器故障导致的变压器诊断训练数据污染，采用分片、隔离、切片和聚合的SISA训练框架。检测到污染后只重训受影响子模型；在仿真匝间短路定位中，取得接近完整重训的准确率并减少重训时间。

**遗忘筛查：** 直接相关。删除污染诊断数据对模型的影响；是电力设备故障定位。会议论文，不属于目标期刊；arXiv初稿日期2026-03-07。

**核验：** 作者机构INL记录及arXiv作者论文摘要交叉核验。日期口径：在线发表日期；卷期年份：2026。

[论文与来源](https://inl.elsevierpure.com/en/publications/a-sisa-based-machine-unlearning-framework-for-power-transformer-i/) · [DOI](https://doi.org/10.1109/PESGM58988.2026.11693380) · [补充来源1](https://arxiv.org/abs/2603.06962)

<a id="U03"></a>
### U03 · A survey of machine unlearning for electric power systems: From privacy compliance to resilient grid operations

**期刊：** Array ｜ **年份：** 2026 ｜ **日期：** 精确日期未核验 ｜ **类型：** Survey

**归类：** 范围外期刊综述 ｜ **电网关联：** 范围外期刊综述

**摘要（中文概述）：** 面向电力系统整理精确和近似机器遗忘、验证指标及隐私扩展，讨论智能电表数据删除、SCADA/PMU污染数据清除、跨电力企业联邦遗忘和在线模型维护。提出速度与稳定性权衡、认证和审计需求；属于综述框架，不能当作四类场景均已工程验证。

**遗忘筛查：** 直接相关。综述对象明确是电力系统机器遗忘；Array不属于目标Nature/Science/Cell子刊。

**核验：** 出版商搜索索引提供题目、期刊、卷期、DOI和完整摘要；页面直接打开403。日期口径：官网检索记录为2026年9月卷31；精确在线发表日期未核验，不能以9月1日代填。；卷期年份：2026。

[论文与来源](https://www.sciencedirect.com/science/article/pii/S2590005626003103) · [DOI](https://doi.org/10.1016/j.array.2026.100987) · [补充来源1](https://doi.org/10.1016/j.array.2026.100987)

<a id="U04"></a>
### U04 · Rethinking machine unlearning for large language models

**期刊：** Nature Machine Intelligence ｜ **年份：** 2025 ｜ **日期：** 2025-02-17 ｜ **类型：** Review Article

**归类：** 目标交叉期刊，但非电网研究 ｜ **电网关联：** 目标交叉期刊，但非电网研究

**摘要（中文概述）：** 综述大语言模型遗忘的定义、方法、指标和应用，强调移除不希望保留的数据影响及相关能力，同时维护无关知识。讨论遗忘范围、数据与模型交互、多维评估，以及与模型编辑、影响函数、可解释性等领域的关系。

**遗忘筛查：** 直接相关。直接研究机器遗忘，但非电网应用；仅可作为方法论文参考，不能计入电网交叉命中。

**核验：** 期刊官网完整摘要与在线日期已核验。日期口径：在线发表日期；卷期年份：2025。

[论文与来源](https://www.nature.com/articles/s42256-025-00985-0) · [DOI](https://doi.org/10.1038/s42256-025-00985-0)

<a id="U05"></a>
### U05 · Mitigating algorithmic unfairness arising from forgetfulness of medical records in clinical artificial intelligence

**期刊：** Nature Communications ｜ **年份：** 2026 ｜ **日期：** 2026-05-04 ｜ **类型：** Article

**归类：** 核心期刊，但非电网研究 ｜ **电网关联：** 核心期刊，但非电网研究

**摘要（中文概述）：** 研究患者记录撤回后临床模型的公平性损失，提出以梯度正交协调遗忘与公平目标的方法。在多医院的感染筛查、死亡和休克预测数据上评估，考察删除有效性、预测能力和人群公平性的联合保持。

**遗忘筛查：** 直接相关。机器遗忘原创研究，但对象是医疗记录而非电网。

**核验：** 期刊官网搜索索引完整摘要与日期已核验。日期口径：在线发表日期；卷期年份：2026。

[论文与来源](https://www.nature.com/articles/s41467-026-72601-7) · [DOI](https://doi.org/10.1038/s41467-026-72601-7)

<a id="U06"></a>
### U06 · Superior resilience to poisoning and amenability to unlearning in quantum machine learning

**期刊：** Nature Communications ｜ **年份：** 2026 ｜ **日期：** 2026-03-09 ｜ **类型：** Article

**归类：** 核心期刊，但非电网研究 ｜ **电网关联：** 核心期刊，但非电网研究

**摘要（中文概述）：** 比较经典与量子神经网络对训练数据污染的响应，分析量子模型的抗噪性及近似遗忘能力。研究以污染样本为遗忘集、干净样本为保留集，对照完整重训，报告量子模型更易清除错误数据的影响。

**遗忘筛查：** 直接相关。直接研究机器遗忘，但不是电网问题；量子模型的能量等术语不能据此归为电网。

**核验：** 期刊官网完整摘要及方法已核验；2026-03-09早期在线，2026-04-23正式版本。日期口径：在线发表日期；卷期年份：2026。

[论文与来源](https://www.nature.com/articles/s41467-026-70420-4) · [DOI](https://doi.org/10.1038/s41467-026-70420-4)

<a id="U07"></a>
### U07 · Towards principled knowledge editing methods for large language model reasoning

**期刊：** Nature Machine Intelligence ｜ **年份：** 2026 ｜ **日期：** 2026-08-14 ｜ **类型：** Perspective

**归类：** 非电网邻近方法参照 ｜ **电网关联：** 非电网邻近方法参照

**摘要（中文概述）：** 讨论无需完整重训的大语言模型知识更新，指出把事实视为可独立编辑的模块会忽视知识之间的依赖关系，破坏多步推理与因果一致性。文章提出围绕演绎闭包回路、模型信念和置信度、情境化复杂知识开展编辑的研究方向，为持续知识适应提供原则性框架，但并不专门解决电网应用或可验证的数据遗忘。

**遗忘筛查：** 邻近但非遗忘。知识编辑可与知识撤回交叉，但本文主要研究推理一致的知识更新；不能等同于机器遗忘，也未涉及电网。

**核验：** 期刊官网摘要、类型、日期与DOI已核验。日期口径：在线发表日期；卷期年份：2026。

[论文与来源](https://www.nature.com/articles/s42256-026-01276-y) · [DOI](https://doi.org/10.1038/s42256-026-01276-y)

## 待核验线索

- **Learning and Unlearning to Operate Profitable Secure Electric Vehicle Charging**：作者实验室主页已确认题名、期刊、卷20期9页11213–11223及2024年9月；IEEE页多次返回机器人验证，未取得可读的一手摘要。 二手索引显示机器遗忘用于PV/储能充电站，但本次不根据二手摘要直接写作已核实条目；保留待核验，不得据此声称电网×遗忘仅有已收录的三篇。 [来源](https://sites.google.com/view/epssg/publications)

- **Replication Package for "Sequential Federated Unlearning for Distributed Electricity Load Forecasting: Utility versus Retraining Fidelity"**：作者发布的Zenodo软件复现包已读取，类型Software；页面未列期刊、论文DOI或正文摘要。 可作为2026新研究线索，不能将软件DOI冒充已发表期刊论文。 [来源](https://zenodo.org/records/21992940)

## 可进一步研究的问题

智能电表用户退出后的负荷预测遗忘、污染SCADA/PMU数据撤回后的运行安全、联邦模型客户端退出，以及电网基础模型中的设备或操作知识撤回，均可作为待验证方向。它们是调研提出的问题，不能从“未检出”直接推导新颖性。评估应同时关注删除效果、保留任务性能、物理约束及调度/可靠性代价。

[研究方向数据](../data/research_directions.json) · [返回首页](../README.md)
