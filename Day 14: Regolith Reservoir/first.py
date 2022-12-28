with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

blocked_steps = set()
# First Star
for line in lines:
    steps = list(map(lambda s: tuple(map(lambda n: int(n), s.split(','))), line.split(' -> ')))
    for idx in range(len(steps)-1):
        if steps[idx][0] == steps[idx+1][0]:
            for y_blocked in range(steps[idx][1], steps[idx+1][1], 1 if steps[idx+1][1] > steps[idx][1] else -1):
                blocked_steps.add((steps[idx][0], y_blocked))
            blocked_steps.add(steps[idx+1])
        else:
            for x_blocked in range(steps[idx][0], steps[idx+1][0], 1 if steps[idx+1][0] > steps[idx][0] else -1):
                blocked_steps.add((x_blocked, steps[idx][1]))
            blocked_steps.add(steps[idx+1])

print(list(blocked_steps))

minX=minY=10000
maxX=maxY=0
for block in blocked_steps:
    if block[0] < minX:
        minX = block[0]
    if block[0] > maxX:
        maxX = block[0]
    if block[1] < minY:
        minY = block[1]
    if block[1] > maxY:
        maxY = block[1]
for y in range(minY-5, maxY+5):
    for x in range(minX-5, maxX+5):
        if x == 500:
            print('o', end='')
        else:
            print('#' if (x,y) in blocked_steps else '.', end='')
    print('')