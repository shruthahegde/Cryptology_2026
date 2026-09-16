#!/usr/bin/env python
# coding: utf-8

# In[1]:


def shift_encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch

    return result

text = input("Enter plaintext: ")

while text.strip() == "":
    print("Error: Text cannot be empty.")
    text = input("Enter plaintext: ")

while True:
    try:
        key = int(input("Enter shift key: "))
        if 0 <= key <= 25:
            break
        print("Error: Key must be between 0 and 25.")
    except ValueError:
        print("Error: Enter a valid integer.")

print("Encrypted text:", shift_encrypt(text, key))


# In[2]:


def shift_decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - key) % 26 + base)
        else:
            result += ch

    return result


# Input validation
text = input("Enter ciphertext: ")

while text.strip() == "":
    print("Error: Ciphertext cannot be empty.")
    text = input("Enter ciphertext: ")

while True:
    try:
        key = int(input("Enter shift key : "))
        if 0 <= key <= 25:
            break
        print("Error: Key must be between 0 and 25.")
    except ValueError:
        print("Error: Enter a valid integer.")

print("Decrypted text:", shift_decrypt(text, key))


# In[3]:


def caesar_encrypt(text):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + 3) % 26 + base)
        else:
            result += ch

    return result

text = input("Enter plaintext: ")

while text.strip() == "":
    print("Error: Plaintext cannot be empty.")
    text = input("Enter plaintext: ")

print("Encrypted text:", caesar_encrypt(text))


# In[4]:


def caesar_decrypt(text):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base - 3) % 26 + base)
        else:
            result += ch

    return result
text = input("Enter ciphertext: ")

while text.strip() == "":
    print("Error: Ciphertext cannot be empty.")
    text = input("Enter ciphertext: ")

print("Decrypted text:", caesar_decrypt(text))


# In[5]:


def rot13_encrypt(text):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + 13) % 26 + base)
        else:
            result += ch

    return result

text = input("Enter plaintext: ")

while text.strip() == "":
    print("Error: Plaintext cannot be empty.")
    text = input("Enter plaintext: ")

print("Encrypted text:", rot13_encrypt(text))


# In[6]:


def rot13_decrypt(text):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + 13) % 26 + base)
        else:
            result += ch

    return result

text = input("Enter ciphertext: ")

while text.strip() == "":
    print("Error: Ciphertext cannot be empty.")
    text = input("Enter ciphertext: ")

print("Decrypted text:", rot13_decrypt(text))


# In[7]:


def atbash_encrypt(text):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr(ord('Z') - (ord(ch) - ord('A')))
        elif ch.islower():
            result += chr(ord('z') - (ord(ch) - ord('a')))
        else:
            result += ch

    return result

text = input("Enter plaintext: ")

while text.strip() == "":
    print("Error: Plaintext cannot be empty.")
    text = input("Enter plaintext: ")

print("Encrypted text:", atbash_encrypt(text))


# In[8]:


def atbash_decrypt(text):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr(ord('Z') - (ord(ch) - ord('A')))
        elif ch.islower():
            result += chr(ord('z') - (ord(ch) - ord('a')))
        else:
            result += ch

    return result

text = input("Enter ciphertext: ")

while text.strip() == "":
    print("Error: Ciphertext cannot be empty.")
    text = input("Enter ciphertext: ")

print("Decrypted text:", atbash_decrypt(text))


# In[1]:


import math


def affine_encrypt(text, a, b):
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            x = ord(ch) - base

            encrypted = (a * x + b) % 26
            result += chr(encrypted + base)
        else:
            result += ch

    return result

text = input("Enter plaintext: ")

while text.strip() == "":
    print("Error: Plaintext cannot be empty.")
    text = input("Enter plaintext: ")

while True:
    try:
        a = int(input("Enter key a: "))

        if math.gcd(a, 26) == 1:
            break

        print("Error: a must be relatively prime to 26.")

    except ValueError:
        print("Error: Enter a valid integer.")


while True:
    try:
        b = int(input("Enter key b : "))

        if 0 <= b <= 25:
            break

        print("Error: b must be between 0 and 25.")

    except ValueError:
        print("Error: Enter a valid integer.")


print("Encrypted text:", affine_encrypt(text, a, b))


# In[3]:


import math


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def affine_decrypt(text, a, b):
    result = ""
    a_inverse = mod_inverse(a, 26)

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            x = ord(ch) - base

            decrypted = (a_inverse * (x - b)) % 26
            result += chr(decrypted + base)
        else:
            result += ch

    return result


text = input("Enter ciphertext: ")

while text.strip() == "":
    print("Error: Ciphertext cannot be empty.")
    text = input("Enter ciphertext: ")

while True:
    try:
        a = int(input("Enter key a: "))

        if math.gcd(a, 26) == 1:
            break

        print("Error: a must be relatively prime to 26.")

    except ValueError:
        print("Error: Enter a valid integer.")

while True:
    try:
        b = int(input("Enter key b: "))

        if 0 <= b <= 25:
            break

        print("Error: b must be between 0 and 25.")

    except ValueError:
        print("Error: Enter a valid integer.")


print("Decrypted text:", affine_decrypt(text, a, b))


# In[ ]:




