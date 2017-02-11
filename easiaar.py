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

QUOTED = re.compile(r'".*?"')
QUOTE_AS_IS = re.compile(r'[!]' + QUOTED.pattern)
OTHERWISE = re.compile(r'\S+')
WORDS = '|'.join([QUOTE_AS_IS.pattern, QUOTED.pattern, OTHERWISE.pattern])
SPLIT_PATTERN = re.compile(WORDS)
SPACE = re.compile(r'^\s*')

for line in sys.stdin:
    indent = SPACE.match(line).group()
    translated = []
    for word in SPLIT_PATTERN.findall(line):
        is_quoted = QUOTED.match(word) is not None
        is_banged = QUOTE_AS_IS.match(word) is not None
        if word in dictionary:
            translated.append(dictionary[word])
        elif is_banged:
            translated.append(word[1:])
        elif is_quoted:
            zipped = translate_words(word.strip('"').split(), dictionary, '')
            translated.append(zipped)
            dictionary[word] = zipped
        else:
            translated.append(word)

    print(indent + ' '.join(translated))
