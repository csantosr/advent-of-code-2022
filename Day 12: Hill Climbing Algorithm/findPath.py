from heapq import heappush, heappop

def get_neighboors(x, y, clean_map):
    height = clean_map[x][y]
    neighboors = []
    for dist_x, dist_y in [(0,1),(0,-1),(1,0),(-1,0)]:
        new_x, new_y = dist_x + x, dist_y + y
        if new_x >= 0 and new_x < len(clean_map) and new_y >= 0 and new_y < len(clean_map[0]):
            if clean_map[new_x][new_y] <= height + 1:
                neighboors.append((new_x, new_y))
    return neighboors

def get_steps(s, e, clean_map):
    visited = set()
    queue = []
    heappush(queue, (0, s))
    while True:
        if not queue:
            break

        steps, node = heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == e:
                return steps
            for nx, ny in get_neighboors(node[0], node[1], clean_map):
                heappush(queue, (steps+1, (nx, ny)))