""" Implements a Class that allows JenkiesBot to easily interface with Commands."""
import re

from .command import Command


class Commands:
    """ Class that allows JenkiesBot to easily interface with Commands."""

    COMMAND_PATTERN_REGEX = re.compile("^/(\S+)\s?(.*)?")

    def __init__(self, command_prefix='/'):
        self.commands = []
        self.command_prefix = command_prefix

    def is_message_command(self, message_content: str):
        """ Checks to see if the message_content passed looks like an actual command.
        A command should start with the command_prefix and then have no space followed
        by a random string of characters."""
        starts_with_command_prefix = message_content[0] == self.command_prefix
        matches_command_pattern = self.COMMAND_PATTERN_REGEX.match(message_content)
        return starts_with_command_prefix and matches_command_pattern

    def add_command(self, command: Command):
        """ Adds a command to the commands list, but only if the command inherits
        from the Command 'Interface' Class."""
        if not isinstance(command, Command):
            raise TypeError("A command must inherit from Command.")
        current_slugs = map(lambda command: command.command_slug, self.commands)
        command_slug = command.command_slug
        if command_slug in current_slugs:
            raise ValueError(
                "A command with the slug {0} has already been " \
                "registered.".format(command_slug))
        self.commands.append(command)
        return self

    def add_commands(self, commands: list):
        """ Adds a list of commands to the commands list by passing each command object
        to the self._add_command() method of this class."""
        for command in commands:
            self.add_command(command)

    def execute_command(self, command_slug: str):
        """ Handles executing the correct command based on the supplied
        command_slug."""
        command_parts = self.COMMAND_PATTERN_REGEX.match(command_slug)
        command_slug = command_parts.group(1)
        command_params = command_parts.group(2).split(" ")
        for command in self.commands:
            if command.command_slug == command_slug:
                return command.execute(command_params)



