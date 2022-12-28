def parsing_input():
    with open('input.txt') as file:
        lines = [line.strip() for line in file.readlines()]

    def parse_tuple(term):
        x, y = term.split(', ')
        return (int(x[2:]), int(y[2:]))

    sensors = []
    beacons = []

    for line in lines:
        sensor, beacon = line.split(': closest beacon is at ')
        sensor = sensor[10:]
        sensor = parse_tuple(sensor)
        sensors.append(sensor)
        beacon = parse_tuple(beacon)
        beacons.append(beacon)

    return sensors, beacons