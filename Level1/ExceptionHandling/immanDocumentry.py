# Imman is watching a documentary about cave painting.

# Some numbers, carved in a chaotic order, immediately attracted his attention. 

# Imman rapidly proposed a guess that they are the remainders of the division of a number n by all integers i from 1 to k.

# Unfortunately, there are too many integers to analyze for Imman.

# Imman wants you to check whether all these remainders are distinct. 

# Formally, he wants to check, if all, 1 ≤ i ≤ k, are distinct, i. e. there is no such pair (i, j) that:

# n mod i

# 1 ≤ i < j ≤ k,

# n mod i = n mod j

# where 

# x mod y

# Is the remainder of division x by y.



try:
    import math
    n,k=map(int,input().split(' '))
    if k > 1:
        limit = min(k,int(math.isqrt(n)))
        for i in range(2,limit+1):
            if n % i == 0:
                print("No")
                break
            else:
                print("Yes")
    else:
        print("Yes")
except:
    print("Invalid Input")