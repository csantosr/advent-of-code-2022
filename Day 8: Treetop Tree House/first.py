inputFile = open('./input.txt', 'r')

# First Star
treeGrid = []
for line in inputFile:
    treeGrid.append(line.replace('\n', ''))

visibleTrees = 2 * len(treeGrid) + 2 * (len(treeGrid) - 2)
for x in range(1, len(treeGrid[0])-1):
    for y in range(1, len(treeGrid) - 1):
        is_visible_left = True
        for lx in range(0, x):
            is_visible_left = is_visible_left and treeGrid[x][y] > treeGrid[lx][y]
        is_visible_right = True
        for rx in range(x+1, len(treeGrid[0])):
            is_visible_right = is_visible_right and treeGrid[x][y] > treeGrid[rx][y]
        is_visible_top = True
        for ty in range(0, y):
            is_visible_top = is_visible_top and treeGrid[x][y] > treeGrid[x][ty]
        is_visible_bottom = True
        for by in range(y+1, len(treeGrid)):
            is_visible_bottom = is_visible_bottom and treeGrid[x][y] > treeGrid[x][by]
        if is_visible_left or is_visible_right or is_visible_top or is_visible_bottom:
            visibleTrees += 1
            print('SE VE ({}, {})'.format(x, y))
        else:
            print('NO SE VE ({}, {})'.format(x, y))
print(visibleTrees)
inputFile.close()
