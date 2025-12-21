# Simon was working in a Casa Grande. 
# His superior officer ordered him to construct a new building by incorporating equilateral, scalene and isosceles triangular shapes wherever possible. 
# But he has no idea about equilateral, scalene and isosceles triangle. 
# Can you clarify his doubt by giving him the correct category of triangle based on the values of sides given by simon?

# Functional Description :
# If All the Sides are Equal then it is a Equilateral Triangle
# If two Sides are Equal then it is a Isosceles Triangle
# If no Sides are Equal then it is a Scalene Triangle


a=int(input())
b=int(input())
c=int(input())
if (a == b) and (b == c):
    print("E")
elif(a == b):
    print("Isosceles triangle")
elif(b==c):
    print("Isosceles triangle")
elif(a==c):
    print("Isosceles triangle")
else:
    print("Scalene triangle")