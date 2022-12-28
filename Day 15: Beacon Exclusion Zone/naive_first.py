from parsing import parsing_input
from util import get_blocked

sensors, beacons = parsing_input()

blocked = set()

for idx in range(len(sensors)):
    blocked = blocked.union(get_blocked(sensors[idx], beacons[idx]))

blocked_in_2000000 = set()
for block in blocked:
    if block[1] == 2000000 and block not in beacons:
        blocked_in_2000000.add(block)

print(len(blocked_in_2000000))

# sensor = (5,5)
# beacon = (5,0)

# blocked = get_blocked(sensor, beacon)

# for y in range(10):
#     for x in range(10):
#         if (x,y) == sensor:
#             print('S', end='')
#         elif (x,y) == beacon:
#             print('B', end='')
#         elif (x,y) in blocked:
#             print('#', end='')
#         else:
#             print('.', end='')
#     print()
        