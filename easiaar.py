import sys

dictionary = {}
for line in open(sys.argv[1]):
    before, after = line.split()
    dictionary[before] = after

for line in sys.stdin:
    words = line.split()
    translated = []
    for word in words:
        if word in dictionary:
            translated.append(dictionary[word])
        else:
            translated.append(word)

    print(' '.join(translated))
