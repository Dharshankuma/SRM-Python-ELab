# Today Ram is Going to Library for book submission. In Library Ram meet one of his collage life friend Manoj. 
# Manoj introduced him self to Ram as Data Science engineer at Amazon. Now Ram introduced him self as Harward Researcher. 
# After that manoj started crying and telling to ram that he is facing a problem. Ram told him to say his problem.

# Manoj told his problem to Ram that he have to perform the following operations : 

# 1. Add two string 
# 2. Exponent of first string 
# 3. Exponent of second string 
# 4. Check whether String B is present in A 
# 5. Check whether String A is present in B 
# 6. Check whether String B not in A 
# 7. Check whether String A not in B

str1=input()
str2=input()
string = str1
sub_string = str2
print(str1 + str2)
print(str1 * 2)
print(str2 * 2)

if string.find(sub_string) != -1:
    print("True")
else:
    print("False")

if str2.find(str1) != -1:
    print("True")
else:
    print("False")

if str1.find(str2) == -1:
    print("True")
else:
    print("False")

if str2.find(str1) == -1:
    print("True")
else:
    print("False")