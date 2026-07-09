# Instructor Guide — Modern AI Developer Workspace Workshop

## Workshop Overview

| Detail | Value |
|---|---|
| **Title** | Modern AI Developer Workspace |
| **Duration** | 90 minutes (extensible to 120 min) |
| **Delivery** | Instructor-led, hands-on, via Zoom |
| **Audience** | Junior developers in an Advanced Technologies & AI program |
| **Experience Level** | Heterogeneous — some coding/vibe-coding experience, some none |
| **Tools** | VS Code, GitHub Copilot, Claude Code/ChatGPT, GitHub Codespaces, Lovable (demo) |
| **Platform** | Windows primary, browser-based (Codespaces) mitigates mixed OS |

---

## Pre-Workshop Preparation (30–60 min before)

### Environment Check

- [ ] Test the Codespace: click "Open in Codespaces" on the boilerplate repo — verify it provisions in <90 seconds
- [ ] Verify the devcontainer installs: Python 3.12, pytest, GitHub Copilot extension, GitHub CLI
- [ ] Run `pytest tests/ -v` in the Codespace — confirm 11 passing, 9 failing tests
- [ ] Test the GitHub Actions CI workflow — push a test commit and verify CI runs
- [ ] Prepare a backup Codespace in case of slow provisioning during the workshop

### Materials Check

- [ ] Zoom session configured with screen sharing and breakout rooms
- [ ] Slides loaded and tested (presenter view with notes)
- [ ] Boilerplate repository published on GitHub (public)
- [ ] Student invitation link ready (bit.ly or similar short link)
- [ ] Exercise handouts accessible (in repo, in `exercises/` folder)
- [ ] Backup exercises for students who finish early

### Personal Demo Prep

- [ ] Your GitHub account is logged in
- [ ] GitHub Copilot is active in your VS Code
- [ ] Claude Code CLI is installed and authenticated (if demoing)
- [ ] Lovable is connected to a GitHub account (if demoing)
- [ ] Terminal font size increased (Zoom students need to read commands)
- [ ] VS Code zoom level set to 150%+ for screen sharing

---

## Timing & Run-of-Show (90 Minutes)

### Block 1: Welcome & The Big Picture (10 min)

| Time | Activity | Detail |
|---|---|---|
| 0:00–0:02 | Welcome & icebreaker | "Who has written code before? Who has used AI to write code?" Quick poll via Zoom |
| 0:02–0:05 | Why this workshop matters | The 2026 developer landscape: every team uses AI. This workshop teaches the workflow, not just tools. |
| 0:05–0:08 | The ecosystem map | Show the slide with the full ecosystem: Git, GitHub, IDE, Terminal, Cloud, AI Assistant. Brief "why each exists." |
| 0:08–0:10 | Agenda walkthrough | "In 90 minutes, we'll go from zero to having collaborated on a team project using AI." Show the 6 exercises. |

### Block 2: Concepts — Why Everything Exists (15 min)

| Time | Activity | Detail |
|---|---|---|
| 0:10–0:13 | Git: The Time Machine | Analogy: shared notebook + time machine. Problem: file versioning nightmare. Solution: track every change. |
| 0:13–0:16 | GitHub: The Shared Library | Analogy: a library where everyone can check out and contribute books. Problem: collaboration. Solution: cloud hosting + collaboration. |
| 0:16–0:19 | IDE & Terminal: The Workbench | Analogy: the workbench in a workshop. VS Code = the workbench. Terminal = the power tools. |
| 0:19–0:22 | Cloud Dev Environments: The Anywhere Office | Analogy: a fully-equipped workshop you can teleport to from any device. Codespaces = no install, instant setup. |
| 0:22–0:25 | AI Assistants: The Junior Developer | Analogy: a junior dev pair-programming with you. Different types: autocomplete (Copilot), agent (Claude Code), generator (Lovable). |

> **Teaching tip:** Use the "Why → Analogy → Problem → Workflow → Example" pattern for each concept. Don't spend more than 3 minutes per concept. The goal is awareness, not mastery.

### Block 3: Exercise 1 — GitHub Account (10 min)

| Time | Activity | Detail |
|---|---|---|
| 0:25–0:27 | Demo: Creating a GitHub account | Screen-share creating a fresh account (or use incognito mode). Show the Student Developer Pack. |
| 0:27–0:35 | Student exercise | Students create accounts. Walk through activation of Student Pack. Monitor Zoom for raised hands. |

> **Contingency:** If GitHub signup is slow/blocked, have students use the "GitHub Web Editor" path (press "." on any repo). They can still participate without a full account.

### Block 4: Exercise 2 — Clone & Explore (10 min)

| Time | Activity | Detail |
|---|---|---|
| 0:35–0:37 | Demo: Forking + Codespaces | Screen-share: fork the repo, open in Codespaces, show the environment. Emphasize "no install needed." |
| 0:37–0:45 | Student exercise | Students fork and open Codespaces. Run `python src/app.py` and `pytest tests/ -v`. Monitor for provisioning issues. |

> **Contingency:** If Codespaces is slow (takes >2 min), tell students to use the GitHub Web Editor (press ".") as a fallback. They can still edit files, though they won't have a terminal.

### Block 5: Exercise 3 — First Edit (10 min)

| Time | Activity | Detail |
|---|---|---|
| 0:45–0:48 | Demo: The three-stage Git model | Show the diagram on slides. Use the "photograph" analogy. Then demo: edit a file, see the diff, stage, commit. |
| 0:48–0:55 | Student exercise | Students edit app.py, stage, commit. Walk around virtually via breakout rooms or screen sharing. |

> **Teaching tip:** This is the first time students interact with Git. Emphasize the FEELING: "You just created a permanent snapshot. You can always return to this point." Show `git log` to make it concrete.

### Block 6: Exercise 4 — AI-Assisted Coding (15 min) ⭐ KEY BLOCK

| Time | Activity | Detail |
|---|---|---|
| 0:55–0:58 | Demo: Copilot inline | Show Copilot completing the `delete_task` method. Type slowly. Let students see the ghost text suggestions. Press Tab to accept. |
| 0:58–1:01 | Demo: Copilot Chat | Ask Copilot Chat to explain the `TaskManager` class. Show the response. |
| 1:01–1:04 | Demo: Claude Code / ChatGPT | Open ChatGPT/Claude in browser. Ask it to implement `mark_complete`. Show the generated code. Paste it into VS Code. Emphasize: REVIEW before accepting. |
| 1:04–1:06 | Demo: Lovable (quick showcase) | Open Lovable. Show how natural language generates a full app. Connect to GitHub. Show the two-way sync. Emphasize: "This is vibe coding — but it still goes through GitHub." |
| 1:06–1:10 | Student exercise | Students use Copilot + ChatGPT/Claude to implement the TODO methods. Run tests. |

> **⭐ This is the centerpiece.** If you're running short on time, protect this block. The AI-assisted coding experience is what makes this workshop different from a traditional Git workshop.

> **Teaching tip:** Emphasize the REVIEW step. Show students that AI can generate incorrect code. Demo a "bad" suggestion and how you catch it by reading the code and running tests.

### Block 7: Exercise 5 — Commit & Push (10 min)

| Time | Activity | Detail |
|---|---|---|
| 1:10–1:12 | Demo: Push + PR | Screen-share: commit changes, push to GitHub, create a PR, watch CI run. Show the green checkmark. |
| 1:12–1:20 | Student exercise | Students commit, push, create PRs, watch CI. Celebrate the green checkmarks in the Zoom chat! |

> **Teaching tip:** The "green checkmark moment" is powerful. When CI passes, it's a tangible achievement. Celebrate it: "You just had your code automatically tested by a robot. That's CI. That's how professional teams work."

### Block 8: Exercise 6 — Team Challenge (20 min)

| Time | Activity | Detail |
|---|---|---|
| 1:20–1:22 | Setup: Breakout rooms | Assign teams of 3–4. Send to Zoom breakout rooms. One person per team creates the shared repo (fork + add collaborators). |
| 1:22–1:35 | Team work | Each member: create branch → implement feature with AI → push → open PR → review a teammate's PR → merge. |
| 1:35–1:38 | Regroup | Bring everyone back from breakout rooms. Quick poll: "How many teams got all PRs merged?" |
| 1:38–1:40 | Celebration & wrap-up | Show the "complete workflow" slide. Point to resources. Announce the winning team. |

> **Contingency:** If team challenge is running short, reduce to 3 features (drop "Due Date Field"). If merge conflicts arise, help one team resolve theirs as a teaching moment for everyone.

### Block 9: Wrap-Up & Resources (5 min)

| Time | Activity | Detail |
|---|---|---|
| 1:40–1:42 | Recap the workflow | Show the full workflow diagram: Fork → Clone → Edit → AI → Commit → Push → PR → CI → Merge |
| 1:42–1:45 | Resources | Point to GitHub Skills, freeCodeCamp, Microsoft Learn, Anthropic courses. Tell students to activate Student Pack. |
| 1:45–1:50 | Q&A and farewell | Open Q&A. If questions are deep, point to resources for further study. |

> **If extending to 120 minutes:** Add 15 minutes to Block 6 (deeper AI demo with Claude Code CLI), 10 minutes to Block 8 (longer team challenge), and 5 minutes to Block 9 (longer Q&A).

---

## Discussion Prompts (use throughout)

### After Block 2 (Concepts)
- "Which of these tools have you used before?"
- "Can you think of a non-software situation where version control would help?"
- "What concerns do you have about AI writing code?"

### After Block 6 (AI-Assisted Coding)
- "How did the AI-generated code compare to what you expected?"
- "Did you catch any mistakes the AI made?"
- "When might AI be harmful vs helpful?"

### After Block 8 (Team Challenge)
- "What was the hardest part of collaborating?"
- "How did code review change the quality?"
- "What would you do differently with a larger team?"

---

## Virtual Classroom Management Tips

1. **Zoom setup**: Use "Gallery View" to see all students. Have them rename with their first name.
2. **Screen sharing**: Keep your zoom at 150%+. Use a dark theme for VS Code (better contrast on screen share).
3. **Breakout rooms**: Pre-assign teams before the workshop if possible. Give clear instructions before sending them to rooms.
4. **Monitoring**: Visit each breakout room for 1-2 minutes. Ask "Any issues?" and move on.
5. **Energy management**: The post-lunch slump is real. The AI demo (Block 6) is the energy peak — keep it engaging.
6. **Inclusivity**: Some students will be faster, some slower. The exercises are designed to be self-paced. Faster students can help slower ones.
7. **Backup plans**: If Codespaces fails, fall back to GitHub Web Editor. If Copilot isn't available, use ChatGPT/Claude in browser. If Zoom fails, switch to the phone bridge.

---

## Contingency Quick Reference

| Issue | Impact | Quick Fix |
|---|---|---|
| Codespaces won't provision | Blocks Exercise 2+ | Use GitHub Web Editor (press "." on repo). No terminal but can edit + commit. |
| Copilot not working | Blocks Exercise 4 | Use ChatGPT/Claude in browser. Paste generated code manually. |
| Student Pack not approved | No free Copilot | Use Copilot free tier (limited) or ChatGPT free tier. |
| GitHub Actions CI not running | Blocks Exercise 5 demo | Show instructor's pre-run CI as example. Students can still push and create PRs. |
| Merge conflicts in team challenge | Blocks Exercise 6 merges | Help one team resolve as teaching moment. Others can proceed. |
| Zoom breakout rooms fail | Blocks Exercise 6 | Have teams collaborate via GitHub only (async PRs). Use Zoom chat for coordination. |
| Running 10+ minutes over | All blocks compressed | Cut Lovable demo. Reduce team challenge to 15 min. Skip Q&A, point to resources. |
| Running 10+ minutes under | Extra time available | Deeper Claude Code demo. Longer team challenge. Extended Q&A. Show git log --graph. |
