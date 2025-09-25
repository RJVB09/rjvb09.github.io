import pandas as pd
import numpy as np
import random as r

dataset = pd.read_csv('hanzile/hsk3words.csv')
mask = dataset['word_simplified'].str.len() == 2
words = list(dataset[mask]['word_simplified'])

mask = (
    (dataset['word_simplified'].str.len() == 1)
)
characters = set([])

for word in words:
    characters.update(set(word))

print(len(characters))

df = pd.DataFrame(characters, columns=['character'])

df.to_csv('hanzile/characters.csv')
df.to_json('hanzile/characters.json')


# Apply the mask
mask = dataset['word_simplified'].str.len() == 2
words = dataset[mask]

# Select only the columns you want and rename them
words = words[['word_simplified', 'pinyin', 'cc_cedict_english_definition']].rename(
    columns={
        'word_simplified': 'word',
        'cc_cedict_english_definition': 'definition'
    }
)

words.to_csv('hanzile/words.csv')