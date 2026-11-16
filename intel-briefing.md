---
layout: default
title: 全球情报行业日报说明
---

# 本站日报说明

这个 Horizon 实例每天自动整理一份**全球情报行业热点与动态**简报，同时发布[中文]({{ '/feed-zh.xml' | relative_url }})和[英文]({{ '/feed-en.xml' | relative_url }})版本。关注范围仅限公开报道，不包括内部、机密或非公开材料。

## 关注范围

- 情报机构、监督机构，以及影响情报授权、预算、人事或问责的政策与法律动态
- 开源情报（OSINT）的方法、工具、调查与行业实践
- 网络威胁情报：行为体与行动报道、官方通告、威胁情报团队的重要研究
- 商业情报、调查和威胁情报公司的产品、合同、并购、融资与人事
- 地理空间与卫星情报（GEOINT），以及明显服务于侦察或情报任务的相关技术

会过滤：一般开发者或人工智能产品新闻、日常漏洞通报、股价评论，以及与上述范围没有直接关系的地缘政治或军事报道。

每日最多收录约 8 条，采集窗口为过去 24 小时。若当天没有达到重要性阈值的条目，站点仍会发布一期「暂无重要动态」说明，不会删除既有历史日报。

## 已启用的信息源

下列源均已在部署前实际抓取并解析，确认是可公开访问的 RSS/Atom，且近期有内容。每条简报都会保留原文链接；对指控、爆料和未经证实的报道，会要求模型明确标注来源，而不写成已证实事实。

| 分类 | 来源 | 地址 | 说明与限制 |
| --- | --- | --- | --- |
| 机构与政策 | [The Cipher Brief](https://www.thecipherbrief.com/feed) | 情报界与国家安全报道 | 也含评论和更宽的安全议题，需靠评分与主题规则筛选 |
| 机构与政策 | [CISA News](https://www.cisa.gov/news.xml) | 美国网络安全与基础设施安全局新闻 | 官方新闻，不含其全部漏洞通告流 |
| 机构与政策 | [NCSC UK News](https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml) | 英国国家网络安全中心新闻 | 官方新闻；技术报告是另一条更新更慢的源，未启用 |
| 机构与政策 | [DefenseScoop](https://defensescoop.com/feed/) | 美国防务技术与机构采购报道 | 会夹杂一般武器试验等无关条目，需筛选 |
| OSINT | [Bellingcat](https://www.bellingcat.com/feed/) | 开源调查 | 更新频率不固定，且常涉及冲突现场，只保留与情报方法或行业相关的条目 |
| 威胁情报 | [The Record](https://therecord.media/feed) | Recorded Future 旗下新闻 | 新闻报道，不是公司博客 |
| 威胁情报 | [CyberScoop](https://cyberscoop.com/feed/) | 网络政策与威胁情报新闻 | 也可能出现偏消费级安全的条目 |
| 威胁情报 | [Unit 42](https://unit42.paloaltonetworks.com/feed/) | Palo Alto Networks 威胁情报研究 | 研究类更新，不一定每天都有 |
| 威胁情报 | [Krebs on Security](https://krebsonsecurity.com/feed/) | 调查报道 | 更新较少，每天最多取 1 条 |
| 威胁情报 | [CERT-EU Threat Intelligence](https://cert.europa.eu/publications/threat-intelligence-rss) | 欧盟机构网络安全团队通报 | 多为月刊或阶段性简报，多数日子不会进入 24 小时窗口 |
| 商业情报 | [Recorded Future](https://www.recordedfuture.com/feed) | 威胁情报公司博客 | 含研究，也可能含产品和市场内容 |
| 商业情报 | [Flashpoint Blog](https://flashpoint.io/blog/feed/) | 商业威胁情报公司博客 | 同上，促销或评奖内容应被低分过滤 |
| 地理空间 | [USGIF](https://usgif.org/feed/) | 美国地理空间情报基金会 | 专业社区动态，有时是奖项、活动或认证消息 |
| 地理空间 | [Via Satellite Government/Military](https://www.satellitetoday.com/government-military/feed/) | 政府与军事卫星报道 | 比综合航天新闻更贴近 GEOINT，仍可能含产业政策杂讯 |

为控制免费模型额度，每个源每天只取最近的少量条目，并按分类设置收录上限，避免单一来源占满 8 条。

## 明确未纳入的来源

在核查中放弃了这些候选，以免写入无法使用或不合适的地址：

- **ODNI、FBI、Palantir、Maxar、Planet、Janes、Intelligence Online、Control Risks、Kroll**：未找到可用的官方 RSS，或页面无法解析为新闻源。没有编造地址。
- **Lawfare Intelligence 专题源**：地址有效，但当前源内没有条目。
- **Europol 新闻源**：可以解析，但条目没有发布日期，无法按 24 小时窗口筛选。
- **澳大利亚网络中心（ACSC）**：抓取超时，不作为稳定源。
- **CISA / CERT-EU 漏洞通告、暗网阅读综合安全新闻、SpaceNews 综合航天新闻、C4ISRNET 主源**：可解析，但日常漏洞清单、消费级安全或宽泛防务/航天内容过多。
- **Google Threat Intelligence / Mandiant 博客**：曾成功解析，但随后多次抓取超时，不作为稳定源。
- **Google News 检索**：能返回结果，但公司名检索会混入大量股价和泛 AI 报道，容易浪费额度，因此未启用。
- 中文候选源（如安全内参、FreeBuf、CNCERT 公开地址）在核查时无法稳定获取，因此本轮未加入中文原始源。日报本身仍由模型输出简体中文和英文。

## 其他限制

- 简报只处理公开网页和官方新闻源，不是情报收集系统，也不能反映非公开信息。
- 模型可能误判相关性或把媒体转述写成确定事实；请以原文为准。
- 每日运行使用 OpenRouter 免费模型，并有请求频率限制。GitHub 定时任务有时会排队，实际发布时间可能晚于设定的 12:00 UTC。
- 历史日报和 `site` 发布分支会保留，不会因为调整主题而删除旧文章。
