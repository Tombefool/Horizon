---
layout: default
title: "Horizon Summary: 2026-11-15 (ZH)"
date: 2026-11-15
lang: zh
---

> 从 16 条内容中筛选出 6 条重要资讯。

---

**科技与 AI 要闻**
1. [SpaceX 星舰 15 号飞行首次捕获上级火箭](#item-tech-lite-1) ⭐️ 9.0/10
2. [CMP 170HX 电压故障注入解锁 80GB 显存和 126 SM](#item-tech-lite-2) ⭐️ 8.0/10
3. [AI 生成代码应开源引发版权与许可争议](#item-tech-lite-3) ⭐️ 7.0/10
4. [MacBook Pro 串联 OLED 的 PWM 调光导致视疲劳问题](#item-tech-lite-4) ⭐️ 7.0/10
5. [联邦法院允许 DRAM 价格垄断诉讼继续审理](#item-tech-lite-5) ⭐️ 7.0/10
6. [Basalt 0.4.0 发布：Qwen 3.8 27B 密集模型达 776 tok/s](#item-tech-lite-6) ⭐️ 7.0/10

---

## 科技与 AI 要闻

<a id="item-tech-lite-1"></a>
### [SpaceX 星舰 15 号飞行首次捕获上级火箭](https://www.spacex.com/launches/starship-flight-15) ⭐️ 9.0/10

SpaceX 在 2026 年 11 月 14 日的星舰 15 号飞行中，成功使用发射塔的“筷子”机械臂捕获返回的星舰上级火箭，实现了自航天飞机以来首次双级火箭全复用演示。此次捕获标志着星舰上级火箭首次完整回收，验证了热盾和精确控制系统的可行性。该成果为后续双级同步捕获和快速复用铺平道路。

hackernews · ls612 · 11月14日 21:22 · [社区讨论](https://news.ycombinator.com/item?id=50500963)

**「背景」** 星舰系统由超重型助推器和星舰上级组成，此前已多次演示助推器回收捕获，但上级火箭的轨道再入和捕获回收是实现完全快速复用的关键剩余步骤。

**「影响」** 这一突破若能转化为常态化操作，将大幅降低轨道发射成本并提高发射频率，使完全复用的重型运载火箭成为现实，对卫星部署、深空探测及商业航天经济模式产生直接影响。

**「社区讨论」** Hacker News 讨论中，用户 Zigurd 指出这是航天飞机以来首个可复用上级演示，但强调航天飞机翻新成本高、发射频率低；small\_model 认为若热盾经受住考验将改变一切，下一步是双级捕获和重复飞行；ChuckMcM 质疑最终有效载荷质量分数，但认同 100% 复用优于猎鹰 9 约 60% 的复用比例（按成本计）。

**标签**: `#spaceflight`, `#aerospace`, `#reusable-rockets`, `#spacex`, `#starship`

---

<a id="item-tech-lite-2"></a>
### [CMP 170HX 电压故障注入解锁 80GB 显存和 126 SM](https://www.reddit.com/r/LocalLLaMA/comments/1xwxzgj/i_finally_succeed_the_cmp_170hx_voltage_glitch/) ⭐️ 8.0/10

Reddit 用户 /u/Yarukiless-cat 成功对 NVIDIA CMP 170HX 挖矿卡实施电压故障注入，利用 Raspberry Pi Pico 实现固件写入访问，耗时约 15 小时解锁 80GB 显存和 126 个 SM，使其性能接近 A100 80GB。该方法于 5 天前公开，用户计划对第二张卡重复操作。

reddit · r/LocalLLaMA · /u/Yarukiless-cat · 11月15日 15:16

**「背景」** CMP 170HX 是 NVIDIA 面向加密货币挖矿推出的专用卡，基于 GA100 芯片但通过固件限制显存和 SM 数量。电压故障注入是一种硬件攻击技术，通过在关键时刻干扰供电电压诱导处理器跳过安全检查，从而获得受限固件区域的写入权限。

**「影响」** 二手挖矿卡通过硬件改造可低成本获得 80GB 显存，大幅降低本地运行大型语言模型的硬件门槛，为个人开发者和小型团队提供接近 A100 级别的推理算力。

**标签**: `#hardware-hacking`, `#local-llm`, `#gpu-modding`, `#nvidia-cmp`, `#voltage-glitching`

---

<a id="item-tech-lite-3"></a>
### [AI 生成代码应开源引发版权与许可争议](https://jakub.jankiewicz.org/blog/ai-code-open-source/) ⭐️ 7.0/10

一篇博客文章主张 AI 生成的代码应当开源，在 Hacker News 上引发 340 条评论的激烈讨论。核心争议点包括：公司涉嫌利用 LLM 克隆 AGPL 许可代码并规避合规义务、美国版权局指导意见认定 AI 辅助代码可获版权保护、以及 Doe 诉 GitHub 案和 Thaler 诉 Perlmutter 案等法律判例对 AI 输出版权归属的界定。

hackernews · jcubic · 11月15日 14:46 · [社区讨论](https://news.ycombinator.com/item?id=50507303)

**「背景」** 这场辩论建立在开源许可证（特别是 AGPL 等强复制许可）与 LLM 在公开代码库上训练之间的长期张力之上，近期美国版权局发布指导意见澄清了 AI 辅助作品的版权可获得性，为讨论提供了新的法律参考框架。

**「影响」** 使用 AI 编程工具的开发者和企业面临许可合规与 AI 生成代码所有权的不确定性，尤其是当训练数据包含强复制许可代码时，可能面临衍生作品许可义务或版权侵权风险。

**「社区讨论」** 评论者对 AI 生成代码是否继承训练数据许可存在分歧：有人引用美国版权局指导意见主张 AI 辅助代码仍可获版权，也有人指出 Doe 诉 GitHub 案判决表明 LLM 输出不自动继承开源许可；另有开发者报告遭遇公司利用 LLM 克隆其 AGPL 代码并移除版权声明的实例。

**标签**: `#AI-generated code`, `#open source licensing`, `#copyright law`, `#software ethics`, `#LLM training data`

---

<a id="item-tech-lite-4"></a>
### [MacBook Pro 串联 OLED 的 PWM 调光导致视疲劳问题](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) ⭐️ 7.0/10

Apple 在 MacBook Pro 中采用的串联 OLED 面板使用 PWM 调光，社区实测显示其有效频率高达 960 Hz（两层面板 480 Hz 反相叠加），但仍对光敏感用户造成眼部不适。文章指出这种实现虽提升亮度与对比度，却在可用亮度范围内引入了可感知的闪烁，成为显示素质的退步。该问题影响依赖长时间阅读代码或文本的开发者与专业用户。

hackernews · MacAnorak · 11月15日 13:15 · [社区讨论](https://news.ycombinator.com/item?id=50506719)

**「背景」** PWM（脉宽调制）通过快速开关背光控制亮度，低频或占空比变化易被敏感人群察觉为闪烁；串联 OLED 叠加两层发光层以提升峰值亮度，但若两层调光不同相位，会产生合成频率更高的残留闪烁。

**「影响」** 对 PWM 敏感的开发者可能无法在新款 MacBook Pro 上长时间工作而不出现眼疲劳、头痛等症状，且目前 macOS 无系统级 DC 调光开关可缓解该问题。

**「社区讨论」** 社区实测者指出串联 OLED 两层面板以 480 Hz、180 度反相运行，合成有效频率达 960 Hz，但仍有用户反馈在可用亮度下能感知亮度不稳；也有脑震荡后遗症用户表示任何屏幕闪烁均会加重症状，呼吁厂商提供真正的 DC 调光选项。

**标签**: `#display-technology`, `#pwm`, `#oled`, `#macbook-pro`, `#hardware-engineering`, `#accessibility`

---

<a id="item-tech-lite-5"></a>
### [联邦法院允许 DRAM 价格垄断诉讼继续审理](https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal) ⭐️ 7.0/10

美国联邦法院驳回了三星、SK 海力士和美光提出的驳回动议，允许针对这三大 DRAM 制造商的价格垄断共谋诉讼继续进行。法院认定原告提供的证据足以支持指控，即这三家占据市场主导地位的厂商通过协调产量和价格实施了反竞争行为。案件将进入证据开示和审理阶段，原告寻求三倍赔偿及禁令救济。

hackernews · ybathaee · 11月15日 01:18 · [社区讨论](https://news.ycombinator.com/item?id=50502988)

**「背景信息」** DRAM 市场长期由三星、SK 海力士和美光三家韩美厂商主导，合计市场份额超过 90%。此前美国司法部曾于 2000 年代和 2010 年代分别对 DRAM 价格垄断提起刑事诉讼，多家厂商认罪并缴纳巨额罚款。本案为民事集体诉讼，由采购方发起，指控厂商在 2016 年后继续通过隐性协调维持高价。

**「潜在影响」** 若原告胜诉，三大厂商可能面临数十亿美元赔偿，并可能被迫改变定价与产能决策机制，直接降低服务器、工作站及消费级内存的采购成本。企业采购方和科研机构可关注案件进展，以评估未来内存预算规划。

**「社区讨论」** 评论者普遍关注高昂内存价格对科研预算的挤压，有用户表示 256GB 内存成本达 4-5 千美元，迫使其在购买与等待间艰难抉择。也有观点认为 DRAM 市场已形成隐性共谋模式，无需显性串通即可维持高价；但亦有声音质疑垄断论，指出 DDR3/4/5 代际升级带来的真实性能提升，以及中国厂商可供应 DDR4 芯片等反驳论据。

**标签**: `#DRAM`, `#antitrust`, `#price-fixing`, `#semiconductors`, `#hardware`

---

<a id="item-tech-lite-6"></a>
### [Basalt 0.4.0 发布：Qwen 3.8 27B 密集模型达 776 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/) ⭐️ 7.0/10

Basalt 0.4.0 发布，新增对密集模型的支持，首发 Qwen 3.8 27B 量化版本。在 RTX 5090 上单流推理可达结构化输出 776 tok/s、对话 262 tok/s、散文 194 tok/s；prefill 阶段 4k 上下文达 12,000 tok/s。模型在 top-1 准确率上达到 BF16 基准的 92.8%（KLD 0.0262），支持聊天、工具调用、思维链、图像与视频，上下文长度高达 262K。同版本还引入多模型路由、视频支持、聊天中文件上传等功能。

reddit · r/LocalLLaMA · /u/jesdga95 · 11月15日 17:30

**「背景」** Basalt 是面向本地大语言模型的推理引擎，专注于内核级优化与量化加速。此前版本已支持 MoE 模型（如 DeepSeek V4.1 Flash），此次 0.4.0 为即将到来的 Qwen 4 做密集模型内核预研，首次提供密集模型量化权重与完整推理管线。

**「影响」** 开发者可在单张 RTX 5090 上以接近 BF16 的精度运行 27B 密集模型，并获得超高吞吐，适合对延迟敏感的本地部署场景；量化权重已上传 Hugging Face，可直接集成至现有 Basalt 工作流。

**标签**: `#local-llm`, `#inference-optimization`, `#quantization`, `#basalt`, `#qwen`

---