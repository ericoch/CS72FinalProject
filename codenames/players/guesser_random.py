"""
Nathan Schneider
schnei.nathan@gmail.com

Eric Och
Eric.H.Och.22@dartmouth.edu

Ian Hou
Ian.K.Hou.22@dartmouth.edu

COSC 072 Final Project
6/7/2022
This is a random guesser player, which randomly guesses a word on the board
It is using the codemaster template

"""
from players.guesser import Guesser
import random


class AIGuesser(Guesser):

    def __init__(self, brown_ic=None, glove_vecs=None, word_vectors=None):
        super().__init__()
        self.brown_ic = brown_ic
        self.glove_vecs = glove_vecs
        self.word_vectors = word_vectors
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
        rand_word = "*"
        while '*' in rand_word:
            rand_word = random.choice(self.words)

        return rand_word
