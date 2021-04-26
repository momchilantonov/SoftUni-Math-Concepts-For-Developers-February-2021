from hashlib import blake2b
from itertools import product
from string import ascii_letters
import time

# Hash size in bytes.
HASH_SIZE = 3
# Number of trails.
TRAILS = 100
# Number of letters by word
WORD_LENGTH = 3


def find_collisions():
    generate_dictionary()
    # Use set for faster search of hashes.
    hash_set = set()
    print("-- Hashing started --")
    # Set start time to measure collision.
    start_time = time.time()
    # The input message.
    collision_count = 0
    total_duration = 0
    file = open('dictionary.txt', 'r')

    for msg in file:
        # Delete \n at the end of string.
        msg = msg.rstrip()
        # Message in bytes.
        byte_str = msg.encode()
        # Hash object constructor, with hash length=3 bytes (24 bits).
        digest = blake2b(byte_str, digest_size=HASH_SIZE)
        # Generate the message digest.
        hashed_msg = digest.hexdigest()

        if hashed_msg in hash_set:
            # Get collision time duration.
            duration = time.time() - start_time
            print(f"Found a collision - word: {msg} -> hash: {hashed_msg} in {duration} seconds.")
            # Empty the hash in every collision.
            hash_set = set()
            # Restart timer.
            start_time = time.time()
            collision_count += 1
            total_duration += duration

        if collision_count == TRAILS:
            total_duration = total_duration / TRAILS
            print(f"Collisions found: {TRAILS}")
            print(f"Average collision found time : {total_duration} seconds.")
            return

        # Adds a new hash value to the set.
        hash_set.add(hashed_msg)

    if collision_count != 0:
        total_duration = total_duration / collision_count
        print(f"Collisions found: {collision_count}")
        print(f"Average collision found time: {total_duration} seconds.")
    else:
        print("No collisions found!")


# Generate a dictionary file. If it already exist, then only reads from it.
def generate_dictionary():
    try:
        # Check if the dictionary file exist.
        file = open('dictionary.txt', 'r')
        print("Opening dictionary ...")
        file.close()
        return
    except IOError:
        print("Generating dictionary ...")

    file = open('dictionary.txt', 'w')

    # All possible combinations of n=WORD_LENGTH letters.
    for i in product(ascii_letters, repeat=WORD_LENGTH):
        file.write(''.join(i) + '\n')
    file.close()


find_collisions()
