# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Rybcz-xTxEftR8_zvmhhXDxmVT5oDtnB

#1
**Caesar Cipher** is a method of encryption where each letter in the plaintext is shifted a certain number of places down or up the alphabet.The Caesar cipher is a type of symmetric key cipher, the same key is used for both encryption and decryption.
"""

#Encryption

def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

#Decryption

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            plaintext += char
    return plaintext

# Example usage:
plaintext = input("Enter the plaintext : ")
shift = int(input("Enter shift position: "))
encrypted_text = caesar_encrypt(plaintext, shift)
print("Encrypted text:", encrypted_text)
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)

"""**Working**

1. **Encryption**

   Defines a function "caesar_encrypt" with two parameters "plaintext, shift", then initializes an empty string "ciphertext" which will store the encrypted text. Then it starts iterating over each character in the plaintext. Then check if the character is an alphabet character. It determines whether the character is uppercase or lowercase and applies the shift accordingly using the ASCII values of the characters. Non-alphabet characters are left unchanged. Last, it returns the fully encrypted ciphertext string after the loop has processed all characters in the plaintext.

2. **Decryption**

    Defines a function "caesar_decrypt" with two parameters "ciphertext, shift" then initializes an empty string "plaintext" which will store the decrypted text. Then it starts iterating over each character in the ciphertext. Then check if the character is an alphabet character. It determines whether the character is uppercase or lowercase and applies the same shift value that was used for encryption.Then it returns the fully decrypted plaintext string after the loop has processed all characters in the ciphertext.

#2
**Vigenere cipher** is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution.It uses a keyword to determine the amount of shift for each letter.
"""

#Encryption

def Vigenere_Encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            char_num = ord(char.upper()) - ord('A')
            key_char_num = ord(key[key_index].upper()) - ord('A')
            encrypted_char = chr(((char_num + key_char_num) % 26) + ord('A'))
            ciphertext += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char

    return ciphertext

#Decryption

def Vigenere_Decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            char_num = ord(char.upper()) - ord('A')
            key_char_num = ord(key[key_index].upper()) - ord('A')
            decrypted_char = chr(((char_num - key_char_num) % 26) + ord('A'))
            plaintext += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char

    return plaintext

# Example usage
plaintext = input("Enter the plaintext : ")
key =  input("Enter a key : ")
Encrypted_text = Vigenere_Encrypt(plaintext, key)
print("Encrypted text :", Encrypted_text)

Decrypted_text = Vigenere_Decrypt(encrypted_text, key)
print("Decrypted text :", Decrypted_text)

"""**Working**

1. **Encryption**

   * Defines a function "Vigenere_Encrypt" with two parameters (plaintext, key).
   * Then initializes an empty string "ciphertext" which will store the encrypted text.
   * "key_index" is initialized to keep track of the current position of the key.
   *Then it starts iterating over each character in the plaintext.
   *Then checks if the character is alphabetic.
   *Then it convert character to uppercase and map it to 0-25 range and does same for the corresponding character in the key.
   * Then applies the Vigenere cipher
formula to encrypt the character.
 * Append the encrypted character to the ciphertext.
 * Move to the next character in the key.
 * Finally, the encrypted text is returned

2. **Decryption**

 * Defines a function "Vigenere_Decrypt" with two parameters (ciphertext, key).
 * Initializes an empty string "plaintext" to store the decrypted text.
 * Then it starts iterating over each character in ciphertext.
 * Then checks if the character is alphabetic.
 * Convert character to uppercase and map it to 0-25 range and does same for the corresponding character in the key.
 * Decrypt the character using the Vigenere cipher formula.
 * Append the decrypted character to the plaintext.
 * Move to the next character in the key.
 * Finally, the decrypted text is returned.

#3
**RSA (Rivest-Shamir-Adleman)**
"""

import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(n, k=5):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 1)
        if gcd(n, a) != 1:
            return False
        if pow(a, n - 1, n) != 1:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Example usage:
p = int(input("Enter the value of p (Prime Number): "))
q = int(input("Enter the value of q (Prime Number): "))
public_key, private_key = generate_keypair(p, q)
print("Public key :", public_key)
print("Private key:", private_key)

plaintext = input("Enter the plaintext: ")
encrypted = encrypt(public_key, plaintext)
print("Encrypted:", encrypted)

decrypted = decrypt(private_key, encrypted)
print("Decrypted:", decrypted)

"""**Working**

* import random module, which provide functions for generating random numbers.
* Then it calculates the Greatest Common Divisor(GCD) of 'a' and 'b'.
* Then calculates the modular multiplicative inverse of 'a' modulo 'm'.
* Then checks whether a number is prime. It uses the probabilistic Miller-Rabin primality test with a parameter k for accuracy.
* Then it generates an RSA key pair given two prime numbers p and q. It calculates the public key (e, n) and private key (d, n).
* Then encrypts a plaintext message using the RSA public key (e, n) and decrypts a ciphertext message using the RSA private key (d, n).

#4
**Hash**

SHA-256(Secure Hash Algorithm 256-bit)It is one of the cryptographic hash functions in the SHA-2 (Secure Hash Algorithm 2) family standardized by the National Institute of Standards and Technology (NIST). It generates a fixed-size 256-bit (32-byte) hash value from an input data of arbitrary size.
"""

import hashlib

def compute_hash(input_string):
  input_bytes=input_string.encode('utf-8')
  hash_result=hashlib.sha256(input_bytes).hexdigest()

  return hash_result

input_string=input("Enter the string : ")
hash_result=compute_hash(input_string)
print("Hash of'{}'is:  {}".format(input_string, hash_result))

