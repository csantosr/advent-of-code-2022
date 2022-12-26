from parseInput import parse_input
from findPath import get_steps

start, end, cleanMap = parse_input()

print(get_steps(start, end, cleanMap))