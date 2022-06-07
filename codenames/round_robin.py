"""
Nathan Schneider
schnei.nathan@gmail.com

Eric Och
Eric.H.Och.22@dartmouth.edu

Ian Hou
Ian.K.Hou.22@dartmouth.edu

COSC 072 Final Project
6/7/2022
This code runs a round-robin style game of codemasters and guessers.

"""
import multiprocessing as mp
import subprocess
import random
import sys
import pandas as pd
import json

NUM_GAMES = 10

# defined codemasters and their arguments
codemasters = {
    "players.codemaster_w2v_05.AICodemaster": ['--glove_cm', 'players/glove/glove.6B.200d.txt', '--w2v', 'players/GoogleNews-vectors-negative300.bin'],
    "players.codemaster_glove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt'],
    "players.codemaster_w2vglove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt', '--w2v', 'players/GoogleNews-vectors-negative300.bin'],
    # "players.codemaster_fasttext.AICodemaster": ['--glove_cm', 'players/glove/wiki-news-300d-1M.vec'],
    "players.codemaster_wn_lin.AICodemaster": [],
    "players.codemaster_random.AICodemaster": [],
    "players.codemaster_gpt3.AICodemaster": [],
    "players.codemaster_gpt3_complex.AICodemaster": []

}
# guessers and their arguments
guessers = {
    "players.guesser_w2v.AIGuesser": ['--w2v', 'players/GoogleNews-vectors-negative300.bin', '--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_glove.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_w2vglove.AIGuesser": ['--w2v', 'players/GoogleNews-vectors-negative300.bin', '--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_fasttext.AIGuesser": ['--glove_guesser', 'players/glove/wiki-news-300d-1M.vec'],
    "players.guesser_wn_lch.AIGuesser": [],
    "players.guesser_wn_path.AIGuesser": [],
    "players.guesser_wn_wup.AIGuesser": [],
    "players.guesser_random.AIGuesser": [],
    "players.guesser_gpt3.AIGuesser": [],

}

# this function generates an ordered list of arguments for bots to play against each other


def generate_args():
    arg_list = []

    const_args = ['--wordnet', 'ic-brown.dat']
    for codemaster in codemasters:
        for guesser in guessers:
            for _ in range(NUM_GAMES):
                arg_list.append(["python", "run_game.py", codemaster,
                                guesser] + codemasters[codemaster] + guessers[guesser] + const_args)

    return arg_list

# this function generates an ordered list of arguments for bots to play with a human


def generate_args_human():
    arg_list = []
    const_args = ['--wordnet', 'ic-brown.dat']

    guesser = "human"
    for codemaster in codemasters:
        for _ in range(NUM_GAMES):
            arg_list.append(["python", "run_game.py", codemaster,
                            guesser] + codemasters[codemaster] + const_args)

    codemaster = "human"
    for guesser in guessers:
        for _ in range(NUM_GAMES):
            arg_list.append(["python", "run_game.py", codemaster,
                            guesser] + guessers[guesser] + const_args)

    return arg_list


# this function returns a single game configuration based on the least common matchups in the data
def get_arg():

    try:
        vals = [json.loads(line)
                for line in open('results/bot_results_new_style.txt')]
    except:
        for line in open("results/bot_results_new_style.txt"):
            print(line)
            print(json.loads(line))
        exit()

    df = pd.DataFrame(vals)

    df = df.drop('cm_kwargs', axis=1).drop(
        'g_kwargs', axis=1).drop('game_name', axis=1)

    const_args = ['--wordnet', 'ic-brown.dat']
    vals = {}
    for codemaster in codemasters:
        for guesser in guessers:
            cm = "<class '%s'>" % codemaster
            g = "<class '%s'>" % guesser
            count = df.loc[(df['codemaster'] == cm) & (
                df['guesser'] == g)]['R'].count()
            vals[(codemaster, guesser)] = count

    min_matchup = min(vals, key=vals.get)
    # print(vals)
    print("Found min matchup: ", min_matchup, vals[min_matchup])

    (codemaster, guesser) = min_matchup
    return ["python", "run_game.py", codemaster,
            guesser] + codemasters[codemaster] + guessers[guesser] + const_args


# this function returns a single human game configuration based on the least common matchups in the data
def get_arg_human():

    try:
        vals = [json.loads(line)
                for line in open('results/bot_results_new_style.txt')]
    except:
        for line in open("results/bot_results_new_style.txt"):
            print(line)
            print(json.loads(line))
        exit()

    df = pd.DataFrame(vals)

    df = df.drop('cm_kwargs', axis=1).drop(
        'g_kwargs', axis=1).drop('game_name', axis=1)

    const_args = ['--wordnet', 'ic-brown.dat']
    vals = {}

    hg = "players.guesser.HumanGuesser"
    hcm = "players.codemaster.HumanCodemaster"

    for guesser in guessers:
        cm = "<class '%s'>" % hcm
        g = "<class '%s'>" % guesser
        count = df.loc[(df['codemaster'] == cm) & (
            df['guesser'] == g)]['R'].count()
        vals[(hcm, guesser)] = count

    for codemaster in codemasters:
        cm = "<class '%s'>" % codemaster
        g = "<class '%s'>" % hg
        count = df.loc[(df['codemaster'] == cm) & (
            df['guesser'] == g)]['R'].count()
        vals[(codemaster, hg)] = count

    print(vals)
    min_matchup = min(vals, key=vals.get)
    print("Found min matchup: ", min_matchup, vals[min_matchup])

    (codemaster, guesser) = min_matchup

    if not 'human' in codemaster.lower():
        codemaster_args = codemasters[codemaster]
    else:
        codemaster_args = []

    if not 'human' in guesser.lower():
        guesser_args = guessers[guesser]
    else:
        guesser_args = []

    return ["python", "run_game.py", codemaster,
            guesser] + codemaster_args + guesser_args + const_args


def run_game(args):  # runs the game with the given arguments
    print(args)
    subprocess.run(args)


def run_min_game(arg):
    args = get_arg()
    run_game(args)


def run_min_game_human(arg):
    args = get_arg_human()
    run_game(args)


def main():

    # if the user wants to play as a human
    if len(sys.argv) > 1 and sys.argv[1] == "--human":

        pool = mp.Pool(1)   # single pool for human games
        pool.map(run_min_game_human, [0]*10000)

    else:
        # multiple pools for multiprocessing games (beware of memory usage)
        pool = mp.Pool(2)
        pool.map(run_min_game, [0]*10000)  # map function usage


if __name__ == "__main__":
    main()
