# 金融主干框架学习笔记

本目录是金融主干框架的统一学习入口，已合并原 `Agents.md` 的课程目录、参考书、原书位置和学习执行原则。每节一个 Markdown 文档，正文按原教材逻辑深度改写。

参考书：

- Mankiw, *Principles of Economics, 10e*
- Mishkin, *The Economics of Money, Banking and Financial Markets, 13th Global Edition*
- Mishkin & Eakins, *Financial Markets and Institutions, 10th Global Edition*
- Bodie, Kane & Marcus, *Investments, 13e*
- Paleologo, *The Elements of Quantitative Investing*
- Di Maggio, *Blockchain, Crypto and DeFi: Bridging Finance and Technology*

参考写作规则：[`../WRITING_GUIDE.md`](../WRITING_GUIDE.md)

学习执行原则：

- 按 1-66 章连续推进，不跳过第二十章之后的行业地图、第二十八章之后的投资学模块、第三十六章之后的量化投资模块和第五十章之后的区块链金融模块。
- 每章学习目标是抓住主干概念、关键机制、典型例子和与前后章节的关系。
- 不以读完原书为目标，而以能复述机制、解释现实金融现象为目标。
- 遇到重复内容时保留不同层次：前面章节学原理，后面章节学市场和机构形态。

## 第一部分：经济学底座

### 第 1 章 稀缺、选择与经济学方法

原书位置：Mankiw Ch.1, Ch.2；Mishkin《货币金融学》Ch.1；Mishkin/Eakins Ch.1。

- [1.1 稀缺、选择与机会成本](ch01-scarcity-choice-method/01.01.md)
- [1.2 边际思维、激励与权衡取舍](ch01-scarcity-choice-method/01.02.md)
- [1.3 效率、公平与经济学评价标准](ch01-scarcity-choice-method/01.03.md)
- [1.4 经济模型、假设与实证思维](ch01-scarcity-choice-method/01.04.md)
- [1.5 金融为什么是跨时间、跨主体的资源配置](ch01-scarcity-choice-method/01.05.md)

### 第 2 章 市场供求、价格与福利

原书位置：Mankiw Ch.4, Ch.5, Ch.6, Ch.7, Ch.8, Ch.10, Ch.11。

- [2.1 需求、供给与市场均衡](ch02-supply-demand-welfare/02.01.md)
- [2.2 弹性与政策效果](ch02-supply-demand-welfare/02.02.md)
- [2.3 消费者剩余、生产者剩余与总剩余](ch02-supply-demand-welfare/02.03.md)
- [2.4 税收归宿、价格管制与无谓损失](ch02-supply-demand-welfare/02.04.md)
- [2.5 外部性、公共品与市场失灵](ch02-supply-demand-welfare/02.05.md)
- [2.6 信息问题与金融市场的特殊性](ch02-supply-demand-welfare/02.06.md)

## 第二部分：宏观经济底座

### 第 3 章 国民收入、物价与失业

原书位置：Mankiw Ch.24, Ch.25, Ch.29；Mishkin《货币金融学》Ch.1 Appendix。

- [3.1 GDP 的定义、口径与局限](ch03-income-prices-unemployment/03.01.md)
- [3.2 支出法：消费、投资、政府购买、净出口](ch03-income-prices-unemployment/03.02.md)
- [3.3 名义变量、实际变量与价格指数](ch03-income-prices-unemployment/03.03.md)
- [3.4 CPI、通胀率与购买力](ch03-income-prices-unemployment/03.04.md)
- [3.5 失业率、劳动参与率与统计口径](ch03-income-prices-unemployment/03.05.md)

### 第 4 章 长期增长、储蓄投资与金融体系

原书位置：Mankiw Ch.26, Ch.27, Ch.28；Mishkin《货币金融学》Ch.2。

- [4.1 生产率与长期增长](ch04-growth-saving-investment/04.01.md)
- [4.2 储蓄、投资与资本形成](ch04-growth-saving-investment/04.02.md)
- [4.3 可贷资金市场与实际利率](ch04-growth-saving-investment/04.03.md)
- [4.4 金融体系如何把储蓄转化为投资](ch04-growth-saving-investment/04.04.md)
- [4.5 现值、风险与基础金融决策](ch04-growth-saving-investment/04.05.md)

## 第三部分：金融体系与货币

### 第 5 章 金融系统总览

原书位置：Mishkin《货币金融学》Ch.2；Mishkin/Eakins Ch.2；Mankiw Ch.27。

- [5.1 金融市场的功能](ch05-financial-system-overview/05.01.md)
- [5.2 直接融资与间接融资](ch05-financial-system-overview/05.02.md)
- [5.3 债务市场、股权市场与金融工具](ch05-financial-system-overview/05.03.md)
- [5.4 一级市场、二级市场、交易所市场与场外市场](ch05-financial-system-overview/05.04.md)
- [5.5 货币市场与资本市场](ch05-financial-system-overview/05.05.md)
- [5.6 金融中介、监管与金融系统地图](ch05-financial-system-overview/05.06.md)

### 第 6 章 货币、支付体系与货币衡量

原书位置：Mishkin《货币金融学》Ch.3；Mankiw Ch.30；Mishkin/Eakins Ch.1 中加密货币案例。

- [6.1 货币的定义与三大职能](ch06-money-payments-measurement/06.01.md)
- [6.2 商品货币、法币、支票与电子支付](ch06-money-payments-measurement/06.02.md)
- [6.3 中央银行货币与商业银行货币](ch06-money-payments-measurement/06.03.md)
- [6.4 M1、M2 与货币衡量口径](ch06-money-payments-measurement/06.04.md)
- [6.5 数字支付、加密资产与“货币”边界](ch06-money-payments-measurement/06.05.md)

## 第四部分：利率、债券与股票

### 第 7 章 利率、现值与债券定价

原书位置：Mishkin《货币金融学》Ch.4；Mishkin/Eakins Ch.3；Mankiw Ch.28。

- [7.1 利率的经济含义](ch07-interest-present-value/07.01.md)
- [7.2 现值、贴现与跨期价值](ch07-interest-present-value/07.02.md)
- [7.3 简单贷款、固定支付贷款、息票债、贴现债](ch07-interest-present-value/07.03.md)
- [7.4 到期收益率与债券定价](ch07-interest-present-value/07.04.md)
- [7.5 债券价格和利率的反向关系](ch07-interest-present-value/07.05.md)
- [7.6 回报率、久期直觉与利率风险](ch07-interest-present-value/07.06.md)

### 第 8 章 利率决定、风险结构与期限结构

原书位置：Mishkin《货币金融学》Ch.5, Ch.6；Mishkin/Eakins Ch.4, Ch.5。

- [8.1 资产需求：财富、预期收益、风险、流动性](ch08-interest-risk-term-structure/08.01.md)
- [8.2 债券市场供求与均衡利率](ch08-interest-risk-term-structure/08.02.md)
- [8.3 预期通胀、费雪效应与商业周期](ch08-interest-risk-term-structure/08.03.md)
- [8.4 货币市场框架与流动性偏好](ch08-interest-risk-term-structure/08.04.md)
- [8.5 违约风险、流动性、税收与信用利差](ch08-interest-risk-term-structure/08.05.md)
- [8.6 收益率曲线与期限结构理论](ch08-interest-risk-term-structure/08.06.md)
- [8.7 收益率曲线的宏观含义](ch08-interest-risk-term-structure/08.07.md)

### 第 9 章 股票市场、预期与有效市场

原书位置：Mishkin《货币金融学》Ch.7；Mishkin/Eakins Ch.6, Ch.13。

- [9.1 普通股、优先股与股东权利](ch09-stocks-expectations-efficiency/09.01.md)
- [9.2 一期估值模型、股利贴现模型与戈登增长模型](ch09-stocks-expectations-efficiency/09.02.md)
- [9.3 市盈率、增长预期与风险](ch09-stocks-expectations-efficiency/09.03.md)
- [9.4 股票价格如何反映预期](ch09-stocks-expectations-efficiency/09.04.md)
- [9.5 理性预期与有效市场假说](ch09-stocks-expectations-efficiency/09.05.md)
- [9.6 有效市场的投资含义](ch09-stocks-expectations-efficiency/09.06.md)
- [9.7 行为金融对有效市场的补充](ch09-stocks-expectations-efficiency/09.07.md)

## 第五部分：金融机构、银行、监管与危机

### 第 10 章 金融机构为何存在

原书位置：Mishkin《货币金融学》Ch.8；Mishkin/Eakins Ch.7。

- [10.1 金融结构的基本事实](ch10-why-financial-institutions-exist/10.01.md)
- [10.2 交易成本与规模经济](ch10-why-financial-institutions-exist/10.02.md)
- [10.3 信息不对称](ch10-why-financial-institutions-exist/10.03.md)
- [10.4 逆向选择、柠檬问题与筛选机制](ch10-why-financial-institutions-exist/10.04.md)
- [10.5 道德风险、委托代理与监督机制](ch10-why-financial-institutions-exist/10.05.md)
- [10.6 债务契约、抵押品与金融中介的价值](ch10-why-financial-institutions-exist/10.06.md)

### 第 11 章 银行经营与银行资产负债表

原书位置：Mishkin《货币金融学》Ch.9；Mishkin/Eakins Ch.17。

- [11.1 银行资产负债表](ch11-banking-balance-sheet/11.01.md)
- [11.2 银行如何创造流动性](ch11-banking-balance-sheet/11.02.md)
- [11.3 准备金、存款流出与流动性管理](ch11-banking-balance-sheet/11.03.md)
- [11.4 资产管理与负债管理](ch11-banking-balance-sheet/11.04.md)
- [11.5 银行资本与资本充足](ch11-banking-balance-sheet/11.05.md)
- [11.6 信用风险、利率风险与表外业务](ch11-banking-balance-sheet/11.06.md)
- [11.7 银行业绩指标与经营约束](ch11-banking-balance-sheet/11.07.md)

### 第 12 章 金融监管与银行业结构

原书位置：Mishkin《货币金融学》Ch.10, Ch.11；Mishkin/Eakins Ch.18, Ch.19。

- [12.1 金融监管的经济学理由](ch12-regulation-banking-structure/12.01.md)
- [12.2 存款保险、政府安全网与道德风险](ch12-regulation-banking-structure/12.02.md)
- [12.3 资本要求、审慎监管与信息披露](ch12-regulation-banking-structure/12.03.md)
- [12.4 微观审慎监管与宏观审慎监管](ch12-regulation-banking-structure/12.04.md)
- [12.5 金融创新、影子银行与监管套利](ch12-regulation-banking-structure/12.05.md)
- [12.6 银行业结构、竞争、合并与国际银行业](ch12-regulation-banking-structure/12.06.md)
- [12.7 大而不能倒与危机后的监管改革](ch12-regulation-banking-structure/12.07.md)

### 第 13 章 金融危机机制

原书位置：Mishkin《货币金融学》Ch.12, Ch.13；Mishkin/Eakins Ch.8, Additional Ch.25。

- [13.1 金融危机的定义：信息问题和信用中断](ch13-financial-crises/13.01.md)
- [13.2 初始冲击：资产价格下跌、不确定性上升、资产负债表恶化](ch13-financial-crises/13.02.md)
- [13.3 银行危机、流动性危机与信用收缩](ch13-financial-crises/13.03.md)
- [13.4 债务通缩、去杠杆与经济衰退](ch13-financial-crises/13.04.md)
- [13.5 2007-2009 金融危机机制](ch13-financial-crises/13.05.md)
- [13.6 新兴市场危机：货币错配、资本流动与汇率崩盘](ch13-financial-crises/13.06.md)
- [13.7 金融危机预防与政策应对](ch13-financial-crises/13.07.md)

## 第六部分：中央银行与货币政策

### 第 14 章 中央银行与货币供给

原书位置：Mishkin《货币金融学》Ch.14, Ch.15；Mankiw Ch.30；Mishkin/Eakins Ch.9。

- [14.1 中央银行的起源、功能与独立性](ch14-central-banks-money-supply/14.01.md)
- [14.2 中央银行资产负债表](ch14-central-banks-money-supply/14.02.md)
- [14.3 货币基础、现金与准备金](ch14-central-banks-money-supply/14.03.md)
- [14.4 银行体系与存款创造](ch14-central-banks-money-supply/14.04.md)
- [14.5 货币乘数与货币供给过程](ch14-central-banks-money-supply/14.05.md)
- [14.6 货币供给过程的现实限制](ch14-central-banks-money-supply/14.06.md)

### 第 15 章 货币政策工具

原书位置：Mishkin《货币金融学》Ch.16；Mishkin/Eakins Ch.10。

- [15.1 准备金市场与政策利率控制](ch15-monetary-policy-tools/15.01.md)
- [15.2 公开市场操作](ch15-monetary-policy-tools/15.02.md)
- [15.3 贴现窗口与最后贷款人](ch15-monetary-policy-tools/15.03.md)
- [15.4 法定准备金率与准备金利率](ch15-monetary-policy-tools/15.04.md)
- [15.5 流动性工具与危机贷款机制](ch15-monetary-policy-tools/15.05.md)
- [15.6 QE、信用宽松、前瞻指引与负利率](ch15-monetary-policy-tools/15.06.md)

### 第 16 章 货币政策战略

原书位置：Mishkin《货币金融学》Ch.17；Mishkin/Eakins Ch.10。

- [16.1 价格稳定与名义锚](ch16-monetary-policy-strategy/16.01.md)
- [16.2 通胀目标制与平均通胀目标制](ch16-monetary-policy-strategy/16.02.md)
- [16.3 就业、产出、增长与金融稳定目标](ch16-monetary-policy-strategy/16.03.md)
- [16.4 规则与相机抉择](ch16-monetary-policy-strategy/16.04.md)
- [16.5 时间不一致性与政策可信度](ch16-monetary-policy-strategy/16.05.md)
- [16.6 泰勒规则、央行沟通与市场预期](ch16-monetary-policy-strategy/16.06.md)
- [16.7 央行是否应对资产价格泡沫作出反应](ch16-monetary-policy-strategy/16.07.md)

### 第 17 章 货币理论、总需求总供给与政策传导

原书位置：Mishkin《货币金融学》Ch.20-Ch.26；Mankiw Ch.31, Ch.34-Ch.36。

- [17.1 数量论、货币增长与长期通胀](ch17-monetary-theory-ad-as-transmission/17.01.md)
- [17.2 货币需求理论](ch17-monetary-theory-ad-as-transmission/17.02.md)
- [17.3 IS 曲线与总需求](ch17-monetary-theory-ad-as-transmission/17.03.md)
- [17.4 货币政策曲线与 AD 曲线](ch17-monetary-theory-ad-as-transmission/17.04.md)
- [17.5 AD-AS 分析与短期经济波动](ch17-monetary-theory-ad-as-transmission/17.05.md)
- [17.6 菲利普斯曲线、预期与政策权衡](ch17-monetary-theory-ad-as-transmission/17.06.md)
- [17.7 货币政策传导机制：利率、资产价格、汇率、信用渠道](ch17-monetary-theory-ad-as-transmission/17.07.md)
- [17.8 预期、可信度与货币政策效果](ch17-monetary-theory-ad-as-transmission/17.08.md)

## 第七部分：开放经济与国际金融

### 第 18 章 外汇市场与汇率决定

原书位置：Mishkin《货币金融学》Ch.18；Mishkin/Eakins Ch.15；Mankiw Ch.32。

- [18.1 外汇市场与汇率报价](ch18-foreign-exchange/18.01.md)
- [18.2 名义汇率、实际汇率与竞争力](ch18-foreign-exchange/18.02.md)
- [18.3 一价定律与购买力平价](ch18-foreign-exchange/18.03.md)
- [18.4 汇率的长期决定因素](ch18-foreign-exchange/18.04.md)
- [18.5 汇率的短期资产市场分析](ch18-foreign-exchange/18.05.md)
- [18.6 利率平价与资本流动](ch18-foreign-exchange/18.06.md)
- [18.7 汇率变动对经济和金融市场的影响](ch18-foreign-exchange/18.07.md)

### 第 19 章 国际金融体系

原书位置：Mishkin《货币金融学》Ch.19；Mishkin/Eakins Ch.16；Mankiw Ch.32, Ch.33。

- [19.1 国际收支与资本流动](ch19-international-financial-system/19.01.md)
- [19.2 固定汇率、浮动汇率与管理浮动](ch19-international-financial-system/19.02.md)
- [19.3 外汇干预、冲销操作与外汇储备](ch19-international-financial-system/19.03.md)
- [19.4 三元悖论、货币主权与资本管制](ch19-international-financial-system/19.04.md)
- [19.5 货币联盟、货币局与美元化](ch19-international-financial-system/19.05.md)
- [19.6 投机攻击与汇率危机](ch19-international-financial-system/19.06.md)
- [19.7 IMF、国际最后贷款人与国际金融安全网](ch19-international-financial-system/19.07.md)

## 第八部分：金融市场与金融机构行业地图

### 第 20 章 货币市场：短期资金市场

原书位置：Mishkin/Eakins Ch.11；Mishkin《货币金融学》Ch.2 中货币市场工具。

- [20.1 货币市场的定义、功能与参与者](ch20-money-markets/20.01.md)
- [20.2 国库券、联邦基金与回购协议](ch20-money-markets/20.02.md)
- [20.3 大额可转让存单、商业票据、银行承兑汇票](ch20-money-markets/20.03.md)
- [20.4 Eurodollars 与跨境短期资金](ch20-money-markets/20.04.md)
- [20.5 货币市场工具的定价、流动性与风险](ch20-money-markets/20.05.md)
- [20.6 货币市场基金与流动性危机](ch20-money-markets/20.06.md)

### 第 21 章 债券市场：利率与信用市场

原书位置：Mishkin/Eakins Ch.12；Mishkin《货币金融学》Ch.4-Ch.6。

- [21.1 债券市场的功能、参与者与交易逻辑](ch21-bond-markets/21.01.md)
- [21.2 国债、机构债、市政债](ch21-bond-markets/21.02.md)
- [21.3 公司债、可转换债与高收益债](ch21-bond-markets/21.03.md)
- [21.4 债券评级、信用风险与信用利差](ch21-bond-markets/21.04.md)
- [21.5 债券定价、当前收益率与到期收益率](ch21-bond-markets/21.05.md)
- [21.6 债券投资、债券基金与债券市场监管](ch21-bond-markets/21.06.md)

### 第 22 章 股票市场：股权融资与估值市场

原书位置：Mishkin/Eakins Ch.13；Mishkin《货币金融学》Ch.7。

- [22.1 股票市场的功能](ch22-stock-markets/22.01.md)
- [22.2 普通股、优先股与股东权利](ch22-stock-markets/22.02.md)
- [22.3 IPO、增发与股票发行](ch22-stock-markets/22.03.md)
- [22.4 股票估值：股利贴现、市盈率与增长预期](ch22-stock-markets/22.04.md)
- [22.5 股票指数、海外股票与证券监管](ch22-stock-markets/22.05.md)

### 第 23 章 抵押贷款市场与证券化

原书位置：Mishkin/Eakins Ch.14；Mishkin《货币金融学》Ch.12 中 2007-2009 危机、CDO、CDS 案例。

- [23.1 抵押贷款的定义与特征](ch23-mortgage-markets-securitization/23.01.md)
- [23.2 固定利率房贷、可调利率房贷与其他房贷类型](ch23-mortgage-markets-securitization/23.02.md)
- [23.3 房贷摊还、房贷利率与贷款机构](ch23-mortgage-markets-securitization/23.03.md)
- [23.4 二级抵押贷款市场](ch23-mortgage-markets-securitization/23.04.md)
- [23.5 MBS、房贷证券化与风险转移](ch23-mortgage-markets-securitization/23.05.md)
- [23.6 次贷、CDO 与房地产金融危机机制](ch23-mortgage-markets-securitization/23.06.md)

### 第 24 章 共同基金、ETF 与资产管理

原书位置：Mishkin/Eakins Ch.20；Mankiw Ch.27；Mishkin《货币金融学》Ch.2 中投资中介。

- [24.1 共同基金的功能与行业增长](ch24-mutual-funds-etf-asset-management/24.01.md)
- [24.2 开放式基金与封闭式基金](ch24-mutual-funds-etf-asset-management/24.02.md)
- [24.3 净资产价值 NAV、申购赎回与费用结构](ch24-mutual-funds-etf-asset-management/24.03.md)
- [24.4 货币基金、债券基金、股票基金、混合基金、指数基金](ch24-mutual-funds-etf-asset-management/24.04.md)
- [24.5 ETF 与被动投资](ch24-mutual-funds-etf-asset-management/24.05.md)
- [24.6 对冲基金、利益冲突与基金行业监管](ch24-mutual-funds-etf-asset-management/24.06.md)

### 第 25 章 保险公司、养老金与长期资金

原书位置：Mishkin/Eakins Ch.21；Mishkin《货币金融学》Ch.2 中契约型储蓄机构。

- [25.1 保险公司的基本功能](ch25-insurance-pensions/25.01.md)
- [25.2 逆向选择、道德风险与保险定价](ch25-insurance-pensions/25.02.md)
- [25.3 寿险、健康险、财产险与再保险](ch25-insurance-pensions/25.03.md)
- [25.4 保险公司资产配置与风险管理](ch25-insurance-pensions/25.04.md)
- [25.5 养老金：DB、DC、公共养老金与私人养老金](ch25-insurance-pensions/25.05.md)
- [25.6 保险与养老金作为长期机构投资者](ch25-insurance-pensions/25.06.md)

### 第 26 章 投行、券商、交易商与 PE/VC

原书位置：Mishkin/Eakins Ch.22；Mishkin《货币金融学》Ch.2 中金融中介类型。

- [26.1 投资银行的功能](ch26-investment-banks-brokers-pe-vc/26.01.md)
- [26.2 承销：IPO、增发与债券发行](ch26-investment-banks-brokers-pe-vc/26.02.md)
- [26.3 并购顾问、重组与企业融资服务](ch26-investment-banks-brokers-pe-vc/26.03.md)
- [26.4 证券经纪商、交易商与财富管理](ch26-investment-banks-brokers-pe-vc/26.04.md)
- [26.5 商业银行与投行业务边界](ch26-investment-banks-brokers-pe-vc/26.05.md)
- [26.6 风险投资、私募股权与创业融资](ch26-investment-banks-brokers-pe-vc/26.06.md)

### 第 27 章 金融机构风险管理与金融衍生品

原书位置：Mishkin/Eakins Ch.23, Ch.24；Mishkin《货币金融学》MyLab Additional Chapter: Financial Derivatives。

- [27.1 金融机构面临的主要风险](ch27-risk-management-derivatives/27.01.md)
- [27.2 信用风险管理：筛选、监督、抵押品与限额](ch27-risk-management-derivatives/27.02.md)
- [27.3 利率风险管理：收入缺口与久期缺口](ch27-risk-management-derivatives/27.03.md)
- [27.4 流动性风险、操作风险与风险治理](ch27-risk-management-derivatives/27.04.md)
- [27.5 远期、期货、期权、互换](ch27-risk-management-derivatives/27.05.md)
- [27.6 衍生品的功能：套期保值、投机、套利、风险转移](ch27-risk-management-derivatives/27.06.md)
- [27.7 金融衍生品、杠杆与系统性风险](ch27-risk-management-derivatives/27.07.md)

## 第九部分：投资学与组合管理

### 第 28 章 投资环境、金融工具与交易制度

原书位置：Bodie/Kane/Marcus《Investments》Ch.1-Ch.4；相关旧笔记：本笔记 Ch.5, Ch.20-Ch.24。

- [28.1 投资过程、实物资产与金融资产](ch28-investment-environment-instruments/28.01.md)
- [28.2 货币市场工具与短期安全资产](ch28-investment-environment-instruments/28.02.md)
- [28.3 债券、股票与市场指数](ch28-investment-environment-instruments/28.03.md)
- [28.4 衍生证券在投资环境中的角色](ch28-investment-environment-instruments/28.04.md)
- [28.5 证券如何交易](ch28-investment-environment-instruments/28.05.md)
- [28.6 共同基金、ETF 与投资公司](ch28-investment-environment-instruments/28.06.md)

### 第 29 章 风险、收益与资本配置

原书位置：Bodie/Kane/Marcus《Investments》Ch.5-Ch.6；相关旧笔记：本笔记 Ch.7-Ch.9。

- [29.1 收益率的度量](ch29-risk-return-capital-allocation/29.01.md)
- [29.2 风险溢价与历史记录](ch29-risk-return-capital-allocation/29.02.md)
- [29.3 风险、波动率与收益分布](ch29-risk-return-capital-allocation/29.03.md)
- [29.4 风险厌恶、效用与投资者选择](ch29-risk-return-capital-allocation/29.04.md)
- [29.5 风险资产与无风险资产之间的资本配置](ch29-risk-return-capital-allocation/29.05.md)
- [29.6 最优风险资产组合与资本配置线](ch29-risk-return-capital-allocation/29.06.md)

### 第 30 章 投资组合理论与指数模型

原书位置：Bodie/Kane/Marcus《Investments》Ch.7-Ch.8；相关旧笔记：本笔记 Ch.8, Ch.9, Ch.24。

- [30.1 分散化与组合风险](ch30-portfolio-theory-index-models/30.01.md)
- [30.2 两种风险资产的组合](ch30-portfolio-theory-index-models/30.02.md)
- [30.3 有效边界与 Markowitz 投资组合优化](ch30-portfolio-theory-index-models/30.03.md)
- [30.4 无风险资产、最优风险组合与分离定理](ch30-portfolio-theory-index-models/30.04.md)
- [30.5 单指数模型：系统性风险与公司特有风险](ch30-portfolio-theory-index-models/30.05.md)
- [30.6 用指数模型构建最优组合](ch30-portfolio-theory-index-models/30.06.md)
- [30.7 Alpha、信息比率与证券分析](ch30-portfolio-theory-index-models/30.07.md)

### 第 31 章 资产定价、市场效率与行为金融

原书位置：Bodie/Kane/Marcus《Investments》Ch.9-Ch.13；相关旧笔记：本笔记 Ch.9。

- [31.1 CAPM 与证券市场线](ch31-asset-pricing-market-efficiency/31.01.md)
- [31.2 CAPM 的扩展、限制与实证问题](ch31-asset-pricing-market-efficiency/31.02.md)
- [31.3 APT 与多因子风险模型](ch31-asset-pricing-market-efficiency/31.03.md)
- [31.4 Fama-French 模型与风险因子](ch31-asset-pricing-market-efficiency/31.04.md)
- [31.5 有效市场假说的形式与证据](ch31-asset-pricing-market-efficiency/31.05.md)
- [31.6 行为金融与技术分析](ch31-asset-pricing-market-efficiency/31.06.md)
- [31.7 证券收益的经验事实](ch31-asset-pricing-market-efficiency/31.07.md)

### 第 32 章 固定收益证券与债券组合管理

原书位置：Bodie/Kane/Marcus《Investments》Ch.14-Ch.16；相关旧笔记：本笔记 Ch.7, Ch.8, Ch.21。

- [32.1 债券价格、收益率与回报](ch32-fixed-income-portfolio-management/32.01.md)
- [32.2 债券契约、赎回条款与违约风险](ch32-fixed-income-portfolio-management/32.02.md)
- [32.3 利率期限结构](ch32-fixed-income-portfolio-management/32.03.md)
- [32.4 久期、凸性与利率风险](ch32-fixed-income-portfolio-management/32.04.md)
- [32.5 债券免疫与资产负债匹配](ch32-fixed-income-portfolio-management/32.05.md)
- [32.6 积极债券管理](ch32-fixed-income-portfolio-management/32.06.md)
- [32.7 信用风险与债券安全性](ch32-fixed-income-portfolio-management/32.07.md)

### 第 33 章 宏观行业分析与股票估值

原书位置：Bodie/Kane/Marcus《Investments》Ch.17-Ch.19；相关旧笔记：本笔记 Ch.9, Ch.22。

- [33.1 宏观经济分析与行业分析](ch33-equity-analysis-valuation/33.01.md)
- [33.2 经济周期、行业结构与公司竞争地位](ch33-equity-analysis-valuation/33.02.md)
- [33.3 股利贴现模型](ch33-equity-analysis-valuation/33.03.md)
- [33.4 自由现金流估值](ch33-equity-analysis-valuation/33.04.md)
- [33.5 市盈率与相对估值](ch33-equity-analysis-valuation/33.05.md)
- [33.6 财务报表分析与盈利能力](ch33-equity-analysis-valuation/33.06.md)
- [33.7 会计质量、增长率与权益估值误差](ch33-equity-analysis-valuation/33.07.md)

### 第 34 章 期权、期货、互换与风险管理

原书位置：Bodie/Kane/Marcus《Investments》Ch.20-Ch.23；相关旧笔记：本笔记 Ch.27。

- [34.1 期权市场与期权收益结构](ch34-options-futures-risk-management/34.01.md)
- [34.2 期权策略、保护性看跌与备兑看涨](ch34-options-futures-risk-management/34.02.md)
- [34.3 看跌-看涨平价与期权边界](ch34-options-futures-risk-management/34.03.md)
- [34.4 二叉树期权定价](ch34-options-futures-risk-management/34.04.md)
- [34.5 Black-Scholes 期权定价](ch34-options-futures-risk-management/34.05.md)
- [34.6 期货价格、基差与套期保值](ch34-options-futures-risk-management/34.06.md)
- [34.7 互换、组合保险与风险管理](ch34-options-futures-risk-management/34.07.md)

### 第 35 章 应用投资组合管理

原书位置：Bodie/Kane/Marcus《Investments》Ch.24-Ch.28；相关旧笔记：本笔记 Ch.24-Ch.27。

- [35.1 投资绩效评价](ch35-applied-portfolio-management/35.01.md)
- [35.2 风格分析与绩效归因](ch35-applied-portfolio-management/35.02.md)
- [35.3 国际分散化](ch35-applied-portfolio-management/35.03.md)
- [35.4 另类资产：对冲基金、私募股权与实物资产](ch35-applied-portfolio-management/35.04.md)
- [35.5 主动投资管理：Alpha 与 Treynor-Black](ch35-applied-portfolio-management/35.05.md)
- [35.6 Black-Litterman 模型](ch35-applied-portfolio-management/35.06.md)
- [35.7 投资政策、目标与约束](ch35-applied-portfolio-management/35.07.md)
- [35.8 机构投资者、个人投资者与 CFA 框架](ch35-applied-portfolio-management/35.08.md)

## 第十部分：量化投资与系统化组合管理

### 第 36 章 量化投资地图

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.1；相关旧笔记：本笔记 Ch.5, Ch.20-Ch.28。

- [36.1 证券、市场与交易方式](ch36-quant-investing-map/36.01.md)
- [36.2 买方、卖方与市场参与者](ch36-quant-investing-map/36.02.md)
- [36.3 超额收益从哪里来](ch36-quant-investing-map/36.03.md)
- [36.4 量化投资流程：信号、风险、组合与执行](ch36-quant-investing-map/36.04.md)

### 第 37 章 收益率、波动率与单资产建模

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.2；相关旧笔记：本笔记 Ch.29。

- [37.1 收益率、超额收益与对数收益](ch37-returns-volatility/37.01.md)
- [37.2 价格、收益率估计与数据质量](ch37-returns-volatility/37.02.md)
- [37.3 金融收益率的经验事实](ch37-returns-volatility/37.03.md)
- [37.4 GARCH 与条件异方差](ch37-returns-volatility/37.04.md)
- [37.5 实现波动率、EWMA 与状态空间波动率估计](ch37-returns-volatility/37.05.md)
- [37.6 Kalman Filter 在波动率估计中的直觉](ch37-returns-volatility/37.06.md)

### 第 38 章 投资绩效的基本度量

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.3；相关旧笔记：本笔记 Ch.29, Ch.35。

- [38.1 期望收益与可投资收益](ch38-performance-basics/38.01.md)
- [38.2 波动率、风险与风险调整收益](ch38-performance-basics/38.02.md)
- [38.3 Sharpe Ratio 的含义和局限](ch38-performance-basics/38.03.md)
- [38.4 策略容量与规模约束](ch38-performance-basics/38.04.md)

### 第 39 章 线性收益模型与因子框架

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.4；相关旧笔记：本笔记 Ch.30, Ch.31。

- [39.1 因子模型的基本形式](ch39-linear-factor-models/39.01.md)
- [39.2 因子暴露、因子收益与残差收益](ch39-linear-factor-models/39.02.md)
- [39.3 Alpha、风险因子与正交化](ch39-linear-factor-models/39.03.md)
- [39.4 旋转、投影与 push-out](ch39-linear-factor-models/39.04.md)
- [39.5 因子模型在归因、风控和组合管理中的用途](ch39-linear-factor-models/39.05.md)
- [39.6 常见因子模型类型](ch39-linear-factor-models/39.06.md)

### 第 40 章 风险模型评估

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.5；相关旧笔记：本笔记 Ch.27, Ch.30, Ch.32。

- [40.1 协方差矩阵为什么重要](ch40-risk-model-evaluation/40.01.md)
- [40.2 波动率和协方差预测的评价](ch40-risk-model-evaluation/40.02.md)
- [40.3 稳健损失函数与多资产风险评估](ch40-risk-model-evaluation/40.03.md)
- [40.4 精度矩阵、最小方差组合与 Mahalanobis 距离](ch40-risk-model-evaluation/40.04.md)
- [40.5 风险模型换手率、Beta 测试与辅助检验](ch40-risk-model-evaluation/40.05.md)

### 第 41 章 基本面因子模型

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.6；相关旧笔记：本笔记 Ch.31, Ch.33。

- [41.1 基本面因子模型的输入和流程](ch41-fundamental-factor-models/41.01.md)
- [41.2 横截面回归与因子收益估计](ch41-fundamental-factor-models/41.02.md)
- [41.3 因子协方差矩阵估计与收缩](ch41-fundamental-factor-models/41.03.md)
- [41.4 短期波动率更新与自相关修正](ch41-fundamental-factor-models/41.04.md)
- [41.5 特质风险、聚类与协方差收缩](ch41-fundamental-factor-models/41.05.md)
- [41.6 缩尾、模型连接与货币重定基](ch41-fundamental-factor-models/41.06.md)
- [41.7 常见基本面因子地图](ch41-fundamental-factor-models/41.07.md)

### 第 42 章 统计因子模型

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.7；相关旧笔记：本笔记 Ch.30, Ch.31。

- [42.1 PCA 与最佳低秩近似](ch42-statistical-factor-models/42.01.md)
- [42.2 最大似然、SVD 与统计因子估计](ch42-statistical-factor-models/42.02.md)
- [42.3 Spiked Covariance Model 与特征值收缩](ch42-statistical-factor-models/42.03.md)
- [42.4 因子数量选择](ch42-statistical-factor-models/42.04.md)
- [42.5 PCA 在真实市场数据中的行为](ch42-statistical-factor-models/42.05.md)
- [42.6 主成分解释：聚类视角与回归视角](ch42-statistical-factor-models/42.06.md)
- [42.7 统计因子模型的生产实现](ch42-statistical-factor-models/42.07.md)

### 第 43 章 Alpha 评价与回测纪律

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.8；相关旧笔记：本笔记 Ch.31, Ch.35。

- [43.1 数据来源、可得性与幸存者偏差](ch43-alpha-backtesting/43.01.md)
- [43.2 研究流程与实验记录](ch43-alpha-backtesting/43.02.md)
- [43.3 Cross-validation 与 walk-forward 回测](ch43-alpha-backtesting/43.03.md)
- [43.4 数据窥探、过拟合与多重检验](ch43-alpha-backtesting/43.04.md)
- [43.5 Rademacher Anti-Serum 的直觉](ch43-alpha-backtesting/43.05.md)
- [43.6 历史 anomaly 与实证检验](ch43-alpha-backtesting/43.06.md)

### 第 44 章 基础组合管理

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.9；相关旧笔记：本笔记 Ch.30, Ch.35。

- [44.1 为什么使用均值-方差优化](ch44-basic-portfolio-management/44.01.md)
- [44.2 均值-方差最优组合](ch44-basic-portfolio-management/44.02.md)
- [44.3 因子模拟组合与因子空间交易](ch44-basic-portfolio-management/44.03.md)
- [44.4 新因子的估计、加入与交易](ch44-basic-portfolio-management/44.04.md)
- [44.5 特质收益空间中的组合管理](ch44-basic-portfolio-management/44.05.md)
- [44.6 信息系数、分散化与信息比率](ch44-basic-portfolio-management/44.06.md)
- [44.7 信号聚合与组合聚合](ch44-basic-portfolio-management/44.07.md)

### 第 45 章 约束优化与模型误差

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.10；相关旧笔记：本笔记 Ch.30, Ch.35。

- [45.1 朴素均值-方差优化的问题](ch45-constrained-portfolio-optimization/45.01.md)
- [45.2 组合约束的类型](ch45-constrained-portfolio-optimization/45.02.md)
- [45.3 约束、惩罚项与实际可交易性](ch45-constrained-portfolio-optimization/45.03.md)
- [45.4 约束会改善还是损害表现](ch45-constrained-portfolio-optimization/45.04.md)
- [45.5 Alpha 误差对 Sharpe Ratio 的影响](ch45-constrained-portfolio-optimization/45.05.md)
- [45.6 风险模型误差对 Sharpe Ratio 的影响](ch45-constrained-portfolio-optimization/45.06.md)

### 第 46 章 交易成本与市场冲击

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.11；相关旧笔记：本笔记 Ch.27, Ch.28, Ch.35。

- [46.1 市场冲击的基本概念](ch46-transaction-costs-market-impact/46.01.md)
- [46.2 临时市场冲击与交易成本函数](ch46-transaction-costs-market-impact/46.02.md)
- [46.3 有限期交易成本感知优化](ch46-transaction-costs-market-impact/46.03.md)
- [46.4 无限期优化、无冲击极限与最优清算](ch46-transaction-costs-market-impact/46.04.md)
- [46.5 确定性 alpha 与 AR(1) 信号下的交易](ch46-transaction-costs-market-impact/46.05.md)

### 第 47 章 组合对冲

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.12；相关旧笔记：本笔记 Ch.27, Ch.34。

- [47.1 对冲问题的基本形式](ch47-hedging/47.01.md)
- [47.2 因子对冲的一般情形](ch47-hedging/47.02.md)
- [47.3 可交易因子的时间序列 Beta 对冲](ch47-hedging/47.03.md)
- [47.4 时间序列的因子模拟组合](ch47-hedging/47.04.md)

### 第 48 章 动态风险配置

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.13；相关旧笔记：本笔记 Ch.29, Ch.35。

- [48.1 Kelly Criterion 的基本思想](ch48-dynamic-risk-allocation/48.01.md)
- [48.2 Kelly 策略的数学性质](ch48-dynamic-risk-allocation/48.02.md)
- [48.3 Fractional Kelly 与风险缩放](ch48-dynamic-risk-allocation/48.03.md)
- [48.4 回撤控制与动态风险预算](ch48-dynamic-risk-allocation/48.04.md)

### 第 49 章 事后绩效归因

原书位置：Paleologo《The Elements of Quantitative Investing》Ch.14-Ch.15；相关旧笔记：本笔记 Ch.35。

- [49.1 绩效归因的基本问题](ch49-ex-post-performance-attribution/49.01.md)
- [49.2 带误差的绩效归因与归因悖论](ch49-ex-post-performance-attribution/49.02.md)
- [49.3 最大化绩效归因](ch49-ex-post-performance-attribution/49.03.md)
- [49.4 选股贡献与仓位大小贡献](ch49-ex-post-performance-attribution/49.04.md)
- [49.5 多空组合绩效归因与全书主题回收](ch49-ex-post-performance-attribution/49.05.md)

## 第十一部分：区块链、加密资产与去中心化金融

### 第 50 章 区块链与金融基础设施

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.1；相关旧笔记：本笔记 Ch.5-Ch.7, Ch.20, Ch.27。

- [50.1 为什么从金融基础设施而不是技术噱头理解区块链](ch50-blockchain-financial-infrastructure/50.01.md)
- [50.2 账本、产权记录与金融合同执行](ch50-blockchain-financial-infrastructure/50.02.md)
- [50.3 哈希、数字签名、Merkle Tree 与不可篡改性](ch50-blockchain-financial-infrastructure/50.03.md)
- [50.4 分布式账本和传统中心化账本的成本比较](ch50-blockchain-financial-infrastructure/50.04.md)
- [50.5 支付、清算、结算与托管的链上重组](ch50-blockchain-financial-infrastructure/50.05.md)
- [50.6 区块链的信任替代：代码、抵押品与经济激励](ch50-blockchain-financial-infrastructure/50.06.md)

### 第 51 章 Bitcoin、私人货币与去中心化支付

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.1；相关旧笔记：本笔记 Ch.6-Ch.8, Ch.20。

- [51.1 Bitcoin 的设计目标和货币实验](ch51-bitcoin-private-money-payments/51.01.md)
- [51.2 私人货币、国家货币与信用货币体系](ch51-bitcoin-private-money-payments/51.02.md)
- [51.3 挖矿、难度调整与安全预算](ch51-bitcoin-private-money-payments/51.03.md)
- [51.4 固定供给、减半机制与通胀叙事](ch51-bitcoin-private-money-payments/51.04.md)
- [51.5 支付媒介、价值储藏和投机资产的张力](ch51-bitcoin-private-money-payments/51.05.md)
- [51.6 Lightning Network 与小额支付的可行性](ch51-bitcoin-private-money-payments/51.06.md)

### 第 52 章 Ethereum 与智能合约平台

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.2；相关旧笔记：本笔记 Ch.5, Ch.27, Ch.46。

- [52.1 Ethereum 为什么是链上金融的操作系统](ch52-ethereum-smart-contract-platforms/52.01.md)
- [52.2 账户、状态、交易和 Gas 机制](ch52-ethereum-smart-contract-platforms/52.02.md)
- [52.3 智能合约如何把金融合同变成代码](ch52-ethereum-smart-contract-platforms/52.03.md)
- [52.4 PoS、质押收益与验证者经济学](ch52-ethereum-smart-contract-platforms/52.04.md)
- [52.5 Burn-and-Mint、手续费市场与 ETH 的资产属性](ch52-ethereum-smart-contract-platforms/52.05.md)
- [52.6 预言机、外部数据与合约执行风险](ch52-ethereum-smart-contract-platforms/52.06.md)

### 第 53 章 Layer 2、跨链与扩展性

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.3；相关旧笔记：本笔记 Ch.2, Ch.27, Ch.46。

- [53.1 区块链不可能三角：安全、去中心化与扩展性](ch53-layer2-crosschain-scalability/53.01.md)
- [53.2 Rollup、状态通道和侧链的基本逻辑](ch53-layer2-crosschain-scalability/53.02.md)
- [53.3 Optimistic Rollup 与 ZK Rollup 的取舍](ch53-layer2-crosschain-scalability/53.03.md)
- [53.4 跨链桥、互操作性与资产迁移风险](ch53-layer2-crosschain-scalability/53.04.md)
- [53.5 Solana、Cardano、Polkadot 等替代链的竞争逻辑](ch53-layer2-crosschain-scalability/53.05.md)
- [53.6 扩展性如何影响金融应用的交易成本和用户体验](ch53-layer2-crosschain-scalability/53.06.md)

### 第 54 章 稳定币与链上货币市场

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.4；相关旧笔记：本笔记 Ch.6-Ch.8, Ch.20-Ch.23。

- [54.1 稳定币为什么是 DeFi 的基础货币](ch54-stablecoins-onchain-money-markets/54.01.md)
- [54.2 法币抵押稳定币与银行存款的相似和差异](ch54-stablecoins-onchain-money-markets/54.02.md)
- [54.3 加密抵押稳定币、超额抵押与清算机制](ch54-stablecoins-onchain-money-markets/54.03.md)
- [54.4 算法稳定币、反身性与崩盘机制](ch54-stablecoins-onchain-money-markets/54.04.md)
- [54.5 储备资产、期限错配和货币市场基金类比](ch54-stablecoins-onchain-money-markets/54.05.md)
- [54.6 稳定币的支付、跨境转账和流动性功能](ch54-stablecoins-onchain-money-markets/54.06.md)

### 第 55 章 CBDC 与数字货币制度

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.5；相关旧笔记：本笔记 Ch.6-Ch.8, Ch.21-Ch.23。

- [55.1 CBDC 是央行负债的数字化还是货币制度重构](ch55-cbdc-digital-money-regime/55.01.md)
- [55.2 账户型、代币型、一层和两层 CBDC 架构](ch55-cbdc-digital-money-regime/55.02.md)
- [55.3 CBDC、商业银行存款和金融脱媒风险](ch55-cbdc-digital-money-regime/55.03.md)
- [55.4 数字货币对货币政策传导的影响](ch55-cbdc-digital-money-regime/55.04.md)
- [55.5 隐私、可编程性和公共部门边界](ch55-cbdc-digital-money-regime/55.05.md)
- [55.6 稳定币、CBDC 与现有支付体系的竞争](ch55-cbdc-digital-money-regime/55.06.md)

### 第 56 章 加密资产定价

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.1-Ch.4, Ch.9；相关旧笔记：本笔记 Ch.29-Ch.33, Ch.37-Ch.43。

- [56.1 加密资产的分类：货币型、平台型、治理型和证券型](ch56-crypto-asset-pricing/56.01.md)
- [56.2 收益率、波动率和尾部风险的经验特征](ch56-crypto-asset-pricing/56.02.md)
- [56.3 网络价值、用户增长和链上基本面指标](ch56-crypto-asset-pricing/56.03.md)
- [56.4 现金流估值、相对估值和网络估值的适用边界](ch56-crypto-asset-pricing/56.04.md)
- [56.5 风险溢价、流动性溢价和泡沫成分](ch56-crypto-asset-pricing/56.05.md)
- [56.6 加密资产与股票、债券、商品的组合关系](ch56-crypto-asset-pricing/56.06.md)

### 第 57 章 代币经济学与协议商业模式

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.2, Ch.6, Ch.9-Ch.10；相关旧笔记：本笔记 Ch.2, Ch.24, Ch.31, Ch.33。

- [57.1 Token 的经济权利：使用权、治理权和现金流请求权](ch57-tokenomics-protocol-business-models/57.01.md)
- [57.2 发行、解锁、通胀和销毁机制](ch57-tokenomics-protocol-business-models/57.02.md)
- [57.3 协议收入、手续费分配和价值捕获](ch57-tokenomics-protocol-business-models/57.03.md)
- [57.4 治理代币、投票权和委托代理问题](ch57-tokenomics-protocol-business-models/57.04.md)
- [57.5 空投、流动性挖矿和增长激励的可持续性](ch57-tokenomics-protocol-business-models/57.05.md)
- [57.6 代币经济设计中的博弈论约束](ch57-tokenomics-protocol-business-models/57.06.md)

### 第 58 章 DeFi 金融中介地图

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.6；相关旧笔记：本笔记 Ch.5, Ch.20-Ch.25, Ch.35。

- [58.1 DeFi 如何拆解银行、券商、交易所和基金的功能](ch58-defi-financial-intermediation-map/58.01.md)
- [58.2 钱包、私钥、托管和用户资产控制权](ch58-defi-financial-intermediation-map/58.02.md)
- [58.3 协议、前端、DAO 和链上治理结构](ch58-defi-financial-intermediation-map/58.03.md)
- [58.4 可组合性：金融积木的效率和脆弱性](ch58-defi-financial-intermediation-map/58.04.md)
- [58.5 DeFi 和 CeFi 的边界：交易所、托管商和做市商](ch58-defi-financial-intermediation-map/58.05.md)
- [58.6 从金融中介理论看 DeFi 的真实价值](ch58-defi-financial-intermediation-map/58.06.md)

### 第 59 章 DeFi 借贷、抵押与链上信用

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.6；相关旧笔记：本笔记 Ch.20-Ch.25, Ch.32, Ch.35。

- [59.1 Aave、Compound 与资金池借贷模型](ch59-defi-lending-collateral-credit/59.01.md)
- [59.2 抵押品、抵押率和清算阈值](ch59-defi-lending-collateral-credit/59.02.md)
- [59.3 利率模型、资金利用率和流动性风险](ch59-defi-lending-collateral-credit/59.03.md)
- [59.4 链上信用为什么高度依赖超额抵押](ch59-defi-lending-collateral-credit/59.04.md)
- [59.5 清算人、套利者和风险转移机制](ch59-defi-lending-collateral-credit/59.05.md)
- [59.6 DeFi 借贷与银行信贷、回购市场的比较](ch59-defi-lending-collateral-credit/59.06.md)

### 第 60 章 DEX、AMM 与链上市场微观结构

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.7；相关旧笔记：本笔记 Ch.27-Ch.28, Ch.46。

- [60.1 去中心化交易所和传统订单簿的差异](ch60-dex-amm-market-microstructure/60.01.md)
- [60.2 恒定乘积做市、价格曲线和库存风险](ch60-dex-amm-market-microstructure/60.02.md)
- [60.3 套利如何把 AMM 价格拉回外部市场](ch60-dex-amm-market-microstructure/60.03.md)
- [60.4 滑点、交易成本和大额交易执行](ch60-dex-amm-market-microstructure/60.04.md)
- [60.5 MEV、抢跑和链上交易排序](ch60-dex-amm-market-microstructure/60.05.md)
- [60.6 AMM 与传统做市商、交易所和暗池的比较](ch60-dex-amm-market-microstructure/60.06.md)

### 第 61 章 流动性池、质押与链上收益

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.8；相关旧笔记：本笔记 Ch.24, Ch.35, Ch.38, Ch.44。

- [61.1 流动性池如何形成可交易市场](ch61-liquidity-pools-staking-onchain-yield/61.01.md)
- [61.2 LP 收益、手续费收入和无常损失](ch61-liquidity-pools-staking-onchain-yield/61.02.md)
- [61.3 Curve Wars、治理激励和流动性竞争](ch61-liquidity-pools-staking-onchain-yield/61.03.md)
- [61.4 质押、流动性质押和再质押的收益来源](ch61-liquidity-pools-staking-onchain-yield/61.04.md)
- [61.5 收益农场、杠杆循环和可持续性问题](ch61-liquidity-pools-staking-onchain-yield/61.05.md)
- [61.6 链上收益和传统固定收益、货币市场收益的比较](ch61-liquidity-pools-staking-onchain-yield/61.06.md)

### 第 62 章 链上衍生品与结构化风险

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.12；相关旧笔记：本笔记 Ch.34, Ch.37-Ch.38, Ch.47。

- [62.1 加密市场的杠杆、保证金和抵押品](ch62-onchain-derivatives-structured-risk/62.01.md)
- [62.2 永续合约、资金费率和期货定价关系](ch62-onchain-derivatives-structured-risk/62.02.md)
- [62.3 链上期权、结构化产品和保险协议](ch62-onchain-derivatives-structured-risk/62.03.md)
- [62.4 预言机价格、强平机制和连环去杠杆](ch62-onchain-derivatives-structured-risk/62.04.md)
- [62.5 衍生品协议的风险准备金和保险基金](ch62-onchain-derivatives-structured-risk/62.05.md)
- [62.6 链上衍生品和传统期货期权市场的差异](ch62-onchain-derivatives-structured-risk/62.06.md)

### 第 63 章 加密交易策略与组合管理

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.12；相关旧笔记：本笔记 Ch.35, Ch.38, Ch.43-Ch.49。

- [63.1 现货、期货、永续合约和跨市场套利](ch63-crypto-trading-portfolio-management/63.01.md)
- [63.2 动量、反转、资金费率和基差策略](ch63-crypto-trading-portfolio-management/63.02.md)
- [63.3 链上数据因子和交易信号构造](ch63-crypto-trading-portfolio-management/63.03.md)
- [63.4 回测偏差、交易成本和策略容量](ch63-crypto-trading-portfolio-management/63.04.md)
- [63.5 加密组合的风险预算和动态仓位管理](ch63-crypto-trading-portfolio-management/63.05.md)
- [63.6 绩效归因：Beta、流动性、杠杆和 Alpha](ch63-crypto-trading-portfolio-management/63.06.md)

### 第 64 章 资产代币化、RWA 与证券市场重构

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.9；相关旧笔记：本笔记 Ch.24, Ch.33, Ch.35。

- [64.1 Tokenization 如何把资产权利搬到链上](ch64-tokenization-rwa-securities-markets/64.01.md)
- [64.2 证券型代币、链上基金和现实世界资产](ch64-tokenization-rwa-securities-markets/64.02.md)
- [64.3 分割性、可组合性和流动性改善](ch64-tokenization-rwa-securities-markets/64.03.md)
- [64.4 抵押品管理、链上登记和证券结算](ch64-tokenization-rwa-securities-markets/64.04.md)
- [64.5 代币化资产的估值、披露和投资者保护](ch64-tokenization-rwa-securities-markets/64.05.md)
- [64.6 代币化资产与传统资本市场的连接方式](ch64-tokenization-rwa-securities-markets/64.06.md)

### 第 65 章 NFT、Web3 应用与数字产权

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.10, Ch.13-Ch.14；相关旧笔记：本笔记 Ch.2, Ch.5, Ch.24, Ch.33。

- [65.1 NFT 的产权、稀缺性和可验证所有权](ch65-nft-web3-digital-property/65.01.md)
- [65.2 NFT 估值：文化资产、会员权益和金融化](ch65-nft-web3-digital-property/65.02.md)
- [65.3 GameFi 的激励设计和虚拟经济](ch65-nft-web3-digital-property/65.03.md)
- [65.4 品牌 Web3、用户关系和平台经济](ch65-nft-web3-digital-property/65.04.md)
- [65.5 NFT 与 DeFi 的结合：抵押、租赁和碎片化](ch65-nft-web3-digital-property/65.05.md)
- [65.6 Web3 应用为什么经常从经济机制走向投机循环](ch65-nft-web3-digital-property/65.06.md)

### 第 66 章 加密金融监管、系统性风险与未来边界

原书位置：Di Maggio《Blockchain, Crypto and DeFi》Ch.11, Ch.15；相关旧笔记：本笔记 Ch.6, Ch.21-Ch.23, Ch.35。

- [66.1 加密资产到底是不是证券](ch66-crypto-regulation-systemic-risk-future/66.01.md)
- [66.2 交易所、托管、储备证明和投资者保护](ch66-crypto-regulation-systemic-risk-future/66.02.md)
- [66.3 DeFi 监管：协议、开发者、前端和 DAO](ch66-crypto-regulation-systemic-risk-future/66.03.md)
- [66.4 稳定币挤兑、杠杆清算和风险传染](ch66-crypto-regulation-systemic-risk-future/66.04.md)
- [66.5 黑客攻击、跨链桥风险和智能合约审计](ch66-crypto-regulation-systemic-risk-future/66.05.md)
- [66.6 AI 与区块链：可信计算、身份、数据和金融自动化](ch66-crypto-regulation-systemic-risk-future/66.06.md)
- [66.7 从技术叙事回到经济机制和金融约束](ch66-crypto-regulation-systemic-risk-future/66.07.md)
