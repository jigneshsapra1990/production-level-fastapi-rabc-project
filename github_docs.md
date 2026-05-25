````md id="d9v1qx"
# Git & GitHub Complete Guide

# 📌 What is Git?

Git is a distributed version control system used to track code changes in projects.

Git helps developers:
- Track file changes
- Manage source code
- Work in teams
- Restore old versions
- Manage branches

---

# 📌 What is GitHub?

GitHub is a cloud-based platform that stores Git repositories online.

Using GitHub, developers can:
- Store code online
- Collaborate with teams
- Share projects
- Manage versions
- Deploy applications
- Review code using Pull Requests

---

# 🔥 Difference Between Git and GitHub

| Git | GitHub |
|---|---|
| Version Control Tool | Cloud Platform |
| Works Locally | Works Online |
| Tracks Changes | Hosts Repositories |
| Installed on Computer | Website Service |

---

# ✅ Advantages of GitHub

## 1️⃣ Team Collaboration
Multiple developers can work together.

---

## 2️⃣ Version History
Track every code change.

---

## 3️⃣ Backup Storage
Your code is safely stored online.

---

## 4️⃣ Branching System
Create separate branches for features.

---

## 5️⃣ Pull Requests
Review code before merging.

---

## 6️⃣ Open Source Contribution
Contribute to public projects.

---

## 7️⃣ CI/CD Integration
Works with deployment pipelines.

---

## 8️⃣ Issue Tracking
Manage bugs and tasks.

---

# ❌ Disadvantages of GitHub

## 1️⃣ Internet Required
Need internet for pushing/pulling code.

---

## 2️⃣ Learning Curve
Git commands can be difficult initially.

---

## 3️⃣ Merge Conflicts
Conflicts happen when multiple developers edit same file.

---

## 4️⃣ Public Repository Risk
Public repos expose code if not managed properly.

---

## 5️⃣ Storage Limits
Free plans have some limitations.

---

# 🚀 Uses of GitHub

## Common Uses

- Source Code Management
- Team Collaboration
- Open Source Projects
- Portfolio Hosting
- CI/CD Pipelines
- Documentation
- Bug Tracking
- Version Control
- Backup Management

---

# 🛠️ Most Used Git Commands

---

# ✅ Configure Git

## Set Username

```bash
git config --global user.name "Your Name"
```

Used to set Git username.

---

## Set Email

```bash
git config --global user.email "youremail@example.com"
```

Used to set Git email.

---

# ✅ Repository Commands

## Initialize Git

```bash
git init
```

Creates new Git repository.

---

## Clone Repository

```bash
git clone <repository-url>
```

Downloads existing repository from GitHub.

Example:

```bash
git clone https://github.com/user/project.git
```

---

# ✅ File Tracking Commands

## Check Status

```bash
git status
```

Shows modified and untracked files.

---

## Add Single File

```bash
git add filename.py
```

Adds one file to staging area.

---

## Add All Files

```bash
git add .
```

Adds all changed files.

---

# ✅ Commit Commands

## Commit Changes

```bash
git commit -m "Added login API"
```

Saves changes locally.

---

# ✅ Push & Pull Commands

## Push Code

```bash
git push origin main
```

Uploads code to GitHub.

---

## Pull Latest Code

```bash
git pull origin main
```

Downloads latest code from GitHub.

---

# ✅ Branch Commands

## Create Branch

```bash
git branch feature-auth
```

Creates new branch.

---

## Switch Branch

```bash
git checkout feature-auth
```

Moves to another branch.

---

## Create + Switch Branch

```bash
git checkout -b feature-auth
```

Creates and switches branch together.

---

## Show Branches

```bash
git branch
```

Displays all branches.

---

# ✅ Merge Commands

## Merge Branch

```bash
git merge feature-auth
```

Merges feature branch into current branch.

---

# ✅ Remote Commands

## Add Remote Repository

```bash
git remote add origin <repository-url>
```

Connect local project with GitHub.

---

## Show Remote URL

```bash
git remote -v
```

Displays connected repositories.

---

# ✅ Stash Commands

## Save Temporary Changes

```bash
git stash
```

Temporarily stores changes.

---

## Restore Stash

```bash
git stash pop
```

Restores saved changes.

---

# ✅ Log Commands

## Show Commit History

```bash
git log
```

Displays all commits.

---

## One Line Log

```bash
git log --oneline
```

Short commit history.

---

# ✅ Reset Commands

## Undo Last Commit

```bash
git reset --soft HEAD~1
```

Removes last commit but keeps changes.

---

## Hard Reset

```bash
git reset --hard HEAD~1
```

Deletes last commit permanently.

---

# ✅ Fetch Command

```bash
git fetch
```

Downloads latest repository data without merging.

---

# ✅ Diff Command

```bash
git diff
```

Shows code differences.

---

# ✅ Remove File

```bash
git rm filename.py
```

Deletes tracked file.

---

# ✅ Rename Branch

```bash
git branch -M main
```

Renames current branch.

---

# 📌 Most Common Git Workflow

## Step 1: Clone Project

```bash
git clone <repo-url>
```

---

## Step 2: Create Branch

```bash
git checkout -b feature-login
```

---

## Step 3: Add Changes

```bash
git add .
```

---

## Step 4: Commit Changes

```bash
git commit -m "Added login functionality"
```

---

## Step 5: Push Branch

```bash
git push origin feature-login
```

---

## Step 6: Create Pull Request

Create PR on GitHub.

---

# 📁 Common Branch Naming

| Branch | Purpose |
|---|---|
| main | Production code |
| develop | Development branch |
| feature/login | New feature |
| bugfix/api | Bug fixing |
| hotfix/payment | Urgent production fix |

---

# 📚 GitHub Features

## Popular Features

- Pull Requests
- Actions (CI/CD)
- Issues
- Wiki
- Releases
- Discussions
- Projects Board
- Security Scanning

---

# 🌟 Best Practices

## Recommended

- Commit small changes
- Write meaningful commit messages
- Use feature branches
- Pull latest code before push
- Never push secret keys
- Use `.gitignore`

---

# 📄 Example `.gitignore`

```bash
__pycache__/
.env
.venv/
*.pyc
.idea/
.vscode/
```

---

# 🚀 Useful GitHub Terms

| Term | Meaning |
|---|---|
| Repository | Project storage |
| Commit | Saved code snapshot |
| Branch | Separate development line |
| Merge | Combine code |
| Pull Request | Request to merge code |
| Fork | Copy repository |
| Clone | Download repository |
| Push | Upload code |
| Pull | Download code |

---

# 🎯 Conclusion

Git is used for version control.

GitHub is used for online repository hosting and collaboration.

Together they help developers:
- Manage projects
- Work in teams
- Track changes
- Deploy applications
- Maintain clean code history
````
