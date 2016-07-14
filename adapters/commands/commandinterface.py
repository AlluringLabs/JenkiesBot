from .. import AdapterMethodNotImplementedError
from discord import Member, Channel


class CommandInterface:

    def execute(self, command_parts: list, author: Member, channel: Channel):
        raise CommandMethodNotImplementedError()


class CommandMethodNotImplementedError(AdapterMethodNotImplementedError):

    def __init__(self, message="A command method was not implemented."):
        self.message = message

    def __unicode__(self):
        return unicode(self).encode('utf-8')()

    def __str__(self):
        return self.message
