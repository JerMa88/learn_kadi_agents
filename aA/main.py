#!/usr/bin/env python3
"""
agentA - agent A

This is a basic KADI agent template.
Replace this content with your actual agent implementation.
"""

import asyncio
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class agentAAgent:
    def __init__(self):
        self.name = "agentA"
        self.description = "agent A"
        
    async def start(self):
        """Start the agent"""
        logger.info(f"🚀 {self.name} is starting...")
        
        # Your agent logic goes here
        logger.info("Hello, World!")
        logger.info("This is a KADI agent running in Python.")
        
        # Example: Keep the agent running
        while True:
            logger.info("Agent is alive...")
            await asyncio.sleep(30)
    
    async def stop(self):
        """Stop the agent gracefully"""
        logger.info("Shutting down...")

async def main():
    agent = agentAAgent()
    
    try:
        await agent.start()
    except KeyboardInterrupt:
        logger.info("Received interrupt signal")
    finally:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main()) 