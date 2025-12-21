# Euler asked the question to Ramanujan that, from the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is ____. Can you help Ramanujan to answer the sum of these multiples ?

# Function description
# Upper limit of natural number should be get from the user and store it to the variable N.


n=int(input())
total = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0 :
        total += i
print(total)