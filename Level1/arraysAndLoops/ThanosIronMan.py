# Question description
# Thanos and iron man had a challenge  to get the stones from Hulk. But Hulk gave the task to them. They need to display the even and odd numbers separately from the numbers.

# Input Format:
# First value is the size of the array.
# Second value onwards the numbers which will be separated as even and odd.


n = int(input())
even = []
odd = []

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
for x in even:
    print(x, end=" ")
print()
print(*odd)