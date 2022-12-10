inputFile = open('./input.txt', 'r')


def get_priority(c):
    if ord(c) >= 97:
        return ord(c) - 96
    return ord(c) - 64 + 26


def str_intersection(s1, s2):
    out = ''
    for c in s1:
        if c in s2 and c not in out:
            out += c
    return out


def str_three_intersection(s1, s2, s3):
    out = ''
    for c in s1:
        if c in s2 and c in s3 and c not in out:
            out += c
    return out


# First Star
# priority_sum = 0
# for line in inputFile:
#     fistCompartment, secondCompartment = line[:len(line)//2], line[len(line)//2:]
#     inter = str_intersection(fistCompartment, secondCompartment)
#     priority_sum += get_priority(inter)
# print(priority_sum)

# Second Star
new_priority_sum = 0
lines = inputFile.readlines()
print(lines)
for idx, line in enumerate(lines):
    print(idx, line)
    if idx == 0 or idx % 3 != 2:
        continue
    inter = str_three_intersection(lines[idx], lines[idx - 1], lines[idx - 2])
    print(inter)
    new_priority_sum += get_priority(inter[0])
print(new_priority_sum)

inputFile.close()

# Print Section
