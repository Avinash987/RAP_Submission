# Directly replace the first line for custom input
L = [int(x) for x in input("Enter the elements in Array : ").split()]
repeating = [0] * (max(L) + 1)
for i in L:
    repeating[i] += 1
for i in range(len(repeating)):
    if repeating[i] > 0:
        print(i,'-', repeating[i])
