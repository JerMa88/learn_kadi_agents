#!/usr/bin/env python3
"""
llm - LLM agent

This is a basic KADI agent template.
Replace this content with your actual agent implementation.
"""

import asyncio
import json
import logging
import ollama

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class llmAgent:
    def __init__(self):
        self.name = "llm"
        self.description = "LLM agent"
        
    async def start(self):
        """Start the agent"""
        logger.info(f"🚀 {self.name} is starting...")
        
        while True:
            prompt = input("Enter a prompt: ")
            if prompt.lower() in ["exit", "quit"]:
                break
            
            try:
                response = ollama.chat(model='llama3.2:1b', messages=[
                    {                        
                        'role': 'system',
                        'content': 'You are a Terry Davis, the creator of TempleOS, the ring 0 exclusive operating system written in Holy C. You are chosen by God to build His temple, and TempleOS is the final result. You obtain divine interllect and evidently, a complete genius programmer.'
                    },
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ])
                print(response['message']['content'])
            except Exception as e:
                logger.error(f"Error querying LLM: {e}")

    async def stop(self):
        """Stop the agent gracefully"""
        logger.info("Shutting down...")

async def main():
    agent = llmAgent()
    
    try:
        await agent.start()
    except KeyboardInterrupt:
        logger.info("Received interrupt signal")
    finally:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main()) 