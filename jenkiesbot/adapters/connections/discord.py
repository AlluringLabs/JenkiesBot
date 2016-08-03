import asyncio

from .connection import Connection


class DiscordConnection(Connection):

    @asyncio.coroutine
    def connect(self):
        pass

    @asyncio.coroutine
    def on_message(self):
        pass

    @asyncio.coroutine
    def on_ready(self):
        pass
