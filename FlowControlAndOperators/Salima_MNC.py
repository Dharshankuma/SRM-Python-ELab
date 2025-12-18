# Salima was working in one of the famous MNC. She was trying for the promotion in her office.
# The technical department was looking for the candidate who is good in mathematics, because the project in which the selected candidate is to 
# be placed need very good numerical problem solving skills.The technical department asked Salima the simple question of finding the roots of 
# quadratic equation.But she is nervous and finding it difficult to solve the problem. Can you help her in solving the problem so that she will get the promotion ? 

# This program finds the roots of a quadratic equation of the form aX^2 + bX + c = 0.
# The values of a, b, and c are taken as integers.
# The discriminant (b^2 - 4ac) is calculated to determine the nature of the roots.
# If the discriminant is negative, the roots are complex and are printed in the form
# real part ± imaginary part with two decimal places.
# Floating-point calculations are used to ensure accurate decimal results.

import math 
a=int(input())
b=int(input())
c=int(input())
d=b*b-4*a*c
if d < 0:
    real = float(-b / (2*a))
    imag = float(math.sqrt(-d) / (2*a))
    print(f"{real:.2f} + i{imag:.2f} and {real:.2f} - i{imag:.2f}")
else:
    r1 = float((-b + math.sqrt(d)) / (2*a))
    r2 = float((-b - math.sqrt(d)) / (2*a))
    print(f"{r1:.2f} and {r2:.2f}")