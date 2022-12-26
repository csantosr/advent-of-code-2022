inputFile = open('./input.txt', 'r')
X = 1
cycles = 0
cycles_log = []
# First Star
for line in inputFile:
    if line.startswith('ad'):
        add = line.split(' ')[1]
        cycles_log.append(X)
        X += int(add)
        cycles_log.append(X)
    else:
        cycles_log.append(X)

log_list = (list(enumerate(cycles_log)))
result = 0

print(log_list[20-2])
result += log_list[20-2][1] * 20
print(log_list[60-2])
result += log_list[60-2][1] * 60
print(log_list[100-2])
result += log_list[100-2][1] * 100
print(log_list[140-2])
result += log_list[140-2][1] * 140
print(log_list[180-2])
result += log_list[180-2][1] * 180
print(log_list[220-2])
result += log_list[220-2][1] * 220

print(result)

inputFile.close()
