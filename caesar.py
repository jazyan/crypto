f = open('test.txt', 'w')
code = raw_input("To decrypt: ").lower()

def caesar (message, shift):
    f = lambda x: chr((ord(x) - 97 + shift) % 26 + 97)
    ans = [f(c) for c in message]
    return ''.join(ans).lower()

for i in range(26):
    f.write(caesar(code, i) + "\n")
