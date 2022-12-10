inputFile = open('./input.txt', 'r')

score = 0
newScore = 0
handScores = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

map_hands = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}


def get_game_score(game_param):
    if game_param[0] == 'A':
        if game_param[1] == 'X':
            return 3
        elif game_param[1] == 'Y':
            return 6
        elif game_param[1] == 'Z':
            return 0
    elif game_param[0] == 'B':
        if game_param[1] == 'X':
            return 0
        elif game_param[1] == 'Y':
            return 3
        elif game_param[1] == 'Z':
            return 6
    elif game_param[0] == 'C':
        if game_param[1] == 'X':
            return 6
        elif game_param[1] == 'Y':
            return 0
        elif game_param[1] == 'Z':
            return 3


def get_game_response(first_hand, expected_result):
    if expected_result == 'Y':
        return [first_hand, map_hands[first_hand]]
    if expected_result == 'X':
        if first_hand == 'A':
            return [first_hand, 'Z']
        elif first_hand == 'B':
            return [first_hand, 'X']
        elif first_hand == 'C':
            return [first_hand, 'Y']
    if expected_result == 'Z':
        if first_hand == 'A':
            return [first_hand, 'Y']
        elif first_hand == 'B':
            return [first_hand, 'Z']
        elif first_hand == 'C':
            return [first_hand, 'X']


for line in inputFile:
    game = line.split()
    score += handScores[game[1]]
    score += get_game_score(game)

    newGame = get_game_response(game[0], game[1])
    newScore += handScores[newGame[1]]
    newScore += get_game_score(newGame)

inputFile.close()

print(score)
print(newScore)
