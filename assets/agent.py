"""The agent behind the profile.

Someone opens an issue titled "agent: <question>". A workflow runs this, the
answer lands on the sheet, and the issue gets a reply and is closed.

It works the same way the fashion assistant does. A rule based router handles
the question on its own, and if GROQ_API_KEY happens to be set in the repo
secrets the answer is written by a model instead. No key means no failure, just
the shorter path, which is the whole point of the second principle on the sheet.

Nothing here trusts the issue body. The question is taken from the title, cut to
length, stripped of markup, and only ever used as data.
"""

import json
import os
import pathlib
import re
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).parent
LOG = HERE / "asked.json"
MAX_Q = 120
KEEP = 4

FACTS = {
    "forge": ("Forge Mentor is a Claude Code plugin. It teaches the architectural "
              "decision, waits for your call, records it to .claude/forge, and blocks "
              "code until the question is answered. 1,216 tests at full coverage."),
    "news": ("The AI News Aggregator reads 164 sites and 36 YouTube channels and emails "
             "five picks every morning. Groq writes the summaries, Gemini covers the "
             "outages."),
    "skyelite": ("SkyElite AI took 3rd at the National AI Hackathon. Seven node LangGraph "
                 "pipeline, ranks destinations against passport and budget, and runs with "
                 "zero API keys because every call degrades to a mock."),
    "bitmadwall": ("BitMadWall carries encrypted messages and Bitcoin across a mesh of "
                   "phones. Bluetooth LE, Wi-Fi Direct and LoRa, up to seven hops, no "
                   "servers anywhere in the path."),
    "employeeos": ("AI Employee OS turns one plain English request into a dependency "
                   "aware workflow, routes each piece to the agent that owns it, and "
                   "hands back the full execution trace."),
    "stack": ("Python, TypeScript and C++ mostly. LangGraph and LangChain for "
              "orchestration, FastAPI and Pydantic v2 on the backend, Postgres and "
              "Supabase underneath, Docker and Vercel to ship."),
    "hire": ("Currently at Arbisoft, open to contract work and startup collaborations "
             "around AI agents and backend systems. Email is on the sheet above."),
    "guardrails": ("Rate limiting, input validation and row level security land before "
                   "the features do, because that is the part a client ends up "
                   "depending on."),
    "agent": ("This answer came from a router in assets/agent.py, triggered by the issue "
              "you opened, written back onto the sheet by a workflow. If GROQ_API_KEY is "
              "set it uses a model instead. It is the same fallback pattern the projects "
              "use."),
}

ROUTES = [
    (r"forge|plugin|claude code|decision|gate", "forge"),
    (r"news|aggregat|digest|scrape|rss", "news"),
    (r"skyelite|travel|hackathon|passport|visa", "skyelite"),
    (r"bitmad|mesh|lora|bluetooth|offline|bitcoin", "bitmadwall"),
    (r"employee|orchestrat|dag|workflow|multi.?agent", "employeeos"),
    (r"stack|tech|language|framework|tool|python|fastapi|langgraph", "stack"),
    (r"hire|hiring|available|freelance|contract|job|work with|remote", "hire"),
    (r"guardrail|security|rls|rate limit|validation|production", "guardrails"),
    (r"how does this work|how do you work|are you real|bot|this agent", "agent"),
]

FALLBACK = ("Not sure I have a good answer for that one. Try asking about a project by "
            "name, the stack, how the guardrails work, or whether he is available.")


def clean(question):
    """Take the question as data. Never as markup, never as instructions."""
    q = re.sub(r"^\s*agent\s*:\s*", "", question, flags=re.I)
    q = re.sub(r"[`<>|*_\[\]\(\)#]", " ", q)
    q = re.sub(r"\s+", " ", q).strip()
    return q[:MAX_Q]


def route(question):
    low = question.lower()
    for pattern, key in ROUTES:
        if re.search(pattern, low):
            return FACTS[key], key
    return FALLBACK, "none"


def via_model(question, key):
    """Optional. Only reached when a key exists, and a failure falls back."""
    system = ("You answer questions about Muhammad Hassaan-ul-Mustafa, an AI engineer in "
              "Islamabad. Facts you may use: " + " ".join(FACTS.values()) +
              " Answer in at most 40 words, plainly, no marketing language. If the facts "
              "do not cover it, say so.")
    payload = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": question}],
        "max_tokens": 120, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(
        "https://api.groq.com/openai/v1/chat/completions", data=payload,
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=25) as r:
        out = json.load(r)
    return out["choices"][0]["message"]["content"].strip()


def answer(question):
    q = clean(question)
    if not q:
        return "", FALLBACK, "empty"
    fallback, key = route(q)
    api = os.environ.get("GROQ_API_KEY", "").strip()
    if api:
        try:
            text = via_model(q, api)
            if text:
                return q, text[:320], key + "+model"
        except (urllib.error.URLError, KeyError, ValueError, OSError) as e:
            print("  model unavailable (%s), using the router" % e)
    return q, fallback, key


def load():
    if LOG.exists():
        try:
            return json.loads(LOG.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return []


def record(question, reply, who, when):
    items = load()
    items.insert(0, {"q": question, "a": reply, "who": who, "when": when})
    items = items[:KEEP]
    LOG.write_text(json.dumps(items, indent=1), encoding="utf-8")
    return items


if __name__ == "__main__":
    import sys
    title = sys.argv[1] if len(sys.argv) > 1 else ""
    who = sys.argv[2] if len(sys.argv) > 2 else "someone"
    when = sys.argv[3] if len(sys.argv) > 3 else ""
    q, a, path = answer(title)
    if not q:
        print("REPLY::Ask me something after the colon, like: agent: what is Forge Mentor")
        raise SystemExit(0)
    record(q, a, who, when)
    print("  routed via: %s" % path)
    print("REPLY::" + a)
