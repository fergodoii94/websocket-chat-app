import unittest

from websockets.asyncio.client import connect
from websockets.exceptions import ConnectionClosedError

from main import MAX_MESSAGE_SIZE, chat_handler, create_server


class FakeWebSocket:
    def __init__(self, messages: list[str]) -> None:
        self.messages = messages
        self.sent: list[str] = []

    def __aiter__(self):
        async def incoming_messages():
            for message in self.messages:
                yield message

        return incoming_messages()

    async def send(self, message: str) -> None:
        self.sent.append(message)


class ChatHandlerTests(unittest.IsolatedAsyncioTestCase):
    async def test_echoes_each_message_to_the_same_client(self):
        websocket = FakeWebSocket(["hello", "second message"])

        await chat_handler(websocket)

        self.assertEqual(websocket.sent, ["Echo: hello", "Echo: second message"])

    async def test_message_size_limit_is_explicit(self):
        self.assertEqual(MAX_MESSAGE_SIZE, 64 * 1024)

    async def test_running_server_echoes_a_real_client_message(self):
        async with create_server(port=0) as server:
            port = server.sockets[0].getsockname()[1]
            async with connect(f"ws://127.0.0.1:{port}") as websocket:
                await websocket.send("integration hello")
                self.assertEqual(await websocket.recv(), "Echo: integration hello")

    async def test_running_server_closes_oversized_message_with_1009(self):
        async with create_server(port=0) as server:
            port = server.sockets[0].getsockname()[1]
            async with connect(f"ws://127.0.0.1:{port}") as websocket:
                await websocket.send("x" * (MAX_MESSAGE_SIZE + 1))
                with self.assertRaises(ConnectionClosedError):
                    await websocket.recv()
                self.assertEqual(websocket.close_code, 1009)


if __name__ == "__main__":
    unittest.main()
