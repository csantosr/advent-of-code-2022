#!/bin/bash

mkdir "$1"
cd "$1" || exit

if [ "--separate" = "$2" ]
then
  printf "inputFile = open('./input.txt', 'r')\n\n# First Star\nfor line in inputFile:\n    pass\ninputFile.close()\n" >> first.py
  printf "inputFile = open('./input.txt', 'r')\n\n# Second Star\nfor line in inputFile:\n    pass\ninputFile.close()\n" >> second.py
else
  printf "inputFile = open('./input.txt', 'r')\n\n# First Star\nfor line in inputFile:\n    pass\n\n# Second Star\nfor line in inputFile:\n    pass\n\ninputFile.close()\n\n# Print Section\n" >> main.py
fi

touch input.txt
touch __init__.py

cd ..