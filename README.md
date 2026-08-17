<!-- ═══════════════════════════════════════════════════════════════
     Muhammad Hassaan-ul-Mustafa — GitHub profile README
     Repo: github.com/Hassaan146/Hassaan146
     One TODO left: the portfolio URL below, once the site is live.
     Banner art lives in assets/ — edit banner-dark.svg and banner-light.svg together.
     ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg" />
  <img src="assets/banner-light.svg" width="100%" alt="Muhammad Hassaan-ul-Mustafa — AI Forward-Deployed Engineer" />
</picture>

<a href="https://github.com/Hassaan146">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1200&color=58A6FF&center=true&vCenter=true&width=620&lines=I+ship+agent+systems%2C+not+demos.;Currently+building+at+Arbisoft.;Enterprise+AI+shipped+at+Tashi.;LangGraph+pipelines+%E2%86%92+live+URLs.;3rd+Place+%E2%80%94+National+AI+Hackathon." alt="I ship agent systems, not demos" />
</a>

<br/>

<!-- TODO: replace the "#" below with your portfolio URL once the site is live -->
[![Portfolio](https://img.shields.io/badge/Portfolio-coming_soon-0d1117?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0d1117)](#)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&labelColor=0d1117)](https://linkedin.com/in/muhammad-hassaan25480a322)
[![Email](https://img.shields.io/badge/Email-Reach_out-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117)](mailto:muhammadhassaanulmustafa@gmail.com)
[![Profile Views](https://komarev.com/ghpvc/?username=Hassaan146&style=for-the-badge&color=1f6feb&label=PROFILE+VIEWS)](https://github.com/Hassaan146)

</div>

---

## Who I am

I build AI systems that make decisions under real constraints — and then I put them in front of real users.

Most "AI projects" stop at a notebook. Mine ship with rate limiting, input validation, row-level security, graceful degradation when an API key is missing, and a URL you can open. That gap — between a working prototype and something a client can depend on — is the part I care about.

```yaml
name:      Muhammad Hassaan-ul-Mustafa
role:      AI Forward-Deployed Engineer · Product & Backend
studying:  BS Computer Science, FAST-NUCES  (Aug 2024 → May 2028)
based_in:  Islamabad, Pakistan  ·  open to remote
now_at:    Arbisoft
before:    Tashi — enterprise AI (BitMadWall, tashitech.ai)
building:
  - Forge Mentor — a Claude Code plugin, now at v1.28
  - AI Employee OS — an org where every seat is an agent
strongest_at:
  - LangGraph / multi-agent orchestration & context passing
  - FastAPI + Pydantic v2 backends that survive production
  - Turning a vague client problem into a shipped, scoped system
looking_for:  Forward-deployed engineering · AI product roles
```

### How I build

Same shape every time — the guardrails and the fallbacks are the part most people skip.

```mermaid
flowchart LR
    A["Vague client<br/>problem"] --> B["Scope it<br/>decide before coding"]
    B --> C["Agent graph<br/>LangGraph StateGraph"]
    C --> D["Guardrails<br/>Pydantic v2 · rate limits · RLS<br/>prompt-injection sanitizing"]
    D --> E["Degrade gracefully<br/>runs with zero API keys"]
    E --> F["Shipped<br/>Vercel · Railway · Render"]
    F -.->|"what broke, what surprised"| B
```

### Recognition

| | |
|---|---|
| 🥉 | **3rd Place — National AI Hackathon** for [SkyElite&nbsp;AI](https://github.com/Hassaan146/ai-travel-planner) |
| ⭐ | **Recognized production adopter** of **GCF (Graph Context Framework)** — listed on *Who Uses GCF* for cross-agent context passing |
| 📜 | **Agent Skills with Anthropic** — DeepLearning.AI |
| 📜 | **CS50P: Introduction to Programming with Python** — Harvard University |
| 📜 | **AI for Everyone** — Andrew Ng, DeepLearning.AI |

---

## Featured work

### 📡 BitMadWall — *"Communications that do not depend on the network."*
> **[bitmadwall.ai →](https://www.bitmadwall.ai/)** · shipped at [Tashi](https://www.tashitech.ai/)

Sovereign secure mesh communications. Encrypted messaging and Bitcoin transactions relay **device to device** over Bluetooth LE, Wi-Fi Direct, and optional LoRa — no internet, no cell tower, no server anywhere in the path.

| | |
|---|---|
| **Crypto** | AES-256-GCM · Signal-style double-ratchet key derivation |
| **Transport** | Bluetooth LE · Wi-Fi Direct · optional LoRa (2–5 km range) |
| **Routing** | Self-healing mesh, up to 7 hops, store-and-forward for delayed delivery |
| **Identity** | Cryptographic — no phone number, no SIM |
| **Safety** | Panic wipe |

Built for the moments when the network is gone or can't be trusted: continuity of government, disaster response, field teams in denied environments.

<br/>

### 🏢 Tashi — the enterprise AI platform site
> **[tashitech.ai →](https://www.tashitech.ai/)**

Built and shipped the public platform site for [Tashi](https://www.tashitech.ai/), an enterprise AI company running on one thesis: *the future of operations is human + agents.* Agents that orchestrate across ERP and CRM systems, carry governance and approvals inside every action, and anchor each operation on-chain so the audit trail is provable rather than promised.

The site is the front door for all of it — platform architecture, six industry solution tracks (finance, retail, healthcare, security, enterprise, education), customer stories, and the demo funnel.

<br/>

### 🛰️ SkyElite AI — travel decisions, not travel blogs
> 🥉 3rd Place, National AI Hackathon · ⭐ Recognized GCF production adopter
> **[Source →](https://github.com/Hassaan146/ai-travel-planner)**

Give it your passport, budget, and interests. It rules out the destinations you legally or financially *can't* reach, then ranks what's left — and tells you what it traded away to get there.

```
intake → filter → visa → research → scoring → tradeoff → final
└──────────── 7-node LangGraph StateGraph ────────────┘
```

- Scores every candidate across **safety, budget, visa difficulty, and scenery**, returning ranked packages with confidence levels, source counts, and honest tradeoffs — not a confident-sounding guess.
- Security-first backend: CORS allow-listing, rate limiting, Pydantic v2 validation, prompt-injection sanitization, and **RLS-enforced** Supabase persistence.
- GRASP + GoF patterns throughout (Repository, Abstract Factory, Adapter, Strategy, Facade).
- **Runs with zero API keys** — every external dependency degrades to a mock or in-memory fallback, so a new contributor is productive in one clone.

| Layer | Stack |
|---|---|
| Frontend | Next.js 15 · TypeScript · Tailwind CSS · Three.js |
| Backend | FastAPI · Pydantic v2 · LangGraph |
| AI | Anthropic API (Claude Haiku 4.5) · Tavily |
| Data | Supabase (Postgres + RLS) |
| Deploy | Vercel · Railway |

<br/>

### 📰 Asme — AI news, filtered down to five things worth reading
> **[Live demo →](https://ai-news-aggregator-weld.vercel.app)** · **[Source →](https://github.com/Hassaan146/ai-news-aggregator)**

The AI feed is a firehose. Asme drinks it so you don't: it scrapes **164 sites and 36 YouTube channels** — labs, product blogs, newsletters, policy sources — then hands each user a personalized top-5 digest in their inbox every morning.

- Modular services for scraping, ranking, digesting, email, subscriptions, reviews, and admin — each behind its own FastAPI REST surface.
- LLM agents write the summaries, with **Groq primary and Gemini fallback** so a single provider outage doesn't kill the digest.
- Real product plumbing: user auth, Stripe payments, a deployed React dashboard.

`React` `Vite` `Tailwind` `FastAPI` `SQLAlchemy` `PostgreSQL (Neon)` `Groq` `Gemini` `Stripe` `Render` `Vercel`

<br/>

### 🔨 Forge Mentor — a Claude Code plugin that makes you decide before you code
> **[Source →](https://github.com/Hassaan146/forge-mentor)** · MIT · v1.28.0

AI coding agents happily write 2,000 lines on top of a decision nobody made. Forge Mentor stops that: it teaches the load-bearing architectural choice, lays out the options with a recommendation, **waits for your call**, records it in `.claude/forge/`, and blocks code from moving past an undecided question.

- Decisions become part of the codebase — rationale, not just result — so the *why* survives the sprint.
- Three workflow modes: `pipeline`, `accept-edits`, `auto`.
- **1,216 tests at 100% coverage.** Every step announces what it will write before writing it.

```bash
/plugin marketplace add Hassaan146/forge-marketplace
```
```bash
/plugin install forge@forge-marketplace
```

`Python 3.12+` `MCP` `Claude` `Git`

<br/>

### 🛍️ AI Fashion Sales Assistant — the DM that closes the sale
> **[Source →](https://github.com/Hassaan146/ai-fashion-sales-assistant)**

Clothing brands lose orders in unread Instagram DMs. This assistant answers them: it understands what the customer actually wants, recommends from the live catalog, reads their mood, and walks the order to completion — across Instagram, WhatsApp, and web chat.

A **three-phase pipeline** does the work:

| Phase | What happens |
|---|---|
| **1 · NLU** | Extracts **11 intent types** plus entities — colour, size, price band |
| **2 · Recommend + sentiment** | Ranks catalog matches, adds upsells, classifies customer mood |
| **3 · Converse** | State machine collects the order; templates keep replies on-brand |

Rule-based fast path for common messages, LLM path for everything else — so it still works with **no API key at all**. 164 automated tests.

`React` `Vite` `Tailwind` `Node.js` `Express` `MongoDB` `JWT` `LangChain` `Llama 3.3` `OpenAI API`

<br/>

### 💳 PayTrace — reconciliation for startups without a finance team
> **[Source →](https://github.com/Hassaan146/PayTrace)**

A desktop system that matches vendor invoices against bank records automatically, through a **four-stage engine**: Exact → Vendor Reference → Tolerant → Partial-Payment. Role-aware KPIs, email notifications, undo/redo, and BCrypt-secured audit trails, built on a Maven architecture using Strategy, Factory, Command, Observer, DAO, MVC, and Singleton.

`Java` `JavaFX` `SQL Server` `Maven` `SMTP` `BCrypt`

<br/>

### 🧑‍💼 AI Employee OS — an org chart where every seat is an agent
> **[Source →](https://github.com/Hassaan146/agentic-ai-workflow)**

A company staffed entirely by AI. Give it a messy request in plain English; it decomposes that into a **dependency-aware workflow**, routes each piece to the specialist agent that should own it, validates what comes back, and shows you the full execution trace instead of asking you to trust it.

Each role — sales, research, ops, engineering — is an agent with its own scope, tools, and handoffs, coordinating like a team instead of firing off one-shot prompts. Everything the other projects taught me about orchestration, pointed at one question: how much of a company can actually run itself?

`Next.js` `React` `FastAPI` `Pydantic` `LangGraph` `LangChain` `Supabase` `Groq` `Gemini` `Vercel` `Render`

<br/>

<details>
<summary><b>More builds — click to expand</b></summary>

<br/>

| Project | What it is | Stack |
|---|---|---|
| [Forge Marketplace](https://github.com/Hassaan146/forge-marketplace) | Install source for the Forge Mentor plugin | Claude Code plugin registry |
| [Agentika](https://github.com/Hassaan146/agentika) | Agentic workflow experiments | Python |
| [AI Client Finder](https://github.com/Hassaan146/ai-client-finder) | Agent that sources and qualifies leads | Python · LLM APIs |
| [CityMind Urban AI](https://github.com/Hassaan146/Citymind_Urban_Ai) | Urban data intelligence prototype | Python |
| [Consumer Price Index](https://github.com/Hassaan146/Consumer-Price-Index) | CPI pipeline built on discrete-mathematics foundations | Python |
| [ChronoRift OS](https://github.com/Hassaan146/ChronoRiftOS) | Operating-systems coursework — low-level systems | C++ |
| [City Management System](https://github.com/Hassaan146/City-Management-System-DSA) | Graph & data-structure heavy simulation | C++ |
| [Super Mario COAL](https://github.com/Hassaan146/Super-Mario-COAL) | Game written in x86 assembly | Assembly |
| [Ivor Hospital DB](https://github.com/Hassaan146/IvorHospitalDB) | Hospital database system | PHP · SQL |
| [Weight Prediction](https://github.com/Hassaan146/WeightPrediction_mlr_rf) | Multiple linear regression vs. random forest, written up in full | Statistical modelling · TeX |

</details>

---

## Stack

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL%20%2F%20T--SQL-CC2927?style=flat-square&logo=sqlalchemy&logoColor=white)
![Assembly](https://img.shields.io/badge/x86%20Assembly-654FF0?style=flat-square&logo=assemblyscript&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=css&logoColor=white)

**AI & agents**

![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-000000?style=flat-square&logo=modelcontextprotocol&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic%20API-D97757?style=flat-square&logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=flat-square&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-6467F2?style=flat-square&logo=openrouter&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)

**Backend**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST-A30000?style=flat-square&logo=django&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white)

**Frontend**

![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white)

**Data**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)
![Neon](https://img.shields.io/badge/Neon-00E599?style=flat-square&logo=neon&logoColor=black)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

**Ship & test**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux%20%2F%20Bash-FCC624?style=flat-square&logo=linux&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=flat-square&logo=render&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white)
![Pytest](https://img.shields.io/badge/Unit%20%C2%B7%20Integration%20%C2%B7%20E2E-0A9EDC?style=flat-square&logo=pytest&logoColor=white)

---

## Activity

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Hassaan146&theme=github_dark" width="88%" alt="Profile summary" />

<br/>

<img height="185" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Hassaan146&theme=github_dark" alt="Languages by repository" />
<img height="185" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Hassaan146&theme=github_dark" alt="Languages by commit" />

<br/>

<img height="185" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=Hassaan146&theme=github_dark&utcOffset=5" alt="Productive time" />

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=Hassaan146&bg_color=0d1117&color=58a6ff&line=1f6feb&point=ffffff&area=true&hide_border=true" width="98%" alt="Contribution graph" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-light.svg" />
  <img src="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-light.svg" width="98%" alt="A snake eating my contribution graph" />
</picture>

</div>

---

## Working with me

Currently at **Arbisoft**, and always interested in **forward-deployed engineering** and **AI product** work — the seat where you sit with the client, find the real problem, and build the thing that fixes it. Contract work and startup collaborations welcome.

Best first message: what you're building and what's stuck.

<div align="center">

[![Email](https://img.shields.io/badge/muhammadhassaanulmustafa@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117)](mailto:muhammadhassaanulmustafa@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn%20%C2%B7%20Let's%20connect-0A66C2?style=for-the-badge&labelColor=0d1117)](https://linkedin.com/in/muhammad-hassaan25480a322)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&section=footer&height=110&color=0:58a6ff,50:1f6feb,100:0d1117" width="100%" alt="" />

</div>
