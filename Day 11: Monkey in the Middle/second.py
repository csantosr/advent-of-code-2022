import copy
inputFile = open('./input.txt', 'r')
monkeys = []
current_monkey = 0
# First Star
for line in inputFile:
    if len(monkeys) < current_monkey + 1:
        monkeys.append({})
    if line == '\n' :
        current_monkey += 1
    else:
        if line.startswith('  Star'):
            items = line[18:-1].split(', ')
            monkeys[current_monkey]['items'] = list(map(lambda x: int(x), items))
        elif line.startswith('  Oper'):
            monkeys[current_monkey]['operation'] = line[19:-1]
        elif line.startswith('  Tes'):
            monkeys[current_monkey]['divisor'] = int(line[21:-1])
        elif line.startswith('    If tr'):
            monkeys[current_monkey]['true'] = int(line[29:-1])
        elif line.startswith('    If fa'):
            monkeys[current_monkey]['false'] = int(line[30:])

general_mod = 1

for monkey in monkeys:
    monkey['test'] = lambda x: monkey['true'] if x%monkey['divisor']==0 else monkey['false']
    monkey['inspected'] = 0
    general_mod *= monkey['divisor']

for round in range(0,10000):
    print(round)
    for idx, monkey in enumerate(monkeys):
        for item in copy.deepcopy(monkey['items']):
            worry = (lambda old: eval(monkey['operation']))(item)
            # worry //= 3
            monkeys[idx]['items'].remove(item)
            monkeys[idx]['inspected'] += 1
            monkeys[monkey['test'](worry)]['items'].append(worry % general_mod)

inspected = []
for idx, monkey in enumerate(monkeys):
    inspected.append(monkey['inspected'])
    print('Monkey {} inspected {}'.format(idx, monkey['inspected']))
max1 = max(inspected)    
print('max', max1)
inspected.remove(max(inspected))
max2 = max(inspected)
print('max2', max2)

print('RESULT', max1*max2)
inputFile.close()
