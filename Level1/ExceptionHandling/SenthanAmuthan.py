# Senthan Amuthan recently graduated Computer Science in university, so he was looking for a job. 

# He applied for several job offers, but he eventually settled for a software engineering job at the famous MNC. 

# Senthan Amuthan was very enthusiastic about his new job and the first mission assigned to him was to implement a message 
# encoding feature to ensure the chat is private and secure.

# Senthan Amuthan has a message, which is a string S with length N containing only lowercase English letters. 

# It should be encoded in two steps as follows:

# Swap the first and second character of the string S, then swap the 3rd and 4th character, then the 5th and 6th character and so on. 
# If the length of S is odd, the last character should not be swapped with any other.
# Replace each occurrence of the letter 'a' in the message obtained after the first step by the letter 'z', each occurrence of 'b' by 'y', 
# each occurrence of 'c' by 'x', etc, and each occurrence of 'z' in the message obtained after the first step by 'a'.
# The string produced in the second step is the encoded message. 

# Help Senthan Amuthan and find this message.


try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(input().strip())
        
        for i in range(0, n-1, 2):
            s[i], s[i+1] = s[i+1], s[i]
        
        for i in range(n):
            s[i] = chr(ord('z') - (ord(s[i]) - ord('a')))
        
        print("".join(s))
except:
    pass