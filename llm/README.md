# llm

LLM agent that uses Ollama to run llama3.2:1b.

## Getting Started

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the agent:
   ```bash
   python main.py
   ```

## Development

This agent is composed of two services:

*   `llm`: The user-facing agent that queries the LLM.
*   `ollama`: The Ollama server that runs the LLM.

The `llm` service is implemented in `main.py`. The `ollama` service is defined in the `Dockerfile`.

The two services are orchestrated using `docker-compose`. The `docker-compose.yml` file is generated from the `agent.json` file.

To start the services, run:

```bash
kadi start
```

This will start the `ollama` service in the background and then start the `llm` service in the foreground.

You can then enter prompts at the command line to query the LLM.

To stop the services, run:

```bash
kadi stop
```

## KADI Integration

This agent can be:

*   Built into a Docker container: `kadi build`
*   Deployed to various platforms: `kadi deploy`
*   Extended with abilities: `kadi install <ability-name>`
