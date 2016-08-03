import asyncio

from unittest import TestCase
from tests.helpers import async_test
from jenkiesbot.adapters.connections import Connection, DiscordConnection


class DiscordConnectionTest(TestCase):

    def setUp(self):
        self.discordConnection = DiscordConnection()

    def test_discord_connection_is_subclass_of_connection(self):
        self.assertIsInstance(self.discordConnection, Connection)

    @async_test
    @asyncio.coroutine
    def test_that_all_required_methods_are_implemented(self):
        yield from self.discordConnection.connect()
        yield from self.discordConnection.on_message()
        yield from self.discordConnection.on_ready()
