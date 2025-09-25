import pandas as pd
import numpy as np
import random as r

dataset = pd.read_csv('hanzile/hsk3words.csv')
words = list(dataset['word_simplified'])

mask = (
    (dataset['word_simplified'].str.len() == 1)
)
characters = set([])

for word in words:
    characters.update(set(word))

print(len(characters))

df = pd.DataFrame(characters, columns=['character'])

df.to_csv('hanzile/characters.csv')