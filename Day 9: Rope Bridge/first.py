inputFile = open('./input.txt', 'r')

tail_position = (0,4)
head_position = (0,4)
visited_by_tail = set()
visited_by_tail.add(head_position)
steps = []

# First Star
for line in inputFile:
    lineSplitted = line.split()
    steps.extend([lineSplitted[0]] * int(lineSplitted[1]))

for step in steps: 
    if step == 'R':
        head_position = (head_position[0] + 1, head_position[1])
    elif step == 'L':
        head_position = (head_position[0] - 1, head_position[1])
    elif step == 'U':
        head_position = (head_position[0], head_position[1] - 1)
    elif step == 'D':
        head_position = (head_position[0], head_position[1] + 1)
    
    diff_x = head_position[0] - tail_position[0]
    diff_y = head_position[1] - tail_position[1]
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        tail_position = (tail_position[0] + int(diff_x/abs(diff_x) if abs(diff_x) > 0 else 0), tail_position[1] + int(diff_y/abs(diff_y) if abs(diff_y) > 0 else 0))
        visited_by_tail.add(tail_position)

print(len(list(set(visited_by_tail))))

inputFile.close()
