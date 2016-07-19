""" Lays out the structure for how Commands should be implemented."""

from discord import Member, Channel
from ..adapter import Adapter


class Command(Adapter):
    """ Interface that describes which methods a command must implement."""

    def __init__(self, command_slug=''):
        if not command_slug:
            raise ValueError('A Command must specify a command_slug.')
        self.command_slug = command_slug

    def execute(self, command_parts: list, author: Member, channel: Channel):
        """ Required method that is called when a command is executed."""
        raise CommandMethodNotImplementedError()


class CommandMethodNotImplementedError(NotImplementedError):
    """ This error is raised when a command does not implement the
    methods described in the Command.
    """

    def __init__(self, message="A command method was not implemented."):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
