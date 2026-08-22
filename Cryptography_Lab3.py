#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("Welcome to Cryptology Lab")
message = "Python Programming"
print(message)
num = int(input("Enter a number: "))
result = num + 10
print(result)


# In[15]:


print("Welcome to Cryptology Lab\n It's interesting to learn Python.\n Students,\"Welcome to the Cryptology Lab\".")


# In[17]:


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("The Addition is =", a + b)
print("The Subtraction is =", a - b)
print("The Multiplication is =", a * b)
print("The Division is =", a / b)
print("The Integer Division is =", a // b)
print("The Remainder is=", a % b)
print("The Exponentiation is =", a ** b)


# In[19]:


num = float(input("Enter a floating number: "))

print("Data type:", type(num))
print("Absolute value:", abs(num))
print("Rounded:", round(num, 2))


# In[21]:


a = 10
b = 3.14
c = 2 + 5j
d = "Shrutha"
e = [1, 2, 3]
f = (4, 5, 6)
g = {7, 8, 9}
h = {"Month": "August", "Year": 2026 }

variables = [a, b, c, d, e, f, g, h]

for i in variables:
    print(i, type(i))


# In[25]:


# Immutable
text = "HELLO"

text = "YELLO"
#will overwrite the previous value and wont add it 
print(text)

# Mutable
numbers = [1, 2, 3]
numbers.append(4)
#will add the value to the existing list 
print(numbers) 


# In[33]:


Prime_numbers=[2,3,5,7,11]
print("First three prime numbers: ",Prime_numbers[:3])
print("last prime numbers: ",Prime_numbers[-1])
Prime_numbers.append(13)
print(Prime_numbers)
Prime_numbers.extend([17,19])
print(Prime_numbers)
print("Total number of elements:",len(Prime_numbers))



# In[35]:


message="CRYPTOLOGY USING PYTHON"
print("length of the string is:",len(message))
print("first five characters:",message[:5])
print("last six characters:",message[-6:])
print("characters from positions 3 to 8:",message[3:9])
print("string in reverse order:",message[::-1])


# In[36]:


message="CRYPTOLOGY USING PYTHON"
print(message.lower())
print(message.upper())

print("PYTHON" in message)

print(message.replace("PYTHON", "PROGRAMMING"))


# In[37]:


message="CRYPTOLOGY USING PYTHON"
print(message.replace(" ",""))


# In[38]:


message="CRYPTOLOGY USING PYTHON"
for ch in message:
    print(ch,"->",ord(ch))


# In[39]:


values = [65, 67, 73, 80, 72, 69, 82]
word=""
for i in values:
    word+=chr(i)
print(word)   


# In[41]:


message = input("Enter message: ")

message = message.strip()
message = message.upper()
message = message.replace(" ", "")

print(message)


# In[44]:


text=input("enter a string:")
for i in range(0,len(text),5):
    print(text[i:i+5])


# In[45]:


text = input("Enter text: ")

while len(text) % 5 != 0:
    text += "X"

for i in range(0, len(text), 5):
    print(text[i:i+5])


# In[46]:


text = "CRYPTOLOGYISINTERESTING"
freq = {}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
print(freq)
highest = max(freq, key=freq.get)
print("Most frequent:", highest)


# In[47]:


text = "CRYPTOLOGYISINTERESTING"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

total = len(text)

for ch in freq:
    percent = (freq[ch] / total) * 100
    print(ch, ":", round(percent, 2), "%")


# In[48]:


print(29 % 26)
print(55 % 26)
print(78 % 26)
print(-3 % 26)
print(-29 % 26)

num = int(input("Enter number: "))
print("Modulo 26 =", num % 26)


# In[51]:


ch = input("Enter uppercase letter: ")

print(ch, "->", ord(ch) - 65)

num = int(input("Enter number: "))

print(num, "->", chr(num + 65))


# In[56]:


num=int(input("enter a number:"))
prime= True
if num<=1:
    prime=False
else:
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            prime=False
            break
if prime:
    print("Prime")
else:
    print("Not Prime")
start = int(input("Start: "))
end = int(input("End: "))

for n in range(start, end + 1):
    if n > 1:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:    
            print(n)
    
    
    
    


# In[57]:


import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

g = math.gcd(a, b)

print("GCD =", g)

if g == 1:
    print("Coprime")
else:
    print("Not Coprime")


# In[62]:


b = int(input("Enter integer: "))

for x in range(1, 26):
    if (b * x) % 26 == 1:
        print("Multiplicative inverse =", x)
        break
else:
    print("Inverse does not exist")






