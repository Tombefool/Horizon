---
layout: default
title: "Horizon Summary: 2026-11-15 (EN)"
date: 2026-11-15
lang: en
---

> From 16 items, 6 important content pieces were selected

---

**Tech &amp; AI News**
1. [SpaceX Catches Starship Upper Stage in Flight 15 Tower Recovery](#item-tech-lite-1) ⭐️ 9.0/10
2. [CMP 170HX voltage glitch unlocks 80GB VRAM and 126 SMs](#item-tech-lite-2) ⭐️ 8.0/10
3. [AI-Generated Code Should Be Open Source, Blog Argues](#item-tech-lite-3) ⭐️ 7.0/10
4. [MacBook Pro Tandem OLED PWM Dimming Causes Eye Strain for Sensitive Users](#item-tech-lite-4) ⭐️ 7.0/10
5. [Court allows DRAM price-fixing suit against Samsung, SK Hynix, Micron to proceed](#item-tech-lite-5) ⭐️ 7.0/10
6. [Basalt 0.4.0 Adds Qwen 3.8 27B Dense Model at 776 tok/s on RTX 5090](#item-tech-lite-6) ⭐️ 7.0/10

---

## Tech &amp; AI News

<a id="item-tech-lite-1"></a>
### [SpaceX Catches Starship Upper Stage in Flight 15 Tower Recovery](https://www.spacex.com/launches/starship-flight-15) ⭐️ 9.0/10

SpaceX successfully caught the Starship upper stage using the launch tower&\#x27;s &quot;chopstick&quot; arms during Flight 15 on November 14, 2026, marking the first recovery of both rocket stages in a single mission since the Space Shuttle program. The catch demonstrated full reusability of the Super Heavy booster and Starship ship, with the upper stage returning to the launch site for tower capture rather than ocean splashdown. SpaceX confirmed the milestone via X post and livestream footage showing the vehicle secured by the mechanical arms.

hackernews · ls612 · Nov 14, 21:22 · [Discussion](https://news.ycombinator.com/item?id=50500963)

**「Background」** Previous Starship flights had recovered the Super Heavy booster via tower catch but relied on ocean splashdown for the upper stage, while the Space Shuttle achieved partial reusability with extensive refurbishment between flights. Flight 15 represented the first attempt to return the Starship upper stage directly to the launch tower for capture.

**「Impact」** If the heat shield and vehicle structure withstand the catch with minimal refurbishment, SpaceX can progress toward rapid reuse of both stages, potentially reducing marginal launch costs and increasing flight cadence beyond Falcon 9&\#x27;s current capabilities.

**「Community Discussion」** Commenters emphasized the economic significance of achieving upper-stage reusability without Shuttle-level refurbishment costs, while noting uncertainty about final payload mass fraction to orbit and the remaining milestone of re-flying a caught vehicle.

**Tags**: `#spaceflight`, `#aerospace`, `#reusable-rockets`, `#spacex`, `#starship`

---

<a id="item-tech-lite-2"></a>
### [CMP 170HX voltage glitch unlocks 80GB VRAM and 126 SMs](https://www.reddit.com/r/LocalLLaMA/comments/1xwxzgj/i_finally_succeed_the_cmp_170hx_voltage_glitch/) ⭐️ 8.0/10

Reddit user /u/Yarukiless-cat successfully voltage-glitched an NVIDIA CMP 170HX mining card using a Raspberry Pi Pico to gain restricted firmware write-access, unlocking 80GB of VRAM and 126 streaming multiprocessors \(SMs\) after approximately 15 hours of work. The method, which surfaced five days prior, effectively converts the restricted mining ASIC into hardware with near-A100 80GB-class performance for local LLM inference. The user plans to apply the same process to a second CMP 170HX card.

reddit · r/LocalLLaMA · /u/Yarukiless-cat · Nov 15, 15:16

**「Background」** The CMP 170HX is a cryptocurrency mining-specific GPU based on the GA100 die \(same as the A100\) but with firmware locks limiting VRAM and active SMs. Voltage glitching is a hardware fault-injection technique that briefly disrupts power to bypass secure boot or write-protection mechanisms, allowing modified firmware to be flashed. Prior to this, the 170HX was restricted to 8GB or 16GB VRAM configurations and fewer active SMs, making it unsuitable for large-model inference.

**「Impact」** This hack enables hobbyists and researchers to obtain 80GB VRAM GPUs at a fraction of the cost of genuine A100 80GB cards, dramatically lowering the barrier for running large language models locally. However, the process requires hardware modification skills, a Pico programmer, and carries a risk of permanently bricking the card.

**Tags**: `#hardware-hacking`, `#local-llm`, `#gpu-modding`, `#nvidia-cmp`, `#voltage-glitching`

---

<a id="item-tech-lite-3"></a>
### [AI-Generated Code Should Be Open Source, Blog Argues](https://jakub.jankiewicz.org/blog/ai-code-open-source/) ⭐️ 7.0/10

A blog post arguing that all AI-generated code should be open source sparked a significant Hacker News discussion with 621 points and 340 comments. The debate centers on copyright ownership, licensing obligations, and ethics of code produced by large language models trained on open-source repositories. Commenters referenced US Copyright Office guidance stating AI-assisted output can be copyrighted, while noting that purely AI-generated output may not qualify. Real-world AGPL violations were cited where companies allegedly used LLMs to clone proprietary open-source systems.

hackernews · jcubic · Nov 15, 14:46 · [Discussion](https://news.ycombinator.com/item?id=50507303)

**「Background」** Large language models are trained on vast corpora of publicly available code, much of it under open-source licenses like AGPL that require derivative works to share source code. The US Copyright Office has issued guidance that AI-assisted works can receive copyright protection if human creativity is involved, but purely AI-generated output may not be copyrightable. Legal cases such as Doe v. GitHub and Thaler v. Perlmutter have begun addressing whether LLM output inherits training-data licenses or constitutes infringement.

**「Impact」** Developers and organizations using AI coding tools face legal uncertainty about whether generated code inherits copyleft obligations from training data. Companies that ship AI-cloned AGPL systems without providing source code may face enforcement actions. The Copyright Office guidance suggests human involvement in prompting and editing may establish copyright, but the boundary remains untested for typical AI-assisted workflows.

**「Community Discussion」** Commenters reported direct experience with AGPL violations where companies used LLMs to clone proprietary open-source systems after failing to comply with license terms. One author noted the LLM clone was buggy but still clearly derived from their creative design. Others cited US Copyright Office guidance that AI assistance does not negate copyright if human creativity directs the output. A counter-argument questioned whether using any open-source framework or learning from Stack Overflow should similarly force code open. Legal precedents Doe v. GitHub and Thaler v. Perlmutter were referenced as limiting automatic open-source inheritance for LLM output.

**Tags**: `#AI-generated code`, `#open source licensing`, `#copyright law`, `#software ethics`, `#LLM training data`

---

<a id="item-tech-lite-4"></a>
### [MacBook Pro Tandem OLED PWM Dimming Causes Eye Strain for Sensitive Users](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/) ⭐️ 7.0/10

Apple&\#x27;s tandem OLED implementation in recent MacBook Pro models uses pulse-width modulation \(PWM\) dimming that community measurements show operates at up to 960 Hz effective frequency, yet still causes eye strain for flicker-sensitive users. The tandem OLED structure appears to drive two OLED layers at 480 Hz each, 180 degrees out of phase, yielding an effective 960 Hz when both layers are active across most usable brightness levels. Despite this relatively high frequency compared to typical smartphone OLEDs \(often 240–480 Hz\), users with concussion history or high flicker sensitivity report perceiving unstable luminosity and cannot comfortably use the displays.

hackernews · MacAnorak · Nov 15, 13:15 · [Discussion](https://news.ycombinator.com/item?id=50506719)

**「Background」** PWM dimming controls brightness by rapidly switching OLED pixels on and off; lower duty cycles reduce perceived brightness but introduce flicker. Tandem OLED stacks two emissive layers to increase peak brightness and longevity, but the phasing of their PWM signals determines the effective flicker frequency. Previous MacBook Pro models used mini-LED backlighting with different dimming characteristics, making this a regression for users who tolerated earlier displays.

**「Impact」** Flicker-sensitive developers and professionals who rely on MacBook Pro for daily work face an accessibility regression: they cannot upgrade without risking eye strain, headaches, or concussion symptom exacerbation. No software toggle to disable PWM or force DC dimming has been documented, leaving affected users to either stay on older hardware or seek external monitors with verified flicker-free operation.

**「Community Discussion」** Hacker News commenters provided technical nuance: one measurement analysis argued the tandem layers run at 480 Hz each, phased 180° apart, producing an effective 960 Hz during dual-layer operation. Others shared personal thresholds — one user reported sensitivity to PWM at 15 kHz on prior generations, while another noted that concussion history made any screen problematic, not just bright OLEDs. The discussion also broadened to related sensitivities such as LED CRI and LCD motion blur.

**Tags**: `#display-technology`, `#pwm`, `#oled`, `#macbook-pro`, `#hardware-engineering`, `#accessibility`

---

<a id="item-tech-lite-5"></a>
### [Court allows DRAM price-fixing suit against Samsung, SK Hynix, Micron to proceed](https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal) ⭐️ 7.0/10

A federal court denied a motion to dismiss a class-action lawsuit alleging that Samsung, SK Hynix, and Micron conspired to fix DRAM prices. The ruling allows the antitrust case to proceed toward discovery and trial. The three manufacturers collectively control the vast majority of global DRAM production.

hackernews · ybathaee · Nov 15, 01:18 · [Discussion](https://news.ycombinator.com/item?id=50502988)

**「Background」** DRAM price-fixing litigation has a long history, including prior settlements by the same manufacturers in the 2000s and 2010s. The current suit alleges a renewed conspiracy to restrict output and raise prices beginning around 2016.

**「Impact」** If plaintiffs prevail, the manufacturers could face treble damages under U.S. antitrust law, potentially totaling billions of dollars, and may be subject to injunctive relief affecting future pricing behavior.

**「Community discussion」** Commenters debate whether high DRAM prices reflect ongoing collusion or legitimate market dynamics such as technology transitions \(DDR4 to DDR5\) and high barriers to entry. Some users report direct budget pressure from current memory costs for workstation and GPU purchases.

**Tags**: `#DRAM`, `#antitrust`, `#price-fixing`, `#semiconductors`, `#hardware`

---

<a id="item-tech-lite-6"></a>
### [Basalt 0.4.0 Adds Qwen 3.8 27B Dense Model at 776 tok/s on RTX 5090](https://www.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/) ⭐️ 7.0/10

Basalt 0.4.0 introduces dense model support with Qwen 3.8 27B, achieving up to 776 tokens per second on structured output, 262 tok/s on conversation, and 194 tok/s on prose using a single RTX 5090. The quantized model reaches 92.8% top-1 accuracy versus the full BF16 baseline \(0.0262 KLD\). The release also adds multi-model routing \(starting with DeepSeek V4.1 Flash\), video and file support in chats, tool use, thinking mode, and up to 262K context length. Prefill speed reaches 12,000 tok/s at 4k context, decreasing as context grows.

reddit · r/LocalLLaMA · /u/jesdga95 · Nov 15, 17:30

**「Background」** Basalt is a local LLM inference engine developed by /u/jesdga95. The previous update added multi-model and router support with DeepSeek V4.1 Flash running at 90 tok/s \(conversation\) and 246 tok/s \(structured\) on an RTX 5090 plus 5060 Ti. This 0.4.0 release builds on that foundation by implementing dense model kernels in preparation for Qwen 4.

**「Impact」** Developers can now run Qwen 3.8 27B locally on a single RTX 5090 with near-BF16 accuracy at speeds suitable for real-time structured output, long-context chat, and multimodal tasks including video and file analysis, reducing reliance on larger GPU clusters or cloud APIs for this model size.

**Tags**: `#local-llm`, `#inference-optimization`, `#quantization`, `#basalt`, `#qwen`

---