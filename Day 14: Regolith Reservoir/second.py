with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

blocked_steps = set()
# First Star
for line in lines:
    steps = list(
        map(lambda s: tuple(map(lambda n: int(n), s.split(','))), line.split(' -> ')))
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

minX = minY = 10000
maxX = maxY = 0
for block in blocked_steps:
    if block[0] < minX:
        minX = block[0]
    if block[0] > maxX:
        maxX = block[0]
    if block[1] < minY:
        minY = block[1]
    if block[1] > maxY:
        maxY = block[1]
minY = -1
maxY += 1
minX -= 50
maxX += 50
for y in range(minY, maxY):
    for x in range(minX, maxX):
        print('#' if (x, y) in blocked_steps else '.', end='')
    print('')
for x in range(minX, maxX):
    print('#', end='')
print()

sand_resting = set()
finished = False
while not finished:
    unit = (500, minY)
    resting = False
    while not resting:
        if unit[1] >= maxY:
            resting = True
            sand_resting.add(unit)
            break
        if (unit[0], unit[1] + 1) not in blocked_steps.union(sand_resting):
            unit = (unit[0], unit[1] + 1)
            continue
        if (unit[0]-1, unit[1] + 1) not in blocked_steps.union(sand_resting):
            unit = (unit[0]-1, unit[1] + 1)
            continue
        if (unit[0]+1, unit[1] + 1) not in blocked_steps.union(sand_resting):
            unit = (unit[0]+1, unit[1] + 1)
            continue
        resting = True
    sand_resting.add(unit)
    if (500,0) in sand_resting:
        finished = True

for y in range(minY, maxY+1):
    for x in range(minX, maxX):
        print('#' if (x, y) in blocked_steps else 'o' if (x,y) in sand_resting else '.', end='')
    print('')
for x in range(minX, maxX):
    print('#', end='')
print()

print(len(sand_resting))