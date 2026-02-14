# Arun and Balaji begin their day with a quick game. 

# They first choose a starting number X0 ≥ 3 and try to reach one million by the process described below.

# Arun goes first and then they take alternating turns. In the i-th turn, the player whose turn it is selects a prime number smaller than the current number and announces the smallest multiple of this prime number that is not smaller than the current number.

# Formally, he or she selects a prime p < Xi - 1 and then finds the minimum Xi ≥ Xi - 1 such that p divides Xi. 

# Note that if the selected prime p already divides Xi - 1, then the number does not change.

# Eve has witnessed the state of the game after two turns. 

# Given X2, help her determine what is the smallest possible starting number X0. 

# Note that the players don't necessarily play optimally. You should consider all possible game evolutions.


try:
    x=int(input())
    spf = 0
    for i in range(2, x + 1):
        if x % i == 0:
            spf = i
            break
    print(x - spf + 1)
except IndexError:
    print("Invalid Input")