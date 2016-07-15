from unittest import TestCase
from jenkiesbot.adapters.commands import Commands, Command


class CommandsTest(TestCase):

    def setUp(self):
        self.commands = Commands()

    def tearDown(self):
        self.commands = None

    def test_commands_list_inits_as_empty(self):
        self.assertEqual(self.commands.commands, [])

    def test_add_command_adds_command_to_commands_list(self):
        new_command = Command()
        self.commands.add_command(new_command)
        self.assertEqual(len(self.commands.commands), 1)
        self.assertEqual(self.commands.commands[0], new_command)

    def test_add_command_fails_if_command_isnt_a_command(self):
        self.not_a_real_command = []
        with self.assertRaises(Exception):
            self.commands.add_command(self.not_a_real_command)

    def test_add_commands_adds_all_commands_by_calling_add_command(self):
        command_1 = Command()
        command_2 = Command()
        command_3 = Command()
        new_commands = [command_1, command_2, command_3]
        self.commands.add_commands(new_commands)
        self.assertEqual(len(self.commands.commands), 3)
