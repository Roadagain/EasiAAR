import sys

def translate_words(words, dictionary, after_sep = ' '):
    translated = []
    for word in words:
        if word in dictionary:
            translated.append(dictionary[word])
        else:
            translated.append(word)

    return after_sep.join(translated)

dictionary = {}
for line in open(sys.argv[1]):
    before, after = line.split()
    dictionary[before] = after

for line in sys.stdin:
    print(translate_words(line.split(), dictionary))
