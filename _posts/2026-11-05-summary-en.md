---
layout: default
title: "Horizon Summary: 2026-11-05 (EN)"
date: 2026-11-05
lang: en
---

> From 23 items, 4 important content pieces were selected

---

**Tech &amp; AI News**
1. [OpenSSH &\#x27;sshole&\#x27; Vulnerability: crypt\(\) &\#x27;\*&\#x27; Hash Bypass in musl libc](#item-tech-lite-1) ⭐️ 8.0/10
2. [Phonon TTS: On-Device Speech Tops Benchmarks](#item-tech-lite-2) ⭐️ 8.0/10
3. [PHP Patches Two Actively Exploited Critical RCE Vulnerabilities](#item-tech-lite-3) ⭐️ 8.0/10
4. [Delta Inference Engine v0.93 adds 64GB RAM support, Unsloth quants, faster first token](#item-tech-lite-4) ⭐️ 7.0/10

---

## Tech &amp; AI News

<a id="item-tech-lite-1"></a>
### [OpenSSH &\#x27;sshole&\#x27; Vulnerability: crypt\(\) &\#x27;\*&\#x27; Hash Bypass in musl libc](https://sshhole.com/) ⭐️ 8.0/10

A critical OpenSSH authentication vulnerability dubbed &\#x27;sshole&\#x27; allows authentication bypass by exploiting how crypt\(\) handles &\#x27;\*&\#x27; hash values in musl libc&\#x27;s SHA crypt implementation. When a user account has &\#x27;\*&\#x27; in /etc/shadow \(indicating password login disabled\), an attacker can supply a crafted password that causes crypt\(password, &quot;\*&quot;\) to return &quot;\*&quot;, making the comparison crypt\(pw, hash\) == hash evaluate to true. The flaw exists because musl implemented a workaround for this edge case in its DES crypt code but omitted it from the SHA-256/512 crypt implementation. The vulnerability affects systems using musl libc \(such as Alpine Linux\) with OpenSSH password authentication enabled for accounts with &\#x27;\*&\#x27; or &\#x27;\!&\#x27; password hashes.

hackernews · josemrb · Nov 5, 12:19 · [Discussion](https://news.ycombinator.com/item?id=50378228)

**「Background」** OpenSSH&\#x27;s sshd validates passwords by calling crypt\(provided\_password, stored\_hash\) and comparing the result to the stored hash. In /etc/shadow, special values like &\#x27;\*&\#x27; and &\#x27;\!&\#x27; conventionally indicate accounts that cannot log in via password. The crypt\(\) function historically uses in-band signaling — returning the salt/hash value itself to indicate errors — which creates ambiguity when the stored hash is itself a special sentinel value. musl libc previously addressed this for DES-based crypt but not for SHA-based crypt.

**「Impact」** Systems using musl libc \(notably Alpine Linux containers and embedded devices\) with OpenSSH password authentication are vulnerable to authentication bypass for any account whose shadow entry contains &\#x27;\*&\#x27; or &\#x27;\!&\#x27;. Administrators should disable password authentication \(PasswordAuthentication no\) or upgrade musl once patched; the workaround of ensuring no accounts have &\#x27;\*&\#x27; or &\#x27;\!&\#x27; hashes is impractical since these are standard defaults for locked accounts.

**「Community Discussion」** Commenters note the root cause is in-band signaling — using &\#x27;\*&\#x27; and &\#x27;\!&\#x27; as both sentinel values and valid crypt\(\) outputs — a design pattern that creates recurring security issues. One user reports failing to reproduce the exploit on Alpine Docker with &\#x27;\!&\#x27; hashes and long passwords, suggesting the vulnerable code path may have specific trigger conditions. Others criticize musl developers for adding &\#x27;convenience&\#x27; changes to core crypto functions without sufficient auditing.

**Tags**: `#security`, `#openssh`, `#vulnerability`, `#authentication`, `#cryptography`, `#musl-libc`

---

<a id="item-tech-lite-2"></a>
### [Phonon TTS: On-Device Speech Tops Benchmarks](https://huggingface.co/blog/phonon-tts) ⭐️ 8.0/10

Hugging Face has released Phonon TTS, a new on-device text-to-speech model that achieves state-of-the-art benchmark results for quality and efficiency. The system enables high-fidelity speech synthesis directly on edge devices without requiring cloud connectivity. This advance targets developers building privacy-preserving voice applications that must operate offline or with limited compute resources.

rss · Hugging Face Blog · Nov 5, 00:00

**「Background」** On-device text-to-speech has historically traded quality for model size and inference speed, forcing many applications to rely on cloud APIs. Recent progress in model compression and efficient architectures has narrowed this gap, making local synthesis viable for more use cases. Phonon TTS builds on this trajectory by optimizing both acoustic modeling and vocoder components for edge deployment.

**「Impact」** Developers can now integrate benchmark-leading TTS into mobile apps, embedded systems, and privacy-sensitive products without network dependencies or per-request cloud costs. The model&\#x27;s efficiency profile also reduces battery drain and latency compared to streaming alternatives.

**Tags**: `#text-to-speech`, `#on-device AI`, `#speech synthesis`, `#Hugging Face`, `#benchmark`

---

<a id="item-tech-lite-3"></a>
### [PHP Patches Two Actively Exploited Critical RCE Vulnerabilities](https://www.infoq.cn/article/qUEjcWbwOj5RO59250Lu?utm_source=rss&amp;utm_medium=article) ⭐️ 8.0/10

PHP has released security patches for two critical remote code execution vulnerabilities that are already being exploited in the wild. The advisory urges all PHP users to update immediately, though specific CVE identifiers, affected version ranges, and fixed versions are not detailed in the available summary.

rss · InfoQ 中文 · Nov 5, 17:06

**「Background」** PHP is a widely deployed server-side scripting language powering a large portion of websites and web applications. Remote code execution vulnerabilities in the PHP interpreter or its core extensions allow attackers to run arbitrary commands on the server, often leading to full system compromise.

**「Impact」** All organizations running PHP in production environments should treat this as an emergency update and apply the latest security releases as soon as possible to prevent active exploitation.

**Tags**: `#PHP`, `#security`, `#vulnerability`, `#remote-code-execution`, `#patch`

---

<a id="item-tech-lite-4"></a>
### [Delta Inference Engine v0.93 adds 64GB RAM support, Unsloth quants, faster first token](https://www.reddit.com/r/LocalLLaMA/comments/1xoq4vq/deepseekv41flash1017_on_one_rtx_3090_big_updates/) ⭐️ 7.0/10

Delta Inference Engine v0.93 now runs DeepSeek-V4.1-Flash-1017 on a single RTX 3090 with system RAM as low as 64 GB, adding native support for Unsloth quantization formats at full speed. Benchmarks on a 24 GB RTX 3090 with an i5-13600K show 21–41 tok/s across UD-IQ2\_XXS, UD-IQ1\_S, UD-Q2\_K\_XL, and UD-IQ3\_XXS quantizations at 64–192 GB RAM. First-token latency improved ~40% \(180-token prompt from 3.8 s to 2.3 s\), EXL3 \(2.5 bpw\) kernels are ~2× faster, and basic dual-GPU \(RTX 3060 + 3090\) yields a 7% uplift. The release includes public CI via GitHub Actions, a web UI setup tab for model selection, and fixes for long contexts,  handling, and OOM on large files. Requirements: Windows 10/11, NVIDIA RTX 12 GB+ VRAM \(24 GB recommended\), 64 GB+ system RAM, fast NVMe, x86-64 with AVX2. MIT licensed at github.com/musicurgy/delta-inference-engine.

reddit · r/LocalLLaMA · /u/musicurgy · Nov 5, 18:23

**「Background」** Delta Inference Engine is a Windows port of the Xolotl inference stack built on Strata, designed to offload model layers to system RAM and NVMe when VRAM is insufficient. The previous release \(ds4 Q2\) required 192 GB RAM for 41 tok/s on an RTX 3090; this update extends viability to 64 GB configurations and integrates Unsloth&\#x27;s Engram-table quantization format.

**「Impact」** Users with 64–128 GB RAM can now run a 300+ GB model at 15–34 tok/s on a single RTX 3090, making high-quality local inference accessible without 192 GB RAM. UD-IQ2\_XXS at 192 GB matches the prior 41 tok/s while scoring 57/99 on a 99-question benchmark \(vs. 52 for ds4 Q2, 59 for the full API\), and agreement with DeepSeek&\#x27;s API next-token predictions reaches 91–96% depending on task type.

**Tags**: `#local-llm`, `#inference-engine`, `#quantization`, `#delta-engine`, `#benchmarking`

---