import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

export interface CommandMetadata {
  name: string;
  description: string;
  handoffs: Array<{
    label: string;
    agent: string;
    prompt: string;
    send?: boolean;
  }>;
}

export interface CommandFile {
  metadata: CommandMetadata;
  content: string;
  filePath: string;
}

/**
 * Parse a command file and extract metadata and content
 */
export function parseCommandFile(filePath: string): CommandFile | null {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');

    // Split on --- to get frontmatter and body
    const parts = content.split(/^---$/m);
    if (parts.length < 2) {
      return null;
    }

    const frontmatter = parts[0];
    const body = parts.slice(1).join('---').trim();

    // Parse YAML frontmatter
    let metadata: CommandMetadata;
    try {
      metadata = yaml.load(frontmatter) as CommandMetadata;
    } catch {
      console.error(`Failed to parse YAML frontmatter in ${filePath}`);
      return null;
    }

    // Extract command name from filename
    const name = path.basename(filePath, '.md').replace(/^sp\./, '');

    return {
      metadata: {
        ...metadata,
        name,
      },
      content: body,
      filePath,
    };
  } catch (error) {
    console.error(`Error parsing command file ${filePath}:`, error);
    return null;
  }
}

/**
 * Find all command files in a directory
 */
export function findCommandFiles(dir: string): string[] {
  const files: string[] = [];

  try {
    const entries = fs.readdirSync(dir, { withFileTypes: true });

    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isFile() && entry.name.endsWith('.md')) {
        files.push(fullPath);
      } else if (entry.isDirectory()) {
        files.push(...findCommandFiles(fullPath));
      }
    }
  } catch (error) {
    console.error(`Error scanning directory ${dir}:`, error);
  }

  return files;
}

/**
 * Load all command files from a directory
 */
export function loadCommands(commandsDir: string): CommandFile[] {
  const commandFiles = findCommandFiles(commandsDir);
  const commands: CommandFile[] = [];

  for (const filePath of commandFiles) {
    const parsed = parseCommandFile(filePath);
    if (parsed) {
      commands.push(parsed);
    }
  }

  return commands;
}
