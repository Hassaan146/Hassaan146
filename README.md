<!-- Muhammad Hassaan-ul-Mustafa. Profile README.
     Banner art is in assets/. Edit banner-dark.svg and banner-light.svg together.
     One placeholder left: the portfolio link below. -->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg" />
  <img src="assets/banner-light.svg" width="100%" alt="Muhammad Hassaan-ul-Mustafa, AI Forward-Deployed Engineer" />
</picture>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=19&pause=1400&color=58A6FF&center=true&vCenter=true&width=560&lines=Building+AI+agents+that+reach+production.;Currently+at+Arbisoft.;3rd+Place%2C+National+AI+Hackathon.;CS+at+FAST-NUCES%2C+Islamabad." alt="Building AI agents that reach production" />

<br/>

<!-- Replace the "#" with your portfolio URL once the site is live -->
[![Portfolio](https://img.shields.io/badge/Portfolio-coming_soon-0d1117?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0d1117)](#)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&labelColor=0d1117)](https://linkedin.com/in/muhammad-hassaan25480a322)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117)](mailto:muhammadhassaanulmustafa@gmail.com)

</div>

---

## About

```yaml
name:   Muhammad Hassaan-ul-Mustafa
role:   AI engineer, product and backend
study:  BS Computer Science, FAST-NUCES (2024 to 2028)
now:    Arbisoft
based:  Islamabad, Pakistan. Open to remote.
```

I build AI agents and the backends they run on. Most of my projects ship with rate limiting, input validation, row-level security, and a fallback for every external call, because that is the part clients end up depending on.

Strongest with LangGraph orchestration, FastAPI, and Pydantic v2.

**Recognition**

- 🥉 3rd Place, National AI Hackathon, for [SkyElite AI](https://github.com/Hassaan146/ai-travel-planner)
- ⭐ Listed as a production adopter of GCF (Graph Context Framework) for cross-agent context passing
- 📜 Agent Skills with Anthropic (DeepLearning.AI) · CS50P (Harvard) · AI for Everyone (DeepLearning.AI)

---

## Featured work

### 📡 BitMadWall
[bitmadwall.ai](https://www.bitmadwall.ai/)

Encrypted messaging and Bitcoin transactions across a mesh of phones, with no internet, no cell service and no server involved. Traffic hops device to device over Bluetooth LE, Wi-Fi Direct and optional LoRa, up to seven hops, with store-and-forward for anything that cannot be delivered yet. Identity is cryptographic, so no phone number or SIM.

`AES-256-GCM` `double ratchet` `Bluetooth LE` `Wi-Fi Direct` `LoRa` `Bitcoin`

### 🛰️ SkyElite AI
[Repo](https://github.com/Hassaan146/ai-travel-planner) · 🥉 3rd Place, National AI Hackathon

Takes your passport, budget and interests, drops the destinations you cannot actually reach, then ranks what is left and writes out what it traded away. Seven-node LangGraph pipeline: intake, filter, visa, research, scoring, tradeoff, final. Runs with zero API keys because every external call degrades to a mock.

`Next.js 15` `TypeScript` `Three.js` `FastAPI` `Pydantic v2` `LangGraph` `Anthropic API` `Supabase`

### 📰 Asme
[Live](https://ai-news-aggregator-weld.vercel.app) · [Repo](https://github.com/Hassaan146/ai-news-aggregator)

Scrapes 164 AI sites and 36 YouTube channels, then emails every user a personalised top-5 digest each morning. Groq writes the summaries and Gemini covers the outages. Stripe handles subscriptions.

`React` `Vite` `FastAPI` `PostgreSQL` `Groq` `Gemini` `Stripe`

### 🔨 Forge Mentor
[Repo](https://github.com/Hassaan146/forge-mentor) · MIT · v1.28

A Claude Code plugin for the decisions people skip. It teaches the architectural choice, lays out options, waits for your call, writes it to `.claude/forge/`, then blocks code from moving past anything still undecided. 1,216 tests at 100% coverage.

```bash
/plugin marketplace add Hassaan146/forge-marketplace
```

`Python 3.12` `MCP` `Claude`

### 🧑‍💼 AI Employee OS
[Repo](https://github.com/Hassaan146/agentic-ai-workflow)

An org where every seat is an agent. Give it a messy request in plain English and it breaks that into a dependency-aware workflow, routes each piece to the agent that owns it, checks the results, and shows you the whole execution trace.

`Next.js` `FastAPI` `Pydantic` `LangGraph` `LangChain` `Supabase` `Groq`

### 🛍️ AI Fashion Sales Assistant
[Repo](https://github.com/Hassaan146/ai-fashion-sales-assistant)

Answers Instagram and WhatsApp DMs for clothing brands. Reads 11 intent types plus colour, size and price, ranks catalog matches, reads the customer's mood, and walks the order to checkout. Drops to keyword matching when there is no API key. 164 tests.

`React` `Node.js` `Express` `MongoDB` `JWT` `LangChain` `Llama 3.3`

### 💳 PayTrace
[Repo](https://github.com/Hassaan146/PayTrace)

Desktop reconciliation for startups with no finance team. Matches vendor invoices against bank records in four passes: exact, vendor reference, tolerant, then partial payment. Role-aware KPIs, undo/redo, BCrypt-secured audit trails.

`Java` `JavaFX` `SQL Server` `Maven` `SMTP`

<details>
<summary><b>More builds</b></summary>

<br/>

| Project | What it is | Stack |
|---|---|---|
| [Forge Marketplace](https://github.com/Hassaan146/forge-marketplace) | Install source for the Forge Mentor plugin | Claude Code |
| [Preflight](https://github.com/Hassaan146/preflight) | Audits AI-generated projects against a 31-area production standard, then fixes and verifies | LangGraph · Groq |
| [Agentika](https://github.com/Hassaan146/agentika) | Research agent with a hand-written ReAct loop, web search and file analysis | FastAPI · Groq |
| [AI Client Finder](https://github.com/Hassaan146/ai-client-finder) | Sources and qualifies leads | Python |
| [B2B SaaS](https://github.com/Hassaan146/B2B-SaaS-) | Team collaboration platform with orgs, tasks and subscriptions | FastAPI · Clerk |
| [CityMind Urban AI](https://github.com/Hassaan146/Citymind_Urban_Ai) | Urban data intelligence prototype | Python |
| [Consumer Price Index](https://github.com/Hassaan146/Consumer-Price-Index) | CPI pipeline built on discrete mathematics | Python |
| [ChronoRift OS](https://github.com/Hassaan146/ChronoRiftOS) | Operating systems coursework | C++ |
| [City Management System](https://github.com/Hassaan146/City-Management-System-DSA) | Graph-heavy simulation | C++ |
| [Super Mario COAL](https://github.com/Hassaan146/Super-Mario-COAL) | Game written in x86 assembly | Assembly |
| [Ivor Hospital DB](https://github.com/Hassaan146/IvorHospitalDB) | Hospital database system | PHP · SQL |

</details>

---

## Stack

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=flat-square&logo=sqlalchemy&logoColor=white)
![Assembly](https://img.shields.io/badge/x86-654FF0?style=flat-square&logo=assemblyscript&logoColor=white)

**AI**

![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-000000?style=flat-square&logo=modelcontextprotocol&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-D97757?style=flat-square&logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=flat-square)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)

**Backend**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white)

**Frontend**

![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Three.js](https://img.shields.io/badge/Three.js-000000?style=flat-square&logo=threedotjs&logoColor=white)

**Data**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

**Ship**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=flat-square&logo=render&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white)

---

## Activity

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=Hassaan146&bg_color=0d1117&color=58a6ff&line=1f6feb&point=ffffff&area=true&hide_border=true" width="98%" alt="Contribution graph" />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-light.svg" />
  <img src="https://raw.githubusercontent.com/Hassaan146/Hassaan146/output/snake-light.svg" width="98%" alt="Snake eating the contribution graph" />
</picture>

</div>

---

## Contact

At Arbisoft right now. Open to contract work and startup collaborations, mostly around AI agents and backend systems.

If you are building something and part of it is stuck, that is the email I like getting.

<div align="center">

[![Email](https://img.shields.io/badge/muhammadhassaanulmustafa@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117)](mailto:muhammadhassaanulmustafa@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&labelColor=0d1117)](https://linkedin.com/in/muhammad-hassaan25480a322)

</div>
