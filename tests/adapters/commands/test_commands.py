from unittest import TestCase
from unittest.mock import patch, call
from jenkiesbot.adapters.commands import Commands, Command


class TestCommand(Command):

    def __init__(self):
        super().__init__(command_slug='test_command')

    def execute(self, command_parts, author, channel):
        pass


class AnotherTestCommand(Command):

    def __init__(self):
        super().__init__(command_slug='another_test_command')


class CommandsTest(TestCase):

    def setUp(self):
        self.commands = Commands()

    def tearDown(self):
        self.commands = None

    def test_that_we_can_override_command_prefix(self):
        commands_with_prefix = Commands(command_prefix='>')
        self.assertEqual(self.commands.command_prefix, '/')
        self.assertEqual(commands_with_prefix.command_prefix, '>')

    def test_is_message_command_returns_true_if_message_looks_like_a_command(self):
        self.assertFalse(self.commands.is_message_command('some random text'))
        self.assertFalse(self.commands.is_message_command(
            "/ I'm still not a command because of the space"))
        self.assertTrue(self.commands.is_message_command('/some_command'))
        self.assertTrue(self.commands.is_message_command(
            '/some_command with params'))

    def test_commands_list_inits_as_empty(self):
        self.assertEqual(self.commands.commands, [])

    def test_add_command_adds_command_to_commands_list(self):
        new_command = TestCommand()
        self.commands.add_command(new_command)
        self.assertEqual(len(self.commands.commands), 1)
        self.assertEqual(self.commands.commands[0], new_command)

    def test_add_command_checks_to_make_sure_command_slugs_are_unique(self):
        class NotUniqueTestCommand(TestCommand):
            pass
        test_command1 = TestCommand()
        test_command2 = NotUniqueTestCommand()
        self.commands.add_command(test_command1)
        with self.assertRaises(ValueError):
            self.commands.add_command(test_command2)

    def test_add_command_fails_if_command_isnt_a_command(self):
        self.not_a_real_command = []
        with self.assertRaises(TypeError):
            self.commands.add_command(self.not_a_real_command)

    def test_add_commands_adds_commands_by_calling_add_command(self):
        command_1 = TestCommand()
        command_2 = TestCommand()
        with patch.object(Commands, 'add_command', return_value=None) as mock_method:
            commands = Commands()
            commands.add_commands([command_1, command_2])
        self.assertTrue(mock_method.call_count, 3)
        mock_method.assert_has_calls([
            call(command_1), call(command_2)])

    def test_add_commands_adds_all_commands(self):
        command_1 = TestCommand()
        command_2 = AnotherTestCommand()
        new_commands = [command_1, command_2]
        self.commands.add_commands(new_commands)
        self.assertEqual(len(self.commands.commands), 2)
        self.assertEqual(self.commands.commands, new_commands)

    def test_execute_command_executes_command_based_on_slug(self):
        command_1 = TestCommand()
        command_2 = AnotherTestCommand()
        # We will mock the execute that we expect to be called.
        with patch.object(TestCommand, 'execute') as mock_execute:
            self.commands.commands = [command_1, command_2]
            self.commands.execute_command('/test_command')
        self.assertTrue(mock_execute.called)

    def test_execute_command_passes_command_params_if_they_exist(self):
        command = TestCommand()
        with patch.object(TestCommand, 'execute') as mock_execute:
            self.commands.commands = [command]
            self.commands.execute_command('/test_command param1 param2')
        self.assertTrue(mock_execute.called)
        self.assertEqual(mock_execute.call_args, ((['param1', 'param2'],),))

    def test_execute_command_returns_executed_commands_return_value(self):
        command = TestCommand()
        test_return_val = 'test'
        with patch.object(TestCommand, 'execute', return_value=test_return_val) as mock_execute:
            self.commands.commands = [command]
            return_val = self.commands.execute_command('/test_command')
        self.assertTrue(mock_execute.called)
        self.assertEqual(return_val, test_return_val)
