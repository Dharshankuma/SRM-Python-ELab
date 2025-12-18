# Athika and Ritu got a nice job at a MNC company . She was confused with the salary credited in her account. 
# To verify if the correct amount of HRA and DA was provided to them.
# Ritu and Athika planned to develop a software that calculates the salary pay if the basic pay was provided. 
# The Salary policy of Athika and Ritu's Company is as follows: HRA is 80% of the basic pay and DA is 40% of basic pay. 
# Can you help Ritu and Athika in the software development? 

bill = float(input('')) 
hra = bill*0.8 
da = bill*0.4
total=hra+da+bill
print('{:.02f}'.format(total))