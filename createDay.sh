#!/bin/bash

mkdir "$1"
cd "$1" || exit

printf "inputFile = open('./input.txt', 'r')\n\n# First Star\nfor line in inputFile:\n    pass\n\n# Second Star\nfor line in inputFile:\n    pass\n\ninputFile.close()\n\n# Print Section\n" >> main.py
touch input.txt

cd ..