from random import choice

already_answered = [
    71, 62, 
    25, 49,
    43, 54, 51,
    17,
    41, 27,
    6, 14, 66, 57, 56
]

print(choice([i for i in range(2, 77) if i not in already_answered]))
