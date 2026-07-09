# Troubleshooting Guide — Common Student Issues

## Quick Reference Table

| Issue | Likely Cause | Fix |
|---|---|---|
| Codespace won't open | Browser, capacity, network | Refresh, try different browser, use Web Editor fallback |
| "command not found: python" | Python not in PATH | Use `python3` instead, or check Codespace terminal |
| "command not found: pytest" | Not installed | Run `pip install -r requirements.txt` in `starter/` |
| Copilot not showing suggestions | Extension not active | Check bottom-right for Copilot icon, sign in to GitHub |
| Copilot says "no suggestions" | Context unclear | Add a comment describing what you want, then start typing |
| Tests fail with "ModuleNotFoundError" | Import path issue | Run pytest from `starter/` directory: `cd starter && pytest` |
| "Permission denied" on git push | Not authenticated | In Codespaces: already authenticated. Local: set up SSH or PAT |
| PR has no CI checks | CI workflow not in repo | Check `.github/workflows/ci.yml` exists. May need to enable Actions in settings |
| Merge conflict | Two branches changed same lines | See merge conflict resolution section below |
| Fork button missing | Not logged in | Log in to GitHub first |
| Student Pack rejected | Verification issue | Use school email. If no school email, contact GitHub support |

---

## Detailed Solutions

### Codespaces Won't Provision

**Symptoms:** "Creating codespace..." spinner runs for >3 minutes, or error message.

**Solutions (in order):**
1. **Refresh the page** — sometimes the UI doesn't update when the codespace is ready
2. **Check Codespaces page** — go to github.com/codespaces to see if it was actually created
3. **Try a different browser** — Chrome or Edge work best with Codespaces
4. **Delete and recreate** — go to github.com/codespaces, delete the stuck codespace, create a new one
5. **Fallback: GitHub Web Editor** — go to the repo, press "." — opens a VS Code-like editor in browser (no terminal, but can edit and commit)

**If multiple students have this issue:** It may be a GitHub capacity issue. Fall back to GitHub Web Editor for all students. They can still do exercises 1-5 (editing, committing, pushing) without a terminal.

### Copilot Not Showing Suggestions

**Symptoms:** Typing in a Python file but no ghost-text suggestions appear.

**Solutions:**
1. **Check the status bar** (bottom-right of VS Code): Look for the Copilot icon
   - If it has a slash through it: Copilot is disabled. Click it and enable.
   - If it says "Sign in": Click and authorize with your GitHub account
2. **Check the extension**: Go to Extensions (Ctrl+Shift+X), search "GitHub Copilot", ensure it's installed and enabled
3. **Check Copilot settings**: Go to Settings (Ctrl+,), search "copilot", ensure "GitHub.copilot.advanced: enable" is true
4. **Reload VS Code**: Ctrl+Shift+P → "Developer: Reload Window"
5. **Fallback**: Use ChatGPT or Claude in a browser tab. Copy/paste code manually.

### Tests Fail with Import Errors

**Symptoms:** `ModuleNotFoundError: No module named 'app'` or similar.

**Cause:** pytest is being run from the wrong directory.

**Solution:**
```bash
# Make sure you're in the starter/ directory
cd starter
pytest tests/ -v
```

The test file uses `sys.path.insert(0, ...)` to find `src/`, but this only works when pytest is run from the `starter/` directory.

### Git Push Fails with Authentication Error

**Symptoms:** `Permission denied (publickey)` or `Authentication failed`.

**In Codespaces:** This should NOT happen — Codespaces is pre-authenticated. If it does:
1. Run `gh auth login` in the terminal and follow the prompts
2. Or use the VS Code Source Control panel instead of the terminal

**Locally:**
1. Use a Personal Access Token (PAT) instead of a password
2. Go to GitHub → Settings → Developer Settings → Personal Access Tokens → Generate new token
3. When pushing, use the PAT as your password
4. Or set up SSH keys (more advanced, see [GitHub SSH guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh))

### Merge Conflicts

**Symptoms:** GitHub says "This branch has conflicts that must be resolved" on a PR.

**Resolution on GitHub (easiest for beginners):**
1. Click "Resolve conflicts" on the PR page
2. GitHub shows a web-based merge editor
3. Look for conflict markers:
   ```
   <<<<<<< main
   This is the main branch version
   =======
   This is your branch version
   >>>>>>> feature/your-branch
   ```
4. Edit to keep the desired version (remove conflict markers)
5. Click "Mark as resolved"
6. Click "Commit merge"

**Resolution in VS Code:**
1. Pull the latest main: `git checkout main && git pull`
2. Switch to your branch: `git checkout feature/your-branch`
3. Merge main: `git merge main`
4. VS Code will show the "Merge Conflict" editor
5. Choose "Accept Current", "Accept Incoming", or manually edit
6. Save, stage, and commit: `git add . && git commit -m "Resolve merge conflict"`

**Teaching opportunity:** Merge conflicts are normal in team development. Use them as a teaching moment — show students how conflicts arise and how to resolve them calmly.

### GitHub Actions CI Not Running

**Symptoms:** PR shows no checks, or "Some checks were not successful" with no details.

**Solutions:**
1. **Check if Actions are enabled**: Go to repo Settings → Actions → General → ensure "Allow all actions" is selected
2. **Check workflow file**: Ensure `.github/workflows/ci.yml` exists and has valid YAML syntax
3. **Check the Actions tab**: Go to the "Actions" tab on GitHub to see if the workflow ran or errored
4. **Manually trigger**: If the workflow has `workflow_dispatch`, you can trigger it manually from the Actions tab

### Student Developer Pack Not Approved

**Symptoms:** Student verification is pending or rejected.

**Solutions:**
1. **Use school email**: The fastest path is using a `.edu` or school-registered email domain
2. **Add proof**: Upload a student ID card or enrollment letter
3. **Be patient**: Review can take up to 2 days during peak periods
4. **Workaround for workshop**: Students can use the Copilot free tier (limited suggestions) or ChatGPT free tier during the workshop. The Student Pack is for long-term benefit, not required for the workshop.

---

## Student Communication Templates

### When a student is stuck on Codespaces:
> "No worries! Let's use the GitHub Web Editor instead. Go to your forked repo and press the period key — that's the '.' key. It opens a code editor right in your browser. You won't have a terminal, but you can still edit files and commit changes."

### When a student is stuck on Copilot:
> "Let's use ChatGPT or Claude instead. Open a new browser tab, go to chat.openai.com or claude.ai. Copy the method you need to implement, paste it in, and ask: 'Can you implement this method?' Then copy the result back into your code. The workflow is the same — just a different AI tool."

### When a student finishes early:
> "Great job! Here are some bonus challenges: 1) Try using Claude Code CLI in the terminal to implement a feature. 2) Connect your repo to Lovable and generate a web UI for the task manager. 3) Read the instructor guide and think about what you'd teach differently."

### When a student is completely lost:
> "Let's start fresh. Open a new browser tab and go to [the repo link]. Click 'Fork', then click 'Code' → 'Codespaces' → 'Create codespace'. This gives you a fresh environment. Then follow along with Exercise 2 — I'll walk through it again on screen."
