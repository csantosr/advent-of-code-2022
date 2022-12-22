inputFile = open('./input.txt', 'r')

tail_position = (0,4)
knob_positions = [
    (0,4),
    (0,4),
    (0,4),
    (0,4),
    (0,4),
    (0,4),
    (0,4),
    (0,4),
    (0,4),
]
head_position = (0,4)
visited_by_tail = set()
visited_by_tail.add(tail_position)
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
    
    diff_x = head_position[0] - knob_positions[0][0]
    diff_y = head_position[1] - knob_positions[0][1]
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        knob_positions[0] = (knob_positions[0][0] + int(diff_x/abs(diff_x) if abs(diff_x) > 0 else 0), knob_positions[0][1] + int(diff_y/abs(diff_y) if abs(diff_y) > 0 else 0))
    
    for knob_index in range(0, len(knob_positions)-1):
        diff_x_inner = knob_positions[knob_index][0] - knob_positions[knob_index+1][0]
        diff_y_inner = knob_positions[knob_index][1] - knob_positions[knob_index+1][1]
        if abs(diff_x_inner) > 1 or abs(diff_y_inner) > 1:
            knob_positions[knob_index+1] = (knob_positions[knob_index+1][0] + int(diff_x_inner/abs(diff_x_inner) if abs(diff_x_inner) > 0 else 0), knob_positions[knob_index+1][1] + int(diff_y_inner/abs(diff_y_inner) if abs(diff_y_inner) > 0 else 0))
            if knob_index+1 == len(knob_positions)-1:
                visited_by_tail.add(knob_positions[knob_index+1])

print(len(visited_by_tail))

inputFile.close()
