""" Module that implements the add_axiom command."""

from discord import Member, Channel
from .command import Command
from ...utils import update_json_file


class AddAxiomCommand(Command):
    """ Class that implements the add_axiom command."""

    def __init__(self):
        super().__init__(command_slug='add_axiom')

    def _update_axiom_json(self, json_file_contents: dict) -> dict:
        """ Used as the call back for add_axiom()'s call to update_json_file.
        Describes how we should add a new axiom to our training corpa json
        file.
        """
        json_file_contents['axioms'].append([
            statement
        ] + responses)
        return json_file_contents

    def execute(self, command_parts: list, author: Member, channel: Channel):
        update_json_file('corpa/training-corpa.json', self._update_axiom_json)
