""" Module that currently holds the core logic behind JenkiesBot."""
import re
import asyncio

from discord import Client, Member, Channel, Message, Game
from .adapters.commands import Commands, AddAxiomCommand
from .chatting import ChatterBotProxy


class JenkiesBot(Client):
    """ The one and only, JenkiesBot!"""

    COMMAND_PATTERN = '^(/\S*)\s(.*)'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # We will set this in on_ready()
        self.chatter = None
        # Temporarily adding the AddAxiom command; user's will decide commands
        # on their own.
        self.commands = Commands()
        self.commands.add_command(AddAxiomCommand())

    @staticmethod
    def can_member_chat(member: Member, channel: Channel):
        """ Checks to see if the member can chat in the channel."""
        return channel.permissions_for(member).send_messages

    @asyncio.coroutine
    def on_ready(self):
        """ Runs when the JenkiesBot successfully connects and logs in to Discord
        via the API.
        """
        self.chatter = ChatterBotProxy()
        yield from self.change_status(game=Game(name='Come Chat With Me!'))

    @asyncio.coroutine
    def on_message(self, message: Message):
        """ Runs when the JenkiesBot successfully sees a in any channel on any server.

        You can access the channel and server that the message came from by doing:
        channel = message.channel
        server = channel.server
        """
        channel = message.channel
        content = message.content
        author = message.author
        if author == self.user:
            return
        if self.commands.is_message_command(content):
            yield from self.commands.execute_command(content)
        else:
            if channel.is_private:
                reply = '{0.mention}: {1}'.format(
                    author, self.chatter.get_reply(content))
                yield from self.send_message(author, reply)
            elif self.can_member_chat(channel.server.me, channel):
                if channel.server.me in message.mentions:
                    if 'chat' in content:
                        yield from self.send_message(channel, "Sure! I'm messaging you now. :)")
                        yield from self.send_message(
                            author, "Hi there, {0.mention}! What's on your mind today?".format(
                                author))

    @asyncio.coroutine
    def on_member_join(self, member: Member):
        """ Called by DiscordPY when a member joins a server that JenkiesBot can read."""
        server_joined = member.server
        for channel in server_joined.channels:
            if channel.is_default:
                msg = 'Please welcome our newest member, {0.mention}, to the server!'.format(member)
                yield from self.send_message(channel, msg)
