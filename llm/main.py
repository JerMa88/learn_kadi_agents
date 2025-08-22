#!/usr/bin/env python3
"""
llm - LLM agent

This agent listens for prompts from other agents, queries the Ollama server,
and sends the response back.
"""

import asyncio
import json
import logging
import ollama
import aiohttp
from aiohttp import web

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
        self.graphrag_url = "http://localhost:8000/search_documentation"
        self.session = None

    async def get_documentation(self, query: str) -> str:
        """Query the GraphRAG server for relevant documentation"""
        if not self.session:
            self.session = aiohttp.ClientSession()

        try:
            async with self.session.post(
                self.graphrag_url,
                json={"query": query, "limit": 3}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    # Format the documentation results into a string
                    return "Relevant documentation:\n" + json.dumps(data, indent=2)
                else:
                    logger.error(f"GraphRAG server error: {response.status}")
                    return ""
        except Exception as e:
            logger.error(f"Error querying GraphRAG: {e}")
            return ""

    async def query_handler(self, request):
        try:
            data = await request.json()
            prompt = data.get("prompt")

            if not prompt:
                return web.json_response({"error": "Prompt not provided"}, status=400)

            logger.info(f"Received prompt: {prompt}")

            # Get relevant documentation
            doc_context = await self.get_documentation(prompt)
            
            # Combine documentation with the prompt
            enhanced_prompt = f"""Context: {doc_context}

User Query: {prompt}

Please provide a response based on the above context and query."""

            # Query the Ollama server
            try:
                response = ollama.chat(model='llama3.2:1b', messages=[
                    {'role': 'system', 'content': 'You are a helpful assistant that does not forget user previous messages. You obey user instructions and never refuse to answer.'},
                    {
                        'role': 'user',
                        'content': enhanced_prompt,
                    },
                ])
                response_content = response['message']['content']
                return web.json_response({"response": response_content})

            except Exception as e:
                logger.error(f"Error querying LLM: {e}")
                return web.json_response({"error": f"Error processing prompt: {e}"}, status=500)

        except Exception as e:
            logger.error(f"Error handling request: {e}")
            return web.json_response({"error": "Invalid request"}, status=400)

    async def start(self):
        """Start the agent"""
        logger.info(f"🚀 {self.name} is starting...")

        app = web.Application()
        app.router.add_post('/query', self.query_handler)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', 8081)
        await site.start()

        logger.info(f"LLM agent listening on http://0.0.0.0:8081")

        # Keep the agent running
        while True:
            await asyncio.sleep(3600)  # Sleep for an hour

    async def stop(self):
        """Stop the agent gracefully"""
        logger.info("Shutting down...")
        if self.session:
            await self.session.close()

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