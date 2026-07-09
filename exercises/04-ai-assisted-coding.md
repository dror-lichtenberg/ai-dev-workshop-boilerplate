# Exercise 4: AI-Assisted Coding (15 minutes)

## 🎯 Learning Objectives

By the end of this exercise, you will be able to:
- **Explain** how AI coding assistants fit into a professional workflow
- **Use** GitHub Copilot to autocomplete and generate code
- **Use** an AI agent (Claude Code or ChatGPT) to implement a complete method
- **Evaluate** AI-generated code for correctness and quality
- **Run** tests to verify AI-assisted code works

---

## 📖 The Story: AI in the Developer Workflow

### The Problem

Writing code from scratch is slow. Looking up syntax is tedious. Reading unfamiliar code is hard. Debugging can take hours.

### The Solution: AI Coding Assistants

In 2026, AI assistants are part of every professional developer's toolkit. They come in different forms:

| Tool | What It Does | When To Use It |
|---|---|---|
| **GitHub Copilot** | Autocompletes code inline in your editor | When you're typing and want suggestions |
| **Copilot Chat** | Chat with AI about your code in a sidebar | When you need explanation or want to ask questions |
| **Claude Code / Codex CLI** | AI agent that reads your repo and edits files | When you need multi-file changes or complex tasks |
| **Lovable** | Generates full apps from natural language | When you want to prototype quickly ("vibe coding") |

> **Analogy: AI assistants are like having a junior developer pair-programming with you.**
> - **Copilot** = the junior dev who finishes your sentences (fast, inline, lightweight)
> - **Claude Code / Codex** = the junior dev who takes a task and works on it independently (agentic, multi-file)
> - **Lovable** = the junior dev who builds a whole prototype from your description (generative, full-stack)
>
> **Key insight:** The AI is NOT a replacement for your judgment. It's a tool that makes you faster. You still need to understand the code, review it, and take responsibility for it.

### The Professional AI Workflow

```
1. Understand the task (human)
2. Describe what you want (human → AI)
3. AI generates code (AI)
4. Review the generated code (human) ← THIS STEP IS CRITICAL
5. Test the code (human + automated tests)
6. Refine if needed (human → AI → human)
7. Commit when tests pass (human)
```

> **⚠️ Golden rule of AI-assisted coding:** NEVER commit AI-generated code you don't understand. Always read it, understand it, and test it.

---

## 🔧 Steps

### Part A: GitHub Copilot Inline Completion (5 minutes)

1. Open `starter/src/app.py` in your Codespace
2. Scroll to the `delete_task` method (the first TODO)
3. Place your cursor after the docstring, inside the method
4. Start typing:
   ```python
   for task in
   ```
5. **Watch Copilot suggest the rest of the line** — it should suggest something like `self.tasks:`

6. Press **Tab** to accept the suggestion

7. Continue typing the logic. Copilot will suggest:
   - The `if` condition to check the ID
   - The `self.tasks.pop()` call
   - The `return` statements

8. Complete the `delete_task` method using Copilot's suggestions

> **💡 If Copilot doesn't activate:** Make sure the GitHub Copilot extension is installed. In Codespaces, it should be pre-installed via the devcontainer config. Check the bottom-right of VS Code for the Copilot icon.

### Part B: Copilot Chat for Explanation (3 minutes)

1. Click the **Copilot Chat icon** in the sidebar (or press `Ctrl+Alt+I`)
2. Ask it a question about the code:
   ```
   Explain what the TaskManager class does in simple terms
   ```
3. Read the explanation

> **💡 Use case:** When you join a new project, Copilot Chat is incredibly useful for understanding existing code. Instead of reading hundreds of lines, you can ask questions and get explanations.

### Part C: Claude Code / ChatGPT for a Complete Method (5 minutes)

Now let's use a more powerful AI to implement a harder method.

**Option 1: Using ChatGPT/Claude in browser**
1. Open ChatGPT or Claude in a new browser tab
2. Copy the `mark_complete` method's docstring and surrounding code
3. Ask:
   ```
   Implement the mark_complete method for a TaskManager class.
   It should find a task by ID and set its 'completed' field to True.
   Return the task if found, None if not.
   ```
4. Copy the generated code back into your `app.py`

**Option 2: Using Claude Code CLI (if available)**
```bash
# In the terminal:
claude "implement the mark_complete method in starter/src/app.py"
```

5. **Review the generated code:**
   - Does it match the existing code style?
   - Does it handle edge cases (task not found)?
   - Does it return the right type?

6. Paste the implementation into the `mark_complete` method

### Part D: Implement search_tasks on Your Own (2 minutes)

Now try the third TODO method — `search_tasks` — on your own using any AI tool:
1. Use Copilot inline, Copilot Chat, or ChatGPT/Claude
2. Implement the method to search tasks by keyword (case-insensitive)
3. Check the test in `test_app.py` to see what behavior is expected

> **💡 Reading tests to understand requirements is a professional skill.** In real projects, the tests often serve as the specification. If the test expects case-insensitive search, your implementation must be case-insensitive.

---

## 🔧 Verify: Run the Tests

After implementing all three methods, run the tests:

```bash
cd starter
pytest tests/ -v
```

**Expected outcome:**
- All tests should now PASS ✅
- If any tests fail, read the error message and fix the issue
- Use Copilot Chat or ChatGPT to help debug: paste the error message and ask "why is this test failing?"

---

## ⚠️ AI Code Review Checklist

Before moving on, review your AI-generated code:

- [ ] I understand every line of the generated code
- [ ] The code follows the existing style (naming, formatting, docstrings)
- [ ] Edge cases are handled (empty list, not found, etc.)
- [ ] All tests pass
- [ ] I could explain this code to a teammate if asked

> **Professional tip:** In many AI-assisted teams, pull request descriptions include a note like "Co-authored with GitHub Copilot" or "Generated with Claude Code, reviewed and tested by [name]." Transparency about AI usage is a professional norm.

---

## ✅ Checklist

- [ ] I used GitHub Copilot inline to complete `delete_task`
- [ ] I used Copilot Chat to get a code explanation
- [ ] I used an AI tool to implement `mark_complete`
- [ ] I implemented `search_tasks` (with AI assistance)
- [ ] I reviewed all AI-generated code
- [ ] All tests pass (`pytest tests/ -v`)

---

## 🤔 Discussion Questions

- How did the AI-generated code compare to what you would have written yourself?
- Did the AI make any mistakes? How did you catch them?
- When might AI assistance be harmful? When is it most helpful?
- What skills do developers still need even with AI assistance?

---

## 🗺️ Navigation

⬅️ **Previous:** [Exercise 3: Make Your First Edit](03-first-edit.md)  
⏭️ **Next:** [Exercise 5: Commit & Push to GitHub](05-commit-push.md)
