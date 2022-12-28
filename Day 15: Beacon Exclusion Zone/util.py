def manhattan(source, target):
    return abs(source[0] - target[0]) + abs(source[1] - target[1])

def get_blocked(source, target):
    distance = manhattan(source, target)
    blocked = set()
    print(source, target)
    for y_gap in range(source[1]-distance, source[1]+distance+1):
        print('y: ', y_gap)
        x_span = abs(abs(y_gap-source[1])-distance)
        blocked.add((source[0], y_gap))
        for x in range(x_span):
            blocked.add((source[0]+(x+1), y_gap))
            blocked.add((source[0]-(x+1), y_gap))
    return blocked