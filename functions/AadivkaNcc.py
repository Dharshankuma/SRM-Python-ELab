# Advika is trying to solve the puzzle problem during Mathematics class hour. she has a graph paper with G X N rows and columns, 
# and the puzzle question is, an NCC training base in each cell for a total of G X N bases. He wants to drop food items to 
# every point based on strategic points on the graph paper, marking each drop point with a red dot. If a base contains 
# at least one food package inside or on top of its border fence, then it's considered to be supplied. 


# Given G and N, what's the minimum number of packages that Luke must drop to supply all of his bases?

# Example :
# G=2, N=3.

# Food Packages can be dropped at the corner between cells (0, 0), (0, 1), (1, 0), (1, 1) , (0, 2) and (1, 2). This supplies all bases using packages.

# Function Description:

#  G: the number of rows
#  N: the number of columns


G, N = map(int, input().split())

r = int((G + 1) / 2)
c =int((N + 1) / 2)

result = r * c

print(result)