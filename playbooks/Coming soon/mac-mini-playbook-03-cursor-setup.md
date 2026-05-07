# Playbook 3: Cursor Setup
### For Women Building AI-Native Businesses

**Series:** Sage AI Studios — Mac Mini AI Powerhouse Setup
**Level:** Beginner-friendly
**Playbook:** 3 of 7

---

## Before You Begin

**⏱ Time Required: 20 minutes**
**Interruption Risk: Low — each step stands on its own**

*This playbook installs Cursor — a code editor with AI built directly into it. By the end, you'll have a visual, point-and-click environment where Claude can help you write, edit, and understand code alongside you.*

**Who needs this playbook:**
- Anyone who wants a visual interface for working with code (vs. the terminal)
- Anyone building projects that involve editing files, reading codebases, or writing scripts
- If you're comfortable with Claude Code in the terminal and never want a visual editor, you can skip this — but most people find they use both

**What to have nearby:**
- [ ] Playbook 2 complete — Claude Code set up on your Mac Mini
- [ ] Your GitHub username and password — you'll use them to sign in to Cursor
- [ ] 20 minutes of focused time — the install is quick, orientation takes the rest

**Not a good time?** Safe stopping points: after Step 2 (Cursor installed), after Step 4 (signed in). Don't stop mid-step.

---

## Cursor vs. Claude Code: What's the Difference?

You already have Claude Code installed from Playbook 2. Why install Cursor too?

| | Claude Code (Terminal) | Cursor (Visual Editor) |
|---|---|---|
| **Interface** | Terminal — text commands | Visual — like a word processor for code |
| **Best for** | Autonomous tasks, running things, file operations | Reading code, editing files, building alongside AI |
| **AI access** | Claude (Anthropic) | Claude, GPT-4o, and others — your choice |
| **Learning curve** | Steeper — terminal fluency helps | Gentler — if you've used Word or Notion, you can use this |
| **When to use** | "Do this for me" | "Help me understand this / do this with me" |

Most people end up using both. Claude Code for autonomous work. Cursor for hands-on work where you want to see what's happening.

---

## Step 1: Create a Cursor Account

Before downloading, create a free account at **cursor.com**.

1. Click **"Sign Up"**
2. Sign up with your **GitHub account** — this links Cursor to your repos automatically. Or use your email if you prefer.
3. Confirm your account — check your email for a verification link if prompted

> **Cursor has a free tier and a Pro tier (~$20/month).** The free tier includes a limited number of AI requests per month — enough to get started and see if it fits your workflow. Start free. Upgrade when you're hitting limits regularly.

---

## Step 2: Download and Install Cursor

1. Go to **cursor.com**
2. Click **"Download for Mac"**
3. Open your **Downloads folder** — click the Finder icon in your dock → Downloads in the left sidebar
4. Double-click the Cursor file you just downloaded
5. An installer window opens. **Drag the Cursor icon into the Applications folder** — same process as Chrome and Claude
6. **Don't close the installer window until the drag is complete**
7. Open **Spotlight** — press **Command + Space** — type **Cursor** — press **Enter**
8. macOS will ask **"Are you sure you want to open this?"** → Click **Open**. This is standard Mac security for apps downloaded outside the App Store. Not a warning — just a check.

Cursor opens. You'll see a welcome screen.

---

## Step 3: Import Settings (or Start Fresh)

Cursor is built on VS Code — the most widely used code editor in the world. If you've used VS Code before, you can import your settings, extensions, and keyboard shortcuts in one click.

**First time using any code editor?**
→ Choose **"Start Fresh."** No settings to import. Cursor's defaults are good.

**Used VS Code before?**
→ Choose **"Import from VS Code."** Your familiar setup carries over automatically.

> **What's VS Code?** Visual Studio Code is Microsoft's free code editor — the foundation Cursor is built on. Same interface, same keyboard shortcuts, same extension library — Cursor just adds AI on top. If you've never heard of it, don't worry. Cursor will feel like home soon enough.

---

## Step 4: Sign In to Cursor

1. Click **"Sign In"** on the welcome screen
2. A browser window opens — sign in with the GitHub account (or email) you used in Step 1
3. Click **"Authorize"** when prompted
4. Switch back to Cursor — you're signed in

You'll see your plan level in the bottom left corner of the app. Free tier users see a monthly request counter. Ignore it for now.

---

## Step 5: Set Claude as Your Default Model

Cursor supports several AI models. Here's what matters for this setup:

1. Click the **gear icon** in the bottom left corner → **Cursor Settings**
2. Find the **Models** section
3. Look for **Claude Sonnet** in the list and make sure it's enabled
4. In the model selector at the top of any chat panel, choose **claude-sonnet** as your default

> **Why Claude in Cursor too?** Consistency. You're already using Claude with Claude Code in the terminal. Using the same model across tools means you're building intuition for how one AI thinks — rather than learning multiple AI personalities at once. You can always switch models mid-session if you want a second opinion.

---

## Step 6: Open Your First Project

Cursor works with folders. Open a folder on your Mac Mini and that folder becomes your project.

**Starting from scratch:**
1. Open **Finder** → go to **Documents** → right-click → **New Folder** → name it `my-first-project`
2. In Cursor, go to **File → Open Folder** → navigate to that folder → click **Open**

You'll see your folder contents in the left sidebar. If the folder is empty, the sidebar is empty. That's fine — you'll add files as you work.

> **macOS may ask Cursor to access your Documents or Desktop folder.** Click **"Allow."** Cursor needs access to your files to help you work with them.

---

## Step 7: Tour the Interface

Cursor has four main areas. Take two minutes to orient yourself before using it.

**Left sidebar — your files**
Everything in your project folder. Click any file to open it. This is your project explorer.

**Main editor — center**
Where files open and where you edit. Click anywhere, type, change things. Works like a word processor.

**AI Chat panel — right side**
Where you talk to Claude. Press **Command + L** to open it. Ask questions, paste error messages, request explanations — Claude sees your project context.

**Bottom bar**
Status information: which git branch you're on, any errors or warnings. You'll refer to this more as your projects grow.

---

## Step 8: Learn the Three AI Gestures

You don't need to learn everything about Cursor to use it well. These three keyboard shortcuts cover 90% of what you'll reach for:

**Command + L — Open Chat**
Opens the AI chat panel. Use this to:
- Ask questions about code you're reading
- Get explanations of error messages
- Have Claude draft something new that you then paste in yourself

**Command + K — Inline Edit**
Click anywhere in an open file, press Command + K, and a small prompt bar appears inline. Type what you want changed. Claude edits that exact spot. Use this for:
- Fixing a specific line
- Rewriting a section
- Adding something at a precise location

**Command + I — Composer (Agent Mode)**
Opens Composer — Cursor's multi-file agent. Like Claude Code in the terminal, but visual. Use this for:
- Changes that span multiple files
- Building something new from scratch
- Tasks where you want Claude to plan and execute, with you reviewing each step

> **Not sure which to use?** Start with Command + L. It's the most conversational — ask, refine, and only apply what you agree with. Command + K and Command + I are for when you're ready to make changes directly.

---

## Step 9: Try It

Open the chat panel with **Command + L**.

Type:

> *"I'm new to Cursor. What's in this project folder, and what would be a good first thing to build or add?"*

Claude will look at your folder contents and respond. If the folder is empty, it'll tell you and suggest what to create first.

This is the key difference between Cursor and a regular chat window: Claude can see your project. It's not answering in the abstract — it's looking at what you actually have.

---

## ✅ What You Just Did

**Win 1 — Cursor is installed.**
You have a visual, AI-powered code editor running on your Mac Mini — no terminal required.

**Win 2 — Claude is your default model.**
Consistent AI across your tools. Claude Code in the terminal, Claude in Cursor. One mental model for how AI thinks and works.

**Win 3 — You know the three gestures.**
Command + L, Command + K, Command + I. That's the whole toolkit for daily use.

**Win 4 — You opened a real project.**
Cursor is connected to your files. The AI sees what you're working with — not just what you tell it.

*You now have two AI-powered environments. The terminal for autonomous work. The editor for hands-on work. Both are yours.*

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
