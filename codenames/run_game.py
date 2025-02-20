"""
Nathan Schneider
schnei.nathan@gmail.com

Eric Och
Eric.H.Och.22@dartmouth.edu

Ian Hou
Ian.K.Hou.22@dartmouth.edu

COSC 072 Final Project
6/7/2022
This code runs a single game. The base logic was from the original repo, but we have made changes
to make it easier to use.

"""


import sys
import importlib
import argparse
import time
import os

from game import Game
from players.guesser import *
from players.codemaster import *


class GameRun:
    """Class that builds and runs a Game based on command line arguments"""

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Run the Codenames AI competition game.",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument(
            "codemaster", help="import string of form A.B.C.MyClass or 'human'")
        parser.add_argument(
            "guesser", help="import string of form A.B.C.MyClass or 'human'")
        parser.add_argument(
            "--seed", help="Random seed value for board state -- integer or 'time'", default='time')

        parser.add_argument(
            "--w2v", help="Path to w2v file or None", default=None)
        parser.add_argument(
            "--glove", help="Path to glove file or None", default=None)
        parser.add_argument(
            "--wordnet", help="Name of wordnet file or None, most like ic-brown.dat", default=None)
        parser.add_argument(
            "--glove_cm", help="Path to glove file or None", default=None)
        parser.add_argument("--glove_guesser",
                            help="Path to glove file or None", default=None)

        parser.add_argument("--no_log", help="Supress logging",
                            action='store_true', default=False)
        parser.add_argument("--no_print", help="Supress printing",
                            action='store_true', default=False)
        parser.add_argument(
            "--game_name", help="Name of game in log", default="default")

        args = parser.parse_args()

        self.do_log = not args.no_log
        self.do_print = not args.no_print
        if not self.do_print:
            self._save_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')
        self.game_name = args.game_name

        self.g_kwargs = {}
        self.cm_kwargs = {}

        # load codemaster class
        if args.codemaster == "human":
            self.codemaster = HumanCodemaster
            print('\nhuman codemaster (that\'s you!)\n')
            print('You are about to play Codenames, a word association game\n')
            print('The rules are simple:\n')
            print(
                'There is a codemaster (you) and a guesser (the computer), who are cooperating\n')
            print('The board displayed contains 25 words\n')
            print(
                'Some words are RED (friendly) and some are BLUE (enemy). Some are CIVILIAN (neutral)\n')
            print(
                'The object of the game is to guess all of the RED words, and as few BLUE words as possible\n')
            print('One word is ASSASSIN, if the computer guesses this word, you lose\n')
            print(
                'You will give clues about the words, and the computer will guess the words\n')
            print('The format will be [clue] [number of words]\n')
            print('An example: "rhino 4" means there are 4 words related to "rhino"\n')
            print('GLHF\n')
            print('please be patient while the game loads!\n')

        else:
            self.codemaster = self.import_string_to_class(args.codemaster)
            # print('loaded codemaster class')

        # load guesser class
        if args.guesser == "human":
            self.guesser = HumanGuesser
            print('\nhuman guesser (that\'s you!)\n')
            print('You are about to play Codenames, a word association game\n')
            print('The rules are simple:\n')
            print(
                'There is a codemaster (the computer) and a guesser (you), who are cooperating\n')
            print('The board displayed contains 25 words\n')
            print(
                'Some words are RED (friendly) and some are BLUE (enemy). Some are CIVILIAN (neutral)\n')
            print(
                'The object of the game is to guess all of the RED words, and as few BLUE words as possible\n')
            print('One word is ASSASSIN, if you guess this word, you lose\n')
            print(
                'The codemaster will give you clues about the words, and you will guess the words\n')
            print('The format will be [clue] [number of words]\n')
            print('An example: "rhino 4" means there are 4 words related to "rhino"\n')
            print('GLHF\n')
            print('please be patient while the game loads!\n')

        else:
            self.guesser = self.import_string_to_class(args.guesser)
            # print('loaded guesser class')

        # if the game is going to have an ai, load up word vectors
        if sys.argv[1] != "human" or sys.argv[2] != "human":
            if args.wordnet is not None:
                brown_ic = Game.load_wordnet(args.wordnet)
                self.g_kwargs["brown_ic"] = brown_ic
                self.cm_kwargs["brown_ic"] = brown_ic
                # print('loaded wordnet')

            if args.glove is not None:
                glove_vectors = Game.load_glove_vecs(args.glove)
                self.g_kwargs["glove_vecs"] = glove_vectors
                self.cm_kwargs["glove_vecs"] = glove_vectors
                # print('loaded glove vectors')

            if args.w2v is not None:
                w2v_vectors = Game.load_w2v(args.w2v)
                self.g_kwargs["word_vectors"] = w2v_vectors
                self.cm_kwargs["word_vectors"] = w2v_vectors
                # print('loaded word vectors')

            if args.glove_cm is not None:
                glove_vectors = Game.load_glove_vecs(args.glove_cm)
                self.cm_kwargs["glove_vecs"] = glove_vectors
                # print('loaded glove vectors')

            if args.glove_guesser is not None:
                glove_vectors = Game.load_glove_vecs(args.glove_guesser)
                self.g_kwargs["glove_vecs"] = glove_vectors
                # print('loaded glove vectors')

        # set seed so that board/keygrid can be reloaded later
        if args.seed == 'time':
            self.seed = time.time()
        else:
            self.seed = int(args.seed)

    def __del__(self):
        """reset stdout if using the do_print==False option"""
        if not self.do_print:
            sys.stdout.close()
            sys.stdout = self._save_stdout

    def import_string_to_class(self, import_string):
        """Parse an import string and return the class"""
        parts = import_string.split('.')
        module_name = '.'.join(parts[:len(parts) - 1])
        class_name = parts[-1]

        module = importlib.import_module(module_name)
        my_class = getattr(module, class_name)

        return my_class


if __name__ == "__main__":
    print("The game is starting...")
    game_setup = GameRun()

    game = Game(game_setup.codemaster,
                game_setup.guesser,
                seed=game_setup.seed,
                do_print=game_setup.do_print,
                do_log=game_setup.do_log,
                game_name=game_setup.game_name,
                cm_kwargs=game_setup.cm_kwargs,
                g_kwargs=game_setup.g_kwargs)

    # print("skip run")
    # exit()
    game.run()
