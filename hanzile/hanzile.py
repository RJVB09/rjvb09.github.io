import pandas as pd
import numpy as np
import random as r

dataset = pd.read_csv('hanzile/hsk3words.csv')
hints = ['⬛','🟨','🟩']

word_length = 2
hsk_level = 1

mask = (
    (dataset['word_simplified'].str.len() == word_length)
    & (dataset['hsk30_level'] <= hsk_level)
)
words = dataset[mask]

tries = 0
max_tries = 20

print(f'Hanzile | {max_tries} tries, {word_length} char long words ({len(words)} words), HSK {hsk_level}')
print('⬜' * word_length)

word_row = words.sample(n=1)
word_hanzi = word_row['word_simplified'].iloc[0]
word_pinyin = word_row['pinyin'].iloc[0]
word_definition = word_row['cc_cedict_english_definition'].iloc[0]

#print(word_hanzi, word_pinyin)

while tries < max_tries:
    guess = input('')
    while guess not in set(words['word_simplified']) or len(guess) != word_length:
        print('Guess must be 2 characters long and be a valid HSK 3 word.')
        print('----')
        guess = input('')
    
    result = ''
    for i, char in enumerate(guess):
        if char in word_hanzi and word_hanzi[i] == char:
            result += hints[2]
        elif char in word_hanzi and word_hanzi[i] != char:
            result += hints[1]
        else:
            result += hints[0]

    print(result)
    print('----')
    if hints[0] not in result and hints[1] not in result:
        print('You win!')
        print(word_hanzi, word_pinyin)
        print(word_definition)
        break

    tries += 1

if tries >= 5:
    print('You lose!')
    print(word_hanzi, word_pinyin)
    print(word_definition)