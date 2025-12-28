# SpecKitPlus MCP Server

This MCP (Model Context Protocol) server exposes [SpecKitPlus](https://github.com/anthropics/spec-kit-plus) command files as prompts and tools for Claude Code.

## Features

- **Auto-discovers** all `.claude/commands/*.md` files
- **Exposes commands** as MCP tools (e.g., `sp.specify`, `sp.plan`)
- **Argument substitution** - `$ARGUMENTS` in command files gets replaced with user input
- **Resource support** - Commands are also available as read-only resources

## Available Commands

| Command | Description |
|---------|-------------|
| `sp.adr` | Create an Architecture Decision Record |
| `sp.analyze` | Analyze codebase or feature |
| `sp.checklist` | Create a checklist for a domain |
| `sp.clarify` | Clarify specification requirements |
| `sp.constitution` | Create or update project constitution |
| `sp.git.commit_pr` | Create git commits and PRs |
| `sp.implement` | Execute implementation workflow |
| `sp.phr` | Create Prompt History Records |
| `sp.plan` | Execute implementation planning workflow |
| `sp.reverse-engineer` | Reverse engineer code into specs |
| `sp.specify` | Create feature specifications |
| `sp.tasks` | Break plan into testable tasks |
| `sp.taskstoissues` | Convert tasks to GitHub issues |

## Installation

```bash
cd mcp-server
npm install
npm run build
```

## Usage with Claude Code

### Option 1: Using MCP Config File

Add to your `claude_desktop_config.json` or MCP settings:

```json
{
  "mcpServers": {
    "speckitplus": {
      "command": "node",
      "args": ["/path/to/mcp-server/dist/index.js"]
    }
  }
}
```

### Option 2: Using --mcp-cli flag

```bash
claude --mcp-cli "node /path/to/mcp-server/dist/index.js"
```

## Usage

Once connected, you can call the commands directly:

```
You: Use sp.specify to create a feature for user authentication

Claude: (executes sp.specify tool with "user authentication" as arguments)
```

Or use them as resources:

```
You: Read the sp.plan command to understand the planning workflow

Claude: (returns sp.plan content as a resource)
```

## Development

```bash
# Run in development mode with hot reload
npm run dev

# Build for production
npm run build

# Type check
npx tsc --noEmit
```

## Project Structure

```
mcp-server/
├── src/
│   ├── index.ts      # Main server entry point
│   └── parser.ts     # Command file parser
├── package.json
├── tsconfig.json
└── claude_desktop_config.json
```

## How It Works

1. **Discovery**: On startup, the server scans `.claude/commands/` for `.md` files
2. **Parsing**: Each file is parsed to extract YAML frontmatter (metadata) and markdown content
3. **Exposure**: Commands are exposed as:
   - **Tools**: Can be called with arguments via `tool.use()`
   - **Resources**: Can be read for reference
4. **Substitution**: When called as a tool, `$ARGUMENTS` in the content is replaced with the provided arguments
