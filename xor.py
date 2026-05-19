plaintext = "save my world!!"

def string_to_binary(s):
    b = []
    for c in s:
        b.append("{:08b}".format(ord(c)))
    return b

print(" ".join(string_to_binary(plaintext)))
