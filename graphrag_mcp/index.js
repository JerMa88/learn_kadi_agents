#!/usr/bin/env node

/**
 * graphrag_mcp - A graphrag agent that integrates with Python abilities
 */

import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { existsSync } from 'fs';

// Configure paths
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ABILITIES_PATH = join(__dirname, 'abilities', 'graphrag_mcp', '1.0.0');
const VENV_PATH = join(ABILITIES_PATH, '.venv');
const PYTHON_PATH = join(VENV_PATH, 'bin', 'python');  // Use venv Python directly
const SERVER_PATH = join(ABILITIES_PATH, 'server.py');

// Add debug logging
console.log('VENV_PATH:', VENV_PATH);
console.log('PYTHON_PATH:', PYTHON_PATH);
console.log('SERVER_PATH:', SERVER_PATH);

class GraphragAgent {
  constructor() {
    this.name = 'graphrag_mcp';
    this.pythonProcess = null;
  }

  async start() {
    console.log(`🚀 ${this.name} is starting...`);
    
    try {
      // Verify paths exist
      if (!existsSync(PYTHON_PATH)) {
        throw new Error(`Python not found at: ${PYTHON_PATH}`);
      }
      if (!existsSync(SERVER_PATH)) {
        throw new Error(`Server script not found at: ${SERVER_PATH}`);
      }

      // Get the current Python path from the virtual environment
      const pythonPath = join(VENV_PATH, 'lib', 'python3.12', 'site-packages');
      
      // Start the Python server with proper environment
      this.pythonProcess = spawn(PYTHON_PATH, [SERVER_PATH], {
        cwd: ABILITIES_PATH,
        stdio: 'pipe',
        env: { 
          ...process.env,
          PYTHONUNBUFFERED: '1',
          VIRTUAL_ENV: VENV_PATH,
          PATH: `${join(VENV_PATH, 'bin')}:${process.env.PATH}`,
          PYTHONPATH: `${pythonPath}:${process.env.PYTHONPATH || ''}`
        }
      });

      // Handle Python process output
      this.pythonProcess.stdout.on('data', (data) => {
        console.log(`Python output: ${data}`);
      });

      this.pythonProcess.stderr.on('data', (data) => {
        console.error(`Python error: ${data}`);
      });

      // Keep the Node.js process running
      setInterval(() => {
        console.log("Agent is alive...");
      }, 30000);

    } catch (error) {
      console.error('Failed to start Python process:', error);
      process.exit(1);
    }
  }

  stop() {
    console.log("\nShutting down...");
    if (this.pythonProcess) {
      this.pythonProcess.kill();
    }
    process.exit(0);
  }
}

// Create and start the agent
const agent = new GraphragAgent();
agent.start();

// Handle graceful shutdown
process.on('SIGINT', () => {
  agent.stop();
});
