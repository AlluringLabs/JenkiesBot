import sys
import json
import discord

from utils import update_json_file
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer


class Chatter:

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
        self.chat_bot.train('chatterbot.corpus.english')
        self.chat_bot.train('.corpa')

    def add_axiom(self, statement: str, responses: str):
        def update_axiom_json(json_file_contents: dict):
            json_file_contents['axioms'].append([
                statement
            ] + responses)
            return json_file_contents
        update_json_file('corpa/training-corpa.json', update_axiom_json)
        # Retraining is required now!
        self.train_from_corpa()

    def get_reply(self, message):
        return self.chat_bot.get_response(message)
