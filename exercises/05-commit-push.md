# Exercise 5: Commit & Push to GitHub (10 minutes)

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:
- **Explain** the difference between local commits and pushing to a remote
- **Commit** multiple file changes as a logical unit
- **Push** changes from your local environment to GitHub
- **Create** a pull request to propose changes
- **Verify** that CI (Continuous Integration) checks pass

---

## 📖 The Story: From Local to Remote

### The Problem

You've been making commits in your Codespace. But those commits only exist on your cloud computer. If the Codespace is deleted, they're gone. And your teammates can't see them.

### The Solution: Pushing

**Pushing** sends your local commits to GitHub (the "remote" repository).

```
  Your Codespace (local)          GitHub (remote)
  ┌─────────────┐                ┌─────────────┐
  │ Your commits│  ── push ──→   │ Shared with │
  │ (only you   │                │   the team  │
  │  can see)   │  ←─ pull ──    │ (everyone)  │
  └─────────────┘                └─────────────┘
```

> **Analogy: Pushing is like publishing a chapter.**
> - **Local commits** = Writing chapters in your notebook (only you can see them)
> - **Push** = Publishing the chapters to the shared library (now everyone can read them)
> - **Pull** = Getting the latest chapters that others have published

### The Pull Request

A **Pull Request** (PR) is a formal proposal: "I made these changes. Please review and merge them into the main project."

```
  Your branch              Main branch
  ┌──────────┐            ┌──────────┐
  │ Feature  │── Pull ──→ │ Review   │── Merge ──→│ Updated │
  │ work     │  Request   │ & Test   │            │ Main    │
  └──────────┘            └──────────┘            └──────────┘
```

> **Analogy: A pull request is like submitting a draft to an editor.**
> - You wrote your chapter (your branch)
> - You submit it to the editor (open a PR)
> - The editor reviews it, maybe asks for changes
> - Once approved, it gets published (merged into main)

---

## 🔧 Steps

### Step 1: Commit Your AI-Assisted Changes

If you haven't already committed the changes from Exercise 4:

1. Open the **Source Control** panel
2. You should see `app.py` and possibly `utils.py` under "Changes"
3. Stage all changes: click the **"+"** next to each file
4. Write a commit message:
   ```
   Implement delete_task, mark_complete, and search_tasks with AI assistance

   Used GitHub Copilot for inline completion and ChatGPT for method generation.
   All tests passing.
   ```
5. Click **✓ (Commit)**

> **💡 Professional commit messages:** A good commit message has:
> - A **summary line** (imperative mood, ≤50 chars): "Implement delete_task, mark_complete, search_tasks"
> - An optional **body** explaining context: what tools were used, why decisions were made
>
> Avoid: "fixed stuff", "updated code", "asdfasdf"

### Step 2: Push to GitHub

1. In the Source Control panel, click **"Sync Changes"** (or the upward arrow ↗)
2. VS Code will push your commits to your forked repository on GitHub

**Alternative (terminal):**
```bash
git push origin main
```

> **What just happened?** Your local commits are now on GitHub. Anyone with access to your repository can see them.

### Step 3: View Your Changes on GitHub

1. Open your forked repository on GitHub (in a new browser tab)
2. You should see your latest commit message at the top
3. Click on the commit to see the diff

### Step 4: Create a Pull Request

Now let's propose merging your changes:

1. On your GitHub repository, click **"Contribute"** → **"Open pull request"**
2. Review the changes shown in the diff
3. Click **"Create pull request"**
4. Write a PR title: `Add delete_task, mark_complete, and search_tasks methods`
5. Write a description:
   ```
   ## What this PR adds
   - Implements `delete_task()` — removes a task by ID
   - Implements `mark_complete()` — sets task completed flag to True
   - Implements `search_tasks()` — case-insensitive keyword search

   ## How it was built
   - Used GitHub Copilot for inline code completion
   - Used ChatGPT for method generation and review
   - All tests pass locally

   ## Testing
   - [x] `pytest tests/ -v` — all tests pass
   - [x] Code reviewed for correctness
   - [x] Edge cases handled (task not found, empty search)
   ```
6. Click **"Create pull request"**

### Step 5: Watch the CI Pipeline

1. On your PR page, look for the **"Checks"** section at the bottom
2. You should see the GitHub Actions CI workflow running
3. Wait for it to complete (usually 1-2 minutes)
4. If it passes, you'll see a **green checkmark ✅**
5. If it fails, click "Details" to see what went wrong

> **What is CI?** **Continuous Integration** is a practice where every push or PR automatically runs tests and checks. This ensures broken code never reaches the main branch.
>
> **Analogy: CI is like an automated proofreader.** Before your chapter gets published, a robot reads it and checks for errors. If it finds any, it flags them for you to fix.

### Step 6: Merge the Pull Request

1. If the CI check passes and you're satisfied with the changes, click **"Merge pull request"**
2. Click **"Confirm merge"**
3. Optionally delete the branch (if you created one)

> **What just happened?** Your changes are now part of the main branch. This is the final step in the professional development workflow: **branch → code → test → PR → review → merge**.

---

## 🎉 The Complete Workflow

You just completed the full professional developer workflow:

```
 Fork → Clone/Codespaces → Edit → AI-Assist → Test → Commit → Push → PR → CI → Merge
```

This is the **same workflow** used by professional development teams at companies like Microsoft, Google, Amazon, and thousands of startups.

---

## ✅ Checklist

- [ ] I committed my AI-assisted code changes
- [ ] I pushed my commits to GitHub
- [ ] I created a pull request with a descriptive title and body
- [ ] I watched the CI pipeline run
- [ ] The CI checks passed (green checkmark)
- [ ] I merged my pull request

---

## 🤔 Discussion Questions

- Why is the pull request workflow important for team collaboration?
- What would happen if everyone pushed directly to main without PRs?
- How does CI change the way teams think about code quality?
- What information should a good PR description contain?

---

## 🗺️ Navigation

⬅️ **Previous:** [Exercise 4: AI-Assisted Coding](04-ai-assisted-coding.md)  
⏭️ **Next:** [Exercise 6: Team Challenge](06-team-challenge.md)
