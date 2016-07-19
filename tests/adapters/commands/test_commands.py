from unittest import TestCase
from unittest.mock import patch, call
from jenkiesbot.adapters.commands import Commands, Command


class CommandsTest(TestCase):

    def setUp(self):
        class TestCommand(Command):
            def __init__(self):
                pass
        self.test_command = TestCommand
        self.commands = Commands()

    def tearDown(self):
        self.commands = None

    def test_commands_list_inits_as_empty(self):
        self.assertEqual(self.commands.commands, [])

    def test_add_command_adds_command_to_commands_list(self):
        new_command = self.test_command()
        self.commands.add_command(new_command)
        self.assertEqual(len(self.commands.commands), 1)
        self.assertEqual(self.commands.commands[0], new_command)

    def test_add_command_fails_if_command_isnt_a_command(self):
        self.not_a_real_command = []
        with self.assertRaises(Exception):
            self.commands.add_command(self.not_a_real_command)

    def test_add_commands_adds_commands_by_calling_add_command(self):
        command_1 = self.test_command()
        command_2 = self.test_command()
        with patch.object(Commands, 'add_command', return_value=None) as mock_method:
            commands = Commands()
            commands.add_commands([command_1, command_2])
        self.assertTrue(mock_method.call_count, 3)
        mock_method.assert_has_calls([
            call(command_1), call(command_2)])

    def test_add_commands_adds_all_commands(self):
        command_1 = self.test_command()
        command_2 = self.test_command()
        command_3 = self.test_command()
        new_commands = [command_1, command_2, command_3]
        self.commands.add_commands(new_commands)
        self.assertEqual(len(self.commands.commands), 3)
