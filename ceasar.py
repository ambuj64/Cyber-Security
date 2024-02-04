# Task-01
# "Implement Caesar Cipher!"
# "create a python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a massage and a shift value to perform encryption and decryption."
#
#
#

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key  : {chars}")

#ENCRYPT
plain_text = input("Enter a massage to encrypt: ")
Cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    Cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {Cipher_text}")   


#DECRYPT
Cipher_text = input("Enter a massage to encrypt: ")
plain_text = ""

for letter in Cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"decrypted message: {Cipher_text}")
print(f"original message: {plain_text}") 