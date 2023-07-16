from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ChatterBotDatabaseAdapter


chatbot = ChatBot("MyChatBot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
chatbot.database_uri = "sqlite:///data/db.sqlite3"
chatbot.storage = ChatterBotDatabaseAdapter()
