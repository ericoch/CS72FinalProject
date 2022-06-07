# Final Project

## Installation Instructions

Follow the installation instructions in the [Codenames AI Competition README](README.md)

## Vector Files
4 Glove Vectors files downloadable [here](https://nlp.stanford.edu/data/glove.6B.zip) and stored in CS72FinalProjct/codenames/glove/

Google News Vectors downloadable [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) and stored in CS72FinalProjct/codenames/

WikiNews FastText Vectors downloadble [here](https://fasttext.cc/docs/en/english-vectors.html) (Choose option 1, wiki-news-300d-1M.vec.zip) and stored in CS72FinalProjct/codenames/

## GPT-3 Key
To access GPT-3 you will need Nathan Schneider's GPT-3 access key (or your own if you have one). This should be placed in this .env file by pasting this:

OPENAI_KEY={GPT-3 Key}

Into the following .env file:

CS72FinalProject/codenames/.env

For security purposes, the key will be a comment on the Canvas submission.

## Our additions to the repo

Many of the files in this repo were provided by the [Codenames AI Competition](e-codenames-ai-competition/home). 
The files added in our work are:

1. The agents we coded:

CS72FinalProject/codenames/players/guesser_random.py
CS72FinalProject/codenames/players/codemaster_random.py
CS72FinalProject/codenames/players/guesser_gpt3.py
CS72FinalProject/codenames/players/codemaster_gpt3_complex.py
CS72FinalProject/codenames/players/codemaster_gpt3.py
CS72FinalProject/codenames/players/guesser_fasttext.py

2. The evaluation tools we developed

CS72FinalProject/codenames/round_robin.py
CS72FinalProject/codenames/results/codenames_analysis.R
