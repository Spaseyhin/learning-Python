questions = [
 "We don't serve strings around here. Are you a string?",
 "What is said on Father's Day in the forest?",
 "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
 "An exploding sheep.",
 "No, I'm a frayed knot.",
 "'Pop!' goes the weasel."
]

x = -1
while(x:= x + 1) < len(questions):
    print(f'Q: {questions[x]}')
    print(f'A: {answers[x]}')
