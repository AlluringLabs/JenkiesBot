import os
import discord

from jenkiesbot import JenkiesBot


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
