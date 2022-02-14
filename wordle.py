from nltk.corpus import words
word_list = words.words()
# prints 236736
print(len(word_list))

for w in word_list:
    if len(w) != 5:
        word_list.remove(w)

print(len(word_list))

pos_1 = ''
pos_2 = 'b'
pos_3 = 'bb'
pos_4 = ''
pos_5 = ''

print(len(pos_1))
print(len(pos_2))
print(len(pos_3))

possible_word_list = []