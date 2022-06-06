
import multiprocessing as mp
import subprocess
import random
import sys
import pandas as pd
import json

NUM_GAMES = 10

codemasters = {
    "players.codemaster_w2v_05.AICodemaster": ['--glove_cm', 'players/glove/glove.6B.200d.txt', '--w2v', 'players/GoogleNews-vectors-negative300.bin'],
    "players.codemaster_glove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt'],
    "players.codemaster_w2vglove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt', '--w2v', 'players/GoogleNews-vectors-negative300.bin'],
    "players.codemaster_wn_lin.AICodemaster": [],
    "players.codemaster_random.AICodemaster": [],
    "players.codemaster_gpt3.AICodemaster": [],
    "players.codemaster_gpt3_complex.AICodemaster": []
}

guessers = {
    "players.guesser_w2v.AIGuesser": ['--w2v', 'players/GoogleNews-vectors-negative300.bin', '--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_glove.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_w2vglove.AIGuesser": ['--w2v', 'players/GoogleNews-vectors-negative300.bin', '--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_wn_lch.AIGuesser": [],
    "players.guesser_wn_path.AIGuesser": [],
    "players.guesser_wn_wup.AIGuesser": [],
    "players.guesser_random.AIGuesser": [],
    "players.guesser_gpt3.AIGuesser": [],

}


def generate_args():
    arg_list = []

    const_args = ['--wordnet', 'ic-brown.dat']
    for codemaster in codemasters:
        for guesser in guessers:
            for _ in range(NUM_GAMES):
                arg_list.append(["python", "run_game.py", codemaster,
                                guesser] + codemasters[codemaster] + guessers[guesser] + const_args)

    return arg_list


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


def get_arg():
    vals = [json.loads(line)
            for line in open('results/bot_results_new_style.txt')]
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
    print("Found min matchup: ", min_matchup, vals[min_matchup])

    (codemaster, guesser) = min_matchup
    return ["python", "run_game.py", codemaster,
            guesser] + codemasters[codemaster] + guessers[guesser] + const_args


def run_game(args):
    print(args)
    subprocess.run(args)


def run_min_game(arg):
    args = get_arg()
    run_game(args)


def main():

    if len(sys.argv) > 1 and sys.argv[1] == "--human":
        arg_list = generate_args_human()
        print("Number of games planned: ", len(arg_list))
        random.shuffle(arg_list)
        pool = mp.Pool(1)
        pool.map(run_game, arg_list)

    else:
        arg_list = generate_args()
        pool = mp.Pool(3)
        pool.map(run_min_game, [0]*10000)


if __name__ == "__main__":
    main()
