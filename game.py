score = 0
vowel = "aeiou"
for i in range(10):
    value = input()
    if value in vowel:
        score+=10
    else:
        score-=2
    print("score=",score)