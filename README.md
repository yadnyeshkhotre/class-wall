# the CODE-VERSE wall 🧱

Every card on the wall arrived as a **pull request**: the same way code reaches production at real companies.

👉 **See the live wall:** open this repository's GitHub Pages link (Settings → Pages), or ask your instructor in the chat.

---

## Get your card on the wall (GitHub Desktop, about 10 minutes)

| # | Where | What to do |
|---|-------|------------|
| 1 | github.com | Open this repository and click **Fork** (top right), then **Create fork**. You now have your own copy. |
| 2 | GitHub Desktop | **File → Clone repository → GitHub.com tab**, pick `YOUR-USERNAME/codeverse-wall`, then **Clone**. If it asks *"How are you planning to use this fork?"*, choose **To contribute to the parent project**. |
| 3 | GitHub Desktop | **Current branch → New branch**, name it `add-YOUR-USERNAME`, then **Create branch**. |
| 4 | VS Code | **Repository → Open in Visual Studio Code**. Copy `students/_template.json`, paste it into the same folder, rename the copy to `students/YOUR-USERNAME.json` and fill in your details. Save. |
| 5 | GitHub Desktop | Write a summary such as `feat: add Asha's card`, then click **Commit to add-YOUR-USERNAME**. |
| 6 | GitHub Desktop | Click **Publish branch**. |
| 7 | GitHub Desktop | Click **Create Pull Request** (or **Preview Pull Request**). Your browser opens. Check that the base is the **original** repository's `main`, fill in the template and click **Create pull request**. |
| 8 | github.com | Watch the **checks**. Green ✓ means a reviewer can merge it. Red ✗? Click **Details**, read the message, fix the file, commit, push. The check runs again by itself. |

When your pull request is merged, your card appears on the wall within seconds. 🎉

### Your card

```json
{
  "name": "Asha Patil",
  "github": "asha-codes",
  "city": "Pune",
  "emoji": "🚀",
  "tagline": "2nd year CSE · learning web dev",
  "funFact": "I can solve a Rubik's cube in 2 minutes"
}
```

Rules the robot checks (`.github/scripts/validate_cards.py`):

- The file name is your GitHub username: `students/asha-codes.json`
- All six fields are filled in, and nothing else is added
- It is valid JSON: every line ends with a comma **except the last one**, and all text sits inside "double quotes"
- You only touch your own file

---

## Prefer the terminal? (Linux, or just for fun)

```bash
# 1. Fork on github.com first, then:
git clone https://github.com/YOUR-USERNAME/codeverse-wall.git
cd codeverse-wall
git switch -c add-YOUR-USERNAME

# 2. Create students/YOUR-USERNAME.json (copy the template), then:
git add students/YOUR-USERNAME.json
git commit -m "feat: add YOUR-NAME's card"
git push -u origin add-YOUR-USERNAME

# 3. On github.com, click "Compare & pull request".
```

## Keep your fork up to date (before your next pull request)

On **your fork** on github.com, click **Sync fork → Update branch**. Then in GitHub Desktop, switch to `main` and click **Fetch origin → Pull origin**.

## Stuck?

| You see | Do this |
|---|---|
| Red ✗ *"not valid JSON"* | Look at the line it names. Usually it's a missing comma, an extra comma after the last line, or a missing quote. |
| Red ✗ *"file name must match"* | Rename your file to exactly your GitHub username, plus `.json`. |
| *"Workflow awaiting approval"* | This is normal for first-time contributors. GitHub doesn't run a stranger's code automatically; your instructor approves it. |
| Pull request opened against your own fork | In GitHub Desktop: **Repository → Repository settings → Fork behavior → To contribute to the parent repository**. |
| *Open in Visual Studio Code* is missing | GitHub Desktop **Options/Settings → Integrations → External editor → Visual Studio Code**. |

Made with ☕ in a CODE-VERSE session. Want to see how the wall works? Read `index.html`. It's about 250 lines.
