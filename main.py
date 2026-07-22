import asyncio
import websockets

async def chat_handler(websocket, path):
    print("New client connected")
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(chat_handler, "localhost", 8765):
        print("Chat Server started on port 8765...")
        await asyncio.Future() # Run forever

if __name__ == "__main__":
    asyncio.run(main())
