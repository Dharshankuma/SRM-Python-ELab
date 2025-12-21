# Three brothers want to take a photo with family members. The photographer is capturing the photo from a long distance. 
# Some of the family members are standing behind that brothers and those people are not visible to the photographer. 
# So the photographer gets confused with the heights of three brothers. 
# To get clarity, he asked, "who is the tallest person among those three brothers? But no one responded clearly. 
# Can you help the photographer in finding the tallest among the three brothers?

h1 = int(input())
h2 = int(input())
h3 = int(input())

if (h1>h2) and (h1>h3):
    print(h1)
elif (h2>h1) and (h2>h3):
    print(h2)
else:
    print(h3)