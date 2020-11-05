import matplotlib.pyplot as plt

'''
1. Analiza caracteristicilor textului în clar  
Scrieți un program (de preferat în limbajul C) care să contorizeze numărul de apariții al fiecărui simbol utilizat într-un text oarecare, dat.
Afișarea rezultatului se va face atât în valoare nominală, respectiv în valoare procentuală.
Programul va primi în intrare un fișier text și va salva rezultatul tot într-un fișier text (care va conține o tabelă și/sau un grafic cu rezultatele obținute).
'''

'''
len(plaintext) ... 100%
frequency[symbol] .... x
'''


frequency = {}
size_of_text = 0

#data to be plotted
symbols = []
frequencies = []
percentages = []

file = open("input.txt", "r")
plaintext = file.read()

#print(plaintext)

for character in plaintext:
    frequency[character] = frequency.get(character, 0) + 1

for symbol in sorted(frequency.keys()):
    symbols.append(symbol)
    frequencies.append(frequency[symbol])
    percentages.append((frequency[symbol] * 100) / len(plaintext))
    #print("Symbol: %s has %d occurences" %(symbol, frequency[symbol]), sep = ' ')

# drawing based on frequencies
fig = plt.figure()
plt.bar(symbols, frequencies)
ax = fig.add_subplot(111)
ax.set_xlabel('Symbols')
ax.set_ylabel('Frequencies')
ax.set_title('Symbols-Frequencies plot')

# drawing based on percentage
fig = plt.figure()
plt.bar(symbols, percentages)
ax = fig.add_subplot(111)
ax.set_title('Symbols-Percentages plot')
ax.set_xlabel('Symbols')
ax.set_ylabel('Percentages')
plt.show()
