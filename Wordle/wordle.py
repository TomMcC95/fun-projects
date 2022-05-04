from nltk.corpus import words

word_list = words.words()

five_letter_words_original = []

for w in word_list:
    if len(w) == 5:
        five_letter_words_original.append(w.lower())

five_letter_words_set = set(five_letter_words_original)

pos_0 = 'a'
pos_1 = 'r'
pos_2 = ''
pos_3 = ''
pos_4 = ''

pos_list = [pos_0, pos_1, pos_2, pos_3, pos_4]

wrong_letters = ['i', 'd', 'u', 'c', 't', 's', 'n']
correct_letters = ['o']

five_letter_words = list(five_letter_words_set)

for i in range(5):

    if len(pos_list[i]) == 1:
        for word in five_letter_words_set:
            if word[i] != pos_list[i]:
                try:
                    five_letter_words.remove(word)
                except:
                    pass
                    
for j in range(5):
    
    for word in five_letter_words_set:
        if word[j] in wrong_letters:
            try:
                five_letter_words.remove(word)
            except:
                pass
            
for k in correct_letters:
    for word in five_letter_words_set:
        if k not in word:
            try:
                five_letter_words.remove(word)
            except:
                pass
            
    
                    
five_letter_words.sort()

print(five_letter_words)