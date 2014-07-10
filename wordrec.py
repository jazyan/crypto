import re
check = raw_input("Input your message: ").lower()

# take out punctuation and repeated words, and convert to list
d = list(set(re.findall(r"[\w']+", open('dictionary.txt', 'r').read().lower())))

d = [word for word in d if len(word) > 1]
d += ["a", "i"]

def wordrec (message):
    if message in d:
        return message
    table = [0 for i in range(len(message)+1)]
    words = [[] for i in range(len(message)+1)]
    table[0] = 1
    for j in range(1, len(message)+1):
        for i in range(j):
            if table[i] and message[i:j] in d:
                print i, j, message[i:j]
                if words[i] == []:
                    words[j].append(message[i:j])
                else:
                    for word in words[i]:
                        words[j].append(word + " " + message[i:j])
                #words[j].append(words[i] + [message[i:j]])
        if words[j] != []:
            table[j] = 1
        #words[j] = list(set(words[j] + words[j-1]))
    return words, table

print wordrec(check)
