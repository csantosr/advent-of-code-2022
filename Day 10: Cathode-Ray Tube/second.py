inputFile = open('./input.txt', 'r')
X = 1
t = -1
cycles = 0
cycles_log = []
image = [['?' for _ in range(40)] for _ in range(6)]
# First Star
for line in inputFile:
    if line.startswith('ad'):
        add = line.split(' ')[1]
        cycles_log.append(X)
        t += 1
        image[t//40][t%40] = ('#' if abs(X-(t%40)) <= 1 else ' ')
        t += 1
        image[t//40][t%40] = ('#' if abs(X-(t%40)) <= 1 else ' ')
        X += int(add)
        cycles_log.append(X)
    else:
        cycles_log.append(X)
        t += 1
        image[t//40][t%40] = ('#' if abs(X-(t%40)) <= 1 else ' ')

log_list = (list(enumerate(cycles_log)))
for line in image:
    print(''.join(line))
inputFile.close()
