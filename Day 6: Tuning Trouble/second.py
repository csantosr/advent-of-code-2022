inputFile = open('./input.txt', 'r')

# First Star
message = ''
for line in inputFile:
    message = line.replace('\n', '')

winner = 0
for index in range(13, len(message)):
    out = ''
    for offset in range(14):
        if message[index-offset] not in out:
            out += message[index-offset]
    if len(out) == 14:
        winner = index + 1
        break

print(winner)
inputFile.close()
