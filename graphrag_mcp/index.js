#!/usr/bin/env node

/**
 * graphrag_mcp - A graphrag agent with code from github.com:rileylemm/graphrag_mcp.git
 *
 * This is a basic KADI agent template.
 * Replace this content with your actual agent implementation.
 */

console.log("🚀 graphrag_mcp is starting...");

// Your agent logic goes here
function main() {
  console.log("Hello, World!");
  console.log(
    "This is a KADI agent running in JavaScript. Press Ctrl+C to stop.",
  );

  // Example: Keep the process running
  setInterval(() => {
    console.log("Agent is alive...");
  }, 30000);
}

// Start the agent
main();

// Handle graceful shutdown
process.on("SIGINT", () => {
  console.log("\nShutting down...");
  process.exit(0);
});
