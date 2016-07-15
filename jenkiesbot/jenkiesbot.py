""" Module that currently holds the core logic behind JenkiesBot."""
import re
import asyncio

from discord import Client, Member, Channel, Message, Game
from .chatting import ChatterBotProxy


class JenkiesBot(Client):
    """ The one and only, JenkiesBot!"""

    COMMAND_PATTERN = '^(/\S*)\s(.*)'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # We will set this in on_ready()
        self.chatter = None

    @staticmethod
    def can_member_chat(member: Member, channel: Channel):
        """ Checks to see if the member can chat in the channel."""
        return channel.permissions_for(member).send_messages

    def add_axiom(self, command_parts: list, author: Member, channel: Channel):
        """ Temporarily implements the add_axiom command. See adapters.commands.addaxiom."""
        question, responses = command_parts[0], command_parts[1:]
        self.chatter.add_axiom(question, responses)
        confirmation_msg = 'Thanks for adding the axiom, {0.mention}.'.format(author)
        return self.send_message(channel, confirmation_msg)

    def run_command(self, content: str, author: Member, channel: Channel):
        """ Currently handles figuring out which command needs to be ran."""
        command_regex = re.search(self.COMMAND_PATTERN, content)
        command, command_params = command_regex.group(1), command_regex.group(2)
        command_parts = list(map(lambda x: x.strip(), command_params.split('|')))
        if command == '/add_axiom':
            return self.add_axiom(command_parts, author, channel)

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
        # This is 100% temp until I can figure out why the command decorator is not
        # working.
        if content[0] == '/':
            yield from self.run_command(content, author, channel)
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
