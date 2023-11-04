import random
import string

#including all possible values from string class
chars=string.ascii_letters+string.digits+string.whitespace+string.punctuation
chars=list(chars) # typecasting string to list
key=chars.copy()  # the sting can be used as key but should shuffle it using .shuffle() method
random.shuffle(key)

# print(f"chars:{chars}")
# print(f"key:{key}")

#Encryption
plain_text=input("Enter the message:")
cipher_text=""
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index] # cipher_text=cipher_text+key[index]
print(f"Original message:{plain_text}")
print(f"Encrypted message:{cipher_text}")

#Decryption
cipher_text=input("Enter the cipher_text:")
plain_text=""
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index] # plain_text=plain_text+chars[index]
print(f"decrypted message:{plain_text}")
