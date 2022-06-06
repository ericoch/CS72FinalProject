import random

from players.codemaster import Codemaster
import openai

import os

openai.api_key = os.getenv('OPENAI_KEY')

setup = """
Here are instructions to play the game Codenames:

Given a list of words, a clue, and a number, determine which set of words correspond most closely to the clue. You must give a list of words that correspond with the clue, with the same number of words as the number you were given. They must be ordered from most similar to the clue to least similar. 

After the clue, say the number of words the clue applies to, from 1 to 3. If the clue applies to 3 red words, give the number 3.
For example:

red words: nut, bark, octopus, candy, birch. 
blue words: clock, bed. 
clue: tree 3

red words: worm, tower. 
blue words: lab chick fire. 
clue: building 1

red words: mouse, undertaker, stadium. 
blue words: gold, drill, fall, rock. 
clue: funeral 1

red words: nut, bark, octopus, candy. 
blue words: clock, bed, pine, maple. 
clue: food 2

red words: yarn, bottle, white, shoe, knit. 
blue words: pants, chair. 
clue: sock 3

red words: parachute, worm, theater, pants, buffalo. 
blue words: blanket, laser. 
clue: animal 2


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

        print(', '.join([w.lower() for w in self.words]))
        red_words = []
        blue_words = []
        for i in range(25):
            if self.maps[i] == "Red" and '*' not in self.words[i]:
                red_words.append(self.words[i].lower())
            elif '*' not in self.words[i]:
                blue_words.append(self.words[i].lower())

        print("RED:\t", red_words)

        prompt = "red words: %s.\nblue words: %s.\nclue:" % (
            ", ".join(red_words), ", ".join(blue_words))
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
        answer = answer.split('\n')[0].split()
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
            print("Clue is in the list of red words, defaulting to random word")
            return self.get_rand_clue()
        return clue, num

    def get_rand_clue(self):
        rand_word = self.words[0]
        while rand_word in self.words:
            rand_word = random.choice(self.cm_wordlist)
        return rand_word, 1
