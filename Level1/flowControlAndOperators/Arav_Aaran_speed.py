# Arav and Aaron are participating in the Bike racing. Arav have crossed some milestores earlier and Aaron crossed some milestores earlier 
# during their racing,because they have changed their speeds at different times.
# Both of them like to know the difference in speeds between them at different stages of racing
# Can you help finding the speed difference between Arav and Aaron?


arav=int(input())
aaran=int(input())

if (arav > aaran):
    print(arav-aaran)
else:
    print(aaran-arav)