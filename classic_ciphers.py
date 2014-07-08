message = raw_input("To encode: ").replace(' ', '').lower()
choice = raw_input("What cipher do you want to use? ")

def caesar (message, shift):
    ans = [chr(ord(c)+shift) for c in message]
    return ''.join(ans).upper()

def affine (message, a, b):
    af = lambda x: (a*x + b)%26
    ans = [chr( af(ord(c) - 97) + 97) for c in message]
    return ''.join(ans).upper()

def vignere (message, key):
    k = [ord(c) - 97 for c in key]

if choice.lower() == "caesar":
    shift = int(raw_input("Shift? (1-25): "))
    print caesar(message, shift)

elif choice.lower() == "affine":
    a, b = map(int, raw_input("a and b? (1-25): ").split())
    print affine(message, a, b)

