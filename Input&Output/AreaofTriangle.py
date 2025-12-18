# Compute the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3 be the lengths of the sides. 
# Let s = (s1 + s2 + s3)/2. Then the area of the triangle can be calculated using the following formula: area =sqrt(s × (s − s1) × (s − s2) × (s − s3)) 
# Develop a program that reads the lengths of the sides of a triangle from the user and displays its area.

# Function Description

# area =sqrt(s × (s − s1) × (s − s2) × (s − s3))


import math
def calculate_triangle_area(s1, s2, s3):
    if s1 <= 0 or s2 <= 0 or s3 <= 0 or (s1 + s2 <= s3) or (s1 + s3 <= s2) or (s2 + s3 <= s1):
        return None
    s = (s1+s2+s3) / 2
    area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
    return area


s1 = float(input())
s2 = float(input())
s3 = float(input())
triangle_area = calculate_triangle_area(s1, s2, s3)
print(f"The area of triangle is {triangle_area}")