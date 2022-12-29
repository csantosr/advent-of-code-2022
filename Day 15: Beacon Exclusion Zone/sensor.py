from util import manhattan

class Sensor:
    def __init__(self, sensor, beacon) -> None:
        self.sensor = sensor
        self.distance = manhattan(sensor, beacon)

        self.top = (sensor[0], sensor[1]-self.distance)
        self.bottom = (sensor[0], sensor[1]+self.distance)
        self.left = (sensor[0]-self.distance, sensor[1])
        self.right = (sensor[0]+self.distance, sensor[1])
    
    def is_row_contained(self, row):
        return self.top[1] <= row <= self.bottom[1]
    
    def is_point_contained(self, point):
        return manhattan(self.sensor, point) <= self.distance
    
    def get_leftest_point(self, row):
        if row == self.left[1]:
            return self.left[0]
        if row == self.top[1]:
            return self.top[0]
        if row == self.bottom[1]:
            return self.bottom[0]
        p1 = self.bottom
        p2 = self.left
        if row < self.left[1]:
            p1 = self.top
        return int((((row-p1[1])*(p2[0]-p1[0]))/(p2[1]-p1[1])) + p1[0])

    def get_rightest_point(self, row):
        if row == self.right[1]:
            return self.right[0]
        if row == self.top[1]:
            return self.top[0]
        if row == self.bottom[1]:
            return self.bottom[0]
        p1 = self.bottom
        p2 = self.right
        if row < self.right[1]:
            p1 = self.top
        return int((((row-p1[1])*(p2[0]-p1[0]))/(p2[1]-p1[1])) + p1[0])

def get_interesting_sensors(row, sensors) -> set[Sensor]:
    interesting_sensors= set()
    for sensor in sensors:
        if sensor.is_row_contained(row):
            interesting_sensors.add(sensor)
    return interesting_sensors