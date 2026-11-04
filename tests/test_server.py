import asyncio
import unittest

from main import MAX_MESSAGE_SIZE, chat_handler


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


if __name__ == "__main__":
    unittest.main()
