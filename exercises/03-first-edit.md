# Exercise 3: Make Your First Edit (10 minutes)

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:
- **Describe** the three-stage Git workflow (working directory → staging → commit)
- **Edit** a file in VS Code
- **Stage** changes using VS Code's Source Control panel
- **Commit** changes with a meaningful commit message

---

## 📖 The Story: How Git Tracks Changes

### The Three Stages of Git

Git uses a three-stage model for managing changes:

```
  Working Directory      Staging Area       Repository
  ┌─────────────┐      ┌─────────────┐    ┌─────────────┐
  │ Your files  │ ──→  │ Changes     │ ──→│ Permanent   │
  │ as you      │ add  │ ready to    │    │ snapshot    │
  │ edit them   │      │ be saved    │commit│ in history │
  └─────────────┘      └─────────────┘    └─────────────┘
```

> **Analogy: Git is like taking a photograph.**
> - **Working Directory** = You're getting dressed (making changes)
> - **Staging Area** = You step in front of the camera and pose (`git add`)
> - **Commit** = The photographer takes the picture (`git commit`)
> - **Repository** = The photo album — a permanent record of that moment
>
> You can change your outfit as many times as you want. But once the photo is taken (committed), that moment is preserved forever.

### Why a Staging Area?

You might ask: "Why not just save directly? Why the extra step?"

The staging area lets you **choose which changes to save together**. Maybe you edited three files but only want to commit two of them as a logical unit. The staging area gives you that control.

> **Professional practice:** Each commit should represent ONE logical change. "Add delete_task method" is a good commit. "Add delete_task, fix typo in README, and change button color" is a bad commit.

---

## 🔧 Steps

### Step 1: Open the Source Control Panel

In VS Code:
- Click the **Source Control** icon in the left sidebar (it looks like a branch/fork symbol)
- Or press `Ctrl+Shift+G` (Windows) / `Cmd+Shift+G` (Mac)

> **What is this?** This is VS Code's visual interface for Git. Instead of typing Git commands, you can click buttons. Behind the scenes, it runs the same Git commands.

### Step 2: Make a Small Edit

1. Open `starter/src/app.py`
2. Scroll to the bottom where it says `if __name__ == "__main__":`
3. Find the line that says:
   ```python
   print("✅ Demo complete! Now implement the TODO methods.")
   ```
4. Change it to:
   ```python
   print(f"✅ Demo complete! {your_name} is ready to implement the TODO methods.")
   ```
   (Replace `your_name` with your actual name, e.g., `Maria`)

5. Save the file (`Ctrl+S` / `Cmd+S`)

### Step 3: See What Changed

1. Go back to the **Source Control** panel
2. You should see `app.py` listed under **"Changes"**
3. Click on `app.py` — you'll see a **diff view**:
   - Red lines = what was removed
   - Green lines = what was added

> **What is a diff?** A "diff" (difference) shows exactly what changed between the current version and the last committed version. This is how code reviews work — reviewers look at diffs to understand what changed.

### Step 4: Stage Your Change

1. In the Source Control panel, hover over `app.py`
2. Click the **"+"** icon next to it
3. The file moves from "Changes" to **"Staged Changes"**

> **What just happened?** You told Git: "I want to include this change in my next commit." This is the visual equivalent of `git add`.

### Step 5: Write a Commit Message

1. In the text box at the top of the Source Control panel, type:
   ```
   Update demo message with student name
   ```
2. Click the **✓ (Commit)** button, or press `Ctrl+Enter`

> **What just happened?** You created a commit — a permanent snapshot of your changes. This is the visual equivalent of `git commit -m "your message"`.

### Step 6: View the Commit History

Open a terminal and run:
```bash
git log --oneline -5
```

You should see your recent commit at the top, with a unique hash (like `a1b2c3d`), the message, and your name.

> **💡 The commit hash:** Every commit gets a unique 40-character identifier (SHA-1 hash). The short version shown by `--oneline` is the first 7 characters. This hash lets you reference any point in your project's history.

---

## ✅ Checklist

- [ ] I edited `app.py` and saved my changes
- [ ] I saw the diff view showing what changed
- [ ] I staged my change using the Source Control panel
- [ ] I wrote a meaningful commit message
- [ ] I committed my change
- [ ] I can see my commit in `git log`

---

## 🤔 Discussion Questions

- Why does Git use a staging area instead of saving changes directly?
- What makes a good commit message? What makes a bad one?
- How might code review change if there were no commit history?

---

## 🗺️ Navigation

⬅️ **Previous:** [Exercise 2: Clone & Explore the Repository](02-clone-explore.md)  
⏭️ **Next:** [Exercise 4: AI-Assisted Coding](04-ai-assisted-coding.md)
