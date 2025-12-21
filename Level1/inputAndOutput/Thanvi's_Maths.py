# Thanvi's Maths teacher taught that a sphere is a three-dimensional solid with no face, 
# no edge, no base and no vertex. It is a round body with all points on its surface equidistant from the center. 
# The volume of a sphere is measured in cubic units.
# Can you help her to find the volume of the sphere for the given radius?

# Function Description
# The volume of the sphere is: V = 4/3 πr^3

# Constraints
# Take π=3.142

pi = 3.142
radius = float(input())
volume = (4/3) * pi * (radius **3)
print(volume)