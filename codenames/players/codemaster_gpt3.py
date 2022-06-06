import random

from players.codemaster import Codemaster
import openai

openai.api_key = "sk-4M4PNISyEDZCz4KSK4gjcv49t63bEXQrLC4bT83R"

setup = """
Here are instructions to play the game Codenames:

Given a list of words, come up with a single new word that describes as many words as possible. The clue must be a single word that is not in the list of words. Also, say the number of words the clue applies to. 
For example:

words: nut, bark, octopus, candy. clue: tree 3
words: yarn, bottle, white, shoe, knit. clue: sock 4
words: parachute, worm, theater, pants, buffalo: clue: animal 2

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

        red_words = []
        for i in range(25):
            if self.maps[i] == "Red" and '*' not in self.words[i]:
                red_words.append(self.words[i].lower())

        prompt = "words: %s. clue:" % ", ".join(red_words)
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
        answer = response['choices'][0]['text'].strip().lower()
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
