# ⚡ Power Grid Papers & Machine Unlearning

> 电网相关高水平子刊文献整理 · 2024—2026 · 更新至 2026-11-02 · v2 摘要直接展开版

![Records](https://img.shields.io/badge/catalogue-194-17324D) ![Period](https://img.shields.io/badge/years-2024--2026-167D8D) ![Unlearning](https://img.shields.io/badge/topic_references-7-9A6B28)

**本轮由85条补充到194条，新增109条；每篇摘要均直接显示在条目下方，无需点击或展开。** 主目录包含144条核心期刊电网文献、30条交叉与扩展期刊文献、20条背景补充；另列7条遗忘专题参照，独立计数。

**时间口径：** 2024-01-01—2026-11-02，按三个日历年处理，优先采用首次在线发表年；卷期年和例外单独保存。摘要为根据来源自行改写的中文概述，原始英文摘要见论文链接。无正式摘要的Comment标为“导语概述”。

**遗忘专项结论：** 在本次选定期刊、时间窗和已核验电网文献中，尚未确认“电网应用 × 定向撤回已学数据、客户端或概念影响”的直接研究。电力专业期刊已有明确研究，见下方专题参照；本次未检出不能证明不存在，也不能据此宣称“首次”。

**覆盖说明：** 第二轮通过官方主题目录、分年关键词和原文核验补齐多处遗漏，包含2026年10月新作；未完成全部数据库和逐期穷尽检索。具体范围、待核验项及访问限制见[覆盖核查](docs/COVERAGE_AUDIT.md)。

## 导航

- [和电网相关的“大子刊”](#journal-scope)
- [分类论文与逐篇摘要](#paper-list)
  - [预测、建模与机器学习](#topic-1)
  - [储能、需求响应与车网互动](#topic-2)
  - [气候风险、韧性与可靠性](#topic-3)
  - [稳定性、安全与停电恢复](#topic-4)
  - [电网规划、互联与新能源融合](#topic-5)
  - [电力市场、政策与转型](#topic-6)
  - [可信AI、隐私与遗忘邻近](#topic-7)
  - [背景补充：资源、环境与转型](#topic-8)
- [遗忘学习、撤回学习与概念撤回](#unlearning)
- [本轮新增与更正](docs/UPDATE_2026-11-02.md) · [逐刊逐年覆盖](docs/COVERAGE_AUDIT.md) · [检索策略](docs/SEARCH_STRATEGY.md)
- 数据：[CSV](data/papers.csv) · [JSON](data/papers.json) · [Excel](data/papers.xlsx) · [BibTeX](data/references.bib)
- [逐条核验详情](docs/CATALOG.md) · [遗忘专题详情](docs/UNLEARNING.md) · [上传与维护](CONTRIBUTING.md)

<a id="journal-scope"></a>
## 和电网相关的“大子刊”

“大子刊”没有统一官方定义。优先关注 **Nature Energy、Nature Communications、Joule、Science Advances、Nature Sustainability、Nature Climate Change**；电网AI方法可交叉关注NMI与NCS，综述可关注NREE。以下“核心/扩展”是本次检索分组，不是官方期刊等级，扩展刊不默认与核心六刊处于同一层级。

|期刊|本次角色|相关方向|本目录条数|
|---|---|---|---:|
|[Nature Energy](https://www.nature.com/nenergy/aims)|核心|能源系统、供需灵活性、电网市场与低碳转型|25|
|[Nature Communications](https://www.nature.com/ncomms/aims)|核心|电网控制、预测、规划、安全、储能与气候风险|86|
|[Science Advances](https://www.science.org/journal/sciadv)|核心|具有广泛科学或工程意义的电力系统研究|3|
|[Joule](https://www.cell.com/joule/aims)|核心|Cell Press能源期刊；能源系统、储能、电网融合及政策|20|
|[Nature Sustainability](https://www.nature.com/natsustain/aims)|核心|电力转型、资源约束、环境影响、公平与可持续规划|17|
|[Nature Climate Change](https://www.nature.com/nclimate/aims)|核心|气候对电力供需、极端事件、适应和减缓的影响|12|
|[Nature Machine Intelligence](https://www.nature.com/natmachintell/aims)|交叉方向|通用AI与遗忘方法；本次主目录未确认电网研究|0|
|[Nature Computational Science](https://www.nature.com/natcomputsci/aims)|交叉方向|计算方法、复杂动力系统及电网验证案例|1|
|[Nature Reviews Electrical Engineering](https://www.nature.com/natrevelectreng/aims)|综述扩展|电力系统与电气工程综述、观点及评论|17|
|[Communications Engineering](https://www.nature.com/commseng/aims)|工程扩展|微电网、控制、保护、配电规划与工程AI|10|
|[Nature Cities](https://www.nature.com/natcities/aims)|城市交叉扩展|城市供电质量、负荷与跨城电力影响；本轮定向补充|3|

条数含该刊背景补充；不是该刊全部电网发文量。NMI的非电网遗忘/知识编辑参照独立列示。Nature Cities为本轮定向扩展，其他潜在相关刊与排除边界见[期刊范围](docs/JOURNALS.md)。

<a id="paper-list"></a>
## 分类论文与逐篇摘要

组内按日期倒序。📘为研究/分析，📚为综述/观点/评论；类型以逐条标注为准。`邻近但非遗忘`表示广义AI、隐私或可信计算背景，不表示已提出遗忘算法。旧编号P001—P085保留，`本轮新增`从P086开始。

<a id="topic-1"></a>
### 预测、建模与机器学习（18条）

<a id="P009"></a>

- 📘 **[2026 · Nature Communications] [Electricity load forecasting under extreme heat and cold waves](https://www.nature.com/articles/s41467-026-77014-0)** · `P009`

  **发表：** 2026-08-21（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对热浪寒潮样本少、常规预测模型难以外推的问题，提出合成极端场景并分离可靠需求信号的方法。在六个地区的80组实际数据上降低负荷预测误差，为极端天气下供需平衡提供提前量。合成样本及信号筛选不等同于删除已训练模型中的指定知识。

  **遗忘筛查：** 邻近但非遗忘。涉及AI建模、信息筛选或隐私保护，但所读摘要未定义遗忘对象、删除目标及删除有效性验证。

  [DOI](https://doi.org/10.1038/s41467-026-77014-0) · [核验与筛查依据](docs/CATALOG.md#P009)

<a id="P174"></a>

- 📘 **[2026 · Nature Cities] [Divergent humidity-driven growth in urban air-conditioning energy demand under climate change](https://www.nature.com/articles/s44284-026-00474-4)** · `P174` · `本轮新增`

  **发表：** 2026-07-24（出版社在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 研究将改进的城市建筑能源模型与全球地球系统模型耦合，区分空调制冷与除湿负荷，分析温度和湿度共同变化对城市需求的影响。在高排放情景下，全球城市除湿用能增加47%，但其在总空调负荷中的占比呈区域分化。相近温度下，潮湿日的需求可达到非潮湿日的两至三倍，提示只依据气温预测负荷可能漏判峰值，电力基础设施规划应纳入湿度。

  [DOI](https://doi.org/10.1038/s44284-026-00474-4) · [核验与筛查依据](docs/CATALOG.md#P174)

<a id="P119"></a>

- 📘 **[2026 · Nature Communications] [A probabilistic forecasting framework for neighbourhood-level disaggregation of electric vehicle adoption scenarios](https://www.nature.com/articles/s41467-026-74155-0)** · `P119` · `本轮新增`

  **发表：** 2026-06-13（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 为配电网投资提供社区尺度的电动汽车普及率预测，将地方车辆登记数据与区域情景相结合，利用高斯过程生成带不确定区间的细粒度预测。英国十个地区、1294个社区的验证显示，该方法在较长预测跨度下改善误差与区间校准，有助于识别低压网络潜在承载风险。

  **遗忘筛查：** 邻近但非遗忘。涉及预测、智能建模或优化，但所读摘要未定义遗忘对象、删除已学习影响的目标及有效性验证。

  [DOI](https://doi.org/10.1038/s41467-026-74155-0) · [核验与筛查依据](docs/CATALOG.md#P119)

<a id="P120"></a>

- 📘 **[2026 · Nature Communications] [Rethinking the use of deep learning methods for photovoltaic power forecasting](https://www.nature.com/articles/s41467-026-73817-3)** · `P120` · `本轮新增`

  **发表：** 2026-06-12（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 重新评估光伏预测中历史观测与未来天气信息的融合方式，提出带多尺度编码、通道相关注意力和层级交叉解码的Cross-Unet模型。在中国与澳大利亚多个电站、不同天气预报来源及预测时长上验证，展示15分钟分辨率、数小时到一周预测对调度和交易的支持作用。

  **遗忘筛查：** 邻近但非遗忘。涉及预测、智能建模或优化，但所读摘要未定义遗忘对象、删除已学习影响的目标及有效性验证。

  [DOI](https://doi.org/10.1038/s41467-026-73817-3) · [核验与筛查依据](docs/CATALOG.md#P120)

<a id="P124"></a>

- 📘 **[2026 · Nature Communications] [Digital twin-driven fault diagnosis of power substations by multi-modal fusion learning](https://www.nature.com/articles/s41467-026-73483-5)** · `P124` · `本轮新增`

  **发表：** 2026-05-20（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 提出数字孪生支持的变电站多模态故障诊断方法，用图注意力和自注意力融合拓扑、告警、故障波形及SCADA测量。基于110千伏变电站仿真场景验证故障位置、类型和保护失效识别，并分析缺测条件下的鲁棒性，为变电站在线诊断与实际部署提供框架。

  **遗忘筛查：** 邻近但非遗忘。涉及预测、智能建模或优化，但所读摘要未定义遗忘对象、删除已学习影响的目标及有效性验证。

  [DOI](https://doi.org/10.1038/s41467-026-73483-5) · [核验与筛查依据](docs/CATALOG.md#P124)

<a id="P072"></a>

- 📘 **[2026 · Communications Engineering] [Diffusion model-based parameter estimation in dynamic power systems](https://www.nature.com/articles/s44172-026-00670-z)** · `P072`

  **发表：** 2026-04-30（在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 针对动态电力系统参数反演不唯一问题，构建联合条件扩散模型，以多组观测约束参数后验分布。复合负荷模型实验显示，相对单条件模型参数误差降低58.6%，并可较准确复现不同电气故障下的动态响应。

  **遗忘筛查：** 邻近但非遗忘。利用扩散模型求解反问题，未涉及概念擦除或数据撤回。

  [DOI](https://doi.org/10.1038/s44172-026-00670-z) · [核验与筛查依据](docs/CATALOG.md#P072)

<a id="P126"></a>

- 📘 **[2026 · Nature Communications] [Lightweight vision architecture deployed in the terminal for safety monitoring and early warning of transmission lines](https://www.nature.com/articles/s41467-026-72321-y)** · `P126` · `本轮新增`

  **发表：** 2026-04-25（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对输电走廊危险物体侵入预警，提出可部署于终端的轻量视觉架构，融合目标检测、姿态估计、深度转换和点云重建。方法同时识别危险目标与其相对导线的安全距离，在复杂地形下进行三维感知，并通过终端人工智能平台和现场摄像设备验证部署适应性。

  **遗忘筛查：** 邻近但非遗忘。涉及预测、智能建模或优化，但所读摘要未定义遗忘对象、删除已学习影响的目标及有效性验证。

  [DOI](https://doi.org/10.1038/s41467-026-72321-y) · [核验与筛查依据](docs/CATALOG.md#P126)

<a id="P002"></a>

- 📘 **[2026 · Nature Communications] [Probabilistic day-ahead forecasting of system-level renewable energy and electricity demand](https://www.nature.com/articles/s41467-026-69015-w)** · `P002`

  **发表：** 2026-02-28（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 构建系统级可再生发电与电力需求的联合概率日前预测方法，结合公开天气信息、机器学习特征选择和概率模型，并采用适当评分规则评价。在加州电力市场分区实验中改进预测表现，联合分布还可支持更有效的运行备用配置。

  **遗忘筛查：** 邻近但非遗忘。涉及AI建模、信息筛选或隐私保护，但所读摘要未定义遗忘对象、删除目标及删除有效性验证。

  [DOI](https://doi.org/10.1038/s41467-026-69015-w) · [核验与筛查依据](docs/CATALOG.md#P002)

<a id="P190"></a>

- 📘 **[2026 · Communications Engineering] [Adaptive hierarchical learning for uncertainty-aware distributed energy resource planning](https://www.nature.com/articles/s44172-026-00591-x)** · `P190` · `本轮新增`

  **发表：** 2026-01-23（在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 针对分布式能源规划中不确定性及第三方无法完整获知电网安全约束的问题，提出自适应分层学习框架，联合决定选址、容量和运行策略。上层采用蒙特卡洛树搜索开展规划，下层以多智能体强化学习处理部分可观测运行。基准系统与实际配电网算例用于评估投资、计算效率和电压稳定性。

  **遗忘筛查：** 邻近但非遗忘。自适应与强化学习用于规划运行，没有指定遗忘集、删除机制或遗忘验证。

  [DOI](https://doi.org/10.1038/s44172-026-00591-x) · [核验与筛查依据](docs/CATALOG.md#P190)

<a id="P001"></a>

- 📘 **[2026 · Nature Communications] [Computationally efficient tail distribution-aware large-scale power system overloading risk assessment](https://www.nature.com/articles/s41467-025-68241-y)** · `P001`

  **发表：** 2026-01-05（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对新能源和负荷不确定性下的大规模电网过载风险，构建深核稀疏多输出高斯过程潮流代理，并在阈值附近自适应重采样修正偏差。新英格兰两万余节点系统实验显示，相对蒙特卡洛基准显著加速风险计算，同时保留尾部分布风险刻画能力。

  **遗忘筛查：** 邻近但非遗忘。涉及AI建模、信息筛选或隐私保护，但所读摘要未定义遗忘对象、删除目标及删除有效性验证。

  **备注：** DOI含2025但在线发表日期为2026-01-05，按2026统计。

  [DOI](https://doi.org/10.1038/s41467-025-68241-y) · [核验与筛查依据](docs/CATALOG.md#P001)

<a id="P016"></a>

- 📘 **[2025 · Nature Communications] [Deep learning predicts real-world electric vehicle direct current charging profiles and durations](https://www.nature.com/articles/s41467-025-65970-y)** · `P016`

  **发表：** 2025-12-05（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用大规模真实直流快充会话训练深度学习模型，从少量充电功率和荷电状态观测预测充电曲线、持续时间及不确定性。模型可随新增观测更新预测，并跨车型和场景泛化，为充电设施运营及用电规划提供依据；这里的实时更新并非撤回已学习信息。

  **遗忘筛查：** 邻近但非遗忘。涉及AI建模、信息筛选或隐私保护，但所读摘要未定义遗忘对象、删除目标及删除有效性验证。

  [DOI](https://doi.org/10.1038/s41467-025-65970-y) · [核验与筛查依据](docs/CATALOG.md#P016)

<a id="P015"></a>

- 📘 **[2025 · Nature Communications] [Data-driven dynamic modeling for inverter-based resources using neural networks](https://www.nature.com/articles/s41467-025-66604-z)** · `P015`

  **发表：** 2025-11-28（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 面向逆变器型资源的复杂动态，组合长短期记忆网络、交叉层和物理约束，从可获取数据学习动态模型。在真实风电、光伏和构网型电池系统及更大电网测试中提高建模精度，并检验分布外泛化，为新能源高占比电网暂态稳定评估提供模型。

  **遗忘筛查：** 邻近但非遗忘。涉及AI建模、信息筛选或隐私保护，但所读摘要未定义遗忘对象、删除目标及删除有效性验证。

  [DOI](https://doi.org/10.1038/s41467-025-66604-z) · [核验与筛查依据](docs/CATALOG.md#P015)

<a id="P192"></a>

- 📘 **[2025 · Communications Engineering] [Voltage regulation in PV-rich distribution networks: an edge pipelined intelligent computing approach](https://www.nature.com/articles/s44172-025-00535-x)** · `P192` · `本轮新增`

  **发表：** 2025-11-26（在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 面向高比例光伏配电网的电压调节，提出部署于数字化边缘站的智能计算框架。通过共享权重神经网络表示不同控制动作，并以流水线并行组织多层计算，降低模型存储和计算开销。研究评估电压越限抑制与执行效率，也考察通信故障和部分观测下的适用性，为分布式电压控制提供实现途径。

  **遗忘筛查：** 邻近但非遗忘。神经网络压缩和边缘推理降低资源需求，并非删除训练数据影响。

  [DOI](https://doi.org/10.1038/s44172-025-00535-x) · [核验与筛查依据](docs/CATALOG.md#P192)

<a id="P074"></a>

- 📘 **[2025 · Communications Engineering] [Scalable reinforcement learning for large-scale coordination of electric vehicles using graph neural networks](https://www.nature.com/articles/s44172-025-00457-8)** · `P074`

  **发表：** 2025-07-01（在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 面向城市规模电动汽车充电协调，提出 EV-GNN，将端到端图神经网络与强化学习结合，并通过分支剪枝提高可扩展性和样本效率。实验考察多类动作空间、充电情景与规模，显示相对强化学习基线的泛化和协调优势。

  **遗忘筛查：** 邻近但非遗忘。分支剪枝用于缩减充电决策问题；不是删除训练数据或客户端的影响。

  [DOI](https://doi.org/10.1038/s44172-025-00457-8) · [核验与筛查依据](docs/CATALOG.md#P074)

<a id="P152"></a>

- 📘 **[2025 · Nature Communications] [A machine learning model for hub-height short-term wind speed prediction](https://www.nature.com/articles/s41467-025-58456-4)** · `P152` · `本轮新增`

  **发表：** 2025-04-03（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 提出融合多种气象变量的短期风速预测网络，以东北地区为例开展轮毂高度、细网格风矢量预测。模型在前六小时预测中优于所比较的数值天气基准，并通过异地迁移和计算效率实验。成果可用于区域风电中心的超短期及短期部署决策，属于电源预测相关方法。

  **遗忘筛查：** 邻近但非遗忘。涉及预测、智能建模或优化，但所读摘要未定义遗忘对象、删除已学习影响的目标及有效性验证。

  [DOI](https://doi.org/10.1038/s41467-025-58456-4) · [核验与筛查依据](docs/CATALOG.md#P152)

<a id="P053"></a>

- 📘 **[2024 · Science Advances] [Potential climate predictability of renewable energy supply and demand for Texas given the ENSO hidden state](https://www.science.org/doi/10.1126/sciadv.ado3517)** · `P053`

  **发表：** 2024-11-01（在线发表日期） · **类型：** Research Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究以非齐次隐马尔可夫模型识别热带太平洋海表温度对应的ENSO隐状态，预测得克萨斯州未来1—6个月的风能、太阳能以及采暖制冷需求。不同ENSO状态与月份对应显著不同的供电过剩、短缺和需求异常概率。论文讨论了这种季节尺度可预测性对系统规划、气候风险管理和金融风险工具的意义。

  **遗忘筛查：** 邻近但非遗忘。隐马尔可夫预测模型学习气候—能源关系；没有撤回训练样本、客户端或概念的目标。

  [DOI](https://doi.org/10.1126/sciadv.ado3517) · [核验与筛查依据](docs/CATALOG.md#P053)

<a id="P187"></a>

- 📚 **[2024 · Joule] [Opportunities for quantum computing within net-zero power system optimization](https://doi.org/10.1016/j.joule.2024.03.020)** · `P187` · `本轮新增`

  **发表：** 2024-04-22（在线发表日期） · **类型：** Review · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 综述量子计算在净零电力系统规划和运行优化中的机会，覆盖机组组合、网侧灵活性协调、网络扩张、仿真、凸优化及机器学习辅助优化。论文讨论潜在计算加速与规模提升，也强调行业级应用仍面临算法、硬件噪声和扩展性限制。提出建立问题基准和性能标准，开发面向具体场景的算法，并将量子与经典计算纳入统一技术路线。

  [DOI](https://doi.org/10.1016/j.joule.2024.03.020) · [核验与筛查依据](docs/CATALOG.md#P187)

<a id="P018"></a>

- 📘 **[2024 · Nature Communications] [Higher-order Granger reservoir computing: simultaneously achieving scalable complex structures inference and accurate dynamics prediction](https://www.nature.com/articles/s41467-024-46852-1)** · `P018`

  **发表：** 2024-03-20（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 提出结合高阶Granger结构推断与储备池计算的HoGRC方法，同步识别复杂系统高阶相互作用并执行多步动态预测。在混沌系统、网络动力学及英国电网结构上的动力系统算例中验证效果。电网是验证场景之一，不能等同于已在实际运行电网部署。

  **遗忘筛查：** 邻近但非遗忘。涉及AI建模、信息筛选或隐私保护，但所读摘要未定义遗忘对象、删除目标及删除有效性验证。

  [DOI](https://doi.org/10.1038/s41467-024-46852-1) · [核验与筛查依据](docs/CATALOG.md#P018)

[返回导航](#导航)

<a id="topic-2"></a>
### 储能、需求响应与车网互动（36条）

<a id="P093"></a>

- 📚 **[2026 · Nature Reviews Electrical Engineering] [Urban building energy modelling in the electrification era](https://www.nature.com/articles/s44287-026-00348-w)** · `P093` · `本轮新增`

  **发表：** 2026-10-29（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 综述城市建筑群能源建模如何应对气候变化和电气化。建筑逐渐由被动用能者转为可与电网互动的资源，要求模型刻画建筑、交通与电网耦合、气候风险及多类型负荷。文章讨论人工智能、数据隐私与验证不足等挑战，并展望模型用于预测电网压力、热浪健康保护和公平投资决策的方向。

  **遗忘筛查：** 邻近但非遗忘。提及数据隐私和AI建模，但没有训练数据撤回或概念删除方法。

  [DOI](https://doi.org/10.1038/s44287-026-00348-w) · [核验与筛查依据](docs/CATALOG.md#P093)

<a id="P111"></a>

- 📘 **[2026 · Nature Communications] [Transforming electrified railway into mechanical energy storage for electricity system decarbonization](https://www.nature.com/articles/s41467-026-78711-6)** · `P111` · `本轮新增`

  **发表：** 2026-10-19（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 把电气化铁路的牵引与再生制动视为可调节的机械储能资源，通过协调列车运行与电力系统交换能量。基于大量站间运行数据估算其潜力，并在中国、欧洲和印度的容量扩展模型中检验。结果显示，该资源可减少专用储能建设需求，在不增加总成本的情况下进一步降低排放。

  **备注：** 已同行评议并接收，提前在线发表；截至检索日尚待正式Version of Record，卷期年份未核实。

  [DOI](https://doi.org/10.1038/s41467-026-78711-6) · [核验与筛查依据](docs/CATALOG.md#P111)

<a id="P112"></a>

- 📘 **[2026 · Nature Communications] [Unlocking electric vehicle flexibility in microgrids via lightweight on-charger coordination](https://www.nature.com/articles/s41467-026-78319-w)** · `P112` · `本轮新增`

  **发表：** 2026-10-17（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 将电动车充电器转变为能够自主协调的边缘智能节点，在硬件资源受限条件下开展分布式充电优化。高保真微电网硬件在环实验表明，框架显著降低存储和通信开销，并通过释放车辆灵活性改善经济收益，为可再生能源丰富的微电网提供车网协同方式。

  **遗忘筛查：** 邻近但非遗忘。边缘智能和分布式充电优化，摘要未说明定向删除样本、客户端或概念影响。

  **备注：** 已同行评议并接收，提前在线发表；截至检索日尚待正式Version of Record，卷期年份未核实。

  [DOI](https://doi.org/10.1038/s41467-026-78319-w) · [核验与筛查依据](docs/CATALOG.md#P112)

<a id="P007"></a>

- 📘 **[2026 · Nature Communications] [Facilitating megacity electricity decarbonization via grid-interactive demand-side resource management](https://www.nature.com/articles/s41467-026-76799-4)** · `P007`

  **发表：** 2026-08-17（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 建立从社区到电网的需求侧资源评估框架，利用深圳建筑、屋顶光伏及电动汽车出行充电信息，估计超大城市缓解供需错配的能力。在设定的高零碳电力情景中，调节需求可显著减少周度供电缺口；行政公平与缓解效率两种目标对应不同的电网改造布局。

  [DOI](https://doi.org/10.1038/s41467-026-76799-4) · [核验与筛查依据](docs/CATALOG.md#P007)

<a id="P103"></a>

- 📘 **[2026 · Nature Energy] [Coordinated planning of European charging infrastructure and energy system for optimal V1G and V2G deployment](https://www.nature.com/articles/s41560-026-02107-5)** · `P103` · `本轮新增`

  **发表：** 2026-07-14（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 把充电基础设施成本内生纳入欧洲能源系统优化，对比无序充电、单向智能充电与双向车网互动的竞争和互补关系。单向智能充电贡献大部分系统成本节约，双向充电的额外系统收益较小，但可提供可观的平衡市场价值。不同地区的风光结构、输电限制和供电稀缺程度影响最优部署，统一的欧洲充电指标可能高估或低估局部需求。

  [DOI](https://doi.org/10.1038/s41560-026-02107-5) · [核验与筛查依据](docs/CATALOG.md#P103)

<a id="P175"></a>

- 📘 **[2026 · Nature Cities] [Intercity inequality in carbon emission reductions from vehicle electrification in China](https://www.nature.com/articles/s44284-026-00465-5)** · `P175` · `本轮新增`

  **发表：** 2026-06-24（出版社在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 研究结合逾2.45亿条车辆登记记录与电网运行系统，追踪中国285座城市电动汽车用电引起的跨城碳转移。2020年，经济较发达城市将41.8%的相关排放转移至较欠发达城市，后者承担更高的减排成本。预计2030年前城市间差异仍较突出，之后随电网脱碳而减弱。结果强调评估电动汽车减排需考虑电力调度、跨城交换与发电地责任。

  [DOI](https://doi.org/10.1038/s44284-026-00465-5) · [核验与筛查依据](docs/CATALOG.md#P175)

<a id="P086"></a>

- 📘 **[2026 · Nature Sustainability] [Rooftop photovoltaic-powered electric vehicle charging for accelerated decarbonization](https://www.nature.com/articles/s41893-026-01854-3)** · `P086` · `本轮新增`

  **发表：** 2026-06-15（出版社在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究利用全球40座城市、2.2万个充电桩的33.8亿条充电记录，评估屋顶光伏供给与电动汽车充电需求的时空匹配。在三类充电策略及不同微电网尺度下，日充电供需能力呈稳定的指数尺度关系。情景预测显示，到2050年充电需求虽显著增加，城市屋顶光伏年度发电量仍足以覆盖需求，并可带来可观的累计减排和经济收益。

  [DOI](https://doi.org/10.1038/s41893-026-01854-3) · [核验与筛查依据](docs/CATALOG.md#P086)

<a id="P030"></a>

- 📘 **[2026 · Nature Energy] [Industrial overcapacity can enable seasonal flexibility in electricity use](https://www.nature.com/articles/s41560-026-02073-y)** · `P030`

  **发表：** 2026-06-12（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 以中国电解铝为例，评估保留部分工业过剩产能用于季节性调节用电的成本收益。闲置能力使企业可在冬季用电高峰停产、在其他季节增产。联合优化结果显示，这可能每年降低脱碳电力系统230亿—320亿元投资和运行成本，足以补偿增加的维护与产品储存成本，并带来跨行业劳动力互补。

  [DOI](https://doi.org/10.1038/s41560-026-02073-y) · [核验与筛查依据](docs/CATALOG.md#P030)

<a id="P004"></a>

- 📘 **[2026 · Nature Communications] [Long-duration electricity storage needs for coping with Dunkelflaute events in Europe](https://www.nature.com/articles/s41467-026-72681-5)** · `P004`

  **发表：** 2026-05-09（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 结合35年历史天气和欧洲电力系统模型，研究长时储能与跨区域输电如何应对长时间低风低光事件。极端能源干旱决定了储能投资和运行需求；在文中互联假设下，应对最严重事件的成本最优系统仍需大量长时储能，地理互济与其他备用技术只能部分降低需求。

  **备注：** 页面标记2026-07-09作者更正；本记录以检索时已更新页面为准。

  [DOI](https://doi.org/10.1038/s41467-026-72681-5) · [核验与筛查依据](docs/CATALOG.md#P004)

<a id="P003"></a>

- 📘 **[2026 · Nature Communications] [Decentralized electric vehicle charging enables large-scale photovoltaic integration in tropical cities](https://www.nature.com/articles/s41467-026-71123-6)** · `P003`

  **发表：** 2026-04-07（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 以新加坡为例，将手机数据推断的出行模式与光伏、电网模型结合，提出分区式电动汽车充放电协调策略。针对局地雷暴造成的光伏快速波动，研究显示分散到城区层级的调控可减少线路潮流压力，提升现有电网的光伏接纳能力；准确出行信息对效果十分重要。

  [DOI](https://doi.org/10.1038/s41467-026-71123-6) · [核验与筛查依据](docs/CATALOG.md#P003)

<a id="P044"></a>

- 📘 **[2026 · Joule] [Proactive grid investment enables V2G for 100% adoption of electric vehicles in urban areas](https://doi.org/10.1016/j.joule.2026.102393)** · `P044`

  **发表：** 2026-04-02（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 构建旧金山湾区2030—2050年交通与配电系统耦合模型，比较全电动车普及下的车网互动、智能充电及无序充电。V2G能缓解变压器过载和排放，却不能完全替代电网升级。研究支持提前投资电网并分阶段推进V2G，同时允许车辆参与多种电力服务，以维持合理收益。

  [DOI](https://doi.org/10.1016/j.joule.2026.102393) · [核验与筛查依据](docs/CATALOG.md#P044)

<a id="P129"></a>

- 📘 **[2026 · Nature Communications] [Energy, power, and infrastructure demands from electrifying airport ground support equipment at United States airports](https://www.nature.com/articles/s41467-026-71125-4)** · `P129` · `本轮新增`

  **发表：** 2026-03-30（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 构建覆盖美国300多个机场的自下而上模型，估算地面保障设备电气化带来的能量需求、峰值功率、充电设施数量及成本。结果显示大型机场可能形成显著新增电力负荷；结合表后储能与光伏能够削减峰值和系统总费用，为机场接电与设施规划提供依据。

  [DOI](https://doi.org/10.1038/s41467-026-71125-4) · [核验与筛查依据](docs/CATALOG.md#P129)

<a id="P094"></a>

- 📚 **[2026 · Nature Reviews Electrical Engineering] [Structural alignment for energy–computation co-design](https://www.nature.com/articles/s44287-026-00273-y)** · `P094` · `本轮新增`

  **发表：** 2026-02-23（在线发表日期） · **类型：** Comment · **范围：** 交叉与扩展期刊

  **内容概述（出版社导语，无正式摘要）：** 评论关注持续运行、规模达到吉瓦级的人工智能计算负荷对电力系统造成的压力。作者认为，需要在能源与计算协同设计中理解两类系统各自的组织约束和演化方式，以结构性协调支持长期共发展；文章提出研究议题，未提供具体模型遗忘方法。

  [DOI](https://doi.org/10.1038/s44287-026-00273-y) · [核验与筛查依据](docs/CATALOG.md#P094)

<a id="P037"></a>

- 📘 **[2025 · Nature Energy] [Vehicle-to-home charging can cut costs and greenhouse gas emissions across the USA](https://www.nature.com/articles/s41560-025-01894-7)** · `P037`

  **发表：** 2025-12-12（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 综合美国不同地区气候、车辆使用及未来电网脱碳路径，评估电动汽车寿命期内充电策略的费用和排放。利用车载电池为住宅转移购电时段，可以同时减少充电及其他家庭负荷的成本和排放。相比无序充电，优化车家互动具有显著收益，但收益随地区、电价和排放结构变化。

  [DOI](https://doi.org/10.1038/s41560-025-01894-7) · [核验与筛查依据](docs/CATALOG.md#P037)

<a id="P132"></a>

- 📘 **[2025 · Nature Communications] [Scenario-adaptive hierarchical optimisation framework for design in hybrid energy storage systems](https://www.nature.com/articles/s41467-025-67377-1)** · `P132` · `本轮新增`

  **发表：** 2025-12-10（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 围绕工业园区光伏发电与多能需求的不匹配，构建混合储能设计的分层优化流程，将需求分析、储能选择、系统建模、配置调度及性能评估相衔接。通过配置与运行之间的反馈，适应不同气候和负荷场景，展示降低能源费用、碳排放及提高可再生能源利用率的潜力。

  **备注：** 在线首发2025，卷期2026；主年份按在线首发统计。

  [DOI](https://doi.org/10.1038/s41467-025-67377-1) · [核验与筛查依据](docs/CATALOG.md#P132)

<a id="P104"></a>

- 📘 **[2025 · Nature Energy] [AI data centres as grid-interactive assets](https://www.nature.com/articles/s41560-025-01927-1)** · `P104` · `本轮新增`

  **发表：** 2025-12-05（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 通过亚利桑那州凤凰城云计算环境中的现场示范，检验人工智能工作负载能否作为电网可调节资源。对256块图形处理器的运行进行软件协调，在三小时高峰期间降低约四分之一功率，同时保持服务质量。结果说明根据实时电网信号调整计算任务，可在不增加储能和硬件的条件下提供需求侧灵活性，为数据中心与电网协同运行提供实证。

  **备注：** 在线首发年份为2025，卷期年份为2026；按在线首发年统计。

  [DOI](https://doi.org/10.1038/s41560-025-01927-1) · [核验与筛查依据](docs/CATALOG.md#P104)

<a id="P035"></a>

- 📘 **[2025 · Nature Energy] [Shaping residential electricity demand with negative pricing](https://www.nature.com/articles/s41560-025-01901-x)** · `P035`

  **发表：** 2025-11-21（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 通过对1918名美国居民的调查研究负电价下的用电调整意愿。超过四分之三的受访者表示愿意迁移用电时段，响应程度高于常规削峰项目；多数人并不愿刻意浪费用电。基于意愿的模拟同时指出，集中响应可能令部分地区负荷骤增，负电价激励的设计需要考虑电网可靠性。

  **备注：** 在线首发年份为2025，卷期年份为2026；按在线首发年统计。

  [DOI](https://doi.org/10.1038/s41560-025-01901-x) · [核验与筛查依据](docs/CATALOG.md#P035)

<a id="P136"></a>

- 📘 **[2025 · Nature Communications] [Cascading marginal emissions signals for green charging with growing electric vehicle adoption](https://www.nature.com/articles/s41467-025-64979-7)** · `P136` · `本轮新增`

  **发表：** 2025-11-19（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 将真实电动车充电数据与美国西部电网模型结合，检验按平均或边际排放信号移峰的效果。大量车辆同时响应、信号噪声及高排放机组跟随可能使传统方案反而增排。提出按小群体依次更新信号的级联策略，在研究场景中降低新增排放，说明需求响应必须考虑规模效应。

  [DOI](https://doi.org/10.1038/s41467-025-64979-7) · [核验与筛查依据](docs/CATALOG.md#P136)

<a id="P137"></a>

- 📘 **[2025 · Nature Communications] [Unlocking vehicle-to-grid potential of load shifting in China’s megacities considering comprehensive real-world behaviors](https://www.nature.com/articles/s41467-025-65073-8)** · `P137` · `本轮新增`

  **发表：** 2025-11-18（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 构建出行与车网互动耦合模型，把私人电动车的行程、充电行为、参与意愿、补偿和电池损耗共同纳入城市调峰分析。深圳48万辆车的案例表明，兼顾用户满意度的策略可以保持较强的削峰填谷能力，并降低损耗和补偿成本；快充普及还会改变资源分配公平性。

  [DOI](https://doi.org/10.1038/s41467-025-65073-8) · [核验与筛查依据](docs/CATALOG.md#P137)

<a id="P142"></a>

- 📘 **[2025 · Nature Communications] [China’s urban EV ultra-fast charging distorts regulated price signals and elevates risk to grid stability](https://www.nature.com/articles/s41467-025-63199-3)** · `P142` · `本轮新增`

  **发表：** 2025-09-26（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 基于中国主要城市真实充电数据模拟超快充扩张，发现其可能放大公共充电负荷的峰谷差。储能虽能平滑部分短时波动，也可能因同步响应分时电价而在低价时段开始时形成更强冲击。研究指出，快充基础设施扩张需要同步调整电网管理及价格机制。

  [DOI](https://doi.org/10.1038/s41467-025-63199-3) · [核验与筛查依据](docs/CATALOG.md#P142)

<a id="P034"></a>

- 📘 **[2025 · Nature Energy] [Solar and battery can reduce energy costs and provide affordable outage backup for US households](https://www.nature.com/articles/s41560-025-01821-w)** · `P034`

  **发表：** 2025-08-01（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 评估超过50万美国家庭配置光伏和储能的经济性及停电备用能力。约60%的家庭具有降费潜力，平均节省约15%；约63%的家庭可获得具有可负担性的备用供电。但技术收益与停电风险较高地区并不充分重合，弱势和人口稀疏社区的可行性较低，提示需要针对性的公平支持政策。

  [DOI](https://doi.org/10.1038/s41560-025-01821-w) · [核验与筛查依据](docs/CATALOG.md#P034)

<a id="P105"></a>

- 📘 **[2025 · Nature Energy] [Redesigning electrification of China’s ammonia and methanol industry to balance decarbonization with power system security](https://www.nature.com/articles/s41560-025-01779-9)** · `P105` · `本轮新增`

  **发表：** 2025-06-05（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 评估中国22个省份氨与甲醇产业电气化路径，分析可再生发电和化工负荷的时空错配如何影响电力排放及安全。单纯依赖电网供电可能抵消减排，共址新能源若缺少自平衡灵活性也会增加系统平衡需求。论文提出绿色灵活化工电气化路径，并讨论通过电价机制激励化工需求管理，使产业减排与电网安全相协调。

  [DOI](https://doi.org/10.1038/s41560-025-01779-9) · [核验与筛查依据](docs/CATALOG.md#P105)

<a id="P012"></a>

- 📘 **[2025 · Nature Communications] [Globally interconnected solar-wind system addresses future electricity demands](https://www.nature.com/articles/s41467-025-59879-9)** · `P012`

  **发表：** 2025-05-15（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 评估全球互联风光电力系统满足未来需求的潜力，联合优化可再生能源布局、储能与跨区域输电。模型表明互联可缓解资源时空波动，并较无互联情景降低初始投资；进一步分析气候极端、发电或输电故障及地缘冲突情景下的系统韧性。

  [DOI](https://doi.org/10.1038/s41467-025-59879-9) · [核验与筛查依据](docs/CATALOG.md#P012)

<a id="P098"></a>

- 📚 **[2025 · Nature Reviews Electrical Engineering] [Pumped-storage renovation for grid-scale, long-duration energy storage](https://www.nature.com/articles/s44287-025-00143-z)** · `P098` · `本轮新增`

  **发表：** 2025-01-20（在线发表日期） · **类型：** Comment · **范围：** 交叉与扩展期刊

  **内容概述（出版社导语，无正式摘要）：** 评论提出利用既有大型水电系统进行抽水蓄能改造，以释放电网级长时和季节性储能潜力。作者从应对风光发电间歇性的需求出发，讨论改造面临的技术挑战与后续研究方向，强调现有水电基础设施在低碳电力系统中的新用途。

  [DOI](https://doi.org/10.1038/s44287-025-00143-z) · [核验与筛查依据](docs/CATALOG.md#P098)

<a id="P045"></a>

- 📚 **[2025 · Joule] [24/7 carbon-free electricity matching accelerates adoption of advanced clean energy technologies](https://www.sciencedirect.com/science/article/pii/S2542435124005440)** · `P045`

  **发表：** 2025-01（作者页面发表月份；卷期日期为2025-02-19） · **类型：** Commentary · **范围：** 核心期刊电网文献

  **内容概述（导语或机构摘要）：** 通过示例建模说明，企业和政府承诺逐小时匹配无碳用电，可为长时储能和稳定清洁电源创造早期市场。初始采购推动技术降本，又吸引更多采购者，可能带来超出直接用电替代的系统减排收益。这里的学习指技术经验积累与成本下降，不属于机器学习或遗忘学习。

  [DOI](https://doi.org/10.1016/j.joule.2024.101808) · [核验与筛查依据](docs/CATALOG.md#P045)

<a id="P157"></a>

- 📘 **[2024 · Nature Communications] [How grid reinforcement costs differ by the income of electric vehicle users](https://www.nature.com/articles/s41467-024-53644-0)** · `P157` · `本轮新增`

  **发表：** 2024-11-08（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 根据真实出行数据开展配电潮流仿真，研究收入差异如何通过电动车保有量、车型和充电偏好影响电网扩容成本。部分情景下高收入社区的投资需求可达低收入社区的33倍，统一电价分摊可能产生不公平负担。文章讨论动态电价、差异化补贴与充电设施可及性等对策，强调规划中的社会经济异质性。

  [DOI](https://doi.org/10.1038/s41467-024-53644-0) · [核验与筛查依据](docs/CATALOG.md#P157)

<a id="P026"></a>

- 📘 **[2024 · Nature Communications] [The value of long-duration energy storage under various grid conditions in a zero-emissions future](https://www.nature.com/articles/s41467-024-53274-6)** · `P026`

  **发表：** 2024-11-03（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 使用Switch容量扩展模型，在39组发电结构、输电扩张及储能成本情景下评估美国西部零排放电网中的长时储能。研究发现其在风电占比较高或水电减少地区更有价值，成本显著下降后季节储能可具经济性；储能配置也会影响高需求时段电价。

  [DOI](https://doi.org/10.1038/s41467-024-53274-6) · [核验与筛查依据](docs/CATALOG.md#P026)

<a id="P160"></a>

- 📘 **[2024 · Nature Communications] [Quantifying benefits of renewable investments for German residential Prosumers in times of volatile energy markets](https://www.nature.com/articles/s41467-024-51967-6)** · `P160` · `本轮新增`

  **发表：** 2024-09-18（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 在能源价格剧烈波动背景下，对德国不同独栋住宅的光伏、家用储能、热泵及电动车投资进行经济和环境评估，并考虑补贴和价格干预。结果显示，光伏具有较稳健的成本与减排收益，其他设备的组合价值取决于用能条件，为居民侧综合能源投资提供参考。

  [DOI](https://doi.org/10.1038/s41467-024-51967-6) · [核验与筛查依据](docs/CATALOG.md#P160)

<a id="P108"></a>

- 📘 **[2024 · Nature Energy] [Multi-year field measurements of home storage systems and their use in capacity estimation](https://www.nature.com/articles/s41560-024-01620-9)** · `P108` · `本轮新增`

  **发表：** 2024-09-16（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 基于德国21套实际运行的户用锂电储能系统、最长八年的高分辨率测量，提出可扩展的在线可用容量估计方法，并用定期现场容量测试验证。结果显示系统平均每年损失约两至三个百分点的可用容量。研究同时公开覆盖约106个系统年的大规模运行数据，为户用光储可靠运行、健康状态评估及透明的容量退化测量提供依据。

  [DOI](https://doi.org/10.1038/s41560-024-01620-9) · [核验与筛查依据](docs/CATALOG.md#P108)

<a id="P109"></a>

- 📘 **[2024 · Nature Energy] [Transforming public transport depots into profitable energy hubs](https://www.nature.com/articles/s41560-024-01580-0)** · `P109` · `本轮新增`

  **发表：** 2024-08-01（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用北京两万余辆公交车的两亿余条定位记录，评估将公交场站改造成配置光伏和储能的能源枢纽。光伏能够减少净充电负荷，加入储能后削峰效果进一步增强，但储能也会降低项目利润。研究量化了电网收益、经济性与减排之间的权衡，为城市公交电气化及场站能源配置提供数据驱动的规划框架。

  [DOI](https://doi.org/10.1038/s41560-024-01580-0) · [核验与筛查依据](docs/CATALOG.md#P109)

<a id="P040"></a>

- 📘 **[2024 · Nature Energy] [Exploiting different electricity markets via highly rate-mismatched modular electrochemical synthesis](https://www.nature.com/articles/s41560-024-01578-8)** · `P040`

  **发表：** 2024-07-05（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究将动力学差异较大的电化学半反应解耦，使模块化化工生产在不同时间尺度调节用电，并参与日前、实时及调频市场。实验与市场分析表明，此类可调工业负荷能够随电力供应变化运行，在研究条件下将化学生产电费降低约30%—40%，为工业需求侧灵活性提供一种技术路径。

  [DOI](https://doi.org/10.1038/s41560-024-01578-8) · [核验与筛查依据](docs/CATALOG.md#P040)

<a id="P164"></a>

- 📘 **[2024 · Nature Communications] [Enhancing smart charging in electric vehicles by addressing paused and delayed charging problems](https://www.nature.com/articles/s41467-024-48477-w)** · `P164` · `本轮新增`

  **发表：** 2024-06-25（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 通过实际充电测试发现，部分电动车在暂停或延迟充电后进入休眠，难以按智能调度恢复，因而需要持续最低功率充电。模型分析表明，消除这一设备限制能够明显扩大削峰、电价响应等智能充电潜力。论文进一步提出面向制造商和政策制定者的技术及制度改进建议。

  [DOI](https://doi.org/10.1038/s41467-024-48477-w) · [核验与筛查依据](docs/CATALOG.md#P164)

<a id="P021"></a>

- 📘 **[2024 · Nature Communications] [Multi-resource dynamic coordinated planning of flexible distribution network](https://www.nature.com/articles/s41467-024-48862-5)** · `P021`

  **发表：** 2024-05-29（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对分布式电源和负荷持续增长，建立基于柔性互联装置的配电网多资源分阶段规划方法。利用概率框架处理源荷不确定性，将电压越限与线路过载风险纳入约束；实际配电网案例显示，可通过调节允许违约概率在建设成本与运行安全之间取得平衡。

  [DOI](https://doi.org/10.1038/s41467-024-48862-5) · [核验与筛查依据](docs/CATALOG.md#P021)

<a id="P019"></a>

- 📘 **[2024 · Nature Communications] [On the potential of vehicle-to-grid and second-life batteries to provide energy and material security](https://www.nature.com/articles/s41467-024-48554-0)** · `P019`

  **发表：** 2024-05-16（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 通过动态物质流分析，评估车网互动和退役电池再利用替代新建电网储能的潜力。在研究假设下，两种方案均有可能覆盖欧盟2040年的固定式储能需求，并减少原生材料使用。结果强调电动汽车电池在电力保障、材料供应安全和应急储备中的协同价值。

  [DOI](https://doi.org/10.1038/s41467-024-48554-0) · [核验与筛查依据](docs/CATALOG.md#P019)

<a id="P173"></a>

- 📘 **[2024 · Nature Climate Change] [Climate change will impact the value and optimal adoption of residential rooftop solar](https://www.nature.com/articles/s41558-024-01978-4)** · `P173` · `本轮新增`

  **发表：** 2024-04-19（出版社在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究结合美国17座城市逾2000户家庭的用电数据、家庭级仿真优化与降尺度气象资料，分析气候变化如何同时改变屋顶光伏发电和制冷需求。在RCP4.5情景下，至世纪末家庭屋顶光伏价值最多增加19%，技术经济最优容量最多增加25%。这一效应在不同城市、家庭和零售电价结构下较稳健，提示分布式光伏规划需纳入未来气候。

  [DOI](https://doi.org/10.1038/s41558-024-01978-4) · [核验与筛查依据](docs/CATALOG.md#P173)

<a id="P083"></a>

- 📚 **[2024 · Nature Reviews Electrical Engineering] [Sustainable plug-in electric vehicle integration into power systems](https://www.nature.com/articles/s44287-023-00004-7)** · `P083`

  **发表：** 2024-01-11（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 综述插电式电动车与电力系统协同的技术趋势，包括充电基础设施规划、智能充放电，以及面向安全和经济运行的控制与优化。讨论车辆灵活性如何促进清洁能源利用和电力交通共同脱碳，并提出后续发展路线。

  [DOI](https://doi.org/10.1038/s44287-023-00004-7) · [核验与筛查依据](docs/CATALOG.md#P083)

[返回导航](#导航)

<a id="topic-3"></a>
### 气候风险、韧性与可靠性（29条）

<a id="P101"></a>

- 📘 **[2026 · Nature Energy] [Heatwave-induced capacity bottlenecks in European electricity grids](https://www.nature.com/articles/s41560-026-02151-1)** · `P101` · `本轮新增`

  **发表：** 2026-10-22（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 将温度相关的用电需求、发电机出力降额与输电线路热约束统一纳入交流最优潮流框架，利用西欧公开电网、气象和需求数据模拟多种热浪情景。结果揭示地区间容量瓶颈及负荷削减风险存在明显差异，西班牙较为脆弱而德国相对稳健。研究强调规划与运行需要同时考虑高温对供需和线路容量的影响。

  [DOI](https://doi.org/10.1038/s41560-026-02151-1) · [核验与筛查依据](docs/CATALOG.md#P101)

<a id="P065"></a>

- 📘 **[2026 · Nature Climate Change] [Flash energy droughts in solar and wind resources under climate change](https://www.nature.com/articles/s41558-026-02753-3)** · `P065`

  **发表：** 2026-09-21（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 论文研究风光出力快速下降后持续低位的突发能源干旱，分析其与缺供电量、灵活性需求及电力成本的关联。气候变化下，这类事件特别是复合事件的持续时间增加，约70.8%的全球风光装机面临频率和持续时间同步上升。优化未来电站布局可缓解暴露，但效果取决于减排力度及技术潜力实现程度。

  [DOI](https://doi.org/10.1038/s41558-026-02753-3) · [核验与筛查依据](docs/CATALOG.md#P065)

<a id="P078"></a>

- 📚 **[2026 · Nature Reviews Electrical Engineering] [Long-horizon resilience of power systems under climate change](https://www.nature.com/articles/s44287-026-00322-6)** · `P078`

  **发表：** 2026-08-21（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 认为基于单次极端天气事件衡量电网韧性难以支撑气候变化下的长期规划。提出跨长期气候情景、独立于单次事件的韧性概念，形成研究、评估和增强韧性的统一框架，并提出与基础设施规划和投资相联的研究议程。

  [DOI](https://doi.org/10.1038/s44287-026-00322-6) · [核验与筛查依据](docs/CATALOG.md#P078)

<a id="P006"></a>

- 📘 **[2026 · Nature Communications] [Navigating optimal solar-wind trade-offs under climate change](https://www.nature.com/articles/s41467-026-75879-9)** · `P006`

  **发表：** 2026-07-24（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 将多模型气候预测与投资调度优化结合，研究气候变化下成本最优的风光比例。最优组合具有明显地区差异；沿用历史技术偏好的部署路径可能偏离适宜比例，其成本影响甚至大于资源均值变化本身。研究强调按地区与气候条件动态设计电源结构。

  [DOI](https://doi.org/10.1038/s41467-026-75879-9) · [核验与筛查依据](docs/CATALOG.md#P006)

<a id="P102"></a>

- 📘 **[2026 · Nature Energy] [Climate change reshapes resource adequacy risks and optimal renewable energy siting in wind and solar energy systems](https://www.nature.com/articles/s41560-026-02109-3)** · `P102` · `本轮新增`

  **发表：** 2026-07-16（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 将高分辨率气候预测与县级电力系统优化结合，评估新英格兰及得克萨斯的风光资源充裕性。制冷需求增长、可再生能源变化和输电约束可能显著增加供电不足风险，而将未来气候纳入风光选址可降低这些风险。研究说明两地适宜的调整路径不同，需要把发电布局、需求位置与输电投资联动考虑。

  [DOI](https://doi.org/10.1038/s41560-026-02109-3) · [核验与筛查依据](docs/CATALOG.md#P102)

<a id="P055"></a>

- 📘 **[2026 · Nature Sustainability] [Resilience metrics to guide back-up investments in the power system during extreme weather](https://www.nature.com/articles/s41893-026-01897-6)** · `P055`

  **发表：** 2026-07-14（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究使用影子价格识别使欧洲净零电力系统承压的关键天气事件，并在PyPSA-Eur模型中分析其运行及规划影响。结果强调需配置足够的韧性备用容量，但天气波动使这些低利用率资源的收入和投资回收存在风险。论文分别提出多日与年度尺度的压力测试和韧性指标，避免仅凭长期可靠性推断短期抗冲击能力。

  [DOI](https://doi.org/10.1038/s41893-026-01897-6) · [核验与筛查依据](docs/CATALOG.md#P055)

<a id="P077"></a>

- 📚 **[2026 · Nature Reviews Electrical Engineering] [From electricity outage analysis and monitoring to mitigation and restoration](https://www.nature.com/articles/s44287-026-00298-3)** · `P077`

  **发表：** 2026-06-03（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 从停电全生命周期出发，梳理历史事件分析、韧性指标、实时监测、风险缓解与供电恢复。讨论历史停电数据和先进传感器如何识别薄弱环节，以及自动控制和恢复策略如何阻断扰动扩散并缩短停电时间。

  [DOI](https://doi.org/10.1038/s44287-026-00298-3) · [核验与筛查依据](docs/CATALOG.md#P077)

<a id="P005"></a>

- 📘 **[2026 · Nature Communications] [High-impact weather effects on wind and solar power systems under future climate scenarios in China](https://www.nature.com/articles/s41467-026-73427-z)** · `P005`

  **发表：** 2026-05-26（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 结合中国高分辨率气象数据、逐小时需求和风光输电协调优化，评估未来高影响天气导致的持续发电缺口。模型显示部分地区可能经历显著且长期的风光减产，跨区域输电能够缓解空间失衡；规划需要同时考虑天气冲击、电源分布与输电走廊。

  [DOI](https://doi.org/10.1038/s41467-026-73427-z) · [核验与筛查依据](docs/CATALOG.md#P005)

<a id="P076"></a>

- 📚 **[2026 · Nature Reviews Electrical Engineering] [Resilient low-inertia power systems through asynchronous energy balancing](https://www.nature.com/articles/s44287-025-00256-5)** · `P076`

  **发表：** 2026-01-20（在线发表日期） · **类型：** Perspective · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 针对低惯量电网对全局同步频率的依赖，讨论由多个独立异步子系统构成的电力系统架构。借鉴通信网络的存储转发思想，利用电力电子、低时延通信和储能主动路由动态能量，以增强韧性和能源安全。

  [DOI](https://doi.org/10.1038/s44287-025-00256-5) · [核验与筛查依据](docs/CATALOG.md#P076)

<a id="P133"></a>

- 📘 **[2025 · Nature Communications] [Rising worldwide challenges to climate-induced extreme low-production events of photovoltaic and wind power](https://www.nature.com/articles/s41467-025-67428-7)** · `P133` · `本轮新增`

  **发表：** 2025-12-10（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 比较多个排放情景下全球光伏和风电极端低出力事件的变化，识别供电可靠性面临的长期气候风险。结果显示，风电低出力异常在多数现有装机区域加剧，光伏风险对情景和地区更敏感；部分低收入经济体承受不成比例的风险，需协同推进减缓与适应措施。

  **备注：** 在线首发2025，卷期2026；主年份按在线首发统计。

  [DOI](https://doi.org/10.1038/s41467-025-67428-7) · [核验与筛查依据](docs/CATALOG.md#P133)

<a id="P059"></a>

- 📘 **[2025 · Nature Sustainability] [Global hydroclimatic risks and strategic decommissioning pathways for thermal power units](https://www.nature.com/articles/s41893-025-01692-9)** · `P059`

  **发表：** 2025-12-09（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究构建全球热力发电机组尺度的风险框架，评估升温和缺水对冷却与可用容量的影响，并将这些风险纳入退役规划。在SSP370情景下，到2050年代约60.5%的装机容量面临风险增加。结合机组级水文气候约束调整保留顺序，可提高优先保留机组的平均可用容量比例，帮助兼顾减排与能源安全。

  **备注：** 在线首发年份为2025，卷期年份为2026；按在线首发年统计。

  [DOI](https://doi.org/10.1038/s41893-025-01692-9) · [核验与筛查依据](docs/CATALOG.md#P059)

<a id="P141"></a>

- 📘 **[2025 · Nature Communications] [Unequal power outages induced by natural disasters](https://www.nature.com/articles/s41467-025-64012-x)** · `P141` · `本轮新增`

  **发表：** 2025-10-08（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用中国2019—2021年高频停电和自然灾害数据，比较不同地区的供电可靠性损失。分析发现，贫困县在灾害后的停电频率和持续时间增幅更大，未来气候情景可能扩大差距。研究强调，电网韧性投资和气候资金分配需考虑脆弱地区承受的不均等风险。

  [DOI](https://doi.org/10.1038/s41467-025-64012-x) · [核验与筛查依据](docs/CATALOG.md#P141)

<a id="P013"></a>

- 📘 **[2025 · Nature Communications] [Vulnerability of power distribution networks to local temperature changes induced by global climate change](https://www.nature.com/articles/s41467-025-59749-4)** · `P013`

  **发表：** 2025-06-02（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 构建从气候变暖、供需和设备容量变化到配电网潮流及停电概率的综合模型。发现气候冲击会经电网物理规律形成非线性风险，并在峰荷时段增加停电风险。提出调整网络拓扑、负荷配置及设备扩容等适应方向，强调各区域风险及扩容需求存在差异。

  [DOI](https://doi.org/10.1038/s41467-025-59749-4) · [核验与筛查依据](docs/CATALOG.md#P013)

<a id="P183"></a>

- 📚 **[2025 · Joule] [Cross-sector energy system resilience and interdependence in a changing climate](https://doi.org/10.1016/j.joule.2025.101967)** · `P183` · `本轮新增`

  **发表：** 2025-06-02（在线发表日期） · **类型：** Commentary · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 分析电气化如何加深发电、输电与终端消费部门之间的依赖关系，并形成灵活性收益与级联故障风险并存的韧性问题。结合全球电气化趋势、得克萨斯案例及极端气候预测，识别部门耦合中的关键脆弱点和调节潜力。文章主张采取面向整体系统的韧性规划与运行策略，以降低跨部门故障传播并发挥电气化协同优势。

  [DOI](https://doi.org/10.1016/j.joule.2025.101967) · [核验与筛查依据](docs/CATALOG.md#P183)

<a id="P011"></a>

- 📘 **[2025 · Nature Communications] [Coordinating power sector climate transitions under policy uncertainty](https://www.nature.com/articles/s41467-025-59126-1)** · `P011`

  **发表：** 2025-04-22（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 使用包含运行细节和区域协调机制的容量扩展模型，分析美国西部政策差异与协调障碍对低碳电力路径的影响。总体协调收益与各州分配收益并不相同；输电、储能和可再生能源投资对政策及市场协调的响应也有差异，提示规划应考虑制度可行性。

  [DOI](https://doi.org/10.1038/s41467-025-59126-1) · [核验与筛查依据](docs/CATALOG.md#P011)

<a id="P176"></a>

- 📘 **[2025 · Nature Cities] [Grid connections and inequitable access to electricity in African cities](https://www.nature.com/articles/s44284-025-00221-1)** · `P176` · `本轮新增`

  **发表：** 2025-04-08（出版社在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 研究在乌干达坎帕拉25个非正规住区结合问卷、访谈与远程电能质量监测，追踪电力公司、中间供电者和用户之间的电流与资金流，识别29类供电服务安排。这些安排在可负担性、可靠性、电压稳定性、使用自主性和安全性方面差异显著，整体水平仍有限。结果说明“已接入电网”不能充分代表获得可靠、安全且公平的现代电力服务。

  [DOI](https://doi.org/10.1038/s44284-025-00221-1) · [核验与筛查依据](docs/CATALOG.md#P176)

<a id="P151"></a>

- 📘 **[2025 · Nature Communications] [A Method to estimate the economy-wide consequences of widespread, long duration electric power interruptions](https://www.nature.com/articles/s41467-025-58537-4)** · `P151` · `本轮新增`

  **发表：** 2025-04-08（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 结合美国伊利诺伊州公用事业客户调查与可计算一般均衡模型，估算大范围、长时间停电对区域经济的影响。方法同时考虑迁移、备用发电等用户响应，发现损失远超单纯电价信号能反映的范围；增加备用供电可缓解部分损失，为电力韧性投资评价提供依据。

  [DOI](https://doi.org/10.1038/s41467-025-58537-4) · [核验与筛查依据](docs/CATALOG.md#P151)

<a id="P153"></a>

- 📘 **[2025 · Nature Communications] [Quantifying cascading power outages during climate extremes considering renewable energy integration](https://www.nature.com/articles/s41467-025-57565-4)** · `P153` · `本轮新增`

  **发表：** 2025-03-16（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 构建气候—能源耦合模型，描述极端天气对新能源发电及输配电网络的共同冲击，并用2022年飓风Fiona引发的波多黎各全网停电验证。分析揭示部分关键部件的早期失效可能改变级联过程；高比例表后光伏若缺乏储能配套，也可能提高灾难性停电概率。

  [DOI](https://doi.org/10.1038/s41467-025-57565-4) · [核验与筛查依据](docs/CATALOG.md#P153)

<a id="P106"></a>

- 📘 **[2025 · Nature Energy] [Mobilizing power quality and reliability measurements for electricity equity and justice in Africa](https://www.nature.com/articles/s41560-025-01717-9)** · `P106` · `本轮新增`

  **发表：** 2025-02-28（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 提出结合能源公平、能力、多维贫困与电力工程的分析框架，研究撒哈拉以南非洲供电质量和可靠性的分布。利用阿克拉一年的远程监测数据，识别不同社区的电能质量与可靠性差异，并发现较差供电状况与贫困社区相联系。研究强调电力接入率之外还应测量实际服务质量，以评估家庭生活能力及电力系统不平等。

  [DOI](https://doi.org/10.1038/s41560-025-01717-9) · [核验与筛查依据](docs/CATALOG.md#P106)

<a id="P028"></a>

- 📘 **[2024 · Nature Communications] [Designing a sector-coupled European energy system robust to 60 years of historical weather data](https://www.nature.com/articles/s41467-024-54853-3)** · `P028`

  **发表：** 2024-12-16（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对单一天气年规划可能低估风险的问题，在62个天气年下优化欧洲部门耦合能源系统，并跨天气年检验运行可靠性与排放。复合极端天气年设计的方案更稳健，而有限备用发电可在小幅增加排放的情况下提高可靠性。结果支持规划中显式考虑年际气象差异。

  [DOI](https://doi.org/10.1038/s41467-024-54853-3) · [核验与筛查依据](docs/CATALOG.md#P028)

<a id="P027"></a>

- 📘 **[2024 · Nature Communications] [Climate change and its influence on water systems increases the cost of electricity system decarbonization](https://www.nature.com/articles/s41467-024-54162-9)** · `P027`

  **发表：** 2024-11-25（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 耦合水资源与电力系统模型，研究美国西部电网如何同时实现2050年脱碳和气候适应。气候变化会提高制冷及供水相关用电、减少水电产出；模型显示，为弥补这些影响可能需要额外发电容量与投资，说明电力规划应共同考虑水电联系与气候脆弱性。

  [DOI](https://doi.org/10.1038/s41467-024-54162-9) · [核验与筛查依据](docs/CATALOG.md#P027)

<a id="P042"></a>

- 📘 **[2024 · Nature Energy] [Impacts of renewable energy resources on the weather vulnerability of power systems](https://www.nature.com/articles/s41560-024-01652-1)** · `P042`

  **发表：** 2024-10-21（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 文章分析天气依赖型风光电源与停电、极端天气脆弱性的关系。研究发现，在所考察的高可再生能源渗透率电网中，停电强度和天气脆弱性反而有所减轻，风光电源对停电的因果影响也趋于下降。结论为评估可再生能源并网安全和电网韧性提供实证依据，但不意味着所有电网和天气情境均适用。

  [DOI](https://doi.org/10.1038/s41560-024-01652-1) · [核验与筛查依据](docs/CATALOG.md#P042)

<a id="P041"></a>

- 📘 **[2024 · Nature Energy] [Temporally compounding energy droughts in European electricity systems with hydropower](https://www.nature.com/articles/s41560-024-01640-5)** · `P041`

  **发表：** 2024-09-27（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用相当于1600年的逐日发电与需求序列，研究五个含水电的欧洲国家出现低发电、高需求的能源短缺事件。文章识别跨季节、跨年度的气象与能源复合机制：例如春季径流不足既削弱水电，也可能加剧夏季热浪，使短期短缺演变为持续供电压力。这些风险需要进入未来电力系统设计。

  [DOI](https://doi.org/10.1038/s41560-024-01640-5) · [核验与筛查依据](docs/CATALOG.md#P041)

<a id="P185"></a>

- 📚 **[2024 · Joule] [Why renewables should be at the center of rebuilding the Ukrainian electricity system](https://doi.org/10.1016/j.joule.2024.08.014)** · `P185` · `本轮新增`

  **发表：** 2024-09-18（在线发表日期） · **类型：** Commentary · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 对乌克兰电力系统及战争造成的破坏进行地理空间梳理，发现集中式电源、输电线路和变电站广泛受损，削弱供电能力。论文提出重建应兼顾速度、韧性、燃料进口依赖与污染减排，并依据风光资源潜力主张将可再生能源作为未来系统的重要基础。讨论乌克兰及国际政策如何引导投资，以支持更分散且更具韧性的电力体系。

  [DOI](https://doi.org/10.1016/j.joule.2024.08.014) · [核验与筛查依据](docs/CATALOG.md#P185)

<a id="P069"></a>

- 📚 **[2024 · Nature Climate Change] [The role of electric grid research in addressing climate change](https://www.nature.com/articles/s41558-024-02092-1)** · `P069`

  **发表：** 2024-08-21（在线发表日期） · **类型：** Perspective · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 这篇观点文章梳理电力系统支撑大规模减排所面临的研究问题，强调建模、分析、控制与新技术整合的重要性。除技术创新外，文章讨论市场机制、监管架构以及参与者激励的协调，主张将电网基础设施研究与气候研究连接起来，形成能够支持十亿吨量级脱碳的研究议程。

  [DOI](https://doi.org/10.1038/s41558-024-02092-1) · [核验与筛查依据](docs/CATALOG.md#P069)

<a id="P092"></a>

- 📘 **[2024 · Nature Sustainability] [Sustainable urban transformations based on integrated microgrid designs](https://www.nature.com/articles/s41893-024-01395-7)** · `P092` · `本轮新增`

  **发表：** 2024-07-16（出版社在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 自然灾害与气候变化加剧城市停电风险，微电网可在主网故障时维持局部供电，但仅按技术指标划分边界可能延续社会不平等。研究将社会经济与技术指标共同纳入城市微电网规划，并通过美国一个县的案例评估韧性、居民福祉和公平性之间的联系，强调微电网分区、储能与关键负荷供电应兼顾不同群体的灾害承受能力。

  [DOI](https://doi.org/10.1038/s41893-024-01395-7) · [核验与筛查依据](docs/CATALOG.md#P092)

<a id="P023"></a>

- 📘 **[2024 · Nature Communications] [Climate change impacts on the extreme power shortage events of wind-solar supply systems worldwide during 1980–2022](https://www.nature.com/articles/s41467-024-48966-y)** · `P023`

  **发表：** 2024-06-18（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用逐小时气象再分析数据，考察全球风光供电系统1980—2022年的极端缺电事件。研究发现事件频率、持续时间与强度总体呈上升趋势，且地区差异明显；风速和辐照的复合极低事件会非线性放大供电不足，说明仅观察平均资源变化不足以判断可靠性。

  [DOI](https://doi.org/10.1038/s41467-024-48966-y) · [核验与筛查依据](docs/CATALOG.md#P023)

<a id="P110"></a>

- 📘 **[2024 · Nature Energy] [Increasing the resilience of the Texas power grid against extreme storms by hardening critical lines](https://www.nature.com/articles/s41560-023-01434-1)** · `P110` · `本轮新增`

  **发表：** 2024-03-01（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 结合输电线路概率失效模型与得克萨斯电网模型，模拟七场历史热带气旋中风致线路故障及级联停电的时空演化。模型能够复现供电中断，并识别静态方法容易遗漏的关键线路。研究发现仅加固约百分之一的线路，就能显著降低最严重停电的发生概率，为在有限信息和预算下提高电网抗风暴能力提供方法。

  [DOI](https://doi.org/10.1038/s41560-023-01434-1) · [核验与筛查依据](docs/CATALOG.md#P110)

<a id="P082"></a>

- 📚 **[2024 · Nature Reviews Electrical Engineering] [Resilience of renewable power systems under climate risks](https://www.nature.com/articles/s44287-023-00003-8)** · `P082`

  **发表：** 2024-01-11（在线发表日期） · **类型：** Perspective · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 分析气候变化、极端天气与高比例新能源叠加对电网的风险。结合美国热带气旋停电资料讨论惯量和灵活性对防止级联故障的作用，并提出微电网、构网型逆变器、分布式储能及气候—能源联合建模等韧性路径。

  [DOI](https://doi.org/10.1038/s44287-023-00003-8) · [核验与筛查依据](docs/CATALOG.md#P082)

[返回导航](#导航)

<a id="topic-4"></a>
### 稳定性、安全与停电恢复（9条）

<a id="P100"></a>

- 📘 **[2026 · Nature Energy] [One-minute frequency disturbances from unintended synchronization in cyber–physical power systems](https://www.nature.com/articles/s41560-026-02144-0)** · `P100` · `本轮新增`

  **发表：** 2026-10-30（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 分析多个电网中持续出现的一分钟周期频率扰动，指出按时钟同步运行的软件控制可使不同能源设备产生非预期的同步功率变化。这类扰动与不间断电源、储能等数字控制设备有关，能够跨电压等级传播，并增加调频需求及水电机组磨损。随着数据中心、储能和联网设备扩张，控制系统设计需要避免周期性同步引起的系统风险。

  [DOI](https://doi.org/10.1038/s41560-026-02144-0) · [核验与筛查依据](docs/CATALOG.md#P100)

<a id="P008"></a>

- 📚 **[2026 · Nature Communications] [Power distribution system blackstart restoration using renewable energy](https://www.nature.com/articles/s41467-026-76692-0)** · `P008`

  **发表：** 2026-08-17（在线发表日期） · **类型：** Review · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 综述利用配电侧构网型分布式资源开展自下而上黑启动的条件与方法，重点梳理逆变器容量余量、频率动态、冷负荷投入、保护与可观测性约束。讨论开关、负荷恢复和电源调度的闭环联合决策，以及不确定性处理、学习代理模型和实际验证需求。

  **遗忘筛查：** 邻近但非遗忘。涉及AI建模、信息筛选或隐私保护，但所读摘要未定义遗忘对象、删除目标及删除有效性验证。

  [DOI](https://doi.org/10.1038/s41467-026-76692-0) · [核验与筛查依据](docs/CATALOG.md#P008)

<a id="P115"></a>

- 📘 **[2026 · Nature Communications] [High-power hybrid commutated converter for carbon-neutral power transmission](https://www.nature.com/articles/s41467-026-75691-5)** · `P115` · `本轮新增`

  **发表：** 2026-07-22（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 提出面向大规模清洁电力输送的混合换相换流器，通过强迫换相与恢复增强换相结合，提高直流输电的可靠性并缓解换相失败风险。研究完成120千伏、360兆瓦级验证，并结合实际工程应用说明该技术支撑高功率、长距离新能源输送的可行性。

  [DOI](https://doi.org/10.1038/s41467-026-75691-5) · [核验与筛查依据](docs/CATALOG.md#P115)

<a id="P180"></a>

- 📚 **[2026 · Joule] [Rethinking the green power grid for stability, not just for climate](https://doi.org/10.1016/j.joule.2026.102522)** · `P180` · `本轮新增`

  **发表：** 2026-06-15（在线发表日期） · **类型：** Commentary · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 以2025年伊比利亚半岛大停电引发的讨论为背景，分析高比例可再生能源电网的稳定性问题。文章认为，通过合成惯量、先进逆变器控制以及协调输电规划，可再生能源不仅能够减少排放，也有潜力增强电网稳定性。储能和电力电子的进展为此提供条件，关键在于将系统动态和韧性要求纳入新能源并网与基础设施决策。

  [DOI](https://doi.org/10.1016/j.joule.2026.102522) · [核验与筛查依据](docs/CATALOG.md#P180)

<a id="P121"></a>

- 📘 **[2026 · Nature Communications] [Detection and countermeasure integrated framework against false data injection attacks in multi-area coupled power systems](https://www.nature.com/articles/s41467-026-74374-5)** · `P121` · `本轮新增`

  **发表：** 2026-06-10（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对多区域耦合电力系统负荷频率控制中的虚假数据注入攻击，提出联合检测和反制框架。利用无迹卡尔曼滤波的采样策略刻画动态耦合，并自适应更新状态与噪声协方差。多种攻击场景实验显示，状态估计、攻击检测和应对效果得到改善。

  [DOI](https://doi.org/10.1038/s41467-026-74374-5) · [核验与筛查依据](docs/CATALOG.md#P121)

<a id="P189"></a>

- 📘 **[2026 · Communications Engineering] [Synapse-inspired energy networks: a neuromorphic approach to microgrid protection without communication links](https://www.nature.com/articles/s44172-026-00643-2)** · `P189` · `本轮新增`

  **发表：** 2026-03-23（在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 针对分布式微电网中传统保护依赖高故障电流和通信链路的问题，提出仿神经脉冲的保护架构。分布式电源依据本地电压、电流形成反映扰动程度的脉冲，利用电力线路实现协同，以首次脉冲触发断路及故障定位。文中测试报告快速跳闸和较高检测、空间选择准确率，减少对外部通信与同步的依赖。

  **遗忘筛查：** 邻近但非遗忘。神经形态脉冲用于故障检测和保护，不以删除已训练模型中的数据或概念为目标。

  [DOI](https://doi.org/10.1038/s44172-026-00643-2) · [核验与筛查依据](docs/CATALOG.md#P189)

<a id="P166"></a>

- 📘 **[2024 · Nature Communications] [Real-time outage management in active distribution networks using reinforcement learning over graphs](https://www.nature.com/articles/s41467-024-49207-y)** · `P166` · `本轮新增`

  **发表：** 2024-06-04（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 将配电网停电后的开关重构和紧急减载建模为图强化学习问题，通过胶囊式图神经网络同时表示网络拓扑变化及节点、边状态的相互依赖。IEEE 13、34和123节点改造系统的验证显示，方法能快速生成接近最优的恢复策略，并对不同停电场景保持泛化能力。

  **遗忘筛查：** 邻近但非遗忘。图强化学习用于停电恢复；切换线路或改变网络拓扑是物理控制，不是模型遗忘。

  [DOI](https://doi.org/10.1038/s41467-024-49207-y) · [核验与筛查依据](docs/CATALOG.md#P166)

<a id="P022"></a>

- 📘 **[2024 · Nature Communications] [Early warning and proactive control strategies for power blackouts caused by gas network malfunctions](https://www.nature.com/articles/s41467-024-48964-0)** · `P022`

  **发表：** 2024-06-03（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究天然气系统故障向电力系统传播引起停电的问题，利用故障信息传递和发电重调度快于气体压力异常传播的时间差，提出气电联合预警与主动控制方法。中国实际耦合系统算例验证其降低停电影响的潜力，重点在基础设施耦合和提前干预。

  [DOI](https://doi.org/10.1038/s41467-024-48964-0) · [核验与筛查依据](docs/CATALOG.md#P022)

<a id="P085"></a>

- 📚 **[2024 · Nature Reviews Electrical Engineering] [Power electronics in wind generation systems](https://www.nature.com/articles/s44287-024-00032-x)** · `P085`

  **发表：** 2024-03-26（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 回顾风电与电力电子技术发展，重点讨论风机从跟随电网转向主动参与系统调节与频率支撑。结合先进变流器控制和欧洲研究示范项目，梳理高风电渗透率、低惯量系统的并网要求及后续研究方向。

  [DOI](https://doi.org/10.1038/s44287-024-00032-x) · [核验与筛查依据](docs/CATALOG.md#P085)

[返回导航](#导航)

<a id="topic-5"></a>
### 电网规划、互联与新能源融合（41条）

<a id="P056"></a>

- 📘 **[2026 · Nature Sustainability] [Navigating the land–energy nexus for carbon-neutral power systems in China](https://www.nature.com/articles/s41893-026-01941-5)** · `P056`

  **发表：** 2026-09-30（在线发表日期） · **类型：** Analysis · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 论文耦合网格化风光容量评估与时空分辨的电力系统优化，研究土地约束如何改变中国碳中和路径。需求附近的中东部土地具有较高系统价值；严格用地限制使新能源向资源富集地区转移，到2060年跨区输电需求约增加20%，年度系统成本最多增加约4.1%。结果说明土地政策、输电规划与电价机制需要联合考虑。

  [DOI](https://doi.org/10.1038/s41893-026-01941-5) · [核验与筛查依据](docs/CATALOG.md#P056)

<a id="P177"></a>

- 📘 **[2026 · Joule] [A minimal methanol backstop for high-electrification scenarios](https://doi.org/10.1016/j.joule.2026.102464)** · `P177` · `本轮新增`

  **发表：** 2026-09-16（卷期日期；在线首发具体日期待核验，同属2026年） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对高度电气化系统仍需航空、航运、备用发电和化工燃料的情况，提出以少量甲醇作为剩余需求的后备。利用欧洲碳中和能源系统模型比较甲醇与氢路径，发现甲醇方案仅小幅增加系统成本，却可减少气体运输储存及基础设施协调的复杂度。结果为电力系统与难电气化部门之间的能源载体、备用能力和基础设施选择提供比较。

  [DOI](https://doi.org/10.1016/j.joule.2026.102464) · [核验与筛查依据](docs/CATALOG.md#P177)

<a id="P122"></a>

- 📘 **[2026 · Nature Communications] [Rethinking the economics and flexibility of U.S. nuclear power through hydrogen integration and policy support](https://www.nature.com/articles/s41467-026-73630-y)** · `P122` · `本轮新增`

  **发表：** 2026-06-02（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究美国既有核电站通过高温电解制氢和辅助服务参与，提高经济性及运行灵活性的潜力。逐小时优化与全生命周期技术经济分析相结合，评估改造、成本下降和政策支持的作用。结果表明，合理的核氢耦合及市场参与可改善净现值并扩大灵活输出，为新能源比例上升下的电网可靠运行提供支撑。

  [DOI](https://doi.org/10.1038/s41467-026-73630-y) · [核验与筛查依据](docs/CATALOG.md#P122)

<a id="P125"></a>

- 📘 **[2026 · Nature Communications] [Flexibility-aware framework for efficient planner-initiated siting of data center](https://www.nature.com/articles/s41467-026-72324-9)** · `P125` · `本轮新增`

  **发表：** 2026-05-16（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 面向大型人工智能数据中心并网缓慢的问题，提出规划方主动选址流程，先以可靠性约束筛选，再评估不同负荷暂停和迁移能力下的市场影响，并进行多指标排序。德州2000节点合成系统案例表明，运行灵活性可增加可选接入位置，为加快接电与控制电网压力提供依据。

  [DOI](https://doi.org/10.1038/s41467-026-72324-9) · [核验与筛查依据](docs/CATALOG.md#P125)

<a id="P029"></a>

- 📘 **[2026 · Nature Energy] [Integrated planning of net-zero power systems for all](https://www.nature.com/articles/s41560-026-02054-1)** · `P029`

  **发表：** 2026-05-04（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 构建具有高空间分辨率和全年逐小时分辨率的全球电力模型，联合优化容量扩张与运行，兼顾净零排放和基本用电公平。研究情景下，满足普遍电力需求的净零系统技术上可行，需要大量风光装机；需求侧管理、跨国输电以及降低新能源贸易壁垒均能削减系统成本，凸显协同规划价值。

  [DOI](https://doi.org/10.1038/s41560-026-02054-1) · [核验与筛查依据](docs/CATALOG.md#P029)

<a id="P071"></a>

- 📚 **[2026 · Nature Computational Science] [Sustainability as a challenge in complex systems dynamics](https://www.nature.com/articles/s43588-026-00971-5)** · `P071`

  **发表：** 2026-04-23（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 综述基础设施复杂系统的集体动力学，重点讨论电力供应与可持续交通。围绕流中断、供需波动和分布式需求引起的非平衡状态，提出结合数据驱动、计算建模与理论分析理解系统失效并指导可持续设计。

  [DOI](https://doi.org/10.1038/s43588-026-00971-5) · [核验与筛查依据](docs/CATALOG.md#P071)

<a id="P127"></a>

- 📘 **[2026 · Nature Communications] [Exploring the feasible net-zero transition pathway in China considering energy system flexibility](https://www.nature.com/articles/s41467-026-71410-2)** · `P127` · `本轮新增`

  **发表：** 2026-04-11（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 在能源—经济—环境模型中加入逐小时负荷、电力平衡、储能运行及需求响应，分析中国净零路径的灵活性约束。更细时间刻画会暴露陡峭爬坡与晚高峰压力，并提高最优减排成本；负荷移时和车网互动可减少部分储能投资，改善可靠性与成本之间的权衡。

  [DOI](https://doi.org/10.1038/s41467-026-71410-2) · [核验与筛查依据](docs/CATALOG.md#P127)

<a id="P128"></a>

- 📘 **[2026 · Nature Communications] [Bulk electrical power extraction through tunnel transmission technology from renewable energy concentrated zones](https://www.nature.com/articles/s41467-026-71221-5)** · `P128` · `本轮新增`

  **发表：** 2026-04-02（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对山区新能源基地外送受地形和生态约束的问题，结合电磁、热流体仿真与全寿命成本评估，比较架空线路、气体绝缘线路及电缆隧道方案。结果说明，导体布置和通风优化可以提升输送容量；在土地、景观及环境外部成本较高的地区，地下气体绝缘输电具备经济竞争力。

  [DOI](https://doi.org/10.1038/s41467-026-71221-5) · [核验与筛查依据](docs/CATALOG.md#P128)

<a id="P043"></a>

- 📚 **[2026 · Joule] [What can we learn from US national transmission studies?](https://www.sciencedirect.com/science/article/pii/S2542435126000231)** · `P043`

  **发表：** 2026-02-18（卷期日期；精确在线首发日待核验） · **类型：** Commentary · **范围：** 核心期刊电网文献

  **内容概述（导语或机构摘要）：** 综合七项美国全国尺度输电研究，比较不同技术和政策情景下的电网扩建需求。多数情景认为到2050年输电规模至少应翻倍，以接纳新负荷和电源并提高可靠性。研究普遍发现显著净成本节约及较高投资收益，建议加强全国协同、多情景和发输电联合优化。

  [DOI](https://doi.org/10.1016/j.joule.2026.102339) · [核验与筛查依据](docs/CATALOG.md#P043)

<a id="P095"></a>

- 📚 **[2026 · Nature Reviews Electrical Engineering] [A systems engineering approach to enhance utilization of renewable energy](https://www.nature.com/articles/s44287-025-00253-8)** · `P095` · `本轮新增`

  **发表：** 2026-01-09（在线发表日期） · **类型：** Comment · **范围：** 交叉与扩展期刊

  **内容概述（出版社导语，无正式摘要）：** 评论讨论电力系统大规模、充分利用可再生能源面临的挑战，主张采用系统工程视角贯通预测、分析、调度和控制。通过强调运行各环节的协同，提出提高新能源利用水平的研究方向。该文属于方法论倡议，出版社公开导语未报告特定算法的实验结果。

  [DOI](https://doi.org/10.1038/s44287-025-00253-8) · [核验与筛查依据](docs/CATALOG.md#P095)

<a id="P131"></a>

- 📘 **[2025 · Nature Communications] [The benefits of exploring a large scenario space for future energy systems](https://www.nature.com/articles/s41467-025-67593-9)** · `P131` · `本轮新增`

  **发表：** 2025-12-23（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对能源规划常使用少量情景而难以覆盖不确定性的问题，提出同时比较超过一万种情景的多指标分析方法，并用于德国电力系统。结果显示，多天气年假设对成本、供电安全和可持续性影响尤其明显，提示稳健规划需要充分探索参数和方法选择，而非依赖单一情景。

  **备注：** 在线首发2025，卷期2026；主年份按在线首发统计。

  [DOI](https://doi.org/10.1038/s41467-025-67593-9) · [核验与筛查依据](docs/CATALOG.md#P131)

<a id="P191"></a>

- 📘 **[2025 · Communications Engineering] [Transforming offshore wind farms into synergistic aggregators to enhance renewable integration and grid flexibility—an Eastern China example](https://www.nature.com/articles/s44172-025-00563-7)** · `P191` · `本轮新增`

  **发表：** 2025-12-08（在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 以中国东部为例，将海上风电场与沿海电厂、储能和海洋牧场组织为协同聚合体，联合优化建设及运行，提升新能源消纳和电网灵活性。研究比较不同储能与柔性负荷配置，评估成本、风电利用及调频收益，说明海洋产业用能与发电协同的潜力，同时指出区域政策和生物物理条件对推广的限制。

  **备注：** 在线首发年份为2025，卷期年份为2026；按在线首发年统计。

  [DOI](https://doi.org/10.1038/s44172-025-00563-7) · [核验与筛查依据](docs/CATALOG.md#P191)

<a id="P134"></a>

- 📘 **[2025 · Nature Communications] [Considering distributive justice as a planning principle helps navigate a diversity of future energy infrastructure designs](https://www.nature.com/articles/s41467-025-65526-0)** · `P134` · `本轮新增`

  **发表：** 2025-11-25（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 将分配正义指标纳入欧洲低碳能源基础设施设计，比较不同公平观念和公众偏好下的技术配置。分析发现，公平标准可在不显著增加成本的情况下缩小可行方案范围；结合公众意见能提高技术容量建议的一致性，为兼顾系统约束和社会接受度的规划提供支持。

  [DOI](https://doi.org/10.1038/s41467-025-65526-0) · [核验与筛查依据](docs/CATALOG.md#P134)

<a id="P181"></a>

- 📚 **[2025 · Joule] [Near-optimal energy planning strategies with modeling to generate alternatives to flexibly explore practically desirable options](https://doi.org/10.1016/j.joule.2025.102144)** · `P181` · `本轮新增`

  **发表：** 2025-11-19（卷期日期；作者机构确认2025年10月已发表，在线具体日待核验） · **类型：** Perspective · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 讨论仅寻找最低成本能源规划方案可能带来的确定性错觉，指出成本相近的替代方案可能更符合社会接受度、韧性等难以量化的要求。论文梳理生成替代方案建模的计算与解释进展，提出五个逐步深入的应用层次，支持系统探索近最优解及其权衡。即使采用较简单的层次，也可改善能源及电力基础设施规划建议的实用性。

  [DOI](https://doi.org/10.1016/j.joule.2025.102144) · [核验与筛查依据](docs/CATALOG.md#P181)

<a id="P139"></a>

- 📘 **[2025 · Nature Communications] [Identifying key uncertainties in energy transitions with a Puerto Rico case study](https://www.nature.com/articles/s41467-025-64143-1)** · `P139` · `本轮新增`

  **发表：** 2025-10-13（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 通过代理模型和敏感性分析，识别能源转型中技术、经济、社会与气候不确定性的主要来源。波多黎各案例显示，飓风发生频率与组织运行低效对预期系统成本影响突出；不同技术路线下的重要变量也会改变，说明电力规划应针对情景识别关键风险，而非只采用单组参数。

  **遗忘筛查：** 邻近但非遗忘。涉及预测、智能建模或优化，但所读摘要未定义遗忘对象、删除已学习影响的目标及有效性验证。

  [DOI](https://doi.org/10.1038/s41467-025-64143-1) · [核验与筛查依据](docs/CATALOG.md#P139)

<a id="P140"></a>

- 📘 **[2025 · Nature Communications] [Regional coordination can alleviate the cost burden of a low-carbon electricity system](https://www.nature.com/articles/s41467-025-64093-8)** · `P140` · `本轮新增`

  **发表：** 2025-10-10（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 在可再生资源分布不均且技术成本存在不确定性的南美区域，比较各国独立规划与跨国协同的低碳电力路径。区域协调可利用资源互补，降低新增发电需求和减排额外成本，并缓解部分规划不确定性；同时，各国具体技术配置仍对技术经济假设敏感。

  [DOI](https://doi.org/10.1038/s41467-025-64093-8) · [核验与筛查依据](docs/CATALOG.md#P140)

<a id="P088"></a>

- 📘 **[2025 · Nature Sustainability] [Strategizing renewable energy transitions to preserve sediment transport integrity](https://www.nature.com/articles/s41893-025-01626-5)** · `P088` · `本轮新增`

  **发表：** 2025-09-26（出版社在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究将水文、泥沙与电力规划结合，评估湄公河流域水电扩张和风光储替代方案。全面开发大型水电会使入海泥沙大幅减少；以风电、光伏和储能替代19座高拦沙坝，可保留最多98%的泥沙输送，而2020—2050年系统成本增加约4%—6%。计入泥沙的生态收益后，新增成本可基本抵消，说明跨境电力规划应同时考虑河流生态约束。

  **备注：** 出版社列有2025-10-06 Publisher Correction；采用当前原文摘要，首次发表日期仍为2025-09-26。

  [DOI](https://doi.org/10.1038/s41893-025-01626-5) · [核验与筛查依据](docs/CATALOG.md#P088)

<a id="P046"></a>

- 📘 **[2025 · Joule] [Assess space-based solar power for European-scale power system decarbonization](https://www.sciencedirect.com/science/article/pii/S2542435125002557)** · `P046`

  **发表：** 2025-09-17（卷期日期；在线首发日待核验） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 采用欧洲电力容量扩张和调度模型，评估两类天基太阳能方案在2050年净零系统中的价值。近连续发电的反射镜集群设计在特定成本假设下可减少系统成本和风光、储能需求；较成熟的平面阵列方案在预测成本下尚不经济。研究给出由补充电源转为主力电源的成本门槛，同时指出季节性平衡仍需要储能。

  [DOI](https://doi.org/10.1016/j.joule.2025.102074) · [核验与筛查依据](docs/CATALOG.md#P046)

<a id="P143"></a>

- 📘 **[2025 · Nature Communications] [Opportunities for decentralised solar power to improve reliability, reduce emissions and avoid stranded assets](https://www.nature.com/articles/s41467-025-62948-8)** · `P143` · `本轮新增`

  **发表：** 2025-08-28（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用能源系统模型分析农村光伏微电网与国家电网互联的收益和投资风险。研究发现，互联微电网可在改善供电可靠性的同时降低单位电费和碳强度；用户需求小幅下降影响有限，但较大幅度流失会损害经济性，因此需要制度安排协调主网改善与分布式投资。

  [DOI](https://doi.org/10.1038/s41467-025-62948-8) · [核验与筛查依据](docs/CATALOG.md#P143)

<a id="P146"></a>

- 📘 **[2025 · Nature Communications] [Grid congestion stymies climate benefit from U.S. vehicle electrification](https://www.nature.com/articles/s41467-025-61976-8)** · `P146` · `本轮新增`

  **发表：** 2025-08-06（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究美国汽车电气化的减排收益如何受输电网络拥塞影响。模型显示，即使增加大量可再生发电，现有线路容量仍可能限制清洁电力送达充电负荷，使车辆减排潜力无法兑现。适度且有针对性的输电扩容能够释放收益，强调交通电气化与电网建设需协同规划。

  [DOI](https://doi.org/10.1038/s41467-025-61976-8) · [核验与筛查依据](docs/CATALOG.md#P146)

<a id="P051"></a>

- 📘 **[2025 · Science Advances] [Quantifying effects of solar power adoption on CO2 emissions reduction](https://www.science.org/doi/10.1126/sciadv.adq5660)** · `P051`

  **发表：** 2025-07-30（在线发表日期） · **类型：** Research Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究使用2018年7月起的五年美国能源信息署数据，以分布滞后统计模型估计光伏增发对本地及相邻区域排放的即时和滞后影响。分析发现光伏的减排收益具有显著时空差异和跨区域联系；光伏发电增加15%与每年减少约854万吨二氧化碳相关。结果为电网互联背景下清洁电源投资的区域协同提供依据。

  [DOI](https://doi.org/10.1126/sciadv.adq5660) · [核验与筛查依据](docs/CATALOG.md#P051)

<a id="P148"></a>

- 📘 **[2025 · Nature Communications] [Delivering equity in low-carbon multisector infrastructure planning](https://www.nature.com/articles/s41467-025-59738-7)** · `P148` · `本轮新增`

  **发表：** 2025-06-19（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 将河流流域与电力系统仿真、人工智能辅助方案设计相结合，研究加纳低碳基础设施投资中的空间公平。结果显示，改善水电服务分配需要同步考虑粮食生产、生态和排放目标；增加可再生能源及输电投资有助于避免在改善公平时反而提高排放或供电削减。

  [DOI](https://doi.org/10.1038/s41467-025-59738-7) · [核验与筛查依据](docs/CATALOG.md#P148)

<a id="P149"></a>

- 📘 **[2025 · Nature Communications] [Green energy and steel imports reduce Europe’s net-zero infrastructure needs](https://www.nature.com/articles/s41467-025-60652-1)** · `P149` · `本轮新增`

  **发表：** 2025-06-12（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 把全球能源供应链与欧洲能源系统模型耦合，比较进口电力、氢能及绿色衍生产品对净零基础设施的影响。进口可以降低成本和本土建设压力，但收益随规模增加而递减；保留部分国内电转化生产有助于消纳波动性新能源，提示进口政策应与电力基础设施规划协同。

  [DOI](https://doi.org/10.1038/s41467-025-60652-1) · [核验与筛查依据](docs/CATALOG.md#P149)

<a id="P182"></a>

- 📘 **[2025 · Joule] [Pathways to national-scale adoption of enhanced geothermal power through experience-driven cost reductions](https://doi.org/10.1016/j.joule.2025.101971)** · `P182` · `本轮新增`

  **发表：** 2025-06-04（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 把有实证基础的增强型地热成本估计与经验曲线结合，模拟截至2050年的美国电力系统部署路径。研究发现，先利用西部高质量资源实现商业化和成本下降，可能使该技术扩展到更广地区，提供可观比例的稳定无碳电力并降低脱碳成本。初始成本偏高会限制增长，支持政策能够缓解这一障碍；文中学习指技术经验带来的成本下降。

  [DOI](https://doi.org/10.1016/j.joule.2025.101971) · [核验与筛查依据](docs/CATALOG.md#P182)

<a id="P097"></a>

- 📚 **[2025 · Nature Reviews Electrical Engineering] [Hydrogen as the nexus of future sustainable transport and energy systems](https://www.nature.com/articles/s44287-025-00178-2)** · `P097` · `本轮新增`

  **发表：** 2025-06-02（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 综述绿氢与燃料电池汽车如何连接低碳交通和能源系统，促进间歇性新能源并网、储能与系统灵活性。文章梳理制氢、燃料电池和加氢基础设施进展，讨论规模化应用的技术、经济及监管障碍，并提出协调制氢与能源交通需求的研究、政策和投资路线。

  [DOI](https://doi.org/10.1038/s44287-025-00178-2) · [核验与筛查依据](docs/CATALOG.md#P097)

<a id="P090"></a>

- 📘 **[2025 · Nature Sustainability] [Trading off regional and overall energy system design flexibility in the net-zero transition](https://www.nature.com/articles/s41893-025-01556-2)** · `P090` · `本轮新增`

  **发表：** 2025-05-02（出版社在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究利用优化模型描绘欧洲2050年净零能源系统的近最优方案，考察区域自主选择与整体稳健性之间的权衡，并纳入不同气象年、成本和土地约束。多数地区存在较大的技术替代空间，但部分区域的光伏或风电难以替代。国家可调整新能源出口与氢能策略，但需协调互联系统；南欧与德国增加光伏投入可扩大欧洲整体的设计选择。

  [DOI](https://doi.org/10.1038/s41893-025-01556-2) · [核验与筛查依据](docs/CATALOG.md#P090)

<a id="P010"></a>

- 📘 **[2025 · Nature Communications] [Global spatiotemporal optimization of photovoltaic and wind power to achieve the Paris Agreement targets](https://www.nature.com/articles/s41467-025-57292-w)** · `P010`

  **发表：** 2025-03-03（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 对192个国家的风电与光伏项目进行时空优化，将储能、输电、技术学习、矿产贸易和供应链纳入低碳转型方案。联合协调能够降低模型估计的减排成本并扩大风光部署。研究提供全球电力转型路线，同时指出资金、资源和社会经济条件的约束。

  [DOI](https://doi.org/10.1038/s41467-025-57292-w) · [核验与筛查依据](docs/CATALOG.md#P010)

<a id="P155"></a>

- 📘 **[2025 · Nature Communications] [Electricity- and hydrogen-driven energy system sector-coupling in net-zero CO2 emission pathways](https://www.nature.com/articles/s41467-025-56365-0)** · `P155` · `本轮新增`

  **发表：** 2025-02-04（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用多种能源系统和综合评估模型，在统一深度脱碳情景下比较欧洲电力与氢能部门耦合路径。模型显示，2050年终端能源中电力和直接用氢的平均占比可分别达到约60%和6%，需要大规模扩张风光发电。电气化在各部门具有成本优势，氢能贡献较小但必要；模型间差异反映路径及氢能作用的不确定性。

  [DOI](https://doi.org/10.1038/s41467-025-56365-0) · [核验与筛查依据](docs/CATALOG.md#P155)

<a id="P184"></a>

- 📚 **[2025 · Joule] [System impacts of wind energy developments: Key research challenges and opportunities](https://doi.org/10.1016/j.joule.2024.11.016)** · `P184` · `本轮新增`

  **发表：** 2025-01-13（在线发表日期） · **类型：** Review · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 综述风电扩大部署与技术、经济、社会及自然环境的相互影响，梳理已有解决方案和研究空白。电网及市场整合虽常被视为主要障碍，实际已存在多种技术方案；规划许可仍是许多地区的近期瓶颈。野生动物影响、叶片回收及高比例风电系统运行等问题仍需研究，为大规模风电接入和跨部门协同提供系统性框架。

  [DOI](https://doi.org/10.1016/j.joule.2024.11.016) · [核验与筛查依据](docs/CATALOG.md#P184)

<a id="P049"></a>

- 📘 **[2024 · Joule] [Grid connection barriers to renewable energy deployment in the United States](https://www.sciencedirect.com/science/article/pii/S2542435124005038)** · `P049`

  **发表：** 2024-12-06（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 整理超过3.8万条项目级并网记录，分析美国风电、光伏和储能项目的并网瓶颈。待并网容量超过现有发电装机两倍，并网所需时间较十年前增加约70%，退出比例居高。高额及不确定的网络升级费用与项目退出相关，研究建议加强长期输电规划与项目并网流程衔接，并提高结果透明度。

  **备注：** 在线首发年份为2024，卷期年份为2025；按在线首发年统计。

  [DOI](https://doi.org/10.1016/j.joule.2024.11.008) · [核验与筛查依据](docs/CATALOG.md#P049)

<a id="P091"></a>

- 📘 **[2024 · Nature Sustainability] [A renewable and socially accepted energy system for astronomical telescopes](https://www.nature.com/articles/s41893-024-01442-3)** · `P091` · `本轮新增`

  **发表：** 2024-10-11（出版社在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 偏远天文台通常依赖化石燃料独立供电，周边社区的需求也易被忽略。研究结合能源系统优化与参与式多准则分析，为阿塔卡马拟建望远镜设计可再生供电方案。结果表明，在不增设容量的情况下，该系统还可满足附近社区约66%的用能需求；将方案推广至邻近天文台有望减少化石发电及排放，利益共享也能改善方案的社会接受度。

  [DOI](https://doi.org/10.1038/s41893-024-01442-3) · [核验与筛查依据](docs/CATALOG.md#P091)

<a id="P161"></a>

- 📘 **[2024 · Nature Communications] [Diverse decarbonization pathways under near cost-optimal futures](https://www.nature.com/articles/s41467-024-52433-z)** · `P161` · `本轮新增`

  **发表：** 2024-09-17（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用能源系统优化探索美国多条接近最低成本的净零路径，避免把单一最优解当作唯一可行未来。不同路径普遍需要快速扩张风光发电、减少煤油使用并推进终端电气化，但天然气、氢能和负排放技术配置差异明显，揭示技术组合与相近总成本之间的替代关系。

  [DOI](https://doi.org/10.1038/s41467-024-52433-z) · [核验与筛查依据](docs/CATALOG.md#P161)

<a id="P194"></a>

- 📘 **[2024 · Communications Engineering] [Decentralized dynamic system for optimal power dispatch in wind farms based on node-dependence nature](https://www.nature.com/articles/s44172-024-00258-5)** · `P194` · `本轮新增`

  **发表：** 2024-08-18（在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 针对风电场功率分配中全局功率约束与分散电压控制难以兼顾的问题，利用节点依赖关系及功率灵敏度构造完全分散的动态调度方法。各控制器依据本地测量执行梯度投影迭代，在满足总功率需求的同时优化电压。论文分析收敛性质，并通过仿真检验接近全局最优解的能力。

  [DOI](https://doi.org/10.1038/s44172-024-00258-5) · [核验与筛查依据](docs/CATALOG.md#P194)

<a id="P025"></a>

- 📘 **[2024 · Nature Communications] [Offshore wind and wave energy can reduce total installed capacity required in zero-emissions grids](https://www.nature.com/articles/s41467-024-50040-6)** · `P025`

  **发表：** 2024-08-09（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 在美国西部2050年零排放电力系统容量扩展模型中，分别和联合考虑海上风电与波浪能。研究确定其具备经济竞争力所需的成本条件，并分析对发电、弃电和输电的影响；在充分部署情景中，技术互补可减少系统需要的总装机。

  [DOI](https://doi.org/10.1038/s41467-024-50040-6) · [核验与筛查依据](docs/CATALOG.md#P025)

<a id="P048"></a>

- 📚 **[2024 · Joule] [The evolving long tail at the edge of the grid: Benefits and concerns](https://www.sciencedirect.com/science/article/pii/S2542435124001892)** · `P048`

  **发表：** 2024-06-19（卷期日期；在线首发日待核验） · **类型：** Perspective · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 文章分析分布式能源普及带来的电网边缘“长尾”结构：设备、服务商和商业模式高度分散，参与主体的能力、资源和动机差异明显。这一变化可提高能源安全并带来环境收益，同时产生协调、监管和安全问题。作者讨论资源规划、网络安全、公平性及治理机制需要如何适应。

  [DOI](https://doi.org/10.1016/j.joule.2024.04.005) · [核验与筛查依据](docs/CATALOG.md#P048)

<a id="P062"></a>

- 📘 **[2024 · Nature Sustainability] [Rethinking energy planning to mitigate the impacts of African hydropower](https://www.nature.com/articles/s41893-024-01367-x)** · `P062`

  **发表：** 2024-06-04（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对非洲拟建水电与可再生能源竞争、河流生态及水库排放的矛盾，研究提出联合能源规划框架。相较单纯最低成本规划，同时考虑环境和技术经济目标的扩容方案可使水电年度排放和河流破碎化影响至少降低50%，而电价与总贴现成本增幅分别不超过1.4%和0.2%。结果支持将生态指标直接纳入电源扩展决策。

  [DOI](https://doi.org/10.1038/s41893-024-01367-x) · [核验与筛查依据](docs/CATALOG.md#P062)

<a id="P039"></a>

- 📘 **[2024 · Nature Energy] [A geographically disaggregated approach to integrate low-carbon technologies across local electricity networks](https://www.nature.com/articles/s41560-024-01542-6)** · `P039`

  **发表：** 2024-05-27（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 将英国超过4万个地区的细粒度空间数据与网络仿真结合，估计分布式光伏、热泵和电动汽车普及引起的配电网升级成本。成本及灵活性资源价值存在显著地区差异，城市和高电气化地区通常承压更大。按地理特征定向配置灵活性，相比将地区视作同质的方案，可节省数亿英镑升级投资。

  **遗忘筛查：** 邻近但非遗忘。正文使用神经网络元模型与聚类进行网络成本估计；未提出训练数据删除或概念撤回，普通机器学习不是机器遗忘。

  [DOI](https://doi.org/10.1038/s41560-024-01542-6) · [核验与筛查依据](docs/CATALOG.md#P039)

<a id="P167"></a>

- 📘 **[2024 · Nature Communications] [Carbon pricing and system reliability impacts on pathways to universal electricity access in Africa](https://www.nature.com/articles/s41467-024-48450-7)** · `P167` · `本轮新增`

  **发表：** 2024-05-16（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 通过高分辨率地理空间分析，比较撒哈拉以南非洲实现居民普遍电力接入的低成本路径，并显式纳入供电可靠性和碳价。惩罚未满足需求或引入碳价会提高离网光伏方案的份额；不同国家的最优干预程度差异明显，说明并网扩展与离网供电应结合需求等级评估。

  [DOI](https://doi.org/10.1038/s41467-024-48450-7) · [核验与筛查依据](docs/CATALOG.md#P167)

<a id="P168"></a>

- 📘 **[2024 · Nature Communications] [Limited impact of hydrogen co-firing on prolonging fossil-based power generation under low emissions scenarios](https://www.nature.com/articles/s41467-024-46101-5)** · `P168` · `本轮新增`

  **发表：** 2024-03-04（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用全球能源系统模型评估氢或氨混烧对现有化石电源退役的影响。在严格减排情景下，部分煤气机组可通过混烧改造提供后备平衡能力，但受燃料成本和低利用小时约束，其发电占比仍很小。研究认为这一灵活性选项不太可能显著推迟化石电源退出。

  [DOI](https://doi.org/10.1038/s41467-024-46101-5) · [核验与筛查依据](docs/CATALOG.md#P168)

<a id="P061"></a>

- 📘 **[2024 · Nature Sustainability] [Hydropower expansion in eco-sensitive river basins under global energy-economic change](https://www.nature.com/articles/s41893-023-01260-z)** · `P061`

  **发表：** 2024-01-22（在线发表日期） · **类型：** Analysis · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究利用能源—水—经济综合模型，比较全球20个生态敏感流域在经济增长、低碳转型及风光并网条件变化下的水电扩展。低碳转型带来的开发压力最强，到2050年超过72%的流域可能开发逾80%的可利用水能。增强风光整合能缓解部分水电开发需求，但不足以完全抵消低碳转型压力。

  [DOI](https://doi.org/10.1038/s41893-023-01260-z) · [核验与筛查依据](docs/CATALOG.md#P061)

<a id="P038"></a>

- 📘 **[2024 · Nature Energy] [The influence of additionality and time-matching requirements on the emissions from grid-connected hydrogen production](https://www.nature.com/articles/s41560-023-01435-0)** · `P038`

  **发表：** 2024-01-08（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究并网电解制氢的用电与可再生能源合同采用年度或小时匹配时的排放差异。不同论文结论的分歧部分源于对新增性及制氢与其他负荷争夺绿电的假设不同。系统政策情景表明，时序匹配规则的排放效果取决于电网和政策背景，作者提出随电力脱碳进程动态调整要求。

  [DOI](https://doi.org/10.1038/s41560-023-01435-0) · [核验与筛查依据](docs/CATALOG.md#P038)

[返回导航](#导航)

<a id="topic-6"></a>
### 电力市场、政策与转型（29条）

<a id="P113"></a>

- 📘 **[2026 · Nature Communications] [Cross-border electricity tariffs undermine power system efficiency, decarbonization and reliability in North America](https://www.nature.com/articles/s41467-026-77773-w)** · `P113` · `本轮新增`

  **发表：** 2026-10-01（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 结合纽约十年电力市场数据和电力系统仿真，评估对加拿大进口电力加征关税的影响。结果显示，贸易受限会使水电及核电进口被化石发电替代，推高价格与排放、削弱经济福利，并压缩运行备用。极端冬季扰动下的停电风险也随之增加，凸显跨境互联的可靠性价值。

  [DOI](https://doi.org/10.1038/s41467-026-77773-w) · [核验与筛查依据](docs/CATALOG.md#P113)

<a id="P169"></a>

- 📘 **[2026 · Nature Climate Change] [The impact of financing cost differences on global energy and industry decarbonization](https://www.nature.com/articles/s41558-026-02756-0)** · `P169` · `本轮新增`

  **发表：** 2026-09-24（出版社在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究将动态、分国家和分行业的资本成本纳入IMAGE综合评估模型，覆盖八类能源与工业部门。相较统一低风险融资假设，发展中国家的投资风险使全球控温减排成本增加约9%，并使减排行动偏向低风险地区。细化融资条件还会减少发展中国家的电网投资、提高绿氢成本并延缓电解制氢发展，显示电网扩建和脱碳路径对金融条件的敏感性。

  [DOI](https://doi.org/10.1038/s41558-026-02756-0) · [核验与筛查依据](docs/CATALOG.md#P169)

<a id="P178"></a>

- 📚 **[2026 · Joule] [Governing AI infrastructure on decarbonizing grids](https://doi.org/10.1016/j.joule.2026.102647)** · `P178` · `本轮新增`

  **发表：** 2026-09-10（在线发表日期） · **类型：** Commentary · **范围：** 核心期刊电网文献

  **内容概述（作者机构说明）：** 基于人工智能与能源转型跨学科研讨，讨论数据中心快速扩张带来的电网容量、脱碳及地方利益分配问题。文章提出把接网条件与灵活性提供、运行透明度和社区收益相联系，强调公开适当的用电信息、协调基础设施规划及成本承担。该治理思路旨在使人工智能基础设施扩张与供电系统能力、环境目标及地方需求相协调。

  [DOI](https://doi.org/10.1016/j.joule.2026.102647) · [核验与筛查依据](docs/CATALOG.md#P178)

<a id="P116"></a>

- 📘 **[2026 · Nature Communications] [Understanding the European energy crisis through structural causal models](https://www.nature.com/articles/s41467-026-75433-7)** · `P116` · `本轮新增`

  **发表：** 2026-07-17（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对欧洲能源危机中法国虽少用天然气却出现显著电价上涨的现象，构建因果图分析法国和西班牙市场的电价与净出口。研究结合线性结构因果模型、树模型及Shapley Flow，区分天然气价格与核电不可用性的联合作用，量化间接影响和反事实情景，说明相关分析可能掩盖市场传导机制。

  **遗忘筛查：** 邻近但非遗忘。因果统计与机器学习用于电价解释，不涉及删除训练数据或概念。

  [DOI](https://doi.org/10.1038/s41467-026-75433-7) · [核验与筛查依据](docs/CATALOG.md#P116)

<a id="P179"></a>

- 📚 **[2026 · Joule] [Revisiting the relationship between demand growth and electricity prices](https://doi.org/10.1016/j.joule.2026.102528)** · `P179` · `本轮新增`

  **发表：** 2026-07-15（卷期日期；作者机构确认2026年6月已发表，在线具体日待核验） · **类型：** Commentary · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对数据中心等工商业负荷增长必然推高电价的常见判断，重新梳理需求与电价的短期及长期关系。文章从系统容量利用率、扩建成本和电价设计中的成本分配三个维度展开，解释历史需求增长为何常伴随电价下降，也分析未来增长可能推升费用的条件。研究强调新增需求的价格影响取决于电网约束、投资及费用分摊机制。

  [DOI](https://doi.org/10.1016/j.joule.2026.102528) · [核验与筛查依据](docs/CATALOG.md#P179)

<a id="P118"></a>

- 📘 **[2026 · Nature Communications] [Assessing grid affordability for universal electricity access in Sub-Saharan Africa](https://www.nature.com/articles/s41467-026-75104-7)** · `P118` · `本轮新增`

  **发表：** 2026-07-09（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 汇集撒哈拉以南非洲48国居民电价，并结合收入分布和分级用电需求评估支付能力。结果显示，大量居民难以负担较高等级的电力服务；将居民负担与公用事业财务状况共同分析，可识别电网扩展的可行地区及电气化陷阱，支持并网和离网方案的差异化选择。

  [DOI](https://doi.org/10.1038/s41467-026-75104-7) · [核验与筛查依据](docs/CATALOG.md#P118)

<a id="P123"></a>

- 📘 **[2026 · Nature Communications] [EU-ETS emergency reserve price curbs coal use and shields consumers during natural gas price shocks](https://www.nature.com/articles/s41467-026-73559-2)** · `P123` · `本轮新增`

  **发表：** 2026-05-25（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用欧洲能源危机期间13个欧盟国家的逐小时电力市场数据，估计天然气价格冲击对燃煤发电、排放及电价的影响。研究比较现有天然气价格上限与排放交易应急机制，提出在气价超过历史基准时自动启动适度拍卖底价，以缓解消费者负担，同时维护脱碳激励并减少临时性政策干预。

  [DOI](https://doi.org/10.1038/s41467-026-73559-2) · [核验与筛查依据](docs/CATALOG.md#P123)

<a id="P036"></a>

- 📘 **[2025 · Nature Energy] [Implications of policy-driven transmission expansion for costs, emissions and reliability in the USA](https://www.nature.com/articles/s41560-025-01921-7)** · `P036`

  **发表：** 2025-12-04（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 比较政策要求各地区增强互联与单纯追求最低成本的美国输电扩建方案。政策方案把跨区输电能力提高约68%，布局更分散；成本最优方案更集中于中部且成本和排放更低。广泛互联在极端事件中改善可靠性，揭示输电政策在经济性、减排及韧性之间的取舍。

  **备注：** 在线首发年份为2025，卷期年份为2026；按在线首发年统计。

  [DOI](https://doi.org/10.1038/s41560-025-01921-7) · [核验与筛查依据](docs/CATALOG.md#P036)

<a id="P138"></a>

- 📘 **[2025 · Nature Communications] [Temporal matching as an accounting principle for green electricity claims](https://www.nature.com/articles/s41467-025-65125-z)** · `P138` · `本轮新增`

  **发表：** 2025-10-20（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用欧洲绿证与电力市场数据，比较年度、季度、月度直到小时级匹配对绿色用电声明的影响。年度总量匹配会掩盖季节及日内供需错配。论文建议先采用更细的季度或月度核算，再推进小时匹配，并把储能纳入证书体系，以提高绿色电力采购的可信度。

  [DOI](https://doi.org/10.1038/s41467-025-65125-z) · [核验与筛查依据](docs/CATALOG.md#P138)

<a id="P096"></a>

- 📚 **[2025 · Nature Reviews Electrical Engineering] [Translating energy equity from a sociological concept to an electric power engineering perspective](https://www.nature.com/articles/s44287-025-00210-5)** · `P096` · `本轮新增`

  **发表：** 2025-09-24（在线发表日期） · **类型：** Perspective · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 从电力工程视角讨论如何将能源公平转化为可操作的研究目标。文章梳理欧美相关政策及工程研究，将公平问题联系到电力可及性、可负担性与韧性，比较量化和嵌入工程决策的途径，并提出技术应用面临的挑战及研究路线，帮助电力系统设计与运行更明确地考虑社会分配影响。

  [DOI](https://doi.org/10.1038/s44287-025-00210-5) · [核验与筛查依据](docs/CATALOG.md#P096)

<a id="P014"></a>

- 📘 **[2025 · Nature Communications] [Electric transmission value and its drivers in United States power markets](https://www.nature.com/articles/s41467-025-63143-5)** · `P014`

  **发表：** 2025-08-28（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用2012—2022年美国批发电价数据评估新增输电能力的市场价值，发现跨区域互联的潜在收益尤其突出。相当部分年度价值来自少数高价值时段，并受运行前短期变化驱动。多处线路的估计收益超过年化建设成本，提示规划评估与开发障碍值得重新审视。

  [DOI](https://doi.org/10.1038/s41467-025-63143-5) · [核验与筛查依据](docs/CATALOG.md#P014)

<a id="P144"></a>

- 📘 **[2025 · Nature Communications] [Assessment of carbon-abatement pricing to maximize the value of electrolytic hydrogen in emissions-intensive power sectors](https://www.nature.com/articles/s41467-025-62952-y)** · `P144` · `本轮新增`

  **发表：** 2025-08-28（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对化石燃料占比较高的电网，构建电—氢—电系统经济可行性框架，联合考虑调度机构、风险厌恶投资者和政府目标。分析碳减排定价及市场调度规则如何影响制氢、备用和投资收益，强调仅追求降低边际电价不足以实现氢能在低碳电力系统中的综合价值。

  [DOI](https://doi.org/10.1038/s41467-025-62952-y) · [核验与筛查依据](docs/CATALOG.md#P144)

<a id="P145"></a>

- 📘 **[2025 · Nature Communications] [The impact of temporal hydrogen regulation on hydrogen exporters and their domestic energy transition](https://www.nature.com/articles/s41467-025-62873-w)** · `P145` · `本轮新增`

  **发表：** 2025-08-12（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 采用摩洛哥部门耦合能源模型，研究大规模并网电解制氢出口对国内电价、排放和转型的影响。氢能出口与本地减排可形成协同，但在化石能源占优时也会提高居民用电成本。按时间匹配制氢与清洁发电能够改善利益分配，说明出口监管需兼顾本国电力消费者。

  [DOI](https://doi.org/10.1038/s41467-025-62873-w) · [核验与筛查依据](docs/CATALOG.md#P145)

<a id="P147"></a>

- 📘 **[2025 · Nature Communications] [Assessing the real implications for CO2 as generation from renewables increases](https://www.nature.com/articles/s41467-025-59800-4)** · `P147` · `本轮新增`

  **发表：** 2025-08-02（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 使用加州与德州逐小时发电和排放数据，分析风光增长对传统热电机组运行效率的影响。可再生能源通常显著减少系统排放，但其波动也会迫使机组低效运行、产生额外排放惩罚。研究揭示减排收益的非线性，强调新能源接入应与灵活性及机组调度共同评估。

  [DOI](https://doi.org/10.1038/s41467-025-59800-4) · [核验与筛查依据](docs/CATALOG.md#P147)

<a id="P080"></a>

- 📚 **[2025 · Nature Reviews Electrical Engineering] [Designing the future electricity spot market with high renewables via reliable simulations](https://www.nature.com/articles/s44287-025-00163-9)** · `P080`

  **发表：** 2025-04-23（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 综述高比例新能源电力现货市场设计及仿真方法，强调运行安全、系统稳定和新能源投资激励。重点讨论多智能体强化学习、现实评价指标及适用性，并以 TradeRES 项目考察欧洲全可再生电力市场设计与未决问题。

  **遗忘筛查：** 邻近但非遗忘。多智能体策略学习用于市场仿真，没有定向遗忘对象。

  [DOI](https://doi.org/10.1038/s44287-025-00163-9) · [核验与筛查依据](docs/CATALOG.md#P080)

<a id="P154"></a>

- 📘 **[2025 · Nature Communications] [Repositioning coal power to accelerate net-zero transition of China’s power system](https://www.nature.com/articles/s41467-025-57559-2)** · `P154` · `本轮新增`

  **发表：** 2025-03-08（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 基于中国省级逐小时调度模型，同时考虑煤电提前退役和碳捕集改造，研究煤电由基荷电源转向灵活性资源的作用。在相同减排目标下，这种定位能够缓解资产搁浅、促进更多风光接入并降低系统转型成本，提出配套的灵活调度、退役与改造激励需求。

  [DOI](https://doi.org/10.1038/s41467-025-57559-2) · [核验与筛查依据](docs/CATALOG.md#P154)

<a id="P033"></a>

- 📘 **[2025 · Nature Energy] [Multi-country evidence on societal factors to include in energy transition modelling](https://www.nature.com/articles/s41560-025-01719-7)** · `P033`

  **发表：** 2025-02-21（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 在31个欧洲国家的电力系统转型模型中加入基础设施、决策主体及社会制度等六类因素，并用1990—2019年历史回溯检验模型表现。适当纳入社会因素后，部分技术装机路径的拟合改善最高达27%；公众接受、投资风险和基础设施锁定较为关键，为模型选取社会因素提供经验依据。

  [DOI](https://doi.org/10.1038/s41560-025-01719-7) · [核验与筛查依据](docs/CATALOG.md#P033)

<a id="P107"></a>

- 📘 **[2025 · Nature Energy] [Demand-side strategies enable rapid and deep cuts in buildings and transport emissions to 2050](https://www.nature.com/articles/s41560-025-01703-1)** · `P107` · `本轮新增`

  **发表：** 2025-02-05（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用多种全球综合评估模型，对建筑和交通中的活动变化、能效提升及终端电气化三类策略进行比较，并考虑系统间相互作用。电气化具有较大的直接减排潜力，但需求增长会改变供应侧投资需求。联合采用多类需求侧措施可在减排的同时降低电力需求，减少发电和基础设施投资压力，说明电气化应与需求管理协同推进。

  [DOI](https://doi.org/10.1038/s41560-025-01703-1) · [核验与筛查依据](docs/CATALOG.md#P107)

<a id="P032"></a>

- 📘 **[2025 · Nature Energy] [Power price stability and the insurance value of renewable technologies](https://www.nature.com/articles/s41560-025-01704-0)** · `P032`

  **发表：** 2025-01-28（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 用2030年欧洲电源规划及历史燃料价格、气象和用电波动模拟未来电力市场。研究提出衡量电价对天然气价格敏感性的指标，发现扩大风光装机能够降低持续电价冲击。由此产生的价格保险价值和社会福利收益未被现有市场机制充分反映，建议在能源政策评估中明确考虑。

  [DOI](https://doi.org/10.1038/s41560-025-01704-0) · [核验与筛查依据](docs/CATALOG.md#P032)

<a id="P031"></a>

- 📚 **[2025 · Nature Energy] [Lessons from wholesale market success for system service procurement design in high renewable electricity markets](https://www.nature.com/articles/s41560-024-01699-0)** · `P031`

  **发表：** 2025-01-15（在线发表日期） · **类型：** Perspective · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 讨论高比例风光电力系统中辅助及系统服务的采购设计。新增服务具有特殊经济属性，传统采购办法难以直接照搬。文章借鉴批发电力市场中技术与经济学合作的经验，提出未来需要协同研究的四个方向，以兼顾安全运行和服务采购效率。

  [DOI](https://doi.org/10.1038/s41560-024-01699-0) · [核验与筛查依据](docs/CATALOG.md#P031)

<a id="P057"></a>

- 📘 **[2025 · Nature Sustainability] [Decarbonization and electricity price vulnerability](https://www.nature.com/articles/s41893-024-01502-8)** · `P057`

  **发表：** 2025-01-07（在线发表日期） · **类型：** Analysis · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对欧洲天然气价格冲击向电价传导的问题，研究构建国家层面的脆弱性指标。结果表明，电力脱碳程度更高的国家并不更易受天然气价格冲击；但风光等间歇性电源占比较高与轻微更高的脆弱性相关，可能源于其与燃气发电的互补关系。作者据此主张采用适合各国市场结构的政策，而非统一限价。

  [DOI](https://doi.org/10.1038/s41893-024-01502-8) · [核验与筛查依据](docs/CATALOG.md#P057)

<a id="P024"></a>

- 📘 **[2024 · Nature Communications] [Impacts of large-scale deployment of vertical bifacial photovoltaics on European electricity market dynamics](https://www.nature.com/articles/s41467-024-50762-7)** · `P024`

  **发表：** 2024-08-06（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 分析垂直双面光伏大规模部署对欧洲电力市场的影响。改变光伏日内出力形态可提高太阳能发电的市场价值，缓解价格波动并影响基荷电价；各国太阳能资源和跨境互联条件决定发电及进口的变化，显示技术选择与市场和输电结构相互关联。

  [DOI](https://doi.org/10.1038/s41467-024-50762-7) · [核验与筛查依据](docs/CATALOG.md#P024)

<a id="P162"></a>

- 📘 **[2024 · Nature Communications] [The social factors shaping community microgrid operation](https://www.nature.com/articles/s41467-024-50736-9)** · `P162` · `本轮新增`

  **发表：** 2024-07-31（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 调查1021名美国居民对社区微电网在长时间停电期间分配有限电量的偏好。多数受访者接受按支付水平提供差异化配额，个人备用电源拥有者也愿意出售部分储能。研究分析公平感、保障自身需求与补偿之间的关系，为社区微电网运营机制提供社会接受度证据。

  [DOI](https://doi.org/10.1038/s41467-024-50736-9) · [核验与筛查依据](docs/CATALOG.md#P162)

<a id="P099"></a>

- 📚 **[2024 · Nature Reviews Electrical Engineering] [Sustainable electrification in the era of AI](https://www.nature.com/articles/s44287-024-00083-0)** · `P099` · `本轮新增`

  **发表：** 2024-07-31（在线发表日期） · **类型：** Comment · **范围：** 交叉与扩展期刊

  **内容概述（出版社导语，无正式摘要）：** 评论指出电网既支撑经济脱碳，也为人工智能发展提供基础，因此需要将人工智能增长与可持续电气化共同考虑。作者提出跨材料发现、计算机体系结构、智能电网和系统理论的综合研究议程，推动高效率、大规模、低碳电气化；公开导语侧重研究方向，并未报告特定控制算法的验证结果。

  [DOI](https://doi.org/10.1038/s44287-024-00083-0) · [核验与筛查依据](docs/CATALOG.md#P099)

<a id="P172"></a>

- 📘 **[2024 · Nature Climate Change] [Just Energy Transition Partnerships and the future of coal](https://www.nature.com/articles/s41558-024-02086-z)** · `P172` · `本轮新增`

  **发表：** 2024-07-31（出版社在线发表日期） · **类型：** Brief Communication · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究利用全球能源模型评估南非、印度尼西亚与越南的公正能源转型伙伴关系，比较既有政策、伙伴关系承诺及全球1.5摄氏度路径下的能源与排放结果。这些国际融资安排聚焦煤电依赖经济体的电力转型，其目标使相关国家更接近1.5摄氏度所要求的轨迹。结果支持以国际协作促进煤电退出与清洁电源扩张，同时强调落实能源和减排承诺。

  [DOI](https://doi.org/10.1038/s41558-024-02086-z) · [核验与筛查依据](docs/CATALOG.md#P172)

<a id="P163"></a>

- 📘 **[2024 · Nature Communications] [Power supply disruptions deter electric vehicle adoption in cities in China](https://www.nature.com/articles/s41467-024-50447-1)** · `P163` · `本轮新增`

  **发表：** 2024-07-18（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 利用中国全国停电和电动车采用数据，检验供电基础设施故障对终端电气化的反馈。研究发现，停电增加会降低新增电动车采用，持续性供电恶化还可能形成较长期的抑制效应，削弱交通减排收益。结果强调推进电气化时需要同步提升电网可靠性。

  [DOI](https://doi.org/10.1038/s41467-024-50447-1) · [核验与筛查依据](docs/CATALOG.md#P163)

<a id="P186"></a>

- 📚 **[2024 · Joule] [Making resource adequacy a private good: The good, the bad, and the ugly](https://doi.org/10.1016/j.joule.2024.04.001)** · `P186` · `本轮新增`

  **发表：** 2024-05-15（卷期日期；在线首发日期待核验，同属2024年） · **类型：** Commentary · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 讨论把资源充裕性从统一提供的公共保障转变为按用户偏好定制的服务，同时为医院等必要负荷保持保障。该思路可能改善容量采购效率，降低用户费用，激励分布式资源和非必要用电灵活调整。论文同时指出，必要负荷的社会定义、能源获取公平以及实施中的伦理和技术难题，需要在市场设计中妥善处理。

  [DOI](https://doi.org/10.1016/j.joule.2024.04.001) · [核验与筛查依据](docs/CATALOG.md#P186)

<a id="P017"></a>

- 📘 **[2024 · Nature Communications] [Avoiding ecosystem and social impacts of hydropower, wind, and solar in Southern Africa’s low-carbon electricity system](https://www.nature.com/articles/s41467-024-45313-z)** · `P017`

  **发表：** 2024-02-05（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对南部非洲电力发展，量化低生态与社会影响的风光水资源，并在土地、淡水保护及碳目标下优化发电组合。保护约束改变水电、风光与电池的配置，部分拟建水电存在环境社会冲突；兼顾低碳和保护目标可在有限额外系统成本下实现。

  [DOI](https://doi.org/10.1038/s41467-024-45313-z) · [核验与筛查依据](docs/CATALOG.md#P017)

<a id="P188"></a>

- 📘 **[2024 · Joule] [System-level impacts of voluntary carbon-free electricity procurement strategies](https://doi.org/10.1016/j.joule.2023.12.007)** · `P188` · `本轮新增`

  **发表：** 2024-01-11（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 通过美国西部电力系统容量扩张与运行分析，比较自愿无碳电力采购机制的长期系统影响。在研究政策条件下，年度电量匹配及按短期边际排放抵消的减排效果有限；逐小时匹配可明显降低系统排放，并带动清洁稳定电源和长时储能部署，但参与者成本更高。清洁电力标准等公共政策能进一步提高自愿采购的有效性。

  [DOI](https://doi.org/10.1016/j.joule.2023.12.007) · [核验与筛查依据](docs/CATALOG.md#P188)

[返回导航](#导航)

<a id="topic-7"></a>
### 可信AI、隐私与遗忘邻近（12条）

<a id="P079"></a>

- 📚 **[2026 · Nature Reviews Electrical Engineering] [End-to-end cyber resilience enhancement for renewable-dominated power grids](https://www.nature.com/articles/s44287-026-00334-2)** · `P079`

  **发表：** 2026-10-09（在线发表日期） · **类型：** Perspective · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 指出新能源与储能设备联网扩大攻击面，低惯量使网络入侵更快影响物理供电。提出贯穿攻击生命周期的网络—物理协同韧性框架，以后果、协调和反馈联接防御环节，并用示例分析网络性能退化与服务损失之间的关系。

  [DOI](https://doi.org/10.1038/s44287-026-00334-2) · [核验与筛查依据](docs/CATALOG.md#P079)

<a id="P073"></a>

- 📚 **[2026 · Communications Engineering] [Operating smart grids by customizing large model agents](https://www.nature.com/articles/s44172-026-00709-1)** · `P073`

  **发表：** 2026-06-24（在线发表日期） · **类型：** Perspective · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 讨论如何把大模型智能体用于电网控制室，支持状态监测、跨职能协调与运行决策。提出任务数据准备、电网知识检索、安全校验、分阶段部署和人工监督等路径，强调与现有调度工具和操作人员协作。

  **遗忘筛查：** 邻近但非遗忘。涉及检索增强、持续学习和智能体记忆，但未提出训练影响删除或概念撤回方法。

  [DOI](https://doi.org/10.1038/s44172-026-00709-1) · [核验与筛查依据](docs/CATALOG.md#P073)

<a id="P068"></a>

- 📘 **[2025 · Nature Climate Change] [Dynamic grid management reduces wildfire adaptation costs in the electric power sector](https://www.nature.com/articles/s41558-025-02436-5)** · `P068`

  **发表：** 2025-09-25（在线发表日期） · **类型：** Analysis · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究利用约2.5万英里高风险线路的天气与植被数据建立起火风险预测模型，比较美国大型电力公司不同野火治理措施的成本、可靠性与风险收益。高风险天气下调整保护装置灵敏度，比线路地下化或植被治理等传统方案更具成本效益。论文强调适应投资评价应同时计入停电可靠性、风险降低及资本激励。

  **遗忘筛查：** 邻近但非遗忘。使用风险预测模型，但动态保护管理是物理运行调整，摘要未描述从已训练模型删除特定数据或知识。

  [DOI](https://doi.org/10.1038/s41558-025-02436-5) · [核验与筛查依据](docs/CATALOG.md#P068)

<a id="P067"></a>

- 📘 **[2025 · Nature Climate Change] [Prolonged wind droughts in a warming climate threaten global wind power security](https://www.nature.com/articles/s41558-025-02387-x)** · `P067`

  **发表：** 2025-07-28（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 研究基于21个气候模型的逐小时数据，评估持续低风速事件对全球风力发电安全的影响。低排放与高排放情景均显示，到2100年风力干旱持续时间总体增加，北半球中纬度区域风险突出。约五分之一现有风机位于未来破纪录风旱的高风险地区，提示风电规划和供电保障需纳入长持续时间资源短缺。

  [DOI](https://doi.org/10.1038/s41558-025-02387-x) · [核验与筛查依据](docs/CATALOG.md#P067)

<a id="P081"></a>

- 📚 **[2025 · Nature Reviews Electrical Engineering] [Developments, challenges and future opportunities in cybersecure microgrid control](https://www.nature.com/articles/s44287-025-00189-z)** · `P081`

  **发表：** 2025-07-07（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 综述微电网控制的网络安全问题，描述网络物理结构、攻击面及电压频率与功率共享受到的影响。按建模方式和控制目标分类攻击检测、缓解方法，并讨论多攻击协同防御、生成式人工智能等未来机会。

  **遗忘筛查：** 邻近但非遗忘。控制层面检测和缓解攻击，不等于删除已训练模型中的恶意训练影响。

  [DOI](https://doi.org/10.1038/s44287-025-00189-z) · [核验与筛查依据](docs/CATALOG.md#P081)

<a id="P050"></a>

- 📚 **[2024 · Joule] [Foundation models for the electric power grid](https://www.sciencedirect.com/science/article/pii/S2542435124004707)** · `P050`

  **发表：** 2024-12-18（卷期日期；在线首发日待核验） · **类型：** Perspective · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 提出面向电网的基础模型GridFM，通过多种网络拓扑和运行数据开展自监督预训练，再针对潮流、状态估计、安全分析和控制等任务微调。文章给出基于图神经网络的GridFM-v0实施路线，讨论仿真加速、泛化和私有数据验证等机会与限制，是电网基础模型研究的路线性文献。

  **遗忘筛查：** 邻近但非遗忘。官网正文讨论隐私保护联邦学习、差分隐私、私有数据、持续学习及微调；这些不等同于删除指定数据或概念对模型的影响，未见遗忘算法与删除后验证。

  [DOI](https://doi.org/10.1016/j.joule.2024.11.002) · [核验与筛查依据](docs/CATALOG.md#P050)

<a id="P156"></a>

- 📘 **[2024 · Nature Communications] [A blockchain consensus mechanism for real-time regulation of renewable energy power systems](https://www.nature.com/articles/s41467-024-54626-y)** · `P156` · `本轮新增`

  **发表：** 2024-12-05（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 提出面向可再生能源电力系统实时调控的区块链共识机制Proof of Task，把计算任务直接关联于系统稳定和控制性能。通过新的验证机制改善传统区块链响应慢的问题，在三个电力系统中展示安全控制与可信计算能力，讨论其用于复杂动态系统的可能性。

  **遗忘筛查：** 邻近但非遗忘。区块链共识服务于实时安全控制与可信计算；不等于删除训练数据影响。

  [DOI](https://doi.org/10.1038/s41467-024-54626-y) · [核验与筛查依据](docs/CATALOG.md#P156)

<a id="P075"></a>

- 📘 **[2024 · Communications Engineering] [Data-driven and privacy-preserving risk assessment method based on federated learning for smart grids](https://www.nature.com/articles/s44172-024-00300-6)** · `P075`

  **发表：** 2024-11-02（在线发表日期） · **类型：** Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 针对电网高维运行数据的风险评估与运营商隐私保护，结合深度卷积网络、联邦学习和同态加密。研究构造两级风险指标及扩展数据集，在 IEEE 14、118 节点系统验证风险评估准确性与训练过程的数据保护。

  **遗忘筛查：** 邻近但非遗忘。保护分布式训练数据和参数；未提出从已训练模型删除指定数据影响的机制。

  [DOI](https://doi.org/10.1038/s44172-024-00300-6) · [核验与筛查依据](docs/CATALOG.md#P075)

<a id="P159"></a>

- 📘 **[2024 · Nature Communications] [Introducing edge intelligence to smart meters via federated split learning](https://www.nature.com/articles/s41467-024-53352-9)** · `P159` · `本轮新增`

  **发表：** 2024-10-19（首次在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 针对智能电表计算、存储及通信资源不足，同时面临用户用电数据隐私约束的问题，提出端—边—云联邦拆分学习框架。在仅有192 KB静态内存的硬件上开展建筑和家庭负荷预测，明显降低训练内存、耗时及通信开销，并保持与高配置服务器方案相当的预测性能。

  **遗忘筛查：** 邻近但非遗忘。联邦拆分学习解决端侧资源与隐私问题；所读摘要未提出撤回客户端历史贡献或训练数据影响的机制。

  [DOI](https://doi.org/10.1038/s41467-024-53352-9) · [核验与筛查依据](docs/CATALOG.md#P159)

<a id="P047"></a>

- 📚 **[2024 · Joule] [Exploring the capabilities and limitations of large language models in the electric energy sector](https://www.sciencedirect.com/science/article/pii/S254243512400237X)** · `P047`

  **发表：** 2024-06-19（卷期日期；在线首发日待核验） · **类型：** Commentary · **范围：** 核心期刊电网文献

  **内容概述（导语或机构摘要）：** 讨论大语言模型在电力行业运行维护中的用途与限制，提出电力领域数据收集和微调、将专业分析工具接入模型、利用检索增强生成建立知识库等方向。文章强调安全关键任务中的可靠性问题，为电力行业应用大模型提供研究议程，属于评论文章而非机器遗忘方法论文。

  **遗忘筛查：** 邻近但非遗忘。出版商导语与可获取正文讨论微调、专业工具、RAG和安全；不包含删除指定数据或概念的训练影响这一目标。

  [DOI](https://doi.org/10.1016/j.joule.2024.05.009) · [核验与筛查依据](docs/CATALOG.md#P047)

<a id="P020"></a>

- 📘 **[2024 · Nature Communications] [Break down the decentralization-security-privacy trilemma in management of distributed energy systems](https://www.nature.com/articles/s41467-024-48860-7)** · `P020`

  **发表：** 2024-05-27（在线发表日期） · **类型：** Article · **范围：** 核心期刊电网文献

  **摘要（中文概述）：** 提出区块链与可并行优化结合的分布式能源管理框架。参与者以掩蔽的成本函数和约束提交子问题，由其他节点验证求解并迭代交换决策与价格。在算例中兼顾去中心化、安全与隐私，并降低系统成本。其隐私保护发生在优化与信息交换环节，所读摘要未显示删除已训练模型中数据影响的机制。

  **遗忘筛查：** 邻近但非遗忘。涉及AI建模、信息筛选或隐私保护，但所读摘要未定义遗忘对象、删除目标及删除有效性验证。

  [DOI](https://doi.org/10.1038/s41467-024-48860-7) · [核验与筛查依据](docs/CATALOG.md#P020)

<a id="P084"></a>

- 📚 **[2024 · Nature Reviews Electrical Engineering] [Artificial intelligence-based methods for renewable power system operation](https://www.nature.com/articles/s44287-024-00018-9)** · `P084`

  **发表：** 2024-02-09（在线发表日期） · **类型：** Review Article · **范围：** 交叉与扩展期刊

  **摘要（中文概述）：** 综述机器学习、深度学习和强化学习支持新能源电力系统预测、调度、控制及市场的潜力。讨论新能源不确定性带来的供需平衡和价格挑战，以及分布式新能源、储能多样化和市场复杂化所需的算法发展。

  **遗忘筛查：** 邻近但非遗忘。通用学习方法综述，公开摘要未见定向训练影响删除。

  [DOI](https://doi.org/10.1038/s44287-024-00018-9) · [核验与筛查依据](docs/CATALOG.md#P084)

[返回导航](#导航)

<a id="topic-8"></a>
### 背景补充：资源、环境与转型（20条）

<a id="P114"></a>

- 📘 **[2026 · Nature Communications] [Extreme vulnerability to intruder attacks destabilizes network dynamics](https://www.nature.com/articles/s41467-026-76342-5)** · `P114` · `本轮新增`

  **发表：** 2026-08-13（首次在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 研究网络中的单个恶意节点如何破坏同步、共识等稳定动态状态，发现集中攻击某些低入度节点可能比攻击枢纽更具破坏性。理论从线性系统延伸至非线性振子网络，并讨论电网平衡等应用背景。其核心贡献是一般网络脆弱性分析，不能直接等同于真实电网攻击验证。

  [DOI](https://doi.org/10.1038/s41467-026-76342-5) · [核验与筛查依据](docs/CATALOG.md#P114)

<a id="P117"></a>

- 📘 **[2026 · Nature Communications] [Efficiency-weighted cooling degree days reveal opposing temperature and humidity effects on energy demand](https://www.nature.com/articles/s41467-026-75388-9)** · `P117` · `本轮新增`

  **发表：** 2026-07-11（首次在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 提出考虑制冷效率的有效制冷度日指标，同时描述气温和湿度对空调用能的作用。北美历史与未来情景分析表明，单纯以温度推算负荷会遗漏湿热与干热条件下的效率差异。论文为电力需求和气候风险评估提供输入改进，但并非电网调度或机器遗忘研究。

  [DOI](https://doi.org/10.1038/s41467-026-75388-9) · [核验与筛查依据](docs/CATALOG.md#P117)

<a id="P054"></a>

- 📘 **[2026 · Nature Sustainability] [Coal plants persist as a large barrier to the global solar energy transition](https://www.nature.com/articles/s41893-026-01836-5)** · `P054`

  **发表：** 2026-05-15（在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 研究基于全球电站级数据，量化燃煤电站附近气溶胶污染对光伏发电的抑制。结果估计2023年全球光伏发电损失为5.8%，中国损失比例为7.7%，且既有系统的污染损失会抵消部分新增光伏收益。论文强调评估电力转型时应考虑煤电与光伏共址的相互影响，否则可能高估清洁发电与减排贡献。

  [DOI](https://doi.org/10.1038/s41893-026-01836-5) · [核验与筛查依据](docs/CATALOG.md#P054)

<a id="P064"></a>

- 📘 **[2026 · Nature Climate Change] [Building façade photovoltaics enhance global climate resilience](https://www.nature.com/articles/s41558-026-02606-z)** · `P064`

  **发表：** 2026-03-27（在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 论文综合全球建筑数据、气候预测与立面尺度模拟，评估建筑立面光伏发电和降低制冷负荷的共同效益。估计可部署系统年发电量约732.5TWh，尽管建设成本较高，超过80%的城市分区可通过发电和节省冷负荷降低全寿命支出。结果支持将立面光伏作为城市减排与气候适应的补充方案。

  [DOI](https://doi.org/10.1038/s41558-026-02606-z) · [核验与筛查依据](docs/CATALOG.md#P064)

<a id="P087"></a>

- 📘 **[2026 · Nature Sustainability] [Global gridded dataset of heating and cooling degree days under climate change scenarios](https://www.nature.com/articles/s41893-025-01754-y)** · `P087` · `本轮新增`

  **发表：** 2026-01-26（出版社在线发表日期） · **类型：** Resource · **范围：** 背景补充

  **摘要（中文概述）：** 研究发布全球升温1.0、1.5与2.0摄氏度情景下的采暖和制冷度日数据集，以30幅网格图和五类统计量表征十年尺度的气候差异。结果显示采暖需求指标普遍下降，而制冷需求指标非线性增加，升温早期已出现明显变化。数据可为气候适应与用能需求规划提供输入，但度日指标并不直接等同于实测电力负荷或电网潮流。

  [DOI](https://doi.org/10.1038/s41893-025-01754-y) · [核验与筛查依据](docs/CATALOG.md#P087)

<a id="P130"></a>

- 📘 **[2026 · Nature Communications] [Towards high resolution, validated and open global wind power assessments](https://www.nature.com/articles/s41467-026-68337-z)** · `P130` · `本轮新增`

  **发表：** 2026-01-14（首次在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 发布开放的全球风电时序模拟流程ETHOS.RESKit，结合高分辨率风资源图谱、再分析数据及可定制机型，生成陆上和海上风电输出。通过多国测风塔、机组与统计发电量进行校准验证，为选址和系统集成提供输入数据；本目录将其归为资源与建模背景。

  [DOI](https://doi.org/10.1038/s41467-026-68337-z) · [核验与筛查依据](docs/CATALOG.md#P130)

<a id="P060"></a>

- 📘 **[2025 · Nature Sustainability] [Ownership of power plants stranded by climate mitigation](https://www.nature.com/articles/s41893-025-01707-5)** · `P060`

  **发表：** 2025-12-11（在线发表日期） · **类型：** Analysis · **范围：** 背景补充

  **摘要（中文概述）：** 论文利用全球电站及企业所有权数据，评估气候政策导致化石燃料发电资产提前退役、改造和收入减少的财务风险。资产风险高度集中：在1.5°C和2°C情景中，风险最大的25家公司分别持有超过7700亿和2240亿美元的搁浅资产，大型持有者多为国有企业。结果揭示电力转型中的企业风险与政策阻力来源。

  **备注：** 在线首发年份为2025，卷期年份为2026；按在线首发年统计。

  [DOI](https://doi.org/10.1038/s41893-025-01707-5) · [核验与筛查依据](docs/CATALOG.md#P060)

<a id="P135"></a>

- 📘 **[2025 · Nature Communications] [Ambitious climate targets can make the phaseout of India’s coal-fired power plants cost-beneficial](https://www.nature.com/articles/s41467-025-66580-4)** · `P135` · `本轮新增`

  **发表：** 2025-11-24（首次在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 构建电厂级混合整数非线性动态优化模型，比较印度煤电在不同温控目标下的退出路线及成本收益。结果表明，更积极的气候目标可能具有更高净收益，把社会收益纳入评价可进一步增强退役可行性。研究关注电力资产转型，不包含网络运行或模型遗忘机制。

  [DOI](https://doi.org/10.1038/s41467-025-66580-4) · [核验与筛查依据](docs/CATALOG.md#P135)

<a id="P058"></a>

- 📘 **[2025 · Nature Sustainability] [Environmental impact and net-zero pathways for sustainable artificial intelligence servers in the USA](https://www.nature.com/articles/s41893-025-01681-y)** · `P058`

  **发表：** 2025-11-10（在线发表日期） · **类型：** Analysis · **范围：** 背景补充

  **摘要（中文概述）：** 研究分析美国AI服务器扩张的能源、水和碳影响，发现2024—2030年的扩张规模、能效、电网脱碳速度及服务器选址共同决定其环境足迹。最佳实践虽可显著减排节水，仍受现有能源基础设施限制，行业2030年净零目标可能依赖不确定的抵消措施。论文强调协调数据中心布局与清洁电力建设。

  [DOI](https://doi.org/10.1038/s41893-025-01681-y) · [核验与筛查依据](docs/CATALOG.md#P058)

<a id="P052"></a>

- 📘 **[2025 · Science Advances] [The role of offshore wind and solar PV resources in global low-carbon transition](https://www.science.org/doi/10.1126/sciadv.adx5580)** · `P052`

  **发表：** 2025-10-24（在线发表日期） · **类型：** Research Article · **范围：** 背景补充

  **摘要（中文概述）：** 论文综合技术、环境和经济约束识别海上风电与光伏可开发区域，并量化各国发电和减排潜力。在仅利用1%适宜区域的假设下，两类资源年发电量分别约6049和14173TWh，合计接近2050年预期全球电力需求的30%。研究同时考察资源互补性，为海上电源布局和低碳供电规划提供依据。

  [DOI](https://doi.org/10.1126/sciadv.adx5580) · [核验与筛查依据](docs/CATALOG.md#P052)

<a id="P089"></a>

- 📘 **[2025 · Nature Sustainability] [Negotiating risks to natural capital in net-zero transitions](https://www.nature.com/articles/s41893-025-01576-y)** · `P089` · `本轮新增`

  **发表：** 2025-05-29（出版社在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 净零转型需要大规模新能源基础设施，但固定的土地可用性假设容易忽略生物多样性、农业及原住民权益。研究以澳大利亚为例，将国家能源转型模型与多种土地保护情景结合，识别新能源布局因自然资本约束而不可行或成本上升的地区。结果提出持续、协同地调整能源与土地规划，以降低脱碳目标和生态保护之间的冲突。

  [DOI](https://doi.org/10.1038/s41893-025-01576-y) · [核验与筛查依据](docs/CATALOG.md#P089)

<a id="P150"></a>

- 📘 **[2025 · Nature Communications] [Droughts worsen air quality and health by shifting power generation](https://www.nature.com/articles/s41467-025-60090-z)** · `P150` · `本轮新增`

  **发表：** 2025-05-22（首次在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 以拉美及加勒比地区二十年的电厂级月度数据，分析干旱导致水电减少、燃烧型电厂增发后对细颗粒物和健康的影响。结果表明，这种发电替代会恶化附近空气质量，并可能产生持续健康负担。论文提供电源结构适应气候风险的环境背景，不直接研究电网控制。

  [DOI](https://doi.org/10.1038/s41467-025-60090-z) · [核验与筛查依据](docs/CATALOG.md#P150)

<a id="P193"></a>

- 📘 **[2025 · Communications Engineering] [Lifecycle carbon intensity with embodied emissions of battery and hydrogen-driven integrative low-carbon systems](https://www.nature.com/articles/s44172-025-00411-8)** · `P193` · `本轮新增`

  **发表：** 2025-05-07（在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 研究未来清洁电网情景如何影响电池和氢能循环体系的全生命周期碳足迹，建立覆盖原材料到回收阶段的数据库，并绘制中国不同气候区域的碳强度分布。结合零能耗系统方案分析经济可行性，说明电网低碳化、储能路径及隐含排放之间的联系，为技术选择和政策评估提供依据。

  [DOI](https://doi.org/10.1038/s44172-025-00411-8) · [核验与筛查依据](docs/CATALOG.md#P193)

<a id="P170"></a>

- 📘 **[2025 · Nature Climate Change] [Trade risks to energy security in net-zero emissions energy scenarios](https://www.nature.com/articles/s41558-025-02305-1)** · `P170` · `本轮新增`

  **发表：** 2025-04-09（出版社在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 研究分析净零情景中燃料与关键矿产贸易如何改变能源安全。多数国家因减少化石燃料进口而降低总体贸易风险，但在更依赖进口材料的国家中，约82%的电力或交通系统贸易风险会上升。研究进一步检验贸易网络、能源结构、材料强度和回收率的影响，揭示低碳电力转型需要同时关注上游矿产供应链，而不能仅以燃料进口依赖度衡量安全性。

  [DOI](https://doi.org/10.1038/s41558-025-02305-1) · [核验与筛查依据](docs/CATALOG.md#P170)

<a id="P066"></a>

- 📘 **[2025 · Nature Climate Change] [Worldwide rooftop photovoltaic electricity generation may mitigate global warming](https://www.nature.com/articles/s41558-025-02276-3)** · `P066`

  **发表：** 2025-03-07（在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 研究结合地理数据挖掘和AI，以1公里分辨率估计全球屋顶面积，再利用九个地球系统模型分析屋顶光伏的气候减缓潜力。结果认为，到2050年前可能避免0.05—0.13°C升温，且收益随太阳辐射、基础设施与电网碳强度明显变化。其电力替代假设另有2025年Matters Arising讨论，使用减排估计时应连同争议阅读。

  **遗忘筛查：** 邻近但非遗忘。使用AI提取屋顶数据，但摘要及可见方法为识别与外推，未描述数据撤回或概念擦除。

  **备注：** 原文页面标注2025-10-22发布相关Matters Arising；减排替代效应存在学术讨论，不能将潜力估计视为实际减排保证。 后续学术讨论：2025-10-22的Matters Arising（10.1038/s41558-025-02459-y）指出，若未充分捕捉替代效应，屋顶光伏减排收益可能被高估；其美国案例估计较原分析低41%—98%。该结果限于评论所分析情景，不代表全球结果被统一修正。这是方法争议，非撤稿，也不是机器遗忘。

  [DOI](https://doi.org/10.1038/s41558-025-02276-3) · [核验与筛查依据](docs/CATALOG.md#P066)

<a id="P158"></a>

- 📘 **[2024 · Nature Communications] [The key role of sufficiency for low demand-based carbon neutrality and energy security across Europe](https://www.nature.com/articles/s41467-024-53393-0)** · `P158` · `本轮新增`

  **发表：** 2024-10-19（首次在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 从欧洲各国的自下而上需求模型出发，研究减少能源服务过度消费等充足性措施对低需求净零路径的贡献。情景显示，大幅降低终端需求可减轻可再生能源供给、进口与碳移除技术压力，并改善国别公平。该文属于能源需求转型背景，未明确建模电网投资和运行约束。

  [DOI](https://doi.org/10.1038/s41467-024-53393-0) · [核验与筛查依据](docs/CATALOG.md#P158)

<a id="P171"></a>

- 📘 **[2024 · Nature Climate Change] [Carbon dioxide emissions from global overseas coal-fired power plants](https://www.nature.com/articles/s41558-024-02114-y)** · `P171` · `本轮新增`

  **发表：** 2024-09-19（出版社在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 研究汇总全球908座海外投资煤电厂的投资资料，估算其当前年排放约5.3亿吨二氧化碳，历史累计排放约260亿吨。若政策与技术不变，至2060年还可能直接增加150亿至300亿吨累计排放，并通过刺激当地煤电扩张产生额外影响。结果表明，国际资本对新兴经济体电力部门的碳锁定有持续作用，低碳政策干预十分关键。

  [DOI](https://doi.org/10.1038/s41558-024-02114-y) · [核验与筛查依据](docs/CATALOG.md#P171)

<a id="P070"></a>

- 📘 **[2024 · Nature Climate Change] [Elevated urban energy risks due to climate-driven biophysical feedbacks](https://www.nature.com/articles/s41558-024-02108-w)** · `P070`

  **发表：** 2024-09-12（在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 研究将城市气候与采暖制冷能耗的双向反馈纳入混合模型，发现常见度日法会误估未来需求变化的大小、非线性和不确定性。在极高排放情景下，到2099年制冷需求增幅可达220%，采暖需求下降47%，变化幅度约为既有方法的两倍。结果表明城市能源及电力负荷规划需要显式考虑本地气候—用能反馈。

  [DOI](https://doi.org/10.1038/s41558-024-02108-w) · [核验与筛查依据](docs/CATALOG.md#P070)

<a id="P063"></a>

- 📘 **[2024 · Nature Sustainability] [Offsetting the greenhouse gas footprint of hydropower with floating solar photovoltaics](https://www.nature.com/articles/s41893-024-01384-w)** · `P063`

  **发表：** 2024-06-26（在线发表日期） · **类型：** Brief Communication · **范围：** 背景补充

  **摘要（中文概述）：** 部分水电站因水库温室气体排放而具有较高的单位电量排放。研究评估在现有水库部署漂浮式光伏、与水电联合运行的减排潜力，发现技术可行的组合有望使全球超过一半高排放强度水电站达到低排放能源基准。论文为水电项目管理和多能互补部署提供依据，重点是发电组合的碳强度。

  [DOI](https://doi.org/10.1038/s41893-024-01384-w) · [核验与筛查依据](docs/CATALOG.md#P063)

<a id="P165"></a>

- 📘 **[2024 · Nature Communications] [The transition to synchronization of networked systems](https://www.nature.com/articles/s41467-024-48203-6)** · `P165` · `本轮新增`

  **发表：** 2024-06-10（首次在线发表日期） · **类型：** Article · **范围：** 背景补充

  **摘要（中文概述）：** 研究一般网络动态系统的同步转变，用图拉普拉斯矩阵的特征值和特征向量近似预测同步簇出现的顺序与耦合阈值。在合成及真实拓扑网络上进行仿真验证，正文包含电网拓扑案例；该案例使用通用振子动力学，应视为方法背景而非真实电网调度模型。

  [DOI](https://doi.org/10.1038/s41467-024-48203-6) · [核验与筛查依据](docs/CATALOG.md#P165)

[返回导航](#导航)

<a id="unlearning"></a>
## 遗忘学习、撤回学习与概念撤回

这里按研究目标判断，而不只看术语：是否有明确待撤回的样本、客户端、任务、知识或概念；是否移除其对已训练模型的影响；是否评估删除有效性及其他能力的保留。

- **可算直接相关：** 机器遗忘、联邦遗忘、认证删除、定向概念或知识移除，且符合上述目标。
- **不能自动等同：** 联邦学习、差分隐私、在线更新、概念漂移、避免灾难性遗忘、推理时屏蔽、RAG文档删除、物理线路切除、论文撤稿。
- **本次结论：** 主目录尚未确认直接交叉命中；下面前三条说明电力系统领域已有专业期刊/会议研究。U04—U06是目标刊中的非电网遗忘参照，U07是非电网知识编辑邻近参照。

### 已有直接电力研究与综述（范围外）

<a id="U01"></a>

- 📘 **[2024 · IEEE Transactions on Power Systems] [Task-Aware Machine Unlearning and Its Application in Load Forecasting](https://ieeexplore.ieee.org/abstract/document/10472091)** · `U01`

  **发表：** 2024-03-13（在线发表日期） · **类型：** Article · **范围：** 范围外电力专业期刊

  **摘要（中文概述）：** 针对恶意数据或用户撤回需求，研究从已训练负荷预测器中删除指定数据影响。利用影响函数与样本重加权平衡遗忘和预测性能，并将调度、再调度成本纳入三层优化，在真实负荷数据及线性、CNN、MLP-Mixer模型上验证。

  **遗忘筛查：** 直接相关。已训练负荷预测器；指定数据遗忘；下游电力调度成本评价。属于电网×机器遗忘，但不在本次大子刊名单。

  [DOI](https://doi.org/10.1109/TPWRS.2024.3376828) · [核验与筛查依据](docs/UNLEARNING.md#U01)

<a id="U02"></a>

- 📘 **[2026 · 2026 IEEE Power & Energy Society General Meeting (PESGM)] [A SISA-based Machine Unlearning Framework for Power Transformer Inter-Turn Short-Circuit Fault Localization](https://inl.elsevierpure.com/en/publications/a-sisa-based-machine-unlearning-framework-for-power-transformer-i/)** · `U02`

  **发表：** 2026-07-23（在线发表日期） · **类型：** Conference paper · **范围：** 范围外会议论文

  **摘要（中文概述）：** 针对传感器故障导致的变压器诊断训练数据污染，采用分片、隔离、切片和聚合的SISA训练框架。检测到污染后只重训受影响子模型；在仿真匝间短路定位中，取得接近完整重训的准确率并减少重训时间。

  **遗忘筛查：** 直接相关。删除污染诊断数据对模型的影响；是电力设备故障定位。会议论文，不属于目标期刊；arXiv初稿日期2026-03-07。

  [DOI](https://doi.org/10.1109/PESGM58988.2026.11693380) · [核验与筛查依据](docs/UNLEARNING.md#U02)

<a id="U03"></a>

- 📚 **[2026 · Array] [A survey of machine unlearning for electric power systems: From privacy compliance to resilient grid operations](https://www.sciencedirect.com/science/article/pii/S2590005626003103)** · `U03`

  **发表：** 精确日期未核验（官网检索记录为2026年9月卷31；精确在线发表日期未核验，不能以9月1日代填。） · **类型：** Survey · **范围：** 范围外期刊综述

  **摘要（中文概述）：** 面向电力系统整理精确和近似机器遗忘、验证指标及隐私扩展，讨论智能电表数据删除、SCADA/PMU污染数据清除、跨电力企业联邦遗忘和在线模型维护。提出速度与稳定性权衡、认证和审计需求；属于综述框架，不能当作四类场景均已工程验证。

  **遗忘筛查：** 直接相关。综述对象明确是电力系统机器遗忘；Array不属于目标Nature/Science/Cell子刊。

  [DOI](https://doi.org/10.1016/j.array.2026.100987) · [核验与筛查依据](docs/UNLEARNING.md#U03)

### 非电网遗忘方法参照

<a id="U04"></a>

- 📚 **[2025 · Nature Machine Intelligence] [Rethinking machine unlearning for large language models](https://www.nature.com/articles/s42256-025-00985-0)** · `U04`

  **发表：** 2025-02-17（在线发表日期） · **类型：** Review Article · **范围：** 目标交叉期刊，但非电网研究

  **摘要（中文概述）：** 综述大语言模型遗忘的定义、方法、指标和应用，强调移除不希望保留的数据影响及相关能力，同时维护无关知识。讨论遗忘范围、数据与模型交互、多维评估，以及与模型编辑、影响函数、可解释性等领域的关系。

  **遗忘筛查：** 直接相关。直接研究机器遗忘，但非电网应用；仅可作为方法论文参考，不能计入电网交叉命中。

  [DOI](https://doi.org/10.1038/s42256-025-00985-0) · [核验与筛查依据](docs/UNLEARNING.md#U04)

<a id="U05"></a>

- 📘 **[2026 · Nature Communications] [Mitigating algorithmic unfairness arising from forgetfulness of medical records in clinical artificial intelligence](https://www.nature.com/articles/s41467-026-72601-7)** · `U05`

  **发表：** 2026-05-04（在线发表日期） · **类型：** Article · **范围：** 核心期刊，但非电网研究

  **摘要（中文概述）：** 研究患者记录撤回后临床模型的公平性损失，提出以梯度正交协调遗忘与公平目标的方法。在多医院的感染筛查、死亡和休克预测数据上评估，考察删除有效性、预测能力和人群公平性的联合保持。

  **遗忘筛查：** 直接相关。机器遗忘原创研究，但对象是医疗记录而非电网。

  [DOI](https://doi.org/10.1038/s41467-026-72601-7) · [核验与筛查依据](docs/UNLEARNING.md#U05)

<a id="U06"></a>

- 📘 **[2026 · Nature Communications] [Superior resilience to poisoning and amenability to unlearning in quantum machine learning](https://www.nature.com/articles/s41467-026-70420-4)** · `U06`

  **发表：** 2026-03-09（在线发表日期） · **类型：** Article · **范围：** 核心期刊，但非电网研究

  **摘要（中文概述）：** 比较经典与量子神经网络对训练数据污染的响应，分析量子模型的抗噪性及近似遗忘能力。研究以污染样本为遗忘集、干净样本为保留集，对照完整重训，报告量子模型更易清除错误数据的影响。

  **遗忘筛查：** 直接相关。直接研究机器遗忘，但不是电网问题；量子模型的能量等术语不能据此归为电网。

  [DOI](https://doi.org/10.1038/s41467-026-70420-4) · [核验与筛查依据](docs/UNLEARNING.md#U06)

### 非电网知识编辑邻近方向

<a id="U07"></a>

- 📚 **[2026 · Nature Machine Intelligence] [Towards principled knowledge editing methods for large language model reasoning](https://www.nature.com/articles/s42256-026-01276-y)** · `U07`

  **发表：** 2026-08-14（在线发表日期） · **类型：** Perspective · **范围：** 非电网邻近方法参照

  **摘要（中文概述）：** 讨论无需完整重训的大语言模型知识更新，指出把事实视为可独立编辑的模块会忽视知识之间的依赖关系，破坏多步推理与因果一致性。文章提出围绕演绎闭包回路、模型信念和置信度、情境化复杂知识开展编辑的研究方向，为持续知识适应提供原则性框架，但并不专门解决电网应用或可验证的数据遗忘。

  **遗忘筛查：** 邻近但非遗忘。知识编辑可与知识撤回交叉，但本文主要研究推理一致的知识更新；不能等同于机器遗忘，也未涉及电网。

  [DOI](https://doi.org/10.1038/s42256-026-01276-y) · [核验与筛查依据](docs/UNLEARNING.md#U07)

### 尚待核验

IEEE TII的[Learning and Unlearning to Operate Profitable Secure Electric Vehicle Charging](https://doi.org/10.1109/TII.2024.3396524)已确认题名与刊期，但一手摘要仍受访问限制；2026年“Sequential Federated Unlearning for Distributed Electricity Load Forecasting”目前只核实到[软件复现包](https://zenodo.org/records/21992940)，不能冒充正式期刊论文。两者不计入已核验论文数，详见[待核验记录](data/pending_candidates.json)。

## 数据与使用

全文元数据在`data/papers.json`，每条含题目、摘要、期刊、年份、DOI、来源和筛查理由。可使用页面搜索按年份、期刊、主题或ID定位。新旧数量、日期例外及检索边界见[更新记录](docs/UPDATE_2026-11-02.md)和[覆盖核查](docs/COVERAGE_AUDIT.md)。

解压仓库包后，将内部文件直接上传到GitHub仓库根目录即可，操作见[维护说明](CONTRIBUTING.md)。本仓库不打包论文PDF；原论文权利归原权利人，中文概述仅供文献导航。正式引用前请阅读原文并核对完整书目信息。
