---
layout: default
title: "Horizon Summary: 2026-11-08 (EN)"
date: 2026-11-08
lang: en
---

> From 15 items, 3 important content pieces were selected

---

**Tech &amp; AI News**
1. [Llama-modchip runs 284B DeepSeek on 64GB RAM via weight streaming](#item-tech-lite-1) ⭐️ 7.0/10
2. [Claude Code &quot;Don&\#x27;t Ask Again&quot; leaks secrets in 1,122 GitHub files](#item-tech-lite-2) ⭐️ 7.0/10
3. [Open-source tool maps LLM responses to censorship questions by country](#item-tech-lite-3) ⭐️ 7.0/10

---

## Tech &amp; AI News

<a id="item-tech-lite-1"></a>
### [Llama-modchip runs 284B DeepSeek on 64GB RAM via weight streaming](https://github.com/synchopate/llama-modchip) ⭐️ 7.0/10

Llama-modchip demonstrates running a 284-billion-parameter DeepSeek model on 64 GB of system RAM without a GPU by streaming weights from disk and applying approximately 2-bit quantization. The technique trades model quality for memory efficiency, fitting the full model within consumer-grade memory capacity. The project is hosted on GitHub by synchopate and was shared on Hacker News on 2026-11-08.

hackernews · joshcsimmons · Nov 8, 10:22 · [Discussion](https://news.ycombinator.com/item?id=50411961)

**「Background」** Weight streaming loads model parameters from storage into memory only as needed during inference, avoiding the requirement to hold all weights in RAM simultaneously. Aggressive quantization below 4-bit is known to degrade model quality non-linearly, with 4-bit widely considered the practical sweet spot for size-to-performance ratio. The llama.cpp ecosystem has multiple forks exploring streaming and custom quantization schemes, but upstream integration has been slow due to a large pull-request backlog.

**「Impact」** Developers with 64 GB RAM but no GPU can now run a 284B model locally, albeit at reduced quality from ~2-bit quantization. Users requiring higher fidelity should expect significant quality loss compared to 4-bit or 8-bit quantizations, and should verify output suitability for their specific tasks before relying on this configuration.

**「Community discussion」** Commenters emphasize that the quantization level \(likely 2-bit\) is the critical missing detail, noting empirical evidence that quality drops sharply below 4-bit. Several users reference other llama.cpp forks \(Bonsai, Strata, Pulsar\) implementing similar weight-streaming features, and express frustration with the slow upstream PR review process in llama.cpp.

**Tags**: `#llm-inference`, `#quantization`, `#weight-streaming`, `#local-ai`, `#systems-engineering`

---

<a id="item-tech-lite-2"></a>
### [Claude Code &quot;Don&\#x27;t Ask Again&quot; leaks secrets in 1,122 GitHub files](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) ⭐️ 7.0/10

Security researchers at Apiiro found 1,122 public GitHub files containing secrets exposed through Claude Code&\#x27;s &quot;Don&\#x27;t Ask Again&quot; feature. When users approve commands containing credentials via this feature, the full command string—including API keys and passwords—is stored in .claude/settings.local.json. If that local settings file is accidentally committed to a repository \(contrary to documentation and automatic gitignore behavior\), the secrets become publicly visible. The exposure requires both approving a secret-containing command and manually committing the local settings file.

hackernews · shmulc · Nov 7, 20:45 · [Discussion](https://news.ycombinator.com/item?id=50407882)

**「Background」** Claude Code&\#x27;s &quot;Don&\#x27;t Ask Again&quot; feature lets users permanently approve specific commands so the agent stops prompting for permission. Approved commands are written to a local settings file that the tool automatically adds to .gitignore when created, but users can override this by manually creating or committing the file.

**「Impact」** Developers using Claude Code should audit repositories for committed .claude/settings.local.json files and rotate any exposed credentials; the fix is to store secrets only in environment variables and enforce a global gitignore rule for the .claude directory.

**「Community Discussion」** Commenters emphasize the root cause is storing full command strings with secrets rather than the feature itself, and recommend using environment variables for secrets plus a machine-wide gitignore for .claude/; a Claude Code team member confirmed the file is auto-gitignored and exposures resulted from manual commits.

**Tags**: `#security`, `#ai-coding-assistants`, `#secrets-management`, `#claude-code`, `#github`

---

<a id="item-tech-lite-3"></a>
### [Open-source tool maps LLM responses to censorship questions by country](https://www.reddit.com/r/LocalLLaMA/comments/1xr09nq/does_censorship_exist_in_country_according_to/) ⭐️ 7.0/10

Developer p-e-w released an open-source tool that systematically queries language models with a yes/no question about censorship in every country and generates SVG world map visualizations of the responses. The program, hosted at github.com/p-e-w/llm-beliefs, automates the process of probing LLM beliefs across geopolitical entities and renders the results as color-coded maps. The author reports being surprised by the model outputs, though specific model names, question phrasing, and result patterns are not detailed in the announcement.

reddit · r/LocalLLaMA · /u/-p-e-w- · Nov 8, 14:56

**「Background」** Evaluating LLM bias and alignment often involves probing model responses to sensitive or politically charged prompts across different contexts. Prior work has used targeted prompts to measure refusal rates, sycophancy, or geographic bias, but automated, country-level visualization of a single repeated question is a less common evaluation format.

**「Impact」** Researchers and developers can reuse the codebase to compare how different models or prompt variations answer the same censorship question across all recognized countries, enabling systematic benchmarking of geopolitical sensitivity and alignment behavior.

**Tags**: `#LLM evaluation`, `#AI bias`, `#censorship detection`, `#open source tools`, `#AI alignment`

---