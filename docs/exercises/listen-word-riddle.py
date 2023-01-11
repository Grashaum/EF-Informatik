ALPHABET = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
MESSAGE = [12, 9, 19, 20, 0, 18, 9, 4, 4, 12, 5]

text = ''
for i in MESSAGE:
    text = text + ALPHABET[i]

print(text)


for msg in MESSAGE:
    print(ALPHABET[msg], end='')