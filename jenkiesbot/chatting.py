""" Module for the JenkiesBot/ChatterBot Integration. TEMPORARY"""

from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer
from .utils import update_json_file


class ChatterBotProxy:
    """ ChatterBotProxy is the core class involved with the integration with
    ChatterBot. It handles abstracting all interactions with ChatterBot.
    """

    def __init__(self):
        self.chat_bot = ChatBot(
            'JenkiesBot',
            storage_adapter='chatterbot.adapters.storage.JsonDatabaseAdapter',
            logic_adapters=[
                'chatterbot.adapters.logic.ClosestMeaningAdapter',
                'chatterbot.adapters.logic.ClosestMatchAdapter'
            ],
            database='./chat-storage.json')
        # Training
        self.chat_bot.set_trainer(ChatterBotCorpusTrainer)
        self.train_from_corpa()

    def train_from_corpa(self):
        """ Trains the ChatterBot instance."""
        self.chat_bot.train('chatterbot.corpus.english')
        self.chat_bot.train('.corpa')

    def get_reply(self, message):
        """ Abstracts away the to our bots method for retrieving a repsonse."""
        return self.chat_bot.get_response(message)
