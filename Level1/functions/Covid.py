# Finally, a COVID vaccine is out on the market and the Indian government has asked you to form a plan to distribute it to the 
# public as soon as possible. There are a total of N people with ages a1,a2, …,aN.
# There is only one hospital where vaccination is done and it is only possible to vaccinate up to D people per day.
# Anyone whose age is ≥80 or ≤9 is considered to be at risk. On each day, you may not vaccinate both a person who is at risk 
# and a person who is not at risk. Find the smallest number of days needed to vaccinate everyone.

# Input Format:
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each test case contains two space-separated integers N and D.
# The second line contains N space-separated integers a1 ,a2,…,aN


import math 

def min_days(d,ages):
    risk = 0 
    no_risk = 0
    
    for age in ages:
        if age<=9 or age>=80:
            risk += 1
        else:
            no_risk += 1 
    days_for_risk = math.ceil(risk/d)
    days_for_noRisk = math.ceil(no_risk/d)
    
    sum = days_for_risk + days_for_noRisk
    return sum
    
t = int(input())

for _ in range(t):
    n,d = map(int,input().split())
    ages = list(map(int,input().split()))
    days = min_days(d,ages)
    print(days)