# Dinesh has a matrix with N rows (numbered 1 through N) and M columns (numbered 1 through M). 

# Let's denote the element in row i and column j by Ai,j. Next, let's define a sub-row of a row r as a sequence

# Ar,x,Ar,x+1,…,Ar,y for some x and y (1≤x≤y≤M) and a sub-column of a column c by Ax,c,Ax+1,c,…,Ay,c for some x and y (1≤x≤y≤N).

# You need to find the number of pairs (sub-row of some row, sub-column of some column) with the following properties:

# Both sequences (the sub-row and the sub-column) have the same length.
# This length is odd.
# The central elements of both sequences are the same (they correspond to the same element of the matrix).
# Both sequences are palindromes.

try:
    t = int(input())
    for _ in range(t):
        M,N=map(int,input().split())
        A = [list(map(int, input().split())) for _ in range(M)]
        
        total =0
        
        for i in range(M):
            for j in range(N):
                
                r = 0
                while j-r >= 0 and j+r < N and A[i][j-r] == A[i][j+r]:
                    r += 1
                
                c = 0
                while i-c >= 0 and i+c < M and A[i-c][j] == A[i+c][j]:
                    c += 1
                
                total += min(r, c)
        
        print(total)

except:
    pass