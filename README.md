<!-- Muhammad Hassaan-ul-Mustafa. Profile README.
     Art is generated. Edit the spec in assets/build.py and rerun it:
         python assets/build.py
     Never hand-edit an SVG in assets/, the next build overwrites it.
     One placeholder remains: the portfolio link in section 04. -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg" />
  <img src="assets/hero-light.svg" width="100%" alt="Muhammad Hassaan-ul-Mustafa. AI engineer, product and backend. Islamabad, Pakistan. I build AI agents and the backends they run on. Arbisoft, FAST-NUCES, open to remote." />
</picture>

## 00 · Identity

Computer Science at FAST-NUCES, currently at Arbisoft. I build AI agents and the backends they run on.

Most AI side projects stop at a notebook. Mine go out with the unglamorous parts attached, because that is what a client ends up depending on. The work I want is the seat where you sit with the person who has the problem, find what it actually is, then build the thing that fixes it.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/principles-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/principles-light.svg" />
  <img src="assets/principles-light.svg" width="100%" alt="Guardrails first: rate limiting, input validation and row level security land before the features do. Degrade, do not die: every external call has a fallback, clone the repo and it runs with zero API keys. Decide before coding: the architectural choice gets made, and written down, ahead of the first line." />
</picture>

## 01 · Systems

Five things I built. Each one shows you what it produces before it tells you anything about itself.

### Forge Mentor
<sub>Claude Code plugin · MIT · v1.28 · **[Repository](https://github.com/Hassaan146/forge-mentor)**</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sys-forge-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/sys-forge-light.svg" />
  <img src="assets/sys-forge-light.svg" alt="A sample session. The plugin asks how sessions should persist, lists three options with their tradeoffs, recommends one, waits for the answer, records the decision to .claude/forge, then opens the gate. 1,216 tests at 100% coverage, v1.28, MIT licence. Python 3.12, MCP, Claude, Git." />
</picture>

An AI agent will happily write two thousand lines on top of a decision nobody made. This one refuses to, and the reasoning it records outlives the sprint.

```bash
/plugin marketplace add Hassaan146/forge-marketplace
```

### AI News Aggregator
<sub>**[Live](https://ai-news-aggregator-weld.vercel.app)** · **[Repository](https://github.com/Hassaan146/ai-news-aggregator)**</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sys-news-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/sys-news-light.svg" />
  <img src="assets/sys-news-light.svg" alt="A sample digest. Five items kept from 412 collected, each with its kind and source, delivered at 07:00 daily. Groq writes the summaries with Gemini on standby. 164 sites, 36 channels, live. React, Vite, FastAPI, PostgreSQL, Groq, Gemini, Stripe." />
</picture>

The AI feed is a firehose. This drinks it and hands back five things before breakfast.

### SkyElite AI
<sub>3rd Place, National AI Hackathon · **[Repository](https://github.com/Hassaan146/ai-travel-planner)**</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sys-skyelite-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/sys-skyelite-light.svg" />
  <img src="assets/sys-skyelite-light.svg" alt="A sample ranking. Lisbon scores 84 on safety, budget, visa and scenery, with the tradeoff written out and a confidence of 0.78 from six sources, followed by Tbilisi and Medellin. 3rd at a national hackathon, seven graph nodes, zero keys needed to run it. Next.js 15, TypeScript, Three.js, FastAPI, Pydantic v2, LangGraph, Supabase." />
</picture>

It rules out where your passport and budget cannot take you, ranks what survives, and shows its working so you can argue with it.

### BitMadWall
<sub>**[bitmadwall.ai](https://www.bitmadwall.ai/)**</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sys-bitmadwall-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/sys-bitmadwall-light.svg" />
  <img src="assets/sys-bitmadwall-light.svg" alt="A sample relay. A message hops from your phone through two relays to the recipient over Bluetooth LE, Wi-Fi Direct then LoRa, delivered in three hops with no servers, while a second message sits queued for 42 minutes waiting for a peer. AES-256-GCM, seven hops, cryptographic identity with no SIM." />
</picture>

For the places where the network is gone or cannot be trusted: continuity of government, disaster response, field teams.

### AI Employee OS
<sub>**[Repository](https://github.com/Hassaan146/agentic-ai-workflow)**</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sys-employeeos-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/sys-employeeos-light.svg" />
  <img src="assets/sys-employeeos-light.svg" alt="A sample run. One plain English request becomes three agents working in dependency order, research then ops then writer, with every step timed, logged and replayable from the trace. Next.js, FastAPI, Pydantic, LangGraph, LangChain, Supabase, Groq." />
</picture>

An org where every seat is an agent, and the whole run is replayable afterwards.

<details>
<summary><sub><b>Everything else, 11 more builds</b></sub></summary>

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

## 02 · Toolchain

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/toolchain-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/toolchain-light.svg" />
  <img src="assets/toolchain-light.svg" width="100%" alt="Toolchain. Languages: Python, TypeScript, JavaScript, C++, Java, SQL, x86. AI: LangGraph, LangChain, MCP, Anthropic, Groq, Gemini, Pydantic. Backend: FastAPI, Django, DRF, Node, Express, Celery. Frontend: React, Next.js, Vite, Tailwind, Three.js. Data: PostgreSQL, Supabase, MongoDB, Redis, MySQL, SQL Server. Ship: Docker, Git, Linux, Vercel, Render, Railway, Stripe." />
</picture>

## 03 · Signals

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/signals-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/signals-light.svg" />
  <img src="assets/signals-light.svg" width="100%" alt="Public repositories, stars earned, languages and last push date, with the language mix and four credentials: 3rd place at the National AI Hackathon, production adopter of the Graph Context Framework, 1,216 tests at 100% coverage on Forge Mentor, and four certifications from Anthropic, Harvard and DeepLearning.AI." />
</picture>

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-light.svg" />
  <img src="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-light.svg" width="94%" alt="A snake eating my contribution graph" />
</picture>
</div>

## 04 · Contact

At Arbisoft right now. Open to contract work and startup collaborations, mostly around AI agents and backend systems.

If you are building something and part of it is stuck, that is the email I like getting.

|  |  |
|---|---|
| **Email** | [muhammadhassaanulmustafa@gmail.com](mailto:muhammadhassaanulmustafa@gmail.com) |
| **LinkedIn** | [muhammad-hassaan](https://linkedin.com/in/muhammad-hassaan25480a322) |
| **Portfolio** | coming soon <!-- drop the URL here when the site is live --> |

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/signoff-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/signoff-light.svg" />
  <img src="assets/signoff-light.svg" width="100%" alt="" />
</picture>

<sub>**Colophon.** Every mark on this page is drawn by [`assets/build.py`](assets/build.py), which reads a spec, measures each label to size its own box so nothing ever clips, and writes animated SVG. The figures in section 03 come from the GitHub API and a [scheduled job](.github/workflows/refresh.yml) redraws them each morning; if the API cannot be reached it keeps the last correct numbers. No image here queries GitHub when you load the page, which is what turns a stat widget into an error box on a bad day. There are no badge services: the toolchain block replaced 42 separate requests to shields.io. Motion switches itself off for anyone whose system asks for less of it.</sub>
