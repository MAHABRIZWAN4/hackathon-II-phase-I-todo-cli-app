# hackathon-II-phase-I-todo-cli-app

# Agentic Development Setup Guide: Phase I with SpecKit Plus and Claude 

## What is WSL 2?
Windows Subsystem for Linux (WSL 2) provides a real Linux environment on Windows. It is essential for Python development and Claude Code workflows.

### STEP 1: Install WSL 2 Globally

```bash
# Install WSL
wsl --install

# Set WSL 2 as default
wsl --set-default-version 2

# Install Ubuntu
wsl --install -d Ubuntu-22.04

# Verify installation
wsl --list --verbose
```

### STEP 2: Initialize SpecKit Plus in a Folder

**Step A:** Create a simple folder named `Hackathon-II-Todo`.

**Step B:** Open the folder in Ubuntu:

```bash
cd /mnt/c/Users/YourName/Documents/Hackathon-II-Todo
```

**Note:** Windows drives are mounted under `/mnt/` in Ubuntu:  
- C:\ → /mnt/c/  
- D:\ → /mnt/d/

**Verify current path:**

```bash
pwd
```

**Step C:** Since Ubuntu is a separate Linux system, previous installations are not carried over. You need to install everything anew:

- No uv installed  
- No node installed  
- No python installed  
- No npm installed  
- No SpecKit Plus installed  

**Install UV in Ubuntu:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
uv --version  # Expected: uv 0.9.18 (or similar version)
```

**Install SpecKit Plus globally in Linux:**

```bash
uv tool install specifyplus
specifyplus --version
```

**Initialize SpecKit Plus in the folder:**

```bash
specifyplus init phase-I
```

When prompted, select the Claude agent option.  
Then:

```bash
cd phase-I
```

### STEP 3: Free Claude Code Setup with BonsAI (in Ubuntu)

For Hackathon-II, we need to use cloud agents and skills, which require Claude. Paid plans offer these, but using BonsAI CLI with Claude makes creating agents and skills easier and more accessible.

**Step A: Install Node.js and npm**

Run these commands in the Ubuntu terminal:

```bash
# Install Node Version Manager (nvm)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

# Reload terminal
source ~/.bashrc

# Install Node v20
nvm install 20
nvm use 20

# Wait for installation to complete, then verify:
node -v
npm -v
```

**Step B: Install BonsAI CLI**

```bash
# Install globally
npm install -g @bonsai-ai/cli

# Check version
bonsai --version

# Login
bonsai login

# Start Claude with BonsAI
bonsai start claude
```

**Step C: Resolve Common Issue**

After setup, when running `bonsai start claude`, typing commands like `/sp.` may not show suggestions (e.g., `/sp.constitution`, `/sp.specify`, etc.). To fix this, connect an MCP server. The fun part: we won't fix it manually — we'll use prompts to guide the process.

**Issue Resolved: What Did the MCP Server Do and Why Is It Important?**

- **What it did:** Converted Markdown files in the `.claude/commands/` folder (e.g., `sp.constitution.md`, `sp.specify.md`) into prompts for Claude Code. Now, typing `/sp.constitution` automatically provides the file content as instructions to Claude.
- **Why important:** Without MCP, you'd manually copy-paste specifications every time. With MCP, type one command (e.g., `/sp.specify`) and Claude instantly understands what to do — this automation enables true Spec-Driven Development.
- **Real power:** Claude Code is now directly connected to project specs. When you run `/sp.tasks`, Claude automatically references previous specs (constitution, specify, plan) to generate tasks — this is the foundation for "Agent Skills" and "Reusable Intelligence"! 🚀

### STEP 4: Start the Project

**✅ SETUP & INFRASTRUCTURE (COMPLETED)**

- WSL 2 installed ✔  
- Ubuntu setup ✔  
- UV installed ✔  
- SpecKit Plus installed ✔  
- Node.js v20 installed ✔  
- BonsAI CLI installed ✔  
- Claude Code started ✔  
- Phase-I project initialized (`specifyplus init phase-I`) ✔  
- MCP Server setup (`.claude/commands/` prompts available) ✔  

**📝 SPEC-DRIVEN DEVELOPMENT CYCLE (IN PROGRESS)**

**Step 1: Constitution (Foundation) 🏗️**  
Use `/sp.constitution` to create `constitution.md`.  
Define: Project purpose, tech stack, principles, constraints.  
Review and finalize.

**Step 2: Specify (WHAT - Requirements) 📋**  
Use `/sp.specify` to define requirements.  
Example features for a Todo app:  
- Feature 1: Add Task (title, description)  
- Feature 2: Delete Task (by ID)  
- Feature 3: Update Task (modify details)  
- Feature 4: View Task List (with status)  
- Feature 5: Mark Complete/Incomplete  

Define acceptance criteria for each feature.  
Write user journeys.

**Step 3: Plan (HOW - Architecture) 🏛️**  
Use `/sp.plan` to create a technical plan.  
Define: Classes, data structures, functions.  
Component breakdown: TodoManager, Task model, CLI interface.  
Data flow diagram.

**Step 4: Tasks (BREAKDOWN) 📊**  
Use `/sp.tasks` to create atomic tasks.  
Assign Task IDs (T-001, T-002, etc.).  
Link tasks to spec sections.  
Set priority order.

**Step 5: Implement (CODE GENERATION) 💻**  
Use `/sp.implement` to generate code.  
Implement task by task.  
Test after each feature.  
Perform code review (check compliance with constitution).

If we use all these commands with professional prompts,  
**Alhamdulillah**, the Phase I Todo CLI app will be fully completed!

**Happy Agentic Development Everyone!** 🚀🤖
