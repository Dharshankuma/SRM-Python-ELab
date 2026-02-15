# In the evening, after the contest Iniya was bored, and he really felt like maximizing. 
# He remembered that he had a set of N sticks and an instrument. 
# Each stick is characterized by its length li.
# Iniya decided to make a rectangle from the sticks. 
# And due to his whim, he decided to make rectangles in such a way that maximizes their total area. 
# Each stick is used in making at most one rectangle, it is possible that some of sticks remain unused. 
# Bending sticks is not allowed.
# Sticks with lengths a1, a2, a3 and a4 can make a rectangle if the following properties are observed:
# a1 ≤ a2 ≤ a3 ≤ a4
# a1 = a2
# a3 = a4
# A rectangle can be made of sticks with lengths of, for example, 3 3 3 3 or 2 2 4 4. A rectangle cannot be made of, 
# for example, sticks 5 5 5 7.
# Iniya also has an instrument which can reduce the length of the sticks.
#  The sticks are made of a special material, so the length of each stick can be reduced by at most one. 
# For example, a stick with length 5 can either stay at this length or be transformed into a stick of length 4.
# You have to answer the question what maximum total area of the rectangles can Iniya get with a file if makes rectangles from the 
# available sticks?

# Constraints:
# 1 ≤ n ≤ 105
# 2 ≤ li ≤ 106

# Input Format:
# The first line of the input contains a positive integer n the number of the available sticks.
# The second line of the input contains n positive integers li the lengths of the sticks.

# Output Format:
# The first line of the output must contain a single non-negative integer the maximum total area of the rectangles that 
# Iniya can make from the available sticks.

try:
    x=int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    sides = []
    i = 0
    
    while i < x - 1:
        if arr[i] - arr[i+1] <= 1:
            sides.append(min(arr[i], arr[i+1]))
            i += 2
        else:
            i += 1
    
    total = 0
    for i in range(0, len(sides)-1, 2):
        total += sides[i] * sides[i+1]
    
    print(total)

except:
    pass