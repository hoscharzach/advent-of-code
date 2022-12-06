f = open("day2.txt", "r")
rounds = f.read().split("\n")
total_score = 0
scoring = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

losing = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

winning = {
    "C": "X",
    "B": "Z",
    "A": "Y"
}

for i in range(len(rounds) - 1):
    opponent_play = rounds[i][0]
    my_play = rounds[i][-1]

    if my_play == "X":
        lose_round = losing[opponent_play]
        total_score += scoring[lose_round]
    elif my_play == "Y":
        if opponent_play == "A":
            total_score += scoring["X"]
        elif opponent_play == "B":
            total_score += scoring["Y"]
        else:
            total_score += scoring["Z"]
        total_score += 3
    else:
        total_score += 6
        winning_round = winning[opponent_play]
        total_score += scoring[winning_round]



print(total_score)
