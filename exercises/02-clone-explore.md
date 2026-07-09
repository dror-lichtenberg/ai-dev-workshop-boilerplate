# Exercise 2: Clone & Explore the Repository (10 minutes)

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:
- **Explain** what a repository is and why it matters
- **Launch** a GitHub Codespace (cloud development environment)
- **Navigate** a project's file structure in VS Code
- **Run** a Python program and its tests

---

## 📖 The Story: What Is a Repository?

### The Problem

When you join a software team, you need to get a copy of the project code on your computer. But "copying files" isn't enough — you need:
- The code itself
- Configuration files (what tools, what versions)
- Documentation
- Test files
- History of all changes

### The Solution: The Repository

A **repository** (or "repo") is a special folder that Git manages. It contains:
- All your project files
- The complete history of every change ever made
- Configuration for tools and environments

> **Analogy: A repository is like a library archive.**
> - The books = your code files
> - The card catalog = the Git history (who changed what, when)
> - The reading room = your working directory (where you make changes)
> - The librarian = Git itself (keeping everything organized)

### Cloning

**Cloning** means making a local copy of a repository. With **GitHub Codespaces**, "local" means a cloud computer — so it works on any device with a browser.

> **Analogy: Cloning is like checking out a book from the library.** You get your own copy to work with. When you're done, you return the changes.

---

## 🔧 Steps

### Step 1: Fork the Repository

1. Go to the workshop repository on GitHub (your instructor will share the link)
2. Click the **"Fork"** button (top right)
3. Choose your personal account as the destination
4. Click **"Create fork"**

> **What just happened?** You now have your OWN copy of the repository on your GitHub account. You can make changes without affecting anyone else's copy.

### Step 2: Open in Codespaces

1. On YOUR forked repository, click the green **"Code"** button
2. Click the **"Codespaces"** tab
3. Click **"Create codespace on main"**
4. Wait ~60 seconds for your environment to provision

> **What just happened?** GitHub created a cloud computer with VS Code, Python, Git, and all the project files — all in your browser. No installation needed!

> **💡 What is Codespaces?** It's a full development environment running on GitHub's servers. You access it through your browser. It has VS Code, Python, Git, GitHub CLI, and all extensions pre-installed. This is how many modern teams work — especially for onboarding new developers.

### Step 3: Explore the File Structure

In the VS Code Explorer panel (left side), notice the file structure:

```
ai-dev-workshop-boilerplate/
├── .devcontainer/       # Codespaces configuration
├── .github/workflows/   # CI/CD automation
├── starter/             # Your working code
│   ├── src/             # Source code
│   │   ├── app.py       # Main application
│   │   └── utils.py     # Helper functions
│   ├── tests/           # Test files
│   └── requirements.txt # Dependencies
├── exercises/           # Exercise handouts (this file!)
├── solutions/           # Reference solutions (don't peek!)
├── instructor-notes/    # Instructor materials
└── README.md            # Project documentation
```

### Step 4: Read the README

1. Click on `README.md` in the file explorer
2. Read through the project overview
3. Notice the structure, badges, and instructions

> **💡 Why READMEs matter:** In a professional project, the README is the front door. It's the first thing anyone sees. A good README explains: what the project is, how to set it up, and how to contribute.

### Step 5: Run the Application

Open a terminal in VS Code:
- Menu: **Terminal → New Terminal** (or press `` Ctrl+` ``)

Run the demo:
```bash
cd starter
python src/app.py
```

You should see output showing the Task Manager demo — tasks being added and listed.

### Step 6: Run the Tests

In the same terminal:
```bash
pytest tests/ -v
```

You should see:
- ✅ Some tests **PASSING** (the ones for implemented methods)
- ❌ Some tests **FAILING** (the ones for TODO methods — you'll fix these in Exercise 4!)

> **What are tests?** Tests are code that checks if your other code works correctly. When you push to GitHub, the CI pipeline automatically runs these tests. If any test fails, you know something is broken BEFORE it reaches production.

---

## ✅ Checklist

- [ ] I forked the repository to my own GitHub account
- [ ] I opened a Codespace and see VS Code in my browser
- [ ] I can see the project file structure
- [ ] I ran `python src/app.py` and saw the demo output
- [ ] I ran `pytest tests/ -v` and saw some passing and some failing tests

---

## 🤔 Discussion Questions

- What files did you notice in the project? Which ones seem important?
- Why might a project separate code into `src/` and `tests/` folders?
- What would happen if there were no tests?

---

## 🗺️ Navigation

⬅️ **Previous:** [Exercise 1: Create Your GitHub Account](01-github-account.md)  
⏭️ **Next:** [Exercise 3: Make Your First Edit](03-first-edit.md)
