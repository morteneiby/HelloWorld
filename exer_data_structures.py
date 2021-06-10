from pprint import pprint

sentence = "This is a common interview question"
char = {}
for ch in sentence.lower():
    if ch in char:
        char[ch] += 1
    else:
        char[ch] = 1


pprint(char, width=1)