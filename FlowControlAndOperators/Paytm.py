# The Paytm announced a Cashback offer for the people of Tamil Nadu which is a one time offer for the new year. 
# But to avail the Cashback users need to pass the simple tasks given by Paytm.
# One such task given by Paytm is to check the nature of the currency value provided by Paytm.

# Functional Description:
# One more condition imposed by Paytm is that participants need to do this checking using the concept of Operators.

currency = int(input())
if (currency % 2 == 0):
    print("Even Currency")
else:
    print("Odd Currency")