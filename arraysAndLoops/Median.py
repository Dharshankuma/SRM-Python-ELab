# For calculating median in ungrouped data, we have to first arrange the items in ascending or descending order and 
# then median is taken to be the one according to the following:

# If the number of observation is odd, we obtain the median from the size of 
# (n+1) / 2 value. If the number of observation is even, we obtain the median from the arithmetic mean of the 
# (n/2) and (n+1) / 2 

# Here n represents  the number of elements in the data.


n = int(input())
a=[]
for i in range(n):
    num = int(input())
    a.append(num)
    
a.sort()

if n % 2 == 0:
    sum = a[int(n/2)-1] + a[int(n/2)]
    median = sum/2
else:
    median = a[int(n/2)]
print(median)