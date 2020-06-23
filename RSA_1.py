AlphabetNumbers = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
'i':9, 'j':10, 'k':11,'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18,
's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, ' ':27}

AlphabetNumbers2 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h',
9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r',
19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z', 27:' '}

# import random

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p % q
    return p


def keys(p, q):
    d = 1
    e = 2
    if gcd(p, q) != 1:
        return 'error numbers are not prime'
    n = p * q
    phi = (p - 1) * (q - 1)

    while gcd(e, phi) != 1:
        e += 1
    public = e
    public2 = n
    while d * e % phi != 1:
        d += 1
    private = d
    private2 = n
    return public, public2, private, private2

def encrypt(public, public2, word):
    container = []
    for char in word:
        pointer = AlphabetNumbers[char]
        pointer = pointer ** public % public2
        container.append(pointer)
    return container

def decrypt(private, private2, container):
    newContainer = []
    for number in container:
        pointer = number ** private % private2
        pointer = str(AlphabetNumbers2[pointer])
        newContainer.append(pointer)
    return newContainer


public, public2, private, private2 = keys(23,13)
print(public, public2, private, private2)
print(keys(23,13))
print(encrypt(public, public2, 'hello world'))
print(decrypt(private, private2, encrypt(public, public2, 'hello world')))

