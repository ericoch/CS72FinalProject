"""
Nathan Schneider
schnei.nathan@gmail.com

Eric Och
Eric.H.Och.22@dartmouth.edu

Ian Hou
Ian.K.Hou.22@dartmouth.edu

COSC 072 Final Project
6/7/2022
This is a random codemaster player, which randomly guesses a word on the board.

It is using the codemaster template

"""
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem.lancaster import LancasterStemmer

from players.codemaster import Codemaster
import random


class AICodemaster(Codemaster):

    def __init__(self, brown_ic=None, glove_vecs=None, word_vectors=None):
        super().__init__()
        self.brown_ic = brown_ic
        self.glove_vecs = glove_vecs
        self.word_vectors = word_vectors
        self.wordnet_lemmatizer = WordNetLemmatizer()
        self.lancaster_stemmer = LancasterStemmer()
        self.cm_wordlist = []
        with open('players/cm_wordlist.txt') as infile:
            for line in infile:
                self.cm_wordlist.append(line.rstrip())
        self.syns = []
        for word in self.cm_wordlist:
            for synset_in_cmwordlist in wordnet.synsets(word):
                self.syns.append(synset_in_cmwordlist)

    def set_game_state(self, words, maps):
        self.words = words
        self.maps = maps

    def get_clue(self):
        rand_word = self.words[0]
        while rand_word in self.words:
            rand_word = random.choice(self.cm_wordlist)
        return rand_word, 1
