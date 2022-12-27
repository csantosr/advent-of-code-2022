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
linesClean = []
for line in lines:
    if not line:
        continue
    linesClean.append(eval(line))
linesClean.append([[2]])
linesClean.append([[6]])
linesClean.sort(key=cmp_to_key(evaluate))

for idx, item in list(enumerate(linesClean)):
    if item == [[2]] or item == [[6]]:
        print('{}: {}'.format(idx+1, item))