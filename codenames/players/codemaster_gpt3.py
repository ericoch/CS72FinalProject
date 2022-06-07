import random
"""
Nathan Schneider
schnei.nathan@gmail.com

Eric Och
Eric.H.Och.22@dartmouth.edu

Ian Hou
Ian.K.Hou.22@dartmouth.edu

COSC 072 Final Project
6/7/2022
This is a GPT-3 codemaster, which randomly guesses a word on the board.

It is using the codemaster template

"""
from players.codemaster import Codemaster
import openai

import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')

# set up simple instructions for the GPT-3 model
setup = """
Here are instructions to play the game Codenames:

Given a list of words, a clue, and a number, determine which set of words correspond most closely to the clue. You must give a list of words that correspond with the clue, with the same number of words as the number you were given. They must be ordered from most similar to the clue to least similar. 

After the clue, say the number of words the clue applies to, from 1 to 3. If the clue applies to 3 words, give the number 3.
For example:

words: nut, bark, octopus, candy, birch. clue: tree 3
words: worm, tower. clue: building 1
words: mouse, undertaker, stadium. clue: funeral 1
words: nut, bark, octopus, candy. clue: food 2
words: yarn, bottle, white, shoe, knit. clue: sock 3
words: parachute, worm, theater, pants, buffalo. clue: animal 2

"""


class AICodemaster(Codemaster):

    def __init__(self, brown_ic=None, glove_vecs=None, word_vectors=None):
        super().__init__()

        self.cm_wordlist = []
        with open('players/cm_wordlist.txt') as infile:
            for line in infile:
                self.cm_wordlist.append(line.rstrip())

    def set_game_state(self, words, maps):
        self.words = words
        self.maps = maps

    def get_clue(self):

        red_words = []  # get only red words
        for i in range(25):
            if self.maps[i] == "Red" and '*' not in self.words[i]:
                red_words.append(self.words[i].lower())

        prompt = "words: %s. clue:" % ", ".join(red_words)  # build prompt
        # print(prompt)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=setup+prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=2,
            presence_penalty=2,

        )
        answer = response['choices'][0]['text'].strip().lower()
        answer = answer.split('\n')[0].split()  # parse response
        print('GPT3 response: ', answer)
        try:
            clue = answer[0]
            num = int(answer[1])
        except:
            try:
                clue = answer[0]
                num = 1
                print("Failed to get number of words, defaulting to 1")
            except:
                print("Failed to get clue, defaulting to random word")
                return self.get_rand_clue()
        if clue in red_words:
            print("Clue is in the list of words, defaulting to random word")
            return self.get_rand_clue()
        return clue, num

    def get_rand_clue(self):
        rand_word = self.words[0]
        while rand_word in self.words:
            rand_word = random.choice(self.cm_wordlist)
        return rand_word, 1
