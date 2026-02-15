# aSmuthra has no idea, why this problem is called Stone. 
# She also has no idea on how to solve the following problem: given array of N integers A and a number K. 
# During a turn the maximal value over all Ai is chosen, let's call it MAX. 
# Then Ai = MAX - Ai is done for every 1 <= i <= N. 
# Help Samuthra to find out how will the array look like after K turns.

# Constraints:
# 1 <= N <= 105
# 0 <= K <= 109

# Ai does not exceed 2 * 109 by it's absolute value.

# Input Format:
# The numbers N and K are given in the first line of an input. 
# Then N integers are given in the second line which denote the array A.

# Output Format:
# Output N numbers on a single line. 
# It should be the array A after K turns.


try:
    N, K = map(int, input().split())
    arr=list(map(int, input().split()))
    
    if K == 0:
        print(*arr)
    else:
        mx = max(arr)
        arr = [mx - x for x in arr]
        
        if K % 2 == 0:
            mx = max(arr)
            arr = [mx - x for x in arr]
        
        print(*arr)

except:
    pass