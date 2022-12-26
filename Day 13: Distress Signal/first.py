from collections import defaultdict
from functools import cmp_to_key

with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

def evaluate(a, b):
    if type(a) == type(b) == int:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    elif type(a) == type(b) == list:
        n = len(a)
        m = len(b)
        res = 0
        for i in range(min(n, m)):
            res = evaluate(a[i], b[i])
            if res:
                break
        if res == 0:
            if n < m:
                return -1
            elif n > m:
                return 1
            else: return 0
    elif type(a) == int:
        res = evaluate([a], b)
    else:
        res = evaluate(a, [b])
    return res

# Part 1
pair = {}
current_idx = 1
current_key = 'left'
correct_idxs = []
for line in lines:
    if not line:
        continue
    pair[current_key] = eval(line)
    if current_key == 'left':
        current_key = 'right'
    else:
        current_key = 'left'
        res = evaluate(pair['left'], pair['right'])
        if res == -1:
            correct_idxs.append(current_idx)
        current_idx += 1
print(correct_idxs)
print(sum(correct_idxs))