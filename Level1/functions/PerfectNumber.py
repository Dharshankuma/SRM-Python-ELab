# Darsh seemingly down-to-earth guy. Dash has a Brother Nathan. 
# Nathan leads a life of a computer hacker by day and a thief by night. 
# One day, Nathan tries to break the door digital lock of Darsh's room. 
# Darsh who wants to prevent it thinks to give Passcode for security.

# But it only accepts a perfect number as input. Can you help him to make a program for checking the given number 
# is the perfect number or not…

def is_perfect_number(num):
    total = 0

    for i in range(1, int(num / 2 + 1)):
        if num % i == 0:
            total += i

    if total == num:
        return "Perfect Number"
    else:
        return "Not a Perfect Number"


num = int(input())
print(is_perfect_number(num))