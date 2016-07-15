""" Implements an interface that we can use to work with commands."""

from .command import CommandInterface


class Commands:

    def __init__(self):
        self.commands = []

    def add_command(self, command: CommandInterface):
        if not isinstance(command, CommandInterface):
            raise TypeError('A command must inherit from CommandInterface.')
        self.commands.append(command)

    def add_commands(self, commands: list):
        for command in commands:
            self.add_command(command)


