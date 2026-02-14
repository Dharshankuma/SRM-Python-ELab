# Lal is a grizzly bear who desires power and adoration. He wants to win in upcoming elections and rule over the Bigland.

# There are n candidates, including Lal. We know how many citizens are going to vote for each candidate. Now i-th candidate would get ai votes. 

# Lal is candidate number 1. To win in elections, he must get strictly more votes than any other candidate.

# Victory is more important than everything else so Lal decided to cheat. 

# He will steal votes from his opponents by bribing some citizens. 

# To bribe a citizen, Lal must give him or her one candy citizens are bears and bears like candies. 

# Lal doesn't have many candies and wonders how many citizens does he have to bribe?

try:
    n=int(input())
    votes=list(map(int,input().split()))
    bribes = 0
    while True:
        max_votes = max(votes[1:])
        if votes[0] > max_votes:
            break
        votes[0] += 1
        max_index = votes[1:].index(max_votes) + 1
        votes[max_index] -= 1
        bribes += 1
    
    print(bribes)
        

except:
    print("Exception Occured")