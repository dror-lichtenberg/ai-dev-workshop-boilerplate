# 🚀 Modern AI Developer Workspace — Workshop Boilerplate

> **A 90-minute hands-on workshop for junior developers entering AI-assisted software teams in 2026.**

[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/your-org/ai-dev-workshop)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-pytest-green.svg)]()

---

## 📋 Table of Contents

- [What Is This?](#what-is-this)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Quick Start (3 Paths)](#quick-start-3-paths)
- [Exercises Overview](#exercises-overview)
- [The Team Challenge](#the-team-challenge)
- [Git History as a Learning Tool](#git-history-as-a-learning-tool)
- [For Instructors](#for-instructors)
- [Recommended Resources](#recommended-resources)
- [License](#license)

---

## What Is This?

This repository is the **hands-on lab environment** for a 90-minute instructor-led workshop titled **"Modern AI Developer Workspace."** It is designed for junior developers with **heterogeneous coding backgrounds** — some have coding or "vibe coding" experience, others have none.

### What you will learn

1. **Why** modern development teams use Git, GitHub, cloud environments, and AI assistants
2. **How** a professional development workflow operates: `clone → edit → AI-assist → commit → push → verify`
3. **What tools** make up a 2026 developer workspace: VS Code, GitHub Copilot, Claude Code, Codespaces, and Lovable

### Teaching philosophy

> _We don't teach tools. We teach **concepts, workflows, and professional practices** — using tools as the medium._

For every major concept (Git, GitHub, IDE, Terminal, Cloud, AI Assistant), this workshop follows a consistent pattern:
1. **Why it exists** — the problem it solves
2. **A memorable analogy** — to anchor understanding
3. **The professional workflow** it enables
4. **A simple realistic example** — hands-on practice

---

## Repository Structure

```
ai-dev-workshop-boilerplate/
├── .devcontainer/
│   └── devcontainer.json          # Codespaces configuration (zero-install)
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI pipeline (auto-test)
├── starter/                       # The code students work with
│   ├── src/
│   │   ├── app.py                 # Main application (a simple task manager API)
│   │   └── utils.py               # Helper functions (incomplete — for AI exercise)
│   ├── tests/
│   │   └── test_app.py            # Pytest tests (some failing — for AI exercise)
│   └── requirements.txt           # Python dependencies
├── solutions/                     # Completed reference solutions
│   ├── src/
│   │   ├── app.py
│   │   └── utils.py
│   └── tests/
│       └── test_app.py
├── exercises/                     # Step-by-step exercise handouts
│   ├── 01-github-account.md
│   ├── 02-clone-explore.md
│   ├── 03-first-edit.md
│   ├── 04-ai-assisted-coding.md
│   ├── 05-commit-push.md
│   └── 06-team-challenge.md
├── instructor-notes/              # Instructor-only materials
│   ├── instructor-guide.md        # Full teaching guide with timing
│   ├── troubleshooting.md         # Common issues and fixes
│   └── contingency-plans.md       # What to do when things go wrong
├── assets/                        # Diagrams, screenshots, demo assets
├── .gitignore
└── README.md                      # This file
```

---

## Prerequisites

### Minimal (recommended for this workshop)

| Requirement | Details |
|---|---|
| **GitHub account** | Free account at [github.com](https://github.com). No Student Pack needed for the workshop itself. |
| **Web browser** | Chrome, Edge, or Firefox (latest version) |
| **Internet connection** | Stable connection for Codespaces + Zoom |

### Optional (for students who want local setup)

| Requirement | Details |
|---|---|
| **VS Code** | [Download](https://code.visualstudio.com/) — free, cross-platform |
| **Git** | [Download](https://git-scm.com/downloads) — or use built-in on Mac/Linux |
| **Python 3.12+** | [Download](https://www.python.org/downloads/) — only for local execution |
| **GitHub Copilot** | Free for verified students via [GitHub Education](https://education.github.com/pack) |

> **💡 Instructor note:** This workshop is designed for **little-to-no pre-work**. Students can participate fully using GitHub Codespaces (browser-based, zero install). Local setup is optional and provided for motivated students.

---

## Quick Start (3 Paths)

### Path A: Codespaces (Zero Install — Recommended for Workshop)

```
1. Click the "Open in Codespaces" button above
2. Wait ~60 seconds for your cloud environment to provision
3. VS Code opens in your browser — fully configured
4. Start with Exercise 01
```

### Path B: Local VS Code (For Students with Prior Experience)

```bash
# Clone the repository
git clone https://github.com/your-org/ai-dev-workshop.git
cd ai-dev-workshop

# Open in VS Code
code .

# Install Python dependencies
cd starter
pip install -r requirements.txt

# Run tests
pytest tests/
```

### Path C: GitHub Web Editor (Simplest — No Clone Needed)

```
1. Fork the repository (click "Fork" on GitHub)
2. Press "." (period) on the repo page to open the web editor
3. Edit files directly in the browser
4. Commit changes through the web interface
```

---

## Exercises Overview

Each exercise is designed as a **self-contained handout** with clear steps, expected outcomes, and troubleshooting tips.

| # | Exercise | Time | Concept Focus | Tool Focus |
|---|---|---|---|---|
| 1 | [Create Your GitHub Account](exercises/01-github-account.md) | 10 min | Why Git? Why GitHub? | GitHub.com |
| 2 | [Clone & Explore the Repository](exercises/02-clone-explore.md) | 10 min | Repositories, file structure, Codespaces | Codespaces / VS Code |
| 3 | [Make Your First Edit](exercises/03-first-edit.md) | 10 min | Working directory, staging, commits | VS Code Source Control |
| 4 | [AI-Assisted Coding](exercises/04-ai-assisted-coding.md) | 15 min | AI pair programming, prompting, code review | Copilot + Claude Code |
| 5 | [Commit & Push to GitHub](exercises/05-commit-push.md) | 10 min | Remote repositories, push, PRs | Git, GitHub |
| 6 | [Team Challenge](exercises/06-team-challenge.md) | 20 min | Collaboration, branches, merge, CI | Full workflow |

### Learning progression

```
Account → Clone → Edit → AI-Assist → Commit → Push → PR → CI Check → Team Merge
  (1)      (2)     (3)      (4)        (5)     (6)    (7)    (8)        (9)
```

Each exercise builds on the previous one. By the end, you will have experienced the **complete professional development workflow** used by modern AI-assisted software teams.

---

## The Team Challenge

The final exercise is a **team collaboration challenge** that brings everything together:

- Students are grouped into teams of 3–4
- Each team member creates a branch, implements a feature using AI assistance, and opens a pull request
- The team reviews each other's PRs and merges them
- GitHub Actions CI automatically runs tests on each PR
- The first team to get all PRs merged with passing tests wins

**Features to implement (each team member picks one):**
1. Add a "priority" field to tasks (High/Medium/Low)
2. Add a "due date" field to tasks
3. Add a "mark complete" function
4. Add input validation (empty task names rejected)

---

## Git History as a Learning Tool

This repository is intentionally built with a **progressive commit history** (15–20 commits) that tells the story of how a project evolves. Each commit teaches a concept:

```
Commit 1:  "Initial commit — empty repository"
Commit 2:  "Add README with project description"
Commit 3:  "Add .gitignore for Python project"
Commit 4:  "Add basic project structure (src/, tests/)"
Commit 5:  "Add requirements.txt with dependencies"
Commit 6:  "Add app.py with TaskManager class skeleton"
Commit 7:  "Add add_task() and list_tasks() methods"
Commit 8:  "Add utils.py with date formatting helper"
Commit 9:  "Add first test — test_add_task()"
Commit 10: "Add test for list_tasks()"
Commit 11: "Add devcontainer.json for Codespaces"
Commit 12: "Add GitHub Actions CI workflow"
Commit 13: "Fix: handle empty task list in list_tasks()"
Commit 14: "Refactor: extract validation to utils.py"
Commit 15: "Add delete_task() method"
Commit 16: "Add test for delete_task()"
Commit 17: "Docs: update README with exercise instructions"
Commit 18: "Add instructor notes and exercise handouts"
Commit 19: "Add solutions branch with completed code"
Commit 20: "Add team challenge branch with feature stubs"
```

> **💡 Instructor tip:** Run `git log --oneline --graph` during the demo to show students how a real project's history tells a story.

---

## For Instructors

See the [`instructor-notes/`](instructor-notes/) directory for:
- **[Instructor Guide](instructor-notes/instructor-guide.md)** — Full timing, narrative, demos, discussion prompts
- **[Troubleshooting Guide](instructor-notes/troubleshooting.md)** — Common student issues and fixes
- **[Contingency Plans](instructor-notes/contingency-plans.md)** — What to do when things go wrong

---

## Recommended Resources

| Resource | Type | Best For | Link |
|---|---|---|---|
| GitHub Skills: Introduction to GitHub | Interactive exercise | First day on GitHub | [skills.github.com](https://skills.github.com/) |
| Microsoft Learn: Copilot Fundamentals | Self-paced course | Understanding Copilot | [learn.microsoft.com](https://learn.microsoft.com/en-us/training/paths/copilot/) |
| GitHub Student Developer Pack | Free tools | Getting Copilot + Codespaces free | [education.github.com/pack](https://education.github.com/pack) |
| freeCodeCamp Git Crash Course | Video (1 hour) | Git foundations | [freecodecamp.org](https://www.freecodecamp.org/news/git-and-github-crash-course-for-beginners/) |
| Microsoft: Mastering Copilot for Paired Programming | GitHub repo | Advanced Copilot training | [github.com/microsoft](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming) |
| Anthropic: Claude Code in Action | Course | Claude Code CLI workflow | [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-code-in-action) |
| Lovable GitHub Integration Guide | Documentation | Vibe coding → GitHub sync | [docs.lovable.dev](https://docs.lovable.dev/integrations/github) |

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> **Built for the Advanced Technologies & AI program.**
> _Preparing the next generation of developers for AI-assisted software teams._
