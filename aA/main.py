#!/usr/bin/env python3
"""
agentA - agent A

Just a normal agent that calls the ollama service hosted at the llm agent.
"""

import asyncio
import json
import logging
from datetime import datetime
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def call_llm_agent(prompt):
    """
    Call the LLM agent with the given prompt.
    This is a placeholder function that simulates an LLM call.
    """
    logger.info(f"Calling LLM agent with prompt: {prompt}")

    try:
        response = requests.post(
            'http://localhost:8081/query',
            json={"prompt": prompt}
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response from LLM agent")
    except requests.RequestException as e:
        logger.error(f"Error calling LLM agent: {e}")
        return "Error calling LLM agent"

class agentAAgent:
    def __init__(self):
        self.name = "agentA"
        self.description = "agent A"
        
    async def start(self):
        """Start the agent"""
        logger.info(f"🚀 {self.name} is starting...")
        
        while True:
            prompt = input("Enter a prompt for the LLM agent: ")
            if not prompt: 
                logger.error("No prompt provided. Please enter a valid prompt.")
            else:
                response = call_llm_agent(prompt)
                logger.info(f"Response from LLM agent: \n{response}")

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