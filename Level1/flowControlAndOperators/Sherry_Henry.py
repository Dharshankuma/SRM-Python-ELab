# Shree and Harry was living in the town of Denmark , they usually think and do something innovative on weekends. 
# Every day the boys embark on some grand new project, which annoys their controlling sister candace, who tries to bust them. 
# One Sunday they were both sitting under a tree in their back yard. 
# They decide to invent a machine which would allow us to enter 2 numbers it would say whether one of the entered number is an appropriate value of the 
# other number entered. 

# Functional Description:
# According to their logic a number is said to be an approximate value of the other if they differ by utmost 0.5. So they decide to 
# insert a logic into the machine but they are finding it difficult can you help them with the logic


n1 = float(input())
n2 = float(input())
if abs(n1-n2) <= 0.5:
    print("Approximate Number")
else:
    print("Not an Approximate Number")