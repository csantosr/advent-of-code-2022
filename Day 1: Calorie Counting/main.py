inputFile = open('./input.txt', 'r')

elfs = [0]
for line in inputFile:
    if line == '\n':
        elfs.append(0)
    else:
        elfs[-1] += int(line)

inputFile.close()

print(max(elfs))

sortedElfs = sorted(elfs, reverse=True)

print(sum(sortedElfs[:3]))
