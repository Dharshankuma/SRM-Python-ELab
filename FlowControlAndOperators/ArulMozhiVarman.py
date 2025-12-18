# Arulmozhivarman the famous skill trainer planned to conduct a quiz program for his followers in Facebook.
# Arulmozhivarman will give them 2 numbers and the operator. Based on the number and the operator they have to do certain operation on 
# the numbers and have to print the result.

# Constraints:
# Operators will be one among the following : + ,  - , * , /
# 1<=n1<=500
# 1<=n2<=500

op = input()
n1 = float(input())
n2 = float(input())

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print("Invalid Input")