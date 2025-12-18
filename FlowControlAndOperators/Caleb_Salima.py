# Caleb and Salima are living in interior village of Nilgais.Since government of Tamil Nadu announced lockdown both of them struck in the village and 
# its been very hard for them to spend their day because of the lack of friends in the village.So they planned to play a technical game on Lockdown days.
# The rule of the game is simple :
# When one among Caleb and Salima say two numbers to the other.The person at the receiving end need to tell the difference between the numbers 
# if the first number is greater than the second number otherwise they have to tell the sum of those two numbers.

n1 = int(input())
n2 = int(input())
if n1 > n2:
    diff = n1 - n2
    print(diff)
else:
    total = n1+n2
    print(total)