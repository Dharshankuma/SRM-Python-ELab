# Simon wants a number plate for his Brand new luxury car. he likes it to be unrepeatable.

# He came through a display board about fibonacci series he wants to check to whether the number he wants to use 
# for his car comes in fibonacci series or not.Can you help to them for program which checks if a number is 
# present in fibonacci series or not? 

# Functional Description:
# Perfect square value should be generated for the given number (n) which is multiplied by given format that is (5*n*n+4) 
# is double equal to one (or) (5*n*n - 4) is double equal to one


import math

def is_fibonacci(n):
    n = int(n)

    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4

    s1 = int(math.sqrt(x1))
    s2 = int(math.sqrt(x2))

    if s1 * s1 == x1 or s2 * s2 == x2:
        return "Yes"
    else:
        return "No"

num = int(input())
print(is_fibonacci(num))