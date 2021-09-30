import random
import binascii
import time
import string

random.seed(time.time())
def get_rand_str():
    letters = string.ascii_lowercase
    length = random.randint(1, 50)
    return "".join(random.choice(letters) for i in range (length))

hashes = {}
start_time = time.time()
while True: 
    x = get_rand_str()
    hash_code = binascii.crc32(x.encode('utf8'))
    if hashes.get(hash_code) != None and hashes.get(hash_code) != x:
        end_time = time.time()
        print("X: {}".format(x))
        print("Y: {}".format(hashes.get(hash_code)))
        print("Hash Code: {}".format(hash_code))
        print("Total Time: {}".format(end_time - start_time))
        break
    hashes[hash_code] = x

        

