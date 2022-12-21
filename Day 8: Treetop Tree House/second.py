inputFile = open('./input.txt', 'r')

# First Star
treeGrid = []
for line in inputFile:
    treeGrid.append(line.replace('\n', ''))

maxScenicScore = 0
for x in range(0, len(treeGrid[0])):
    for y in range(0, len(treeGrid)):
        reachableView = 1
        if x == 0 or y == 0 or x == len(treeGrid[0])-1 or y == len(treeGrid[0])-1:
            reachableView *= 0

        # print('({},{}) -> {} = {}'.format(x, y, treeGrid[x][y], reachableView))

        leftView = 0
        for lx in range(x-1, -1, -1):
            leftView += 1
            if treeGrid[lx][y] >= treeGrid[x][y]:
                break
        rightView = 0
        for rx in range(x+1, len(treeGrid[0])):
            rightView += 1
            if treeGrid[rx][y] >= treeGrid[x][y]:
                break
        upView = 0
        for uy in range(y-1, -1, -1):
            upView += 1
            if treeGrid[x][uy] >= treeGrid[x][y]:
                break
        bottomView = 0
        for by in range(y+1, len(treeGrid)):
            bottomView += 1
            if treeGrid[x][by] >= treeGrid[x][y]:
                break

        reachableView *= leftView * rightView * upView * bottomView
        if reachableView > maxScenicScore:
            maxScenicScore = reachableView
print("Response: ",maxScenicScore)
inputFile.close()
