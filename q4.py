import binascii
import time

start_time = time.time()
x = "205F61F081602EE5B33A9F3E8EE8E968"
hash_code = binascii.crc32(x.encode('utf8'))

for y in range(0, 4294967295):
    if hash_code == binascii.crc32(y.to_bytes(4, 'big')):
        end_time = time.time()
        print("X: {}".format(x))
        print("Y: {}".format(y))
        print("Y bits: {}".format(bin(64)))
        print("Y Bytes: {}".format(y.to_bytes(8, 'big')))
        print("Hash Code: {}".format(hash_code))
        print("Total Time: {}".format(end_time - start_time))
        break