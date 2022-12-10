inputFile = open('./input.txt', 'r')

# First Star
message = ''
for line in inputFile:
    message = line.replace('\n', '')

winner = 0
for index in range(3, len(message)):
    out = ''
    if message[index] not in out:
        out += message[index]
    if message[index-1] not in out:
        out += message[index-1]
    if message[index-2] not in out:
        out += message[index-2]
    if message[index-3] not in out:
        out += message[index-3]
    if len(out) == 4:
        winner = index + 1
        break

print(winner)
inputFile.close()
