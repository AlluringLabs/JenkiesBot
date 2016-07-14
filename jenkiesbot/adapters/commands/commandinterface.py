""" Lays out the structure for how Commands should be implemented."""

from discord import Member, Channel
from ..adapter import AdapterMethodNotImplementedError


class CommandInterface:
    """ Interface that describes which methods a command must implement."""

    def __init__(self):
        super().__init__()

    def execute(self, command_parts: list, author: Member, channel: Channel):
        """ Required method that is called when a command is executed."""
        raise CommandMethodNotImplementedError()


class CommandMethodNotImplementedError(AdapterMethodNotImplementedError):
    """ This error is raised when a command does not implement the
    methods described in the CommandInterface.
    """

    def __init__(self, message="A command method was not implemented."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
