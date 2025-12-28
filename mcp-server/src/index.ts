import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListResourcesRequestSchema,
  ListToolsRequestSchema,
  ReadResourceRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import { loadCommands, type CommandFile } from './parser.js';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = path.resolve(__dirname, '../..');
const COMMANDS_DIR = path.join(PROJECT_ROOT, '.claude/commands');

// Create MCP server
const server = new Server(
  {
    name: 'speckitplus-commands',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
      resources: {},
    },
  }
);

// Store loaded commands
let commands: CommandFile[] = [];

/**
 * Load commands on startup
 */
function initializeCommands() {
  commands = loadCommands(COMMANDS_DIR);
  console.error(`Loaded ${commands.length} SpecKitPlus commands`);

  for (const cmd of commands) {
    console.error(`  - /sp.${cmd.metadata.name}: ${cmd.metadata.description}`);
  }
}

/**
 * Substitute $ARGUMENTS in content with provided args
 */
function substituteArguments(content: string, args: string): string {
  if (!args) {
    return content;
  }

  // Replace $ARGUMENTS placeholder with the actual arguments
  return content.replace(/\$ARGUMENTS/g, args.trim());
}

/**
 * Get URI for a command resource
 */
function getCommandUri(commandName: string): string {
  return `speckitplus://commands/${commandName}`;
}

// Handle list resources request - list all commands
server.setRequestHandler(ListResourcesRequestSchema, async () => {
  return {
    resources: commands.map((cmd) => ({
      uri: getCommandUri(cmd.metadata.name),
      name: `/sp.${cmd.metadata.name}`,
      description: cmd.metadata.description,
      mimeType: 'text/markdown',
    })),
  };
});

// Handle read resource request - get command content
server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
  const uri = request.params.uri;

  // Parse URI to get command name
  const match = uri.match(/^speckitplus:\/\/commands\/(.+)$/);
  if (!match) {
    throw new Error(`Invalid resource URI: ${uri}`);
  }

  const commandName = match[1];
  const command = commands.find((c) => c.metadata.name === commandName);

  if (!command) {
    throw new Error(`Command not found: ${commandName}`);
  }

  return {
    contents: [
      {
        uri,
        mimeType: 'text/markdown',
        text: command.content,
      },
    ],
  };
});

// Handle list tools request - expose commands as tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: commands.map((cmd) => ({
      name: `sp.${cmd.metadata.name}`,
      description: cmd.metadata.description,
      inputSchema: {
        type: 'object',
        properties: {
          arguments: {
            type: 'string',
            description: 'Arguments to pass to the command (will replace $ARGUMENTS placeholder)',
          },
        },
        required: ['arguments'],
      },
    })),
  };
});

// Handle tool calls - execute commands with arguments
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const toolName = request.params.name;
  const args = request.params.arguments as { arguments?: string };

  if (!toolName.startsWith('sp.')) {
    throw new Error(`Unknown tool: ${toolName}`);
  }

  const commandName = toolName.replace(/^sp\./, '');
  const command = commands.find((c) => c.metadata.name === commandName);

  if (!command) {
    throw new Error(`Command not found: ${commandName}`);
  }

  const argumentText = args.arguments || '';
  const processedContent = substituteArguments(command.content, argumentText);

  return {
    content: [
      {
        type: 'text',
        text: processedContent,
      },
    ],
  };
});

// Main entry point
async function main() {
  initializeCommands();

  const transport = new StdioServerTransport();
  await server.connect(transport);

  console.error('SpecKitPlus MCP Server running on stdio');
}

main().catch((error) => {
  console.error('Server error:', error);
  process.exit(1);
});
