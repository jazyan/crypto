code = raw_input("To decrypt: ").lower()

freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.13001, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def caesar (message, shift):
    f = lambda x: chr((ord(x) - 97 + shift) % 26 + 97)
    ans = [f(c) for c in message]
    return ''.join(ans).lower()

def letterfreq (word):
    ans = [0 for i in range(26)]
    for letter in word:
        ans[ord(letter)-97] += 1
    return [round(float(i)/float(len(word)), 5) for i in ans]

dotprod = lambda x, y: sum([x[i]*y[i] for i in range(len(x))])

def run(msg):
    shifts = [caesar(msg, i) for i in range(26)]
    sim = {s: dotprod(freq, letterfreq(s)) for s in shifts}
    return max(sim, key=sim.get)

print run(code)
