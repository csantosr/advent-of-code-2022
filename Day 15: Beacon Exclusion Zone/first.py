from parsing import parsing_input
from sensor import get_interesting_sensors, Sensor

sensors, beacons, sensors_ints = parsing_input()

search_row = 2000000

interesting_sensors = get_interesting_sensors(search_row, sensors_ints)

print('interesting', len(interesting_sensors))

leftest = 10000000000000
rightest = -10000000000000
for interesting_sensor in interesting_sensors:
    leftest_sensor = interesting_sensor.get_leftest_point(search_row)
    rightest_sensor = interesting_sensor.get_rightest_point(search_row)
    if leftest_sensor < leftest:
        leftest = leftest_sensor
    if rightest_sensor > rightest:
        rightest = rightest_sensor
print(leftest, rightest)
leftest -= 1
rightest += 1
unusable = set()
for x in range(leftest, rightest):
    for interesting_sensor in interesting_sensors:
        point = (x, search_row)
        if interesting_sensor.is_point_contained(point) and point not in beacons:
            unusable.add(point)

print(len(unusable))