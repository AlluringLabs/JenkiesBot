""" Module that implements the add_axiom command."""

from discord import Member, Channel
from .command import Command
from ...utils import update_json_file


class AddAxiomCommand(Command):
    """ Class that implements the add_axiom command."""

    def __init__(self):
        super().__init__(command_slug="add_axiom")

    def _update_axiom_json(self, json_file_contents: dict, statement: str, responses: list) -> dict:
        """ Used as the callback for execute()'s call to update_json_file.
        Implements how we should handle adding a new axiom to our training corpa json
        file.
        """
        json_file_contents['axioms'].append([
            statement
        ] + responses)
        return json_file_contents

    def execute(self, command_parts: list, author: Member, channel: Channel):
        """ Implements the execution portion of the add_axiom command."""
        update_json_file("corpa/training-corpa.json", self._update_axiom_json)
