# Simon celebrates his 25th birthday. Simon's older brother promised to buy him a new motorbike on his birthday if he could solve the question. 
# The question asked by Simpson's brother is that our mother Binitta's birthday is Leap Year or not.
# Help him to solve this puzzle, then only he can celebrate his birthday happily.

# Functional Description

#year mod div by 400==0 && year mod div by 100==0 or year mod div by 4==0



def leap_year(y):
    if (y%4==0 and y%100 != 0) or (y%400==0):
        print("Leap Year")
    else:
        print("Not a Leap Year")


year = int(input())
leap_year(year)