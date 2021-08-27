import random

overs = int(input("Enter the number of overs"))
compscore = random.randint(0, 36)
print("Computer has score ==", end="")
print(compscore)
print("Your target=", end="")
print(compscore + 1)

m = 0
for i in range(1, overs + 1):
    for j in range(1, 7):
        score = int(input("Enter number to bat ="))
        print("Computer's no=", end="")
        compno = random.randint(0, 6)
        print(compno)
        if compno == score:
            print("out")
            break
        else:
            m = m + score
        if m > compscore:
            break

if m <= compscore:
    print("Computer won the Match")
else:
    print("You won the Match")
