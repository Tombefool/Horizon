---
layout: default
title: "Horizon Summary: 2026-11-17 (ZH)"
date: 2026-11-17
lang: zh
---

> 从 13 条内容中筛选出 3 条重要资讯。

---

**全球情报行业动态**
1. [Unit 42 披露东南亚政府遭 HTTP/3 RAT 间谍攻击](#item-intel-news-1) ⭐️ 8.0/10
2. [GAO 报告：五角大楼转向 LEO 星座致工业基础紧张](#item-intel-news-2) ⭐️ 7.0/10
3. [巴基斯坦黑客利用虚假招聘网站窃取国防人员数据](#item-intel-news-3) ⭐️ 7.0/10

---

## 全球情报行业动态

<a id="item-intel-news-1"></a>
### [Unit 42 披露东南亚政府遭 HTTP/3 RAT 间谍攻击](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/) ⭐️ 8.0/10

Unit 42（Palo Alto Networks 威胁研究团队）报告发现一起针对东南亚政府实体的网络间谍活动，攻击者部署了名为 PerfectPioneer 和模块化 KUKURAT 的定制远程访问木马（RAT），并利用 HTTP/3 与 QUIC 协议建立隐蔽的命令与控制（C2）通信通道。该活动利用 HTTP/3 的多路复用和加密特性规避传统流量检测，目标涉及多个东南亚国家的政府机构。报告指出这是首次大规模观测到基于 HTTP/3 的恶意软件针对政府目标，标志着攻击者隐蔽通信技术的显著演进。

rss · Unit 42 · 11月16日 23:00

**「背景」** HTTP/3 基于 QUIC 协议，提供内置加密与多路复用，近期开始被恶意软件作者滥用以绕过基于传统 HTTP/1.1 或 HTTP/2 特征的检测体系。

**「影响」** 威胁情报从业者需优先跟踪基于 HTTP/3 的 C2 技术，并更新检测签名与网络监控方案以覆盖 QUIC 协议流量。

**标签**: `#cyber threat intelligence`, `#APT`, `#Southeast Asia`, `#HTTP/3`, `#QUIC`, `#RAT`, `#espionage`

---

<a id="item-intel-news-2"></a>
### [GAO 报告：五角大楼转向 LEO 星座致工业基础紧张](https://defensescoop.com/2026/11/17/space-industrial-base-stretched-thin-gao-report/) ⭐️ 7.0/10

美国政府问责局（GAO）于 2026 年 11 月 17 日发布报告（GAO-27-108683）警告，五角大楼计划在未来五年投入 330 亿美元，将空间系统从少量大型卫星转向大规模低地球轨道（LEO）星座，以应对中俄威胁，但这一转型正使专业化的空间工业基础承受巨大压力。报告指出，国防部对专用和资本密集型能力的需求，在半导体、电子元件、原材料及制造产能等关键资源上与其他快速增长部门形成激烈竞争，威胁到太空军采购未来任务所需技术的能力。GAO 建议国防部长集中监管空军部和国家侦察办公室（NRO）的供应链短板，并要求空军部长落实采购领导岗位及企业级风险协议；国防部和空军均表示同意。

rss · DefenseScoop · 11月17日 20:15

**「背景」** 自 2020 年起，太空军启动“扩散作战员空间架构”（PWSA），旨在减少对地球同步轨道传统卫星的依赖，部署大量近地小卫星以提高生存能力和重访率。GAO 在 2025 年 8 月至 2026 年 11 月期间评估了 PWSA、GPS III 后续型（GPS IIIF）和弹道导弹预警跟踪中地球轨道（MWT MEO）三个项目的供应链状况。

**「影响」** GAO 披露，PWSA 项目（五年预算 156 亿美元）已因供应链瓶颈导致演示截止日期延误、规模化困难和交付滞后；MWT MEO 项目（五年预算 83 亿美元）则因印制电路板短缺推迟发射，显示工业基础短板正直接拖延关键任务部署。

**标签**: `#GEOINT`, `#Space Force`, `#industrial base`, `#GAO`, `#satellite constellations`

---

<a id="item-intel-news-3"></a>
### [巴基斯坦黑客利用虚假招聘网站窃取国防人员数据](https://cyberscoop.com/pakistani-hackers-defense-workers-fake-job-sites/) ⭐️ 7.0/10

网络安全公司 Lookout 研究发现，一个疑似与巴基斯坦政府有关的黑客组织（被称为 SpaceCobra 或 Cosmic Leopard）正在进行持续的网络间谍活动，通过虚假招聘网站向印度国防承包商和军事人员投放 GravityRAT 间谍软件。该活动已持续 12 个月且仍在进行中。攻击者构建了高度逼真的虚假招聘网站，甚至在“合作客户”栏展示空客、BAE 系统、洛克希德·马丁、诺斯罗普·格鲁曼、莱茵金属、劳斯莱斯、萨博、赛峰和泰雷兹等知名国防企业的标志。Lookout 高级安全情报研究经理 Parth Bhatt 指出，部分网站未提及印度，显示攻击目标可能扩展至全球国防人员。网站还设有虚假的 Google Play 商店下载按钮，点击后提示应用正在审核，诱导用户直接下载恶意软件。GravityRAT 自 2015 年以来持续活跃，能窃取通讯录、通话记录、短信、WhatsApp 消息等数据。

rss · CyberScoop · 11月17日 14:00

**「背景」** GravityRAT 是一款已知的间谍软件家族，自 2015 年起被巴基斯坦相关威胁组织用于针对印度目标的网络间谍行动。SpaceCobra 和 Cosmic Leopard 是安全研究社区对该组织的不同称呼。此次活动的新特点是大规模使用社会工程学手段，构建完整的虚假招聘品牌和网站，而非仅依赖钓鱼邮件或恶意链接。

**「影响」** 该活动表明国家支持的威胁行为体正在投入更多资源打造持久、可信的虚假招聘品牌，以绕过传统安全防护并扩大目标范围。国防行业从业者和安全团队需警惕看似合法的招聘网站，并加强对移动端恶意软件分发渠道的监测。

**标签**: `#cyber threat intelligence`, `#APT`, `#GravityRAT`, `#social engineering`, `#defense sector`

---