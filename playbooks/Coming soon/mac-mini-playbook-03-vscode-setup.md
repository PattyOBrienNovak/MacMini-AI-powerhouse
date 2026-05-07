# Playbook 3: VS Code Setup
### For Women Building AI-Native Businesses

**Series:** Sage AI Studios — Mac Mini AI Powerhouse Setup
**Level:** Beginner-friendly
**Playbook:** 3 of 7

---

## Before You Begin

**⏱ Time Required: 25 minutes**
**Interruption Risk: Low — each step stands on its own**

*This playbook installs VS Code — a visual code editor with AI built in. By the end, you'll have a point-and-click environment where you can browse, edit, and build with AI alongside you.*

**Who needs this playbook:**
- Anyone who wants a visual interface for working with code (vs. the terminal)
- Anyone building projects that involve editing files, reading codebases, or writing scripts
- If you're comfortable with Claude Code in the terminal and never want a visual editor, you can skip this — but most people find they use both

**What to have nearby:**
- [ ] Playbook 2 complete — Claude Code set up on your Mac Mini
- [ ] Your GitHub account login — you'll use it to sign in and clone repos
- [ ] 25 minutes of focused time — the install is quick, orientation takes the rest

**Not a good time?** Safe stopping points: after Step 2 (VS Code installed), after Step 4 (GitHub Copilot installed). Don't stop mid-step.

---

## Why VS Code — and What About Cursor?

VS Code (Visual Studio Code) is Microsoft's free code editor — the most widely used in the world. It's stable, well-documented, and has a large ecosystem of extensions. We're using it as the foundation for this playbook.

**Cursor** is a popular AI code editor built on top of VS Code. It's worth knowing about, and some people prefer it — but as of mid-2026, Cursor has been changing its interface frequently enough that step-by-step instructions go out of date quickly. We've written this playbook for VS Code because the experience is predictable and consistent. If you want to try Cursor later, the concepts from this playbook transfer directly — it's the same underlying editor.

---

## VS Code vs. Claude Code: What's the Difference?

You already have Claude Code installed from Playbook 2. Why install VS Code too?

| | Claude Code (Terminal) | VS Code (Visual Editor) |
|---|---|---|
| **Interface** | Terminal — text commands | Visual — like a word processor for code |
| **Best for** | Autonomous tasks, running things, file operations | Reading code, editing files, building alongside AI |
| **AI access** | Claude (Anthropic) | GitHub Copilot — uses Claude Sonnet on the free plan |
| **Learning curve** | Steeper — terminal fluency helps | Gentler — if you've used Word or Notion, you can use this |
| **When to use** | "Do this for me" | "Help me understand this / do this with me" |

Most people end up using both. Claude Code for autonomous work. VS Code for hands-on work where you want to see what's happening.

---

## Step 1: Download and Install VS Code

1. In Chrome, go to **code.visualstudio.com**
2. Click the big **"Download for Mac"** button — it detects your Mac automatically
3. Open your **Downloads folder** — click the Finder icon in your dock → Downloads in the left sidebar
4. Double-click the VS Code file you just downloaded — it unzips automatically
5. **Drag the VS Code icon into your Applications folder** — open a second Finder window (File → New Finder Window), click Applications in the left sidebar, then drag the icon across
6. **Don't close either window until the drag is complete**
7. Open **Spotlight** — press **Command + Space** — type **Visual Studio Code** — press **Enter**
8. macOS will ask **"Are you sure you want to open this?"** → Click **Open**

VS Code opens. You'll see a Welcome tab.

---

## Step 2: Dismiss the Welcome Tab and Orient

VS Code opens with a Welcome tab showing tips and setup options. You can close it — click the **X** on the Welcome tab at the top of the screen.

You're now looking at the empty editor. Don't worry that it looks plain — it fills up when you open a project.

> **VS Code may ask to collect usage data.** Click **"No, don't send"** — this machine shares data on your terms.

---

## Step 3: Sign In with GitHub

Signing in with GitHub does two things: it lets VS Code sync your settings across machines, and it sets up the GitHub connection you'll need for Copilot and for cloning repos.

1. Click the **person icon** in the bottom left corner of VS Code
2. Click **"Sign in with GitHub to use GitHub Copilot"** — or look for **"Sign in"** if the wording differs
3. A browser window opens — sign in with your GitHub account and click **"Authorize"**
4. Switch back to VS Code — you're signed in

> **macOS may ask: "Visual Studio Code wants to open this URL."** Click **"Open."** This is VS Code completing the sign-in handoff from your browser. It's safe.

---

## Step 4: Install GitHub Copilot

GitHub Copilot is the AI layer inside VS Code. The free plan gives you a meaningful number of AI interactions per month and uses **Claude Sonnet** as one of its available models — keeping you in the same AI ecosystem you're building throughout this series.

1. Click the **Extensions icon** in the left sidebar — it looks like four squares, with one slightly separated
2. In the search bar at the top of the Extensions panel, type **GitHub Copilot**
3. Click **Install** on the first result — "GitHub Copilot" by GitHub
4. When it finishes, VS Code may prompt you to sign in or activate — follow the prompts using your GitHub account

> **You'll be asked to choose a Copilot plan.** Select the **Free plan** — it's enough to get started. You can upgrade later once you know how much you use it.

---

## Step 5: Set Claude Sonnet as Your Copilot Model

By default, Copilot may use a different AI model. Here's how to switch to Claude Sonnet:

1. Click the **Copilot icon** in the bottom right corner of VS Code — it looks like a small Copilot logo
2. Click **"Open Copilot Chat"** — the chat panel opens on the right side
3. At the top of the chat panel, find the **model selector** — it shows the currently active model name
4. Click it and choose **Claude Sonnet** from the list

> **Don't see Claude Sonnet?** It may be listed as "claude-sonnet" or similar. If it's not in the list yet, GPT-4o is a solid alternative while you wait for it to appear — Copilot's model options expand over time.

---

## Step 6: Open Your First Project

VS Code works with folders. Open a folder on your Mac Mini and that folder becomes your project. Choose the option that fits where you are:

**If you have a GitHub repo you want to work in:**
1. Go to your repo on **github.com** and click the green **"Code"** button
2. Make sure **HTTPS** is selected, then click the **copy icon** next to the URL — it'll look like `https://github.com/yourusername/your-repo-name.git`
3. In VS Code, click the **Source Control icon** in the left sidebar — it looks like three circles connected by lines
4. Click **"Clone Repository"**
5. A URL bar appears at the top of the screen — paste your GitHub URL and press **Enter**
6. VS Code asks where to save it — choose your **Documents** folder, then click **"Select as Repository Destination"**
7. When it finishes, VS Code asks **"Would you like to open the cloned repository?"** → Click **Open**

> **VS Code may ask you to sign in to GitHub** during the clone step if you haven't already. Follow the prompts — it's the same GitHub account you used in Step 3.

**Starting from scratch:**
1. Open **Finder** → go to **Documents** → right-click → **New Folder** → name it `my-first-project`
2. In VS Code, go to **File → Open Folder** → navigate to that folder → click **Open**

You'll see your folder contents in the left sidebar. If the folder is empty, the sidebar is empty. That's fine — you'll add files as you work.

> **macOS may ask VS Code to access your Documents or Desktop folder.** Click **"Allow."**

---

## Step 7: Tour the Interface

VS Code has five main areas. Take two minutes to orient yourself before using it.

**Left sidebar — your navigation**
Five icons stacked vertically. From top to bottom: Files, Search, Source Control (Git), Extensions, and at the bottom — your account and settings. Click any icon to open that panel.

**Explorer panel — your files**
Opens when you click the top Files icon. Shows everything in your project folder. Click any file to open it.

**Main editor — center**
Where files open and where you edit. Click anywhere, type, change things. Open multiple files as tabs across the top.

**Copilot Chat panel — right side**
Where you talk to the AI. Click the Copilot icon in the sidebar or bottom right corner to open it. Ask questions, paste errors, request explanations — Copilot sees your project context.

**Bottom bar**
Status information: which git branch you're on, any errors or warnings, the Copilot status. You'll refer to this more as your projects grow.

---

## Step 8: Learn the Three AI Gestures

These three interactions cover 90% of how you'll use AI in VS Code day-to-day:

**Copilot Chat — ask and explore**
Click the **Copilot icon** in the sidebar to open the chat panel. Use this to:
- Ask questions about code you're reading
- Get explanations of error messages
- Have AI draft something new that you review and apply yourself

**Inline Completions — AI as you type**
Just start typing in any file. Copilot watches what you're writing and suggests completions in light gray text. Press **Tab** to accept a suggestion. Press **Escape** to dismiss it. No button to click — it's always on in the background.

**Copilot Edits — make changes across files**
In the Copilot Chat panel, click **"Edits"** at the top to switch to Edits mode. Describe what you want changed. Copilot shows you a diff — exactly what it plans to change — and waits for your approval before touching anything. Use this for:
- Changes that span multiple files
- Refactoring or restructuring a project
- Anything where you want to review before it applies

> **Not sure which to use?** Start with Chat. It's the most conversational — ask, refine, and only apply what you agree with. Inline completions and Edits are for when you're ready to move faster.

---

## Step 9: Try It

Make sure the Copilot Chat panel is open. If it's not, click the Copilot icon in the left sidebar.

Before you type anything, check the model selector at the top of the chat panel and confirm **Claude Sonnet** is selected.

Now type:

> *"I'm new to VS Code. What's in this project folder, and what would be a good first thing to build or add?"*

Copilot will look at your folder contents and respond. If the folder is empty, it'll tell you and suggest what to create first.

This is the key difference between VS Code with Copilot and a regular chat window: the AI can see your project. It's not answering in the abstract — it's looking at what you actually have.

---

## Step 10: Eject Your Installers

When you downloaded VS Code, macOS mounted it as a disk image — a virtual drive that may appear on your desktop or in your Finder sidebar. Now that VS Code is installed, you can eject it.

Look on your **desktop** or in the **Finder sidebar** for a drive icon labeled something like **"VSCode"** or **"Visual Studio Code."**

To eject it:
- **Right-click the icon** and choose **"Eject"**
- Or drag it to the **Trash** — the Trash icon turns into an eject arrow when you hover a disk image over it

> **This is just cleanup — VS Code is already installed in your Applications folder.** Ejecting the disk image doesn't uninstall anything. Think of it like throwing away the box after you've assembled the furniture.

If you don't see any drive icon on your desktop or in the Finder sidebar, you're already clean.

---

## ✅ What You Just Did

**Win 1 — VS Code is installed.**
You have a stable, widely-used visual code editor running on your Mac Mini — no terminal required for day-to-day use.

**Win 2 — GitHub Copilot is live with Claude Sonnet.**
AI assistance is built directly into your editor, using the same Claude model you work with everywhere else in this series.

**Win 3 — You know the three AI interactions.**
Chat, inline completions, and Edits. That's the whole toolkit for daily use.

**Win 4 — You opened a real project.**
VS Code is connected to your files. The AI sees what you're working with — not just what you tell it.

*You now have two AI-powered environments. Claude Code in the terminal for autonomous work. VS Code for hands-on work. Both are yours.*

---

## What Comes Next

**Playbook 4: Jupyter Notebook Setup**
Install Jupyter locally — required for the Anthropic certification course and AI development work.

*Time Required: 20 minutes*

---

> **Remember:** You don't have to do Playbook 4 today. Each playbook is its own complete win. Come back when you have another focused window.

---

*Part of the Sage AI Studios Mac Mini AI Powerhouse Setup Series*
*Created with Claude Code — May 2026*
