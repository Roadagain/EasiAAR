import sys
def replace(sentence, dictionary, after_sep = ' '):
    replaced = []
    for word in sentence.split():
        if word in dictionary:
            replaced.append(dictionary[word])
        else:
            replaced.append(word)

    return after_sep.join(replaced)

dictionary = {}
for line in open(sys.argv[1]):
    before, after = line.split()
    dictionary[before] = after

for line in sys.stdin:
    print(replace(line, dictionary))
