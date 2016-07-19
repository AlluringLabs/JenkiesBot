""" Implements an interface that we can use to work with commands."""

from .command import Command


class Commands:

    def __init__(self):
        self.commands = []

    def add_command(self, command: Command):
        if not isinstance(command, Command):
            raise TypeError('A command must inherit from Command.')
        self.commands.append(command)

    def add_commands(self, commands: list):
        for command in commands:
            self.add_command(command)

    def execute_command(self, command_slug):
        for command in self.commands:
            if command.command_slug == command_slug:
                return command.execute()


