from sensor import Sensor

def parsing_input():
    with open('input.txt') as file:
        lines = [line.strip() for line in file.readlines()]

    def parse_tuple(term):
        x, y = term.split(', ')
        return (int(x[2:]), int(y[2:]))

    sensors = []
    beacons = []
    sensors_ints = []

    for line in lines:
        sensor_tp, beacon_tp = line.split(': closest beacon is at ')
        sensor_tp = sensor_tp[10:]
        sensor_tp = parse_tuple(sensor_tp)
        sensors.append(sensor_tp)
        beacon_tp = parse_tuple(beacon_tp)
        beacons.append(beacon_tp)
        sensors_ints.append(Sensor(sensor_tp, beacon_tp))

    return sensors, beacons, sensors_ints