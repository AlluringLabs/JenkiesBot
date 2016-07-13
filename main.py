import os
import json
import random
import asyncio
import discord

from chatting import Chatter
from discord import Member, Channel, Message, Game
from discord.ext import commands
from discord.ext.commands import Bot


class JenkiesBot(Bot):

    @staticmethod
    def can_bot_talk(member: Member, channel: Channel):
        """ Checks to see if the member can chat in the channel."""
        return channel.permissions_for(member).send_messages

    def add_axiom(self, command_parts: list, author: Member, channel: Channel):
        question, responses = command_parts[0], command_parts[1:]
        self.chatter.add_axiom(question, responses)
        confirmation_msg = 'Thanks for adding the axiom, {0.mention}.'.format(author)
        return self.send_message(channel, confirmation_msg)

    def run_command(self, content: str, author: Member, channel: Channel):
        command_parts = list(map(lambda x: x.strip(), content.split('|')))
        if command_parts[0] == '>add_axiom':
            return self.add_axiom(command_parts[1:], author, channel)

    @asyncio.coroutine
    def on_ready(self):
        """ Runs when the JenkiesBot successfully connects and logs in to Discord
        via the API.
        """
        self.chatter = Chatter()
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
        if author == bot.user:
            return
        # This is 100% temp until I can figure out why the command decorator is not
        # working.
        if '>' == content[0]:
            yield from self.run_command(content, author, channel)
        else:
            if channel.is_private:
                reply = '{0.mention}: {1}'.format(
                    author, self.chatter.get_reply(content))
                yield from self.send_message(author, reply)
            elif self.can_bot_talk(channel.server.me, channel):
                if channel.server.me in message.mentions:
                    if 'chat' in content:
                        yield from self.send_message(channel, "Sure! I'm messaging you now. :)")
                        yield from self.send_message(author, "Hi there, {0.mention}! What's on your mind today?".format(author))
        #yield from bot.process_commands(message)

    @asyncio.coroutine
    def on_member_join(self, member: Member):
        server_joined = member.server
        for channel in server_joined.channels:
            if channel.is_default:
                msg = 'Please welcome our newest member, {0.mention}, to the server!'.format(member)
                yield from self.send_message(channel, msg)


if __name__ == '__main__':
    bot = JenkiesBot(command_prefix='>')
    try:
        bot.run(os.environ['JENKIES_BOT_KEY'])
    except (discord.LoginFailure, discord.HTTPException, TypeError) as e:
        print('Failed To Log In: {0}'.format(e))
    except discord.GatewayNotFound as e:
        print('It seems the Discord API may be down, see this error for more details: {0}'.format(e))
    except discord.ConnectionClosed as e:
        print('The connection to the Discord Server has been closed... This error has been raised: {0}'.format(e))
