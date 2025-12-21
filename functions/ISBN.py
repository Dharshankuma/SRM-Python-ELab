# Selvan asks his friend Arav to buy the book. Arav would recommend a bookstall in Thanjavur. 
# Arav further says that the advice given to Selvan is to have the number ISBN when buying the book. 
# Selvan doesn't know what it is. Arav tells him that. You must have notices every book has a 10 digit series of number. 

# An ISBN (International Standard Book Number) is a 10 digit number that is used to identify a book. 
# The first nine digits of the ISBN number are used to represent the Title, Publisher, Group of the book, and 
# the last digit is used for checking whether ISBN is correct or not. 

# The first 9 digits of it, can take any value between 0 and 9, but the last digits, 
# sometimes may take a value equal to 10; this is done by writing it as ‘X’. 
 
# Functional Description:
# To verify an ISBN, calculate 10 times the first digit, plus 9 times the second digit, plus 8 times the third digit, 
# and so on until we add 1 time the last digit. If the final number leaves no remainder when divided by 11, 
# the code is a valid ISBN.

def is_valid_isbn(isbn):
    isbn = str(isbn)
    
    if len(isbn) != 10:
        return "Invalid"

    total = 0

    for i in range(10):
        if i == 9 and isbn[i] == 'X':
            value = 10
        elif isbn[i].isdigit():
            value = int(isbn[i])
        else:
            return "Invalid"

        total += value * (10 - i)

    if total % 11 == 0:
        return "Valid"
    else:
        return "Invalid"

n = int(input())

for _ in range(n):
    isbn = input().strip()
    print(is_valid_isbn(isbn))
