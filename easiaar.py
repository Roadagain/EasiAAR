import sys
import re

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

SPLIT_PATTERN = re.compile(r'[!]".*?"|".*?"|\S+')

for line in sys.stdin:
    translated = []
    for word in SPLIT_PATTERN.findall(line):
        unquoted = word.strip('"')
        is_banged = (re.match('^[!]".*?"', word) is not None)
        if word in dictionary:
            translated.append(dictionary[word])
        elif is_banged:
            translated.append(word[1:])
        elif word != unquoted:
            zipped = translate_words(unquoted.split(), dictionary, '')
            translated.append(zipped)
            dictionary[word] = zipped
        else:
            translated.append(word)

    print(' '.join(translated))
