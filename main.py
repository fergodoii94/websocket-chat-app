"""Minimal asynchronous WebSocket echo server."""

import asyncio

from websockets.asyncio.server import ServerConnection, serve


async def chat_handler(websocket: ServerConnection) -> None:
    print("New client connected")
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")


async def main() -> None:
    async with serve(chat_handler, "127.0.0.1", 8765):
        print("WebSocket echo server listening on ws://127.0.0.1:8765")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
