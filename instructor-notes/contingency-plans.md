# Contingency Plans — When Things Go Wrong

## Decision Tree: Primary Failure Modes

```
Start
  │
  ├── Codespaces working? ── NO ──→ Use GitHub Web Editor (press ".")
  │                                    │
  │                                    └── No terminal, but can edit + commit
  │                                        Exercises 2-5 still workable
  │                                        Exercise 6 (team) works via web PRs
  │
  ├── Copilot working? ── NO ──→ Use ChatGPT/Claude in browser
  │                                  │
  │                                  └── Copy/paste code manually
  │                                      Exercise 4 still works (slower)
  │
  ├── CI (GitHub Actions) working? ── NO ──→ Show instructor's pre-run CI
  │                                              │
  │                                              └── Students push and create PRs
  │                                                  without seeing CI pass
  │                                                  Explain CI conceptually
  │
  ├── Zoom breakout rooms working? ── NO ──→ Teams collaborate async
  │                                              │
  │                                              └── Each person works on their branch
  │                                                  Opens PR, leaves review comments
  │                                                  Merges when reviewed
  │
  └── Running over time? ── YES ──→ See "Time Compression" section
```

---

## Scenario 1: Codespaces Completely Down

**Probability:** Low (GitHub is very reliable, but can happen during peak hours)

**Impact:** Blocks Exercises 2-6 (anything requiring a terminal or running code)

**Plan A — GitHub Web Editor (works for most exercises):**
1. Students fork the repo on GitHub
2. Press "." on the repo page to open the web editor
3. Students can edit files, see diffs, and commit — all in the browser
4. No terminal, so they can't run `python src/app.py` or `pytest`
5. For Exercise 4 (AI coding): Use ChatGPT/Claude in browser, paste results into Web Editor
6. For Exercise 5 (commit/push): Web Editor handles git operations natively
7. For Exercise 6 (team challenge): All collaboration via GitHub PRs — no terminal needed

**Plan B — Instructor demos everything (worst case):**
1. Instructor screen-shares their working Codespace
2. Students follow along visually
3. Students are given the repo link to explore after the workshop
4. Focus on conceptual understanding and the "why" over hands-on practice
5. Assign exercises as post-workshop homework

**Plan C — Local setup for advanced students:**
1. Students who have VS Code + Python installed can clone locally
2. Provide the git clone URL and setup commands
3. These students become "helpers" for others

---

## Scenario 2: GitHub Copilot Not Available

**Probability:** Medium (extension issues, authentication, Student Pack not approved)

**Impact:** Blocks the Copilot portion of Exercise 4

**Plan A — Use ChatGPT/Claude in browser:**
1. Open chat.openai.com or claude.ai in a browser tab
2. Copy the method signature and docstring
3. Ask the AI to implement it
4. Copy the result back into VS Code
5. The workflow is identical — just not inline

**Plan B — Use Copilot Chat only (if inline doesn't work):**
1. Sometimes Copilot Chat works even when inline suggestions don't
2. Ask Copilot Chat: "Write the delete_task method for this class"
3. Copy the result from the chat panel

**Plan C — Pair programming (human AI):**
1. Pair up students — one writes code, the other reviews
2. This actually teaches valuable code review skills
3. Frame it as "before AI, this is how all teams worked"

---

## Scenario 3: Major Time Overrun (>10 min behind)

**Probability:** High (hands-on workshops always run over)

**Impact:** Need to compress remaining content

### Compression Strategy (in priority order):

| Priority | What to Cut | Time Saved | Impact |
|---|---|---|---|
| 1 | Lovable demo (Block 6) | 3 min | Low — it's a "wow" moment, not a learning objective |
| 2 | Q&A at end (Block 9) | 5 min | Low — point to resources instead |
| 3 | Team challenge duration (Block 8) | 5 min | Medium — reduce to 15 min, 3 features instead of 4 |
| 4 | Student Pack activation (Block 3) | 3 min | Low — can be done after workshop |
| 5 | Copilot Chat demo (Block 6) | 3 min | Medium — but ChatGPT demo covers similar ground |

**Never cut:**
- The Git workflow demo (Blocks 3-5 core) — this is the workshop's spine
- The AI-assisted coding exercise (Block 6 core) — this is the differentiator
- The commit/push/PR exercise (Block 5 core) — this is the payoff

---

## Scenario 4: Major Time Under-run (>10 min ahead)

**Probability:** Low (but possible with experienced students)

**Plan — Add depth, not breadth:**

| What to Add | Time | Value |
|---|---|---|
| Deep Claude Code CLI demo | 5 min | Shows agentic AI workflow (multi-file changes) |
| `git log --oneline --graph` demo | 3 min | Visualizes branch/merge history beautifully |
| Extended team challenge (5 features) | 5 min | More collaboration practice |
| Lovable live build (generate a task manager UI) | 5 min | "Vibe coding" in action — connects to GitHub |
| Extended Q&A with real student questions | 5 min | Addresses specific needs |
| Show `.gitignore` and explain what it does | 3 min | Practical Git knowledge |

---

## Scenario 5: Student Skill Gap (some completely lost)

**Probability:** Medium (heterogeneous audience by design)

**Plan A — Peer helpers:**
1. Identify students who are ahead (finished Exercise 2 while others are on Exercise 1)
2. Ask them to help their neighbors in breakout rooms or via Zoom chat
3. Frame it positively: "You're now a TA for the next 10 minutes"

**Plan B — Scaffolded exercises:**
1. The exercises are designed to be self-paced
2. Students who are behind can focus on Exercises 1-4 (the core workflow)
3. Exercise 6 (team challenge) can be observational for struggling students
4. Give them the solutions repo to study after the workshop

**Plan C — One-on-one via breakout room:**
1. Pull 1-2 struggling students into a separate breakout room
2. Walk them through the exercises step by step
3. Rejoin the main session when they're caught up

---

## Scenario 6: Technical Failure During Demo

**Probability:** Medium (live demos always have risk)

**Plan — "The Show Must Go On":**

1. **Pre-recorded backup:** Record key demos (Copilot completing code, PR creation, CI passing) before the workshop. If the live demo fails, play the recording.

2. **Narrate through failures:** If something breaks during your demo:
   - Don't panic or apologize excessively
   - Narrate what you see: "Hmm, I'm getting an error here. This is actually a great teaching moment — let me show you how I'd debug this."
   - Show the debugging process — it's more valuable than a perfect demo

3. **Have a working state to fall back to:**
   - Keep a branch with all exercises completed
   - If your live environment breaks, switch to showing the completed state
   - Say: "Let me show you what the end result looks like while I fix my environment"

---

## Pre-Workshop Checklist (Reduce Contingency Probability)

- [ ] Test Codespaces provisioning (twice, at different times)
- [ ] Verify CI workflow runs correctly
- [ ] Pre-record the 3 key demos as backup
- [ ] Have a working Codespace open and ready as backup
- [ ] Test Zoom breakout rooms before the session
- [ ] Prepare a "quick start" slide with just the essentials (repo link, exercise order)
- [ ] Have the troubleshooting guide open in a separate tab
- [ ] Test screen sharing with VS Code at 150% zoom
- [ ] Have a co-pilot/TA if possible (monitors chat while you teach)
- [ ] Prepare a "resources" slide for students who finish early
