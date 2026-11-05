<div align="center">

# WebSocket Echo Server

**An asynchronous Python example using persistent WebSocket connections.**

[![CI](https://github.com/fergodoii94/websocket-chat-app/actions/workflows/ci.yml/badge.svg)](https://github.com/fergodoii94/websocket-chat-app/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![WebSocket](https://img.shields.io/badge/Protocol-WebSocket-010101)

</div>

A minimal asynchronous WebSocket echo-server example in Python. It accepts connections on localhost port 8765 and sends each received message back to the same client.

## Current implementation

- Uses the modern asyncio server API from the `websockets` package.
- Handles incoming connections asynchronously.
- Reads messages with an async iterator and responds with an `Echo:` prefix.
- Enforces a 64 KiB maximum incoming message size.
- Logs connection lifecycle events without writing message contents to application logs.
- Includes unit tests for message echo behavior and the configured payload limit.

## Tech stack

- Python 3.10+
- asyncio
- websockets
- unittest
- Ruff

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python main.py
```

The server listens at `ws://127.0.0.1:8765`.

## Quick client test

In a second terminal, run:

```python
import asyncio
from websockets.asyncio.client import connect

async def main():
    async with connect("ws://127.0.0.1:8765") as websocket:
        await websocket.send("hello")
        print(await websocket.recv())

asyncio.run(main())
```

Expected response: `Echo: hello`.

## Quality checks

```bash
ruff check main.py tests
python -m unittest discover -s tests -v
```

GitHub Actions runs these checks on pushes and pull requests to `main`.

## Current limitations

> **Portfolio scope:** This repository is an echo-server exercise, not yet a multi-room chat application.

It does not currently implement user identities, room management, message broadcasting, persistence, authentication, rate limiting, reconnect logic, a browser UI or production deployment configuration. The server binds to loopback by default and is intended for local development.

## Suggested next steps

1. Implement a connection manager and isolated chat rooms.
2. Add structured message schemas and per-user payload quotas.
3. Add authentication and per-connection rate limiting.
4. Add integration tests against a real WebSocket server, including disconnect and oversized-payload cases.
5. Add graceful shutdown, observability and deployment documentation.

---

<div align="center">
  <sub>Part of my Python backend engineering portfolio.</sub>
</div>
