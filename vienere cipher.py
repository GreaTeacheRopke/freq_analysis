# Python code to implement Vigenere Cipher
# This code is contributed by Pratik Somwanshi

# This function generates the key in a cyclic manner until its length is equal to the length of original text
def generateKey(plain_text, key):
    key = list(key)
    if len(plain_text) == len(key):
        return (key)
    else:
        for i in range(len(plain_text) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

# This function returns the encrypted text generated with the help of the key
def cipherText(plain_text, key):
    cipher_text = []
    for i in range(len(plain_text)):
        x = (ord(plain_text[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))

# This function decrypts the encrypted text and returns the original plain text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))

plain_text = "NUMBERTHEORYISAMAZEBALLS"
keyword = "ROPKE"
key = generateKey(plain_text, keyword)
cipher_text = cipherText(plain_text, key)
print("Ciphertext :", cipher_text)
print("Original/Decrypted Text :", originalText(cipher_text, key))


