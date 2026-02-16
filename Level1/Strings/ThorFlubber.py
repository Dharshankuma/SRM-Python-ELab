# Thor and Flubber have the task is to check whether the string has at least one letter(character) and one number. Return “True” 
# if the given string full fill above condition else return “False” (without quotes).

# Can you help them to finish the task?


T = int(input())

for _ in range(T):
    str1=str(input())
    
    has_letter = False
    has_digit = False
    
    for ch in str1:
        if ch.isalpha():
            has_letter = True
        if ch.isdigit():
            has_digit = True
    
    if has_letter and has_digit:
        print("True")
    else:
        print("False")