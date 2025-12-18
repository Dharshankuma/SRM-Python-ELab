# Aaron took his girl friend Binita to a restauraunt as he got a job of his dreams.
# Since he had small welcome interview he was little bit tennsed.
# Binita figured this out and to get back Aaron's confidence she gave him a little task,
# When they received the bill for the food they ordered, She asked Aaron to find out the tax amount of the bill and tip for the meal through a computer code. 
# Aaron can use your local tax rate when computing the amount of tax owing.
# Can you help Aaron to code the suitable logic.

# Note:
# Local tax= 18%
# Tip amount=5%

bill=int(input())
tax=0.18
tip=0.05
billTax=bill*tax
billTip=bill*tip
total=bill+billTax+billTip
print(f"The Tax is {billTax:.2f}")
print(f"The Tip is {billTip:.2f}")
print(f"Total Bill With Tax and Tip is {total:.2f}")
