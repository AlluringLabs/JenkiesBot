import unittest

from adapters.commands import CommandInterface, CommandMethodNotImplementedError


class CommandInterfaceTest(unittest.TestCase):

    def setUp(self):
        class TestCommand(CommandInterface):
            pass

        self.test_command = TestCommand()

    def test_interface_throws_error_if_execute_is_not_implemented(self):
        with self.assertRaises(CommandMethodNotImplementedError):
            self.test_command.execute([], '', '')
