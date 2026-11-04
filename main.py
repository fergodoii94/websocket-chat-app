"""Minimal asynchronous WebSocket echo server."""

import asyncio
import logging

from websockets.asyncio.server import ServerConnection, serve

HOST = "127.0.0.1"
PORT = 8765
MAX_MESSAGE_SIZE = 64 * 1024

logger = logging.getLogger(__name__)


async def chat_handler(websocket: ServerConnection) -> None:
    logger.info("WebSocket client connected")
    try:
        async for message in websocket:
            await websocket.send(f"Echo: {message}")
    finally:
        logger.info("WebSocket client disconnected")


async def main() -> None:
    async with serve(
        chat_handler,
        HOST,
        PORT,
        max_size=MAX_MESSAGE_SIZE,
    ):
        logger.info("WebSocket echo server listening on ws://%s:%s", HOST, PORT)
        await asyncio.Future()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
