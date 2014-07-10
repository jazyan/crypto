import re
from collections import Counter

ctr = Counter()
check = raw_input("Input your message: ").lower()

# take out punctuation and repeated words, and convert to list
d = re.findall(r"[\w]+", open('big.txt', 'r').read().lower())
short = ["i", "a", "ab", "ad", "am", "an", "as", "at", "ax", "be", "by",
         "do", "ex", "go", "he", "hi", "id", "if", "in", "is", "it",
         "ma", "me", "my", "no", "of", "oh", "ok", "on", "op", "or",
         "ow", "ox", "pa", "pi", "qi", "so", "up", "us", "we", "yo"]
d = [w for w in d if len(w) > 2 or w in short]
d += ["a", "i"]
for word in d:
    ctr[word] += 1

d = dict(ctr)

def wordrec (message):
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

def score (m):
    words = re.sub("[^\w]", " ", m).split()
    freq = [d[word] for word in words]
    ans = sum(freq)

scores = {x : score(x) for x in wordrec(check)}
message = min(scores, key=scores.get)
print message
