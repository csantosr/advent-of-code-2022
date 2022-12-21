import FileTree


inputFile = open('./input.txt', 'r')

# Second Star
root = FileTree.FileTree('/', True)
current = root
add_to_current = False
for line in inputFile:
    cleanLine = line.replace('\n', '')
    if cleanLine.startswith('$'):
        if cleanLine == '$ cd /':
            current = root
        elif cleanLine == '$ cd ..':
            current = current.get_parent()
        elif cleanLine.startswith('$ cd '):
            child_name = cleanLine[len('$ cd '):]
            current = current.get_child(child_name)
    else:
        list_prefix, list_name = cleanLine.split()
        current.add_child(FileTree.FileTree(list_name, list_prefix == 'dir', None if list_prefix == 'dir' else int(list_prefix)))

unused_space = 70000000 - root.get_size()
big_dirs = [directory.get_size() for directory in root.get_all_dirs() if directory.get_size() >= 30000000 - unused_space]
print(min(big_dirs))
inputFile.close()
