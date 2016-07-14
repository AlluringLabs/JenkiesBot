""" Module for the JenkiesBot/ChatterBot Integration. TEMPORARY"""

from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer
from .utils import update_json_file


class Chatter:
    """ Chatter is the core class involved with the integration with
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

    def add_axiom(self, statement: str, responses: str):
        """ Adds the user's supplied axiom to the axiom file."""
        def update_axiom_json(json_file_contents: dict) -> dict:
            """ Used as the call back for add_axiom()'s call to update_json_file.
            Describes how we should add a new axiom to our training corpa json
            file.
            """
            json_file_contents['axioms'].append([
                statement
            ] + responses)
            return json_file_contents
        update_json_file('../corpa/training-corpa.json', update_axiom_json)
        # Retraining is required now!
        self.train_from_corpa()

    def get_reply(self, message):
        """ Abstracts away the to our bots method for retrieving a repsonse."""
        return self.chat_bot.get_response(message)
