from itertools import cycle

def string_to_binary(s):
    b = []
    for c in s:
        b.append("{:08b}".format(ord(c)))
    return b

def xor_cipher(plaintext , key):
    x = []
    for t,k in zip(plaintext , cycle(key)):
        x.append(chr(ord(t) ^ ord(k)))
    return x

p = input("plaintext: ")
k = input("key: ")

encrypt = xor_cipher(p, k)

print(encrypt)
print("".join(encrypt))

#decrypt
decrypt = xor_cipher(encrypt, k)
print(decrypt)
print("".join(decrypt))
#print(" ".join(string_to_binary(plaintext)))
