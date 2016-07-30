from unittest import TestCase
from jenkiesbot.adapters import Adapter
from jenkiesbot.adapters.connections import Connection, ConnectionMethodNotImplemented


class ConnectionTest(TestCase):

    def setUp(self):
        self.connection = Connection()

    def test_adapter_is_subclass_of_adapter(self):
        self.assertIsInstance(self.connection, Adapter)

    def test_connection_method_throws_error_if_called_directly(self):
        with self.assertRaises(ConnectionMethodNotImplemented):
            self.connection.connect()
