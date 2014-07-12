import re
import sys
from collections import Counter

# read lines to decode from arg1, store the ans in arg2
fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')
words = fin.readlines()
words = [s.strip("\n") for s in words]

ctr = Counter()

# take out punctuation and repeated words, and convert to list
d = re.findall(r"[\w]+", open('big.txt', 'r').read().lower())
# only keep common short words
short = ["i", "a", "ab", "ad", "am", "an", "as", "at", "ax", "be", "by",
         "do", "ex", "go", "he", "hi", "id", "if", "in", "is", "it",
         "ma", "me", "my", "no", "of", "oh", "ok", "on", "op", "or",
         "ow", "ox", "pa", "pi", "qi", "so", "up", "us", "we", "yo"]
d = [w for w in d if len(w) > 2 or w in short]

# count the frequency of each word
for word in d:
    ctr[word] += 1
d = dict(ctr)

# dynamic programming to find words in message
def findwords (message):
    if message in d:
        return message
    table = [0 for i in range(len(message)+1)]
    words = [[] for i in range(len(message)+1)]
    table[0] = 1
    for j in range(1, len(message)+1):
        for i in range(j):
            if table[i] and message[i:j] in d:
                if words[i] == []:
                    words[j].append(message[i:j])
                else:
                    for word in words[i]:
                        words[j].append(word + " " + message[i:j])
        if words[j] != []:
            table[j] = 1
    return words[-1]

# choose the message with the greatest sum of word frequency
def score (m):
    words = re.sub("[^\w]", " ", m).split()
    freq = [d[word] for word in words]
    ans = sum(freq)

def run (results):
    if results != []:
        if type(results) == str:
            return results
        scores = {x : score(x) for x in results}
        return max(scores, key=scores.get)
    else:
        return "No words recognized"

for i in range(len(words)):
    fout.write(str(i) + ": " + run(findwords(words[i])) + "\n")
