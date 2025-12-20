# Mathematics teacher gave the home work to Pinocchio that addition of square matrices. 
# Can you help him to find the answer for the problems? 

r=int(input())
c=int(input())
A=[]
B=[]
for i in range(r):
    t=[]
    for j in range(c): t.append(int(input()))
    A.append(t)
for i in range(r):
    t=[]
    for j in range(c): t.append(int(input()))
    B.append(t)
for i in range(r):
    for j in range(c):
        if i==r-1 and j==c-1: print(A[i][j]+B[i][j],end="")  # Avoid trailing space for the last matrix element
        else:
            print(A[i][j]+B[i][j],end=" ")
    print()