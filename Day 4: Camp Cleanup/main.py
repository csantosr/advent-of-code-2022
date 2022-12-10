inputFile = open('./input.txt', 'r')

# First Star
overlaps = 0
for line in inputFile:
    first_elf, second_elf = map(lambda x: list(map(lambda y: int(y), x.split('-'))), line.replace('\n', '').split(','))
    if (
            first_elf[0] >= second_elf[0] and first_elf[1] <= second_elf[1]
    ) or (
            second_elf[0] >= first_elf[0] and second_elf[1] <= first_elf[1]
    ):
        overlaps += 1
print(overlaps)

# Second Star
overlaps = 0
for line in inputFile:
    first_elf, second_elf = map(lambda x: list(map(lambda y: int(y), x.split('-'))), line.replace('\n', '').split(','))
    if (
            second_elf[0] <= first_elf[0] <= second_elf[1] or
            second_elf[0] <= first_elf[1] <= second_elf[1] or
            first_elf[0] <= second_elf[0] <= first_elf[1] or
            first_elf[0] <= second_elf[1] <= first_elf[1]
    ):
        overlaps += 1
print(overlaps)