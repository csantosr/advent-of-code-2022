import copy

def parse_input():
    inputFile = open('./input.txt', 'r')
    strMap = []
    start = (0,0)
    end = (0,0)
    cols = 0
    rows = 0
    # First Star
    for line in inputFile:
        strMap.append(line.replace('\n', ''))
        cols = len(line.replace('\n', '')) + 1
        rows += 1
    cleanMap = []
    for ir in range(rows):
        cleanMap.append([])
        for ic in range(cols):
            cleanMap[ir].append(0)
    starts = []

    for idxRow, row in enumerate(copy.deepcopy(strMap)):
        for idxCell, cell in enumerate(copy.deepcopy(row)):
            cellValue = ord(cell) - ord('a')
            if cell == 'a':
                starts.append((idxRow, idxCell))
            if cell == 'S':
                start = (idxRow, idxCell)
                strMap[idxRow] = strMap[idxRow][:idxCell] + 'a' + strMap[idxRow][idxCell + 1:]
                cellValue = 0
            if cell == 'E':
                end = (idxRow, idxCell)
                strMap[idxRow] = strMap[idxRow][:idxCell] + 'z' + strMap[idxRow][idxCell + 1:]
                cellValue = ord('z') - ord('a')
            cleanMap[idxRow][idxCell] = cellValue
    starts.append(start)
    inputFile.close()
    return start, end, cleanMap, starts
