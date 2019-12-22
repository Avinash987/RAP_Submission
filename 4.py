# Directly replace the first line for custom input
score_card = [int(x) for x in input("Enter the scores : ").split()]
batsman_1 = True
score_batsman_1, score_batsman_2 = [], []
for i in range(len(score_card)):
    if i % 6 == 0 and i > 0:
        if batsman_1:
            batsman_1 = False
        else:
            batsman_1 = True
    if batsman_1 and (score_card[i] == 1 or score_card[i] == 3):
        score_batsman_1.append(score_card[i])
        batsman_1 = False
    elif batsman_1:
        score_batsman_1.append(score_card[i])

    elif (not batsman_1) and (score_card[i] == 1 or score_card[i] == 3):
        score_batsman_2.append(score_card[i])
        batsman_1 = True
    else:
        score_batsman_2.append(score_card[i])

print("Total Score : ", sum(score_batsman_1)+sum(score_batsman_2))
print("Batsman-1 Score : ", sum(score_batsman_1), score_batsman_1)
print("Batsman-2 Score : ", sum(score_batsman_2), score_batsman_2)
