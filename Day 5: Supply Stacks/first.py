inputFile = open('./input.txt', 'r')


# First Star
def parse_command(sentence):
    return list(map(lambda x: int(x), sentence.replace('move ', '').replace(' from', '').replace(' to', '').split()))


stacks = []
commands = []
stacks_set = False
before_commands = True
lines = inputFile.readlines()
for index, line in enumerate(lines):
    if before_commands:
        if not stacks_set:
            for _ in range(len(line)//4):
                stacks.append([])
            stacks_set = True
        for indexFragment, fragment in enumerate(line):
            if indexFragment % 4 == 1 and fragment != ' ':
                if stacks[indexFragment//4]:
                    stacks[indexFragment // 4].append(fragment)
                else:
                    stacks[indexFragment // 4] = [fragment]
    else:
        commands.append(parse_command(line.replace('\n', '')))

    if line == '\n':
        before_commands = False

for index in range(len(stacks)):
    stacks[index].pop()
    stacks[index].reverse()

print(stacks)
print(commands)

for command in commands:
    for _ in range(command[0]):
        stacks[command[2]-1].append(stacks[command[1]-1].pop())

print(stacks)
print(commands)

for stack in stacks:
    print(stack[-1], end='')