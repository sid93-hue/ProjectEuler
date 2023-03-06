""" Problem 22 """


def name_score(name):
    """Returns the name score of the input string"""
    alphabet = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26,
    }
    score = 0
    for x in name:
        score += alphabet[x]
    return score


f = open("res/p022_names.txt", "r")

names = f.readlines()
name_list = names[0].split(",")
for idx, name in enumerate(name_list):
    name = name.replace('"', "")
    name_list[idx] = name
name_list.sort()

answer = 0
for idx, name in enumerate(name_list):
    answer += (idx + 1) * name_score(name)

print(f"Answer = {answer}")

f.close()
