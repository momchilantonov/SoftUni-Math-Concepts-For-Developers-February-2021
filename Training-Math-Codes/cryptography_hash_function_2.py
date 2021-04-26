from Crypto.Hash import MD5  # Requires Python3.5 and PyCrypto
from time import time

print(' Simple Collision Test\n', "=-=" * 5)
m1 = input("To be hashed: ")
m2 = input("To proceed: ")
m1 = m1 + "%d"
m2 = m2 + "%d"
m1 = m1.encode("ascii")
m2 = m2.encode("ascii")

i = input("To how many places? ")
i = int(i)


def make_hash(str, int):
    h = MD5.new(str % int)
    x = h.hexdigest()[:i]
    return x


h1 = ""
h2 = ""
start = time()
nonce = 0
total_attempts = 0

while True:
    nonce += 1

    h1 = make_hash(m1, nonce)
    h2 = make_hash(m2, nonce)
    if h1 == h2:
        break
    total_attempts += 1

print("Total Attempts: %s / Took %0.2f seconds" % (total_attempts, time() - start))
print(MD5.new(m1 % nonce).hexdigest())
print(MD5.new(m1 % nonce).hexdigest())
