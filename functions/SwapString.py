# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters 
# and vice versa.

# Function Description
# Complete the swap_case function in the editor below.
# swap_case has the following parameters:
# string s: the string to modify

def swap_case(s):
    result = ""
    for ch in s:
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += ch.upper()
        else:
            result += ch

    return result

s = input()
print(swap_case(s))