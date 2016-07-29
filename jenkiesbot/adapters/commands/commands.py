""" Implements a Class that allows JenkiesBot to easily interface with Commands."""

from .command import Command


class Commands:
    """ Class that allows JenkiesBot to easily interface with Commands."""

    def __init__(self, command_prefix='/'):
        self.commands = []
        self.command_prefix = command_prefix

    def add_command(self, command: Command):
        """ Adds a command to the commands list, but only if the command inherits
        from the Command 'Interface' Class."""
        if not isinstance(command, Command):
            raise TypeError('A command must inherit from Command.')
        current_slugs = map(lambda command: command.command_slug, self.commands)
        command_slug = command.command_slug
        if command_slug in current_slugs:
            raise ValueError(
                'A command with the slug {0} has already been registered.'.format(command_slug))
        self.commands.append(command)

    def add_commands(self, commands: list):
        """ Adds a list of commands to the commands list by passing each command object
        to the self._add_command() method of this class."""
        for command in commands:
            self.add_command(command)

    def execute_command(self, command_slug):
        """ Handles executing the correct command(s) based on the command_slug."""
        for command in self.commands:
            if command.command_slug == command_slug:
                return command.execute()


