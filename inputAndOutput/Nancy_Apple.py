# Nancy bought apples in a fruit shop. 
# The shop keeper specified the the bill amount. Nancy also given some amount to the shop keeper for paying the bill. 
# But she likes to know the quotient and remainder after dividing the amount given by her by the bill amount specified by shop keeper. 
# Can you help Nancy in finding it?


amnt=int(input()) 
bill=int(input())

print("Quotient:{}\nRemainder:{}".format(int(amnt/bill),amnt%bill))