python run_game.py human players.guesser_glove.AIGuesser --glove_guesser players/glove/glove.6B.100d.txt

python run_game.py players.codemaster_wn_lin.AICodemaster players.guesser_w2v.AIGuesser --seed 3442 --w2v players/GoogleNews-vectors-negative300.bin --wordnet ic-brown.dat

python run_game.py human players.guesser_w2v.AIGuesser --seed 3442 --w2v players/GoogleNews-vectors-negative300.bin --wordnet ic-brown.dat

python run_game.py players.codemaster_glove_07.AICodemaster human --seed 250 --glove_cm players/glove/glove.6B.50d.txt


python run_game.py players.codemaster_glove_07.AICodemaster human  --glove_cm players/glove/glove.6B.50d.txt


python run_game.py human human 


python run_game.py players.codemaster_gpt3.AICodemaster human --seed 150 


python run_game.py human players.guesser_gpt3.AIGuesser --seed 150 


python run_game.py players.codemaster_gpt3_complex.AICodemaster players.guesser_gpt3.AIGuesser

python run_game.py players.codemaster_gpt3.AICodemaster players.guesser_gpt3.AIGuesser --seed 150 


python run_game.py players.codemaster_wn_lin.AICodemaster players.guesser_w2v.AIGuesser --seed 3442 --w2v players/GoogleNews-vectors-negative300.bin --wordnet ic-brown.dat

python run_game.py players.codemaster_glove_05.AICodemaster players.guesser_glove.AIGuesser --seed 3442 --glove_cm players/glove/glove.6B.50d.txt --glove_guesser players/glove/wiki-news-300d-1M.vec


python run_game.py players.codemaster_fasttext.AICodemaster players.guesser_glove.AIGuesser --seed 3442 --glove_guesser players/glove/glove.6B.50d.txt --glove_cm players/glove/wiki-news-300d-1M.vec

