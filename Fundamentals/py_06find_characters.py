def check_char_in_string(string, char):
    if str(string).find(char) > -1:
        return True
    else:
        return False

# define input list
word_list = ['hello', 'world', 'omy', 55, 'name', 'is', 'Anna']
search_char = "o"
new_words = []

# cycle through each word in the list
for words in word_list:
    if (check_char_in_string(words, search_char) == True):
        new_words.append(words)

print new_words
