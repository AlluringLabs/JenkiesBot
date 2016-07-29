from unittest import TestCase
from unittest.mock import patch
from jenkiesbot.adapters.commands import AddAxiomCommand, Command


class TestAddAxiomCommand(TestCase):

    def setUp(self):
        self.base_dict = {'axioms': []}
        self.add_axiom_command = AddAxiomCommand()

    def tearDown(self):
        self.add_axiom_command = None

    def test_add_axiom_command_extends_command_interface(self):
        self.assertTrue(issubclass(AddAxiomCommand, Command))

    def test_add_axiom_command_slug_is_add_axiom(self):
        self.assertEqual(
            self.add_axiom_command.command_slug, 'add_axiom')

    @patch('jenkiesbot.adapters.commands.addaxiom.update_json_file')
    def test_execute_command_exists(self, mock_update_json_method):
        # The Command parent object will throw an error if it's
        # not correctly implemented so all we have to do is make
        # a single call.
        self.add_axiom_command.execute([], '', '')

    @patch.object(AddAxiomCommand, '_update_axiom_json')
    @patch('jenkiesbot.adapters.commands.addaxiom.update_json_file')
    def test_execute_calls_update_json_from_utils(
            self, mock_update_json_file, mock_update_json_method):
        # Currently the add_axiom command should replicate what was
        # initially within the ChatterBotProxy class. This includes
        # just calling the update_json_file util function and...
        # updating the file.
        self.add_axiom_command.execute([], '', '')
        mock_update_json_file.assert_called_once_with(
            'corpa/training-corpa.json', mock_update_json_method)

    def test_update_axiom_json_exists(self):
        self.add_axiom_command._update_axiom_json(self.base_dict, '', [])

    def test_update_axiom_json_appends_to_the_dicts_axioms_list(self):
        statement = 'test statement'
        response_one = 'response one'
        response_two = 'response two'
        responses = [response_one, response_two]
        updated_dict = self.add_axiom_command._update_axiom_json(
            self.base_dict, statement, responses)
        self.assertEqual(updated_dict, {
            'axioms': [
                [statement, response_one, response_two]
            ]
        })

