
import multiprocessing as mp
import subprocess
import random
import sys

NUM_GAMES = 1

codemasters = {
    "players.codemaster_w2v_05.AICodemaster": ['--glove_cm', 'players/glove/glove.6B.200d.txt', '--w2v', 'players/GoogleNews-vectors-negative300.bin'],
    "players.codemaster_glove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt'],
    "players.codemaster_w2vglove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt', '--w2v', 'players/GoogleNews-vectors-negative300.bin'],
    # "players.codemaster_w2vglove_03.AICodemaster":  ['--glove_cm', 'players/glove/wiki-news-300d-1M.vec'],
    # "players.codemaster_glove_07.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.300.txt'],
    "players.codemaster_wn_lin.AICodemaster": [],
    "players.codemaster_random.AICodemaster": [],
    "players.codemaster_gpt3.AICodemaster": [],
    "players.codemaster_gpt3_complex.AICodemaster": []


    # "players.codemaster_w2v_05.AICodemaster": ['--glove_cm', 'players/glove/glove.6B.200d.txt'],
    # "players.codemaster_glove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt'],
    # "players.codemaster_w2vglove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt'],
    # "players.codemaster_w2vglove_03.AICodemaster":  ['--glove_cm', 'players/glove/wiki-news-300d-1M.vec'],
    # "players.codemaster_glove_07.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.300.txt'],
    # "players.codemaster_wn_lin.AICodemaster": [],
    # "players.codemaster_random.AICodemaster": []
}

guessers = {
    # "players.guesser_glove.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    # "players.guesser_w2vglove.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_w2v.AIGuesser": ['--w2v', 'players/GoogleNews-vectors-negative300.bin', '--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_glove.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_w2vglove.AIGuesser": ['--w2v', 'players/GoogleNews-vectors-negative300.bin', '--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    # "players.guesser_wn_jcn.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_wn_lch.AIGuesser": [],
    # "players.guesser_wn_lin.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_wn_path.AIGuesser": [],
    # "players.guesser_wn_res.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_wn_wup.AIGuesser": [],
    # "players.vector_guesser.VectorGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
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


def run_game(args):
    print(args)
    subprocess.run(args)


def main():

    if len(sys.argv) > 1 and sys.argv[1] == "--human":
        arg_list = generate_args_human()
        pool = mp.Pool(1)

    else:
        arg_list = generate_args()
        pool = mp.Pool(3)

    print("Number of games planned: ", len(arg_list))
    random.shuffle(arg_list)

    pool.map(run_game, arg_list)


if __name__ == "__main__":
    main()
