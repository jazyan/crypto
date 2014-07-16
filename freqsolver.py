from fractions import gcd

code = raw_input("To decrypt: ").lower()

freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.13001, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def caesar (message, shift):
    f = lambda x: chr((ord(x) - 97 + shift) % 26 + 97)
    ans = [f(c) for c in message]
    return ''.join(ans).lower()

def affine (message, a, b):
    f = lambda x: chr((a*(ord(x) - 97) + b) % 26 + 97)
    ans = [f(c) for c in message]
    return ''.join(ans).lower()

def vigenere (message, key):
    shift = lambda x, y: chr((ord(x) - 97 + y) % 26 + 97)
    k = [ord(c) - 97 for c in key]
    ans = [shift(message[i], k[i%len(k)]) for i in range(len(message))]
    return ''.join(ans).lower()

def letterfreq (word):
    ans = [0 for i in range(26)]
    for letter in word:
        ans[ord(letter)-97] += 1
    return [round(float(i)/float(len(word)), 5) for i in ans]

dotprod = lambda x, y: round(sum([x[i]*y[i] for i in range(len(x))]), 5)

def caesarrun (msg):
    shifts = [caesar(msg, i) for i in range(26)]
    sim = {s: dotprod(freq, letterfreq(s)) for s in shifts}
    return max(sim, key=sim.get)

def affinerun (msg):
    valid_a = [i for i in range(26) if gcd(i, 26) == 1]
    shifts = [affine(msg, a, b) for a in valid_a for b in range(26)]
    sim = {s: dotprod(freq, letterfreq(s)) for s in shifts}
    return max(sim, key=sim.get)

def shift_coinc (msg, num):
    shift = msg[:(len(msg)-num)]
    stick = msg[num:]
    return sum([1 for i in range(len(shift)) if shift[i] == stick[i]])

def key (msg, l):
    print msg, len(msg)
    ans = [0 for i in range(l)]
    for i in range(l):
        letters = [msg[x] for x in range(len(msg)) if x%l == i]
        check = [x for x in range(len(msg)) if x%l == i]
        #print letters, len(letters), check
        As = [freq[y:] + freq[:y] for y in range(len(freq))]
        shifts = [caesar(letters, k) for k in range(26)]
        dotp = [dotprod(letterfreq(s), freq) for s in shifts]
        #print i, dotp
        ans[i-1] = chr(dotp.index(max(dotp))+97)
    return ans

#def vigenererun (msg):
#find shift with most coincidences
#guess length -> guess key

l = [shift_coinc(code, i) for i in range(1, 10)]
length = l.index(max(l)) + 1
print key(code, length)

#print "CAESAR:", caesarrun(code)
#print "AFFINE:", affinerun(code)
