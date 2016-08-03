import asyncio

from unittest import TestCase
from jenkiesbot.adapters import Adapter
from jenkiesbot.adapters.connections import Connection, ConnectionMethodNotImplemented
from tests.helpers import async_test


class ConnectionTest(TestCase):

    def setUp(self):
        self.connection = Connection()

    def test_adapter_is_subclass_of_adapter(self):
        self.assertIsInstance(self.connection, Adapter)

    def test_enforce_that_connect_is_a_coroutine(self):
        self.assertTrue(asyncio.iscoroutinefunction(self.connection.connect))

    @async_test
    @asyncio.coroutine
    def test_connection_method_throws_error_if_called_directly(self):
        with self.assertRaises(ConnectionMethodNotImplemented):
            yield from self.connection.connect()

    def test_enforce_that_on_ready_is_a_coroutine(self):
        self.assertTrue(asyncio.iscoroutinefunction(self.connection.on_ready))

    @async_test
    @asyncio.coroutine
    def test_on_ready_method_throws_error_if_called_directly(self):
        with self.assertRaises(ConnectionMethodNotImplemented):
            yield from self.connection.on_ready()

    def test_enforce_on_message_method_is_a_coroutine(self):
        self.assertTrue(asyncio.iscoroutinefunction(self.connection.on_message))

    @async_test
    @asyncio.coroutine
    def test_on_message_method_throws_error_if_called_directly(self):
        with self.assertRaises(ConnectionMethodNotImplemented):
            yield from self.connection.on_message()

