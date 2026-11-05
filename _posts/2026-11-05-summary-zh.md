---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05
lang: zh
---

> 从 23 条内容中筛选出 4 条重要资讯。

---

**科技与 AI 要闻**
1. [OpenSSH sshole 漏洞：crypt\(\) 处理 &\#x27;\*&\#x27; 哈希值缺陷](#item-tech-lite-1) ⭐️ 8.0/10
2. [Hugging Face 发布 Phonon TTS：设立新基准的设备端语音合成模型](#item-tech-lite-2) ⭐️ 8.0/10
3. [PHP 修复两个已遭利用的严重 RCE 漏洞](#item-tech-lite-3) ⭐️ 8.0/10
4. [Delta Inference Engine v0.93 发布：支持 64 GB 内存、Unsloth 量化全速运行、首 token 提速 40% 等](#item-tech-lite-4) ⭐️ 7.0/10

---

## 科技与 AI 要闻

<a id="item-tech-lite-1"></a>
### [OpenSSH sshole 漏洞：crypt\(\) 处理 &\#x27;\*&\#x27; 哈希值缺陷](https://sshhole.com/) ⭐️ 8.0/10

OpenSSH 密码认证机制中存在名为 sshole 的关键漏洞，利用 crypt\(\) 函数对 &\#x27;\*&\#x27; 哈希值的处理缺陷。攻击者可在特定配置下使 crypt\(password, &\#x27;\*&\#x27;\) 返回 &\#x27;\*&\#x27;，从而绕过 sshd 的密码验证。该漏洞影响 musl libc 的 SHA 加密实现，musl 此前已在 DES crypt 中修复类似问题，但遗漏了 SHA crypt 路径。Alpine Linux 等使用 musl 的发行版可能受影响。

hackernews · josemrb · 11月5日 12:19 · [社区讨论](https://news.ycombinator.com/item?id=50378228)

**「背景」** 在 Unix 系统中，/etc/shadow 里的密码字段使用 &\#x27;\*&\#x27; 或 &\#x27;\!&\#x27; 表示账户禁用密码登录。crypt\(\) 函数在哈希出错时也可能返回 &\#x27;\*&\#x27;。OpenSSH 的 sshd 通过比较 crypt\(输入密码, 存储哈希\) 与存储哈希来验证密码。当存储哈希为 &\#x27;\*&\#x27; 且 crypt\(\) 因特定盐值返回 &\#x27;\*&\#x27; 时，比较即为真，导致认证绕过。这是典型的带内信号冲突问题。

**「影响」** 使用 musl libc 的系统（如 Alpine Linux）在特定配置下面临 SSH 认证绕过风险。管理员应检查 shadow 文件中是否存在 &\#x27;\*&\#x27; 哈希账户，并关注 musl libc 及 OpenSSH 的补丁发布。该漏洞提示密码处理中不应使用特殊字符作为带内信号。

**「社区讨论」** Hacker News 讨论中，mpyne 详细解释了攻击原理：攻击者需使 crypt\(pw, &\#x27;\*&\#x27;\) == &\#x27;\*&\#x27; 成立。BoppreH 指出这是带内信号设计缺陷，&\#x27;\*&\#x27; 不应同时用作“禁用密码”和“哈希错误”标记。amluto 发现 musl 在 DES crypt 中已有变通修复，但 SHA crypt 遗漏。nxobject 批评 musl 开发者在核心加密函数中为便利性修改却缺乏审计。scandinavian 尝试在 Alpine Docker 中复现但未成功，默认 shadow 使用 &\#x27;\!&\#x27; 而非 &\#x27;\*&\#x27;。

**标签**: `#security`, `#openssh`, `#vulnerability`, `#authentication`, `#cryptography`, `#musl-libc`

---

<a id="item-tech-lite-2"></a>
### [Hugging Face 发布 Phonon TTS：设立新基准的设备端语音合成模型](https://huggingface.co/blog/phonon-tts) ⭐️ 8.0/10

Hugging Face 博客介绍了 Phonon TTS，这是一种新的设备端文本转语音模型，据称在质量和效率基准测试中达到了最先进水平。该模型专为边缘部署设计，支持隐私保护的语音合成。目前仅有标题和简要分析可用，详细技术规格、模型大小、支持语言、基准测试对比数据及可用性信息未在提供的材料中给出。

rss · Hugging Face Blog · 11月5日 00:00

**「背景」** 设备端 TTS 旨在无需云端连接即可在本地生成语音，保护用户隐私并降低延迟。Hugging Face 此前已托管多种开源 TTS 模型（如 Coqui TTS、Bark、VITS 等），Phonon TTS 是其博客新近推介的、主打高质量与高效率平衡的最新成果。

**标签**: `#text-to-speech`, `#on-device AI`, `#speech synthesis`, `#Hugging Face`, `#benchmark`

---

<a id="item-tech-lite-3"></a>
### [PHP 修复两个已遭利用的严重 RCE 漏洞](https://www.infoq.cn/article/qUEjcWbwOj5RO59250Lu?utm_source=rss&amp;utm_medium=article) ⭐️ 8.0/10

PHP 官方发布安全更新，修复了两个正在野外被积极利用的严重远程代码执行（RCE）漏洞。此次更新涉及的具体 CVE 编号、受影响版本范围及补丁版本号在源标题中未给出，建议管理员尽快查阅官方公告并升级。

rss · InfoQ 中文 · 11月5日 17:06

**「背景」** PHP 为全球大量 Web 应用提供运行时支持，远程代码执行漏洞允许攻击者在未授权情况下在服务器上执行任意代码，风险极高。此类漏洞一旦被公开利用，未修补系统极易遭受自动化攻击。

**「影响」** 所有运行受影响 PHP 版本的 Web 服务器均面临被远程接管的风险，运维人员应立即评估版本、应用补丁或实施缓解措施（如禁用危险函数、部署 WAF 规则），并排查是否已遭入侵。

**标签**: `#PHP`, `#security`, `#vulnerability`, `#remote-code-execution`, `#patch`

---

<a id="item-tech-lite-4"></a>
### [Delta Inference Engine v0.93 发布：支持 64 GB 内存、Unsloth 量化全速运行、首 token 提速 40% 等](https://www.reddit.com/r/LocalLLaMA/comments/1xoq4vq/deepseekv41flash1017_on_one_rtx_3090_big_updates/) ⭐️ 7.0/10

Delta Inference Engine v0.93 发布，在单张 RTX 3090 24 GB 上运行 DeepSeek-V4.1-Flash-1017。新版本将最低内存要求从 192 GB 降至 64 GB，Unsloth IQ2\_XXS 量化在 192 GB 内存下仍保持 41 tok/s，且质量更接近完整模型（99 题基准测试 57 分 vs 旧版 52 分，完整模型 59 分）。首 token 延迟缩短约 40%（180 token 提示词从 3.8 秒降至 2.3 秒），新增 EXL3 支持（2.5 bpw，GPU 内核约 2 倍加速）、基础多 GPU 支持（3060+3090 组合提升 7%）、公开 CI（GitHub Actions 构建发布包）及多项修复。基准数据显示：64 GB 内存下 UD-IQ2\_XXS 21.0 tok/s，96 GB 下 29.3 tok/s，128 GB 下 34.0 tok/s，192 GB 下 41.0 tok/s。要求 Windows 10/11、NVIDIA RTX 12 GB+ 显存、64 GB+ 系统内存、NVMe SSD、x86-64 CPU。MIT 许可，仓库：github.com/musicurgy/delta-inference-engine。

reddit · r/LocalLLaMA · /u/musicurgy · 11月5日 18:23

**「背景」** Delta Inference Engine 是 Xolotl 推理引擎的 Windows 移植版，基于 Strata 构建，专为消费级硬件上的大模型离线推理设计。早期版本需要 192 GB 系统内存才能以可用速度运行 DeepSeek 等大模型，限制了普通用户部署。Unsloth 近期发布了基于 Engram 表的低比特量化格式（UD-IQ1\_S、UD-IQ2\_XXS 等），但此前引擎未原生支持，导致速度受损。

**「影响」** 拥有 64–128 GB 内存和单张 RTX 3090/4090 的用户现在可在本地以 21–34 tok/s 运行 DeepSeek-V4.1-Flash 级别模型，且质量接近完整模型；首 token 延迟大幅降低改善交互体验；Unsloth 量化原生支持避免了转换损耗；公开 CI 使构建过程可复现。但 AMD GPU 暂不支持，多 GPU 扩展性有限（3 张以上建议用 Project Maya），且仅在作者单台机器上测试，其他硬件表现待验证。

**标签**: `#local-llm`, `#inference-engine`, `#quantization`, `#delta-engine`, `#benchmarking`

---