message = raw_input("To encode: ").replace(' ', '').lower()
choice = raw_input("What cipher do you want to use? ")

def caesar (message, shift):
    f = lambda x: chr((ord(x) - 97 + shift) % 26 + 97)
    ans = [f(c) for c in message]
    return ''.join(ans).upper()

def affine (message, a, b):
    f = lambda x: chr((a*(ord(x) - 97) + b) % 26 + 97)
    ans = [f(c) for c in message]
    return ''.join(ans).upper()

def vigenere (message, key):
    shift = lambda x, y: chr((ord(x) - 97 + y) % 26 + 97)
    k = [ord(c) - 97 for c in key]
    ans = [shift(message[i], k[i%len(k)]) for i in range(len(message))]
    return ''.join(ans).upper()

if choice.lower() == "caesar":
    shift = int(raw_input("Shift? (1-25): "))
    print caesar(message, shift)

elif choice.lower() == "affine":
    a, b = map(int, raw_input("a and b? (1-25): ").split())
    print affine(message, a, b)

elif choice.lower() == "vigenere":
    key = raw_input("Key? ")
    print vigenere(message, key)
