from unittest import TestCase
from jenkiesbot.adapters import Adapter
from jenkiesbot.adapters.commands import Command, CommandMethodNotImplementedError


class CommandTest(TestCase):

    def setUp(self):
        class TestCommand(Command):
            def __init__(self):
                super().__init__(command_slug='test_command')
        self.test_command = TestCommand()

    def test_command_is_child_class_of_adapter(self):
        self.assertTrue(issubclass(Command, Adapter))

    def test_command_throws_error_if_execute_is_not_implemented(self):
        with self.assertRaises(CommandMethodNotImplementedError):
            self.test_command.execute([], '', '')

    def test_command_throws_error_if_slug_is_not_specified(self):
        class TestCommand(Command):
            def __init__(self):
                super().__init__()
        with self.assertRaises(ValueError):
            TestCommand()
