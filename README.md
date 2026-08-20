<!-- Muhammad Hassaan-ul-Mustafa. Profile README.

     All art in assets/ is generated. To change it, edit the spec in
     assets/build.py and run:

     STYLE at the top of that file switches the whole look:
     "signal", "glass", "luxury" or "cyber".

         python assets/build.py

     Never hand-edit an SVG in assets/, the next build overwrites it.
     One placeholder remains: the portfolio link at the top. -->

<img src="assets/hero.svg" width="100%" alt="Muhammad Hassaan-ul-Mustafa. AI engineer, product and backend. Islamabad, Pakistan. I build AI agents and the backends they run on. Arbisoft, FAST-NUCES, open to remote." />

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-coming_soon-c08a3e?style=for-the-badge&logo=vercel&logoColor=white&labelColor=08080a)](#)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-9a958d?style=for-the-badge&labelColor=08080a)](https://linkedin.com/in/muhammad-hassaan25480a322)
[![Email](https://img.shields.io/badge/Email-8d6b3a?style=for-the-badge&logo=gmail&logoColor=white&labelColor=08080a)](mailto:muhammadhassaanulmustafa@gmail.com)

</div>

---

## 00 · Identity

I build **AI agents** and the **backends** they run on. Computer Science at FAST-NUCES, currently at **Arbisoft**.

> **What I care about:** most AI side projects stop at a notebook. Mine go out with the unglamorous parts attached, because that is what a client ends up depending on.

<img src="assets/principles.svg" width="100%" alt="Guardrails first: rate limiting, validation and row level security before features. Degrade, do not die: every external call has a fallback, clone it and it runs with zero keys. Decide before coding: the architectural choice gets made, and written down, first." />

**3rd Place**, National AI Hackathon &nbsp;·&nbsp; production adopter of the Graph Context Framework &nbsp;·&nbsp; Islamabad, Pakistan, open to remote

---

## 01 · Systems

<a id="forge-mentor"></a>

<img src="assets/sys-forge.svg" alt="Forge Mentor. A Claude Code plugin, MIT, v1.28. Pipeline: question, options, you decide, recorded, code runs. 1,216 tests, 100% coverage. Python 3.12, MCP, Claude, Git." />

An AI agent will happily write two thousand lines on top of a decision nobody made. **This one refuses to.**

| | |
|---|---|
| **Decision gate** | Blocks code from moving past an architectural question you have not answered |
| **Recorded rationale** | Every call written to `.claude/forge/`, so the reasoning outlives the sprint |
| **1,216 tests** | At 100% coverage |
| **Three modes** | `pipeline` · `accept-edits` · `auto` |

```bash
/plugin marketplace add Hassaan146/forge-marketplace
```

[![Repository](https://img.shields.io/badge/Star_Forge_Mentor-111113?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hassaan146/forge-mentor)

<br/>

<a id="ai-news-aggregator"></a>

<img src="assets/sys-news.svg" alt="AI News Aggregator. Full stack, deployed, daily at 07:00. Pipeline: scrape, store, rank, summarise, email. 164 sites, 36 channels, five picks a day. React, Vite, FastAPI, PostgreSQL, Groq, Gemini, Stripe." />

The AI feed is a firehose. **This drinks it and hands back five things before breakfast.**

| | |
|---|---|
| **Coverage** | 164 sites and 36 YouTube channels: labs, product blogs, newsletters, policy |
| **Summaries** | Groq writes them, Gemini covers the outages |
| **Delivery** | A personalised top five, emailed every morning |
| **Payments** | Stripe subscriptions, user accounts, review system |

[![Live](https://img.shields.io/badge/Try_it_live-c08a3e?style=for-the-badge&logoColor=white&labelColor=08080a)](https://ai-news-aggregator-weld.vercel.app)
[![Repository](https://img.shields.io/badge/Repository-111113?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hassaan146/ai-news-aggregator)

<br/>

<a id="skyelite-ai"></a>

<img src="assets/sys-skyelite.svg" alt="SkyElite AI. Hackathon build, 3rd nationally, open source. Pipeline: intake, filter, visa, research, scoring, tradeoff, final. Seven graph nodes, zero keys to run it. Next.js 15, TypeScript, Three.js, FastAPI, Pydantic v2, LangGraph, Supabase." />

It rules out where your passport and budget cannot take you, ranks what survives, and **shows its working so you can argue with it.**

| | |
|---|---|
| **3rd Place** | National AI Hackathon |
| **Seven node graph** | `intake → filter → visa → research → scoring → tradeoff → final` |
| **Security first** | CORS allow-listing, rate limits, prompt-injection sanitising, RLS on Supabase |
| **Zero keys to run** | Every external call degrades to a mock, so a fresh clone just works |
| **Recognised** | Listed production adopter of the Graph Context Framework |

[![Repository](https://img.shields.io/badge/Repository-111113?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hassaan146/ai-travel-planner)

<br/>

<a id="bitmadwall"></a>

<img src="assets/sys-bitmadwall.svg" alt="BitMadWall. Product work, shipped, bitmadwall.ai. Pipeline: your phone, relay, relay, recipient. AES-256-GCM, seven mesh hops, no servers in the path, cryptographic identity with no SIM." />

Encrypted messaging and Bitcoin across a mesh of phones, **for the places where the network is gone or cannot be trusted.**

| | |
|---|---|
| **Transport** | Bluetooth LE · Wi-Fi Direct · optional LoRa, reaching 2 to 5 km |
| **Crypto** | AES-256-GCM with Signal style double ratchet |
| **Routing** | Self healing mesh, up to seven hops, store and forward when nobody is in range |
| **Identity** | Cryptographic. No phone number, no SIM |
| **Panic wipe** | On device, for denied environments |

[![Visit](https://img.shields.io/badge/bitmadwall.ai-c08a3e?style=for-the-badge&logoColor=white&labelColor=08080a)](https://www.bitmadwall.ai/)

<br/>

<a id="ai-employee-os"></a>

<img src="assets/sys-employeeos.svg" alt="AI Employee OS. Agent orchestration, in progress. Pipeline: request, decompose, route to agents, validate, trace. Next.js, FastAPI, Pydantic, LangGraph, LangChain, Supabase, Groq." />

An org where **every seat is an agent**, and the whole run is replayable afterwards.

| | |
|---|---|
| **Input** | One messy request, in plain English |
| **Decompose** | Broken into a dependency aware workflow |
| **Route** | Each piece handed to the agent that owns it |
| **Trace** | Every step timed, logged and replayable |

[![Repository](https://img.shields.io/badge/Repository-111113?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hassaan146/agentic-ai-workflow)

<details>
<summary><b>Everything else, 11 more builds</b></summary>

<br/>

| Project | What it is | Stack |
|---|---|---|
| [AI Fashion Sales Assistant](https://github.com/Hassaan146/ai-fashion-sales-assistant) | Answers Instagram and WhatsApp DMs for clothing brands. 11 intent types, catalog ranking, order state machine, 164 tests | React · Node · MongoDB · LangChain |
| [PayTrace](https://github.com/Hassaan146/PayTrace) | Desktop reconciliation. Matches invoices to bank records in four passes, BCrypt audit trails | Java · JavaFX · SQL Server |
| [Preflight](https://github.com/Hassaan146/preflight) | Audits AI-generated projects against a 31 area production standard, then fixes and verifies | LangGraph · Groq |
| [Agentika](https://github.com/Hassaan146/agentika) | Research agent with a hand written ReAct loop, web search and file analysis | FastAPI · Groq |
| [Forge Marketplace](https://github.com/Hassaan146/forge-marketplace) | Install source for the Forge Mentor plugin | Claude Code |
| [AI Client Finder](https://github.com/Hassaan146/ai-client-finder) | Sources and qualifies leads | Python |
| [B2B SaaS](https://github.com/Hassaan146/B2B-SaaS-) | Team collaboration platform with orgs, tasks and subscriptions | FastAPI · Clerk |
| [CityMind Urban AI](https://github.com/Hassaan146/Citymind_Urban_Ai) | Urban data intelligence prototype | Python |
| [Consumer Price Index](https://github.com/Hassaan146/Consumer-Price-Index) | CPI pipeline built on discrete mathematics | Python |
| [ChronoRift OS](https://github.com/Hassaan146/ChronoRiftOS) | Operating systems coursework | C++ |
| [Super Mario COAL](https://github.com/Hassaan146/Super-Mario-COAL) | A game written in x86 assembly | Assembly |

</details>

---

## 02 · Toolchain

<div align="center">

**AI and agents**

![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langgraph&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-000000?style=for-the-badge&logo=modelcontextprotocol&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

**Languages**

[![Languages](https://skillicons.dev/icons?i=python,typescript,javascript,cpp,java,cs&theme=dark&perline=10)](https://skillicons.dev)

**Backend**

[![Backend](https://skillicons.dev/icons?i=fastapi,django,nodejs,express,redis,rabbitmq&theme=dark&perline=10)](https://skillicons.dev)

**Frontend**

[![Frontend](https://skillicons.dev/icons?i=react,nextjs,vite,tailwind,threejs,html,css&theme=dark&perline=10)](https://skillicons.dev)

**Data**

[![Data](https://skillicons.dev/icons?i=postgres,supabase,mongodb,mysql,sqlite&theme=dark&perline=10)](https://skillicons.dev)

**Ship and test**

[![Ship](https://skillicons.dev/icons?i=docker,git,linux,vercel,postman,bash&theme=dark&perline=10)](https://skillicons.dev)

</div>

---

## 03 · Signals

<img src="assets/signals.svg" width="100%" alt="Public repositories, stars earned, languages and last push date, with the language mix and four credentials: 3rd place at the National AI Hackathon, production adopter of the Graph Context Framework, 1,216 tests at 100% coverage on Forge Mentor, and four certifications from Anthropic, Harvard and DeepLearning.AI." />

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-light.svg" />
  <img src="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-light.svg" width="94%" alt="A snake eating my contribution graph" />
</picture>
</div>

---

## 04 · Contact

At **Arbisoft** right now. Open to contract work and startup collaborations, mostly around AI agents and backend systems.

If you are building something and part of it is stuck, that is the email I like getting.

<div align="center">

[![Email](https://img.shields.io/badge/muhammadhassaanulmustafa@gmail.com-8d6b3a?style=for-the-badge&logo=gmail&logoColor=white&labelColor=08080a)](mailto:muhammadhassaanulmustafa@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-9a958d?style=for-the-badge&labelColor=08080a)](https://linkedin.com/in/muhammad-hassaan25480a322)

<img src="assets/signoff.svg" width="100%" alt="" />

</div>

<sub>**Colophon.** Every panel on this page is drawn by [`assets/build.py`](assets/build.py), which reads a spec, measures every label to size its own box so nothing clips, and writes animated SVG. The figures in section 03 come from the GitHub API, and a [scheduled job](.github/workflows/refresh.yml) redraws them each morning; when the API is unreachable it keeps the last correct numbers and says so in the build log. Motion switches itself off for anyone whose system asks for less of it.</sub>
