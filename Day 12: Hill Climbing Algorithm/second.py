from parseInput import parse_input
from findPath import get_steps

_, end, cleanMap, starts = parse_input()

paths = []

for start in starts:
    steps = get_steps(start, end, cleanMap)
    if steps is not None:
        paths.append(steps)

print(min(paths))