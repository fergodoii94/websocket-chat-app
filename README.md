# WebSocket Echo Server

A minimal asynchronous WebSocket echo-server example in Python. It accepts connections on localhost port 8765 and sends each received message back to the same client.

## Current implementation

- Uses the `websockets` Python package.
- Handles incoming connections asynchronously.
- Reads messages with an async iterator and responds with an `Echo:` prefix.
- Keeps the server running until the process is stopped.

## Requirements and run

Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install websockets
python main.py
```

The server listens at `ws://localhost:8765`.

## Quick client test

In a second terminal, run:

```python
import asyncio
from websockets.asyncio.client import connect

async def main():
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("hello")
        print(await websocket.recv())

asyncio.run(main())
```

Expected response: `Echo: hello`.

## Current limitations

This repository is an echo-server exercise, not yet a multi-room chat application. It does not currently implement user identities, room management, message broadcasting, persistence, authentication, rate limiting, reconnect logic, a browser UI, automated tests or deployment configuration.

## Suggested next steps

1. Add structured message schemas and payload-size limits.
2. Implement a connection manager and isolated chat rooms.
3. Add authentication and per-connection rate limiting.
4. Add async tests for connection, messaging and disconnect scenarios.
5. Add graceful shutdown, observability and deployment documentation.

