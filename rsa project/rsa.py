from math import lcm, gcd
import random
from Crypto.Util import number

# key generation strategy citation: https://www.di-mgt.com.au/rsa_alg.html
def keygeneration(b):
    # set public key
    e = 253
    # random prime generation - check against e to make sure e has inverse mod lambda
    while True:
        p = number.getPrime(int(b/2))
        q = number.getPrime(int(b-b/2))
        if gcd((p-1)*(q-1),e) == 1 & q != p:
            break
    n = p * q
    # calculate private key
    lamb = lcm(p-1, q-1)
    d = pow(e, -1, lamb)
    return d, e, n

# ENCRYPT
def encrypt(message, e, n):
    # make sure numbers are stored as ints
    e = int(e)
    n = int(n)
    # encode each character separately, then put them in a list
    m = []
    for c in message:
        m.append(pow(ord(c),e,n))
    cyphertext = ""
    for i in range(len(m)):
        cyphertext = cyphertext + f'{m[i]:04}'
    # result
    return cyphertext

# DECRYPT
def decrypt(cyphertext, d, n):
    n = int(n)
    d = int(d)
    # split in groups of 4 then decode each one
    decoded = ""
    for i in range(int(len(cyphertext)/4)):
        decoded = decoded + chr(pow(int(cyphertext[4*i:4*i+4]),d,n))
    return decoded

# Apology for handling errors
from flask import redirect, render_template, request, session

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code