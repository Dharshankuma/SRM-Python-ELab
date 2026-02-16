# Lokesh usually likes to play cricket, but now, he is bored of playing it too much, so he is trying new games with strings. 

# Lokesh's friend Tina gave him binary strings S and R, each with length N, and told him to make them identical. 

# However, unlike Tina, Lokesh does not have any superpower and Tina lets Lokesh perform only operations of one type: 
# choose any pair of integers (i,j) such that 1≤i,j≤N and swap the i-th and j-th character of S. 

# He may perform any number of operations (including zero).

# For Lokesh, this is much harder than cricket and he is asking for your help. 

# Tell him whether it is possible to change the string S to the target string R only using operations of the given type.


T=int(input())

for _ in range(T):
    n=int(input())
    s1=str(input())
    s2=str(input())
    
    if s1.count('0') == s2.count('0') and s1.count('1') == s2.count('1'):
        print("YES")
    else:
        print("NO")