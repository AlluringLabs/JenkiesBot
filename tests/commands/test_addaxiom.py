import unittest

from adapters.commands import AddAxiomCommand, CommandInterface


class TestAddAxiomCommand(unittest.TestCase):

    def test_add_axiom_command_extends_command_interface(self):
        self.assertTrue(issubclass(AddAxiomCommand, CommandInterface))
