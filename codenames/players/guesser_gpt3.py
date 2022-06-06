from players.guesser import Guesser
import random

from players.codemaster import Codemaster
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')

setup = """
Here are instructions to play the game Codenames:

Given a list of words, a clue, and a number, determine which set of words correspond most closely to the clue. You must give a list of words that correspond with the clue, with the same number of words as the number you were given. 

 For example:

words: buffalo, tag, beat, fly, centaur, undertaker, rock, fair. clue: hooves 2. answers: buffalo, centaur
words: wave, bar, day, ambulance, press, strike, pie, casino. clue: place 2. answers: bar, casino
"""


class AIGuesser(Guesser):

    def __init__(self, brown_ic=None, glove_vecs=None, word_vectors=None):
        super().__init__()

        self.num = 0

    def set_board(self, words):
        self.words = words

    def set_clue(self, clue, num):
        self.clue = clue
        self.num = num
        print("The clue is:", clue, num)
        li = [clue, num]

        return li

    def keep_guessing(self):
        return self.num > 0

    def get_answer(self):
        remaining_words = [word.lower()
                           for word in self.words if '*' not in word]
        prompt = "words: %s. clue: %s %s. answers:" % (
            ", ".join(remaining_words), self.clue, self.num)

        print(prompt)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=setup+prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=2,
            presence_penalty=2,

        )
        answer = response['choices'][0]['text'].strip()
        answer = answer.split('\n')[0].split(',')
        print('GPT3 response: ', answer)
        try:
            answer = answer[0].strip()
            if answer in remaining_words:
                self.num -= 1
                return answer
            else:
                print("GPT3 response not in word list, defaulting to random word")
                self.num -= 1
                return self.get_random_answer()
        except:
            pass
        self.num -= 1
        return self.get_random_answer()

    def get_random_answer(self):
        rand_word = "*"
        while '*' in rand_word:
            rand_word = random.choice(self.words)

        return rand_word
