# Janaki set the password of her locker that the possible set of substrings from the string. 
# Can you help her to set the password?

 
 
 
s=str(input())
n = len(s)

for i in range(n):
    for j in range(i+1,n+1):
        print(s[i:j])