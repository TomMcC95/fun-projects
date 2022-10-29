from nltk.corpus import words
import pandas as pd

word_list = words.words()
print(len(word_list))

five_letter_word_original = [i.lower() for i in word_list if len(i) == 5]
print(len(five_letter_word_original))

five_letter_words_list = list(set(five_letter_word_original))
print(len(five_letter_words_list))

flw_list_list = [list(i) for i in five_letter_words_list]

pos_list = ['pos_0', 'pos_1', 'pos_2', 'pos_3', 'pos_4']
df = pd.DataFrame(data=flw_list_list, columns=pos_list)
df['score'] = 0


print(df.head())

print(df['pos_0'].value_counts().to_frame().loc['s', 'pos_0'])

for i in df.index:
    for pos in pos_list:
        letter = df.loc[i, pos]
        df.loc[i, 'score'] += df[pos].value_counts().to_frame().loc[letter, pos]

df = df.copy().sort_values(by='score', ascending=False)

print(df.head())

# THIS SCRIPT SCORES EACH OF THE REMAINING 5 WORDS

