# Exercise 6: Team Challenge (20 minutes)

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:
- **Collaborate** on a shared repository using branches
- **Create** a feature branch for your specific task
- **Implement** a feature using AI assistance
- **Open** a pull request for team review
- **Review** a teammate's pull request
- **Merge** approved pull requests
- **Resolve** any merge conflicts that arise

---

## 📖 The Story: How Teams Actually Work

### The Problem

In Exercise 5, you worked alone. But real software development is a team sport. If everyone edits the same files at the same time, chaos ensues:
- Changes get overwritten
- Bugs sneak in
- Nobody knows who changed what

### The Solution: Branching

**Branches** let each person work on their own copy of the code without affecting others. When the work is done, it gets merged back.

```
                    main
                      │
          ┌───────────┼───────────┐
          │           │           │
     feature/priority  │  feature/due-date
          │           │           │
   (Alice's work)  (Bob's work)  (Carol's work)
          │           │           │
          └───────────┼───────────┘
                      │
                 merge all PRs
                      │
              updated main (all features)
```

> **Analogy: Branching is like parallel universes.**
> - Each branch is a separate timeline where you can make changes
> - The changes don't affect the "main" timeline until you merge them
> - Multiple people can work in parallel universes simultaneously
> - When ready, the universes merge back together

---

## 🔧 Setup

### Team Formation

- Your instructor will assign you to teams of 3–4 people
- One person in each team will be the **Repository Owner** (they'll host the shared repo)
- The others will be **Contributors**

### Repository Setup (Repository Owner Only)

1. Go to the workshop repository on GitHub
2. Click **"Fork"** → create the fork under your account
3. Go to **Settings → Collaborators**
4. Click **"Add people"** and add your teammates by their GitHub usernames
5. Share the repository URL with your team in the Zoom chat

### Team Access (Contributors)

1. Check your email for the collaboration invitation from the Repository Owner
2. Accept the invitation
3. You should now have push access to the shared repository

---

## 🔧 The Challenge

### Overview

Your team will implement **4 new features** for the Task Manager. Each team member picks ONE feature, creates a branch, implements it with AI assistance, and opens a PR.

### Feature Assignments

| Feature | Branch Name | Description |
|---|---|---|
| **Priority Field** | `feature/priority-field` | Add a `priority` field (1=High, 2=Medium, 3=Low) to tasks. Use `priority_label()` from utils.py. |
| **Due Date Field** | `feature/due-date` | Add a `due_date` field to tasks (optional, ISO format string). Add a method to filter tasks by due date. |
| **Mark Complete Toggle** | `feature/complete-toggle` | Improve `mark_complete` to toggle (if completed, un-complete it). Add a `mark_incomplete` method. |
| **Input Validation** | `feature/validation` | Add validation for priority (must be 1-3) and due_date (must be valid ISO date). Add tests. |

> **💡 If your team has only 3 people:** Skip the "Due Date Field" feature.

### Steps for Each Team Member

#### Step 1: Create Your Branch

In your Codespace (or local clone of the SHARED repo):

```bash
# Make sure you're on main and up to date
git checkout main
git pull origin main

# Create and switch to your feature branch
git checkout -b feature/your-feature-name
```

> **💡 Branch naming convention:** Professional teams use prefixes like `feature/`, `bugfix/`, `hotfix/`, `docs/` to categorize branches. This makes the project history cleaner.

#### Step 2: Implement Your Feature

Use any AI tool (Copilot, ChatGPT, Claude Code) to implement your feature:

1. Read the existing code in `app.py` and `utils.py`
2. Understand what your feature requires
3. Use AI to generate the code
4. **Review the AI-generated code** — make sure it fits the existing style
5. Add or update tests for your feature

> **⚠️ Important:** Each person is working on a DIFFERENT branch. You should NOT see your teammates' changes until you merge PRs.

#### Step 3: Commit and Push Your Branch

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Add priority field to tasks with label helper

- Tasks now accept optional priority (1=High, 2=Medium, 3=Low)
- Uses priority_label() from utils.py for human-readable output
- Added tests for priority field validation"

# Push your branch to GitHub
git push origin feature/your-feature-name
```

#### Step 4: Open a Pull Request

1. Go to the shared repository on GitHub
2. You should see a banner: "Compare & pull request" for your branch
3. Click it
4. Write a clear PR description:
   ```
   ## Feature: [Your feature name]

   ### What it adds
   - [Description of what was implemented]

   ### How it was built
   - [Which AI tools were used]
   - [What approach was taken]

   ### Testing
   - [x] New tests added
   - [x] All existing tests still pass
   - [x] CI check passes
   ```
5. Assign a teammate as reviewer
6. Click **"Create pull request"**

#### Step 5: Review a Teammate's PR

1. Go to the **"Pull requests"** tab on the shared repository
2. Click on a teammate's PR
3. Go to the **"Files changed"** tab
4. Review the code:
   - Does it look correct?
   - Does it follow the existing code style?
   - Are there tests?
5. If it looks good, click **"Review changes"** → **"Approve"**
6. If changes are needed, leave comments and click "Request changes"

> **💡 Code review is a critical professional skill.** In professional teams, no code gets merged without review. Reviews catch bugs, spread knowledge, and maintain code quality.

#### Step 6: Merge Approved PRs

1. Once a PR is approved and CI passes, click **"Merge pull request"**
2. Merge all team members' PRs one by one
3. After each merge, other team members should pull the updated main:
   ```bash
   git checkout main
   git pull origin main
   ```

> **⚠️ Merge conflicts:** If two PRs modify the same lines of code, you may get a merge conflict. GitHub will show this and ask you to resolve it. Your instructor can help with conflict resolution.

### Step 7: Verify the Final Result

After all PRs are merged:

1. Pull the latest main:
   ```bash
   git checkout main
   git pull origin main
   ```
2. Run all tests:
   ```bash
   cd starter
   pytest tests/ -v
   ```
3. All tests should pass ✅
4. Run the demo:
   ```bash
   python src/app.py
   ```

---

## 🏆 Winning Criteria

The first team to achieve ALL of the following wins:

1. ✅ All 4 features implemented (one per team member)
2. ✅ All 4 PRs opened, reviewed, and merged
3. ✅ All tests pass (CI green checkmark)
4. ✅ No merge conflicts remaining
5. ✅ Each PR has a descriptive title and description
6. ✅ Each PR was reviewed by at least one teammate

---

## ✅ Checklist

- [ ] I created a feature branch with a proper name
- [ ] I implemented my feature using AI assistance
- [ ] I reviewed the AI-generated code
- [ ] I added tests for my feature
- [ ] I committed with a descriptive message
- [ ] I pushed my branch to GitHub
- [ ] I opened a pull request with a clear description
- [ ] I reviewed at least one teammate's PR
- [ ] All PRs were merged
- [ ] All tests pass on the final main branch

---

## 🤔 Discussion Questions

- What was the hardest part of collaborating on the same repository?
- Did any merge conflicts occur? How were they resolved?
- How did AI assistance change the way you approached the feature?
- What would you do differently in a real project with a larger team?
- How did code review affect the quality of the merged code?

---

## 🎉 Congratulations!

You've completed the **Modern AI Developer Workspace Workshop!**

You now have hands-on experience with:
- ✅ GitHub accounts and navigation
- ✅ Codespaces (cloud development environments)
- ✅ VS Code and Git workflows
- ✅ GitHub Copilot and AI-assisted coding
- ✅ Commits, pushes, and pull requests
- ✅ CI/CD with GitHub Actions
- ✅ Team collaboration with branches and PRs
- ✅ Code review

**This is the same workflow used by professional AI-assisted software teams in 2026.**

### What's Next?

- **Activate your GitHub Student Developer Pack** for free Copilot, Codespaces, and more
- **Complete [GitHub Skills: Introduction to GitHub](https://skills.github.com/)** for a deeper Git foundation
- **Watch the [freeCodeCamp Git Crash Course](https://www.freecodecamp.org/news/git-and-github-crash-course-for-beginners/)** (1 hour) for comprehensive Git training
- **Explore [Microsoft Learn: Copilot Fundamentals](https://learn.microsoft.com/en-us/training/paths/copilot/)** for advanced Copilot skills
- **Try [Lovable](https://lovable.dev)** to experience vibe coding and see how AI can generate full applications
- **Read about [Claude Code](https://anthropic.skilljar.com/claude-code-in-action)** to learn about agentic AI coding workflows

---

## 🗺️ Navigation

⬅️ **Previous:** [Exercise 5: Commit & Push to GitHub](05-commit-push.md)  
🏠 **Home:** [README](../README.md)
