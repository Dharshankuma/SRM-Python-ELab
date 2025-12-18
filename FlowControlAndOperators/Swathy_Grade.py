# Mrs.Swathy is the Principal of a Government School.
# The School have been opened after lock down so Mrs. Swathy instructed all the Class teachers to conduct a surprise test to check the progress of her students.
# As per instructions test have been conducted and the answer sheets were distributed to the students.
# Upon receiving the papers Swathy asked students from all the classes to calculate their grade based on the marks they have scored in all the five subjects.
# But student were finding it tough calculate the percentage and find their grade accordingly ?
# Can you help the students ?

# If the Percentage 
# >= 90 - Grade A
# >= 80 - Grade B
# >= 70 - Grade C
# >= 60 - Grade D
# >= 40 - Grade E
# Otherwise - Grade F


s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())

percentage = (s1+s2+s3+s4+s5) / 5

if percentage >= 90:
    grade = "Grade A"
elif percentage >= 80:
    grade = "Grade B"
elif percentage >= 70:
    grade = "Grade C"
elif percentage >= 60:
    grade = "Grade D"
elif percentage >= 40:
    grade = "Grade E"
else:
    grade = "Grade F"

print(f"{percentage:.2f} Percent")
print(grade)
