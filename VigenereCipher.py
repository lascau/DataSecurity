import string

file = open("input.txt", "r")
plaintext = file.read()
key = str(input('Key: '))

print(plaintext)

# make key the same length as the plaintext by concatenating with key itself multiple times 
index = 0
mod = len(key)
while len(key) < len(plaintext):
	key = key + key[index]
	index = (index + 1) % mod

# encryption
start = ord('A')
encrypted_plaintext = []
for t, k in zip(plaintext, key):
	shift = ord(k) - start
	pos = start + (ord(t) - start + shift) % 26
	encrypted_plaintext.append(chr(pos))

encrypted_text = ''.join([l for l in encrypted_plaintext])
print(encrypted_text)

# decryption
start = ord('A')
decrypted_plaintext = []
for t, k in zip(encrypted_text , key):
	shift = ord(k) - start
	pos = start + (ord(t) - start - shift + 26) % 26
	decrypted_plaintext.append(chr(pos))

print(''.join([l for l in decrypted_plaintext]))
