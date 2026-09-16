#!/usr/bin/env python
# coding: utf-8

# In[1]:


def one_time_pad_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()

    if len(plaintext) != len(key):
        print("Error: Plaintext and key must have the same length.")
        return

    ciphertext = ""

    for p, k in zip(plaintext, key):
        if p.isalpha():
            value = (ord(p) - ord('A') + ord(k) - ord('A')) % 26
            ciphertext += chr(value + ord('A'))
        else:
            ciphertext += p

    return ciphertext
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = one_time_pad_encrypt(plaintext, key)

print("Ciphertext:", ciphertext)


# In[3]:


def brute_force_shift_cipher(ciphertext):
    ciphertext = ciphertext.upper()

    for shift in range(26):
        plaintext = ""

        for char in ciphertext:
            if char.isalpha():
                value = (ord(char) - ord('A') - shift) % 26
                plaintext += chr(value + ord('A'))
            else:
                plaintext += char

        print("Shift", shift, ":", plaintext)


ciphertext = input("Enter ciphertext: ")
brute_force_shift_cipher(ciphertext)


# In[4]:


def rail_fence_encrypt(text, rails):
    if rails <= 1:
        return text

    fence = ['' for _ in range(rails)]

    row = 0
    direction = 1

    for char in text:
        fence[row] += char

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)
text = input("Enter plaintext: ")
rails = int(input("Enter number of rails: "))

ciphertext = rail_fence_encrypt(text, rails)

print("Encrypted text:", ciphertext)


# In[ ]:




