from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sys,os
from contextlib import contextmanager

@contextmanager
def suppress_stdout():		# this is to repress the bot training log
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def train_bot(bot_name,bot_corpus="chatterbot.corpus.english"):	# trains the bot
	chatbot = ChatBot(bot_name)
	trainer = ChatterBotCorpusTrainer(chatbot)
	trainer.train(bot_corpus)
	return chatbot

def get_response(question,trained_bot):	# get response from the bot
	response = trained_bot.get_response(question)
	return response

if __name__ == "__main__":
	# usage: python3 bot_module.py [QUESTION]
	# input: 1 arg: question to be asked
	# output: 1 string: answer to question
	with suppress_stdout():
		mybot = train_bot('EGbot')
	question = sys.argv[1]	# get the first argument [QUESTION]
	response = get_response(question,mybot)
	print(response)
	sys.exit(0)
