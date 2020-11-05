import string

plaintext = str(input('Text: '))
key = int(input('Key: '))
encrypted_plaintext = ['0'] * len(plaintext)


for index in range(len(plaintext)):
    if plaintext[index].isupper():
        encrypted_plaintext[index] = chr(65 + (ord(plaintext[index]) - ord('A') + key) % 26)
    else:
        encrypted_plaintext[index] = chr(97 + (ord(plaintext[index]) - ord('a') + key) % 26)
    
print('Encrypted using Casaer Cipher: %s\n' %''.join(encrypted_plaintext))


# brute force all keys in order to decrypt the message

for current_key in range(26):
    message = encrypted_plaintext
    for index in range(len(message)):
        if message[index].isupper():
            message[index] = chr(65 + (ord(message[index]) - ord('A') + current_key) % 26)
        else:
            message[index] = chr(97 + (ord(message[index]) - ord('a') + current_key) % 26)
    print('Message: %s Key: %d' %(''.join(message), current_key))


