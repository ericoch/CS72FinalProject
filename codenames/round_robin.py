
import multiprocessing as mp
import subprocess
import random
import sys

NUM_GAMES = 2

codemasters = {
    "players.codemaster_w2v_05.AICodemaster": ['--glove_cm', 'players/glove/glove.6B.200d.txt'],
    "players.codemaster_glove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt'],
    "players.codemaster_w2vglove_05.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.200d.txt'],
    # "players.codemaster_w2vglove_03.AICodemaster":  ['--glove_cm', 'players/glove/wikipedia-news-300d-1M.vec'],
    "players.codemaster_glove_07.AICodemaster":  ['--glove_cm', 'players/glove/glove.6B.300.txt'],
    "players.codemaster_wn_lin.AICodemaster": [],
    "players.codemaster_random.AICodemaster": []
}

guessers = {
    "players.guesser_w2v.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_glove.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_w2vglove.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    # "players.guesser_wn_jcn.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_wn_lch.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    # "players.guesser_wn_lin.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_wn_path.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    # "players.guesser_wn_res.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_wn_wup.AIGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.vector_guesser.VectorGuesser": ['--glove_guesser', 'players/glove/glove.6B.300d.txt'],
    "players.guesser_random.AIGuesser": []
}


def get_arg_list():
    arg_list = []
    counter = 250

    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_w2v_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove", "players/glove/glove.6B.300d.txt",
                         "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_w2v_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove", "players/glove/glove.6B.300d.txt",
                         "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_w2v_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove", "players/glove/glove.6B.300d.txt",
                         "--seed", str_counter])
        counter += 50

    # glove300_thresholds vs w2vglove300 (GLOVE V GLOVE)
    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    # glove200_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    # glove100_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    # glove50_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(["python", "run_game.py", "players.codemaster_glove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
                         "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    # w2vglove300_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    # w2vglove200_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    # w2vglove100_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    # w2vglove50_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    counter = 250
    for i in range(NUM_GAMES):
        str_counter = str(int(counter))
        arg_list.append(
            ["python", "run_game.py", "players.codemaster_w2vglove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
             "--glove_guesser", "players/glove/glove.6B.300d.txt", "--seed", str_counter])
        counter += 50

    return arg_list


def generate_args():
    arg_list = []

    const_args = ['--w2v', 'players/GoogleNews-vectors-negative300.bin',
                  '--wordnet', 'ic-brown.dat']
    for codemaster in codemasters:
        for guesser in guessers:
            for _ in range(NUM_GAMES):
                arg_list.append(["python", "run_game.py", codemaster,
                                guesser] + codemasters[codemaster] + guessers[guesser] + const_args)

    return arg_list


def generate_args_human():
    arg_list = []
    const_args = ['--w2v', 'players/GoogleNews-vectors-negative300.bin',
                  '--wordnet', 'ic-brown.dat']

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

    if sys.argv[1] == "--human":
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
