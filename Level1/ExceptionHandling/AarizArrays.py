# Aariz has got a large array of sizes n. Aariz doesn't like large arrays so he intends to make them smaller.

# Aariz doesn't care about anything in the array except the beauty of it. 

# The beauty of the array is defined to be the maximum number of times that some number occurs in this array. 

# He wants to choose the smallest subsegment of this array such that the beauty of it will be the same as the original array.

# Help Aariz by choosing the smallest subsegment possible.

try:
    n = int(input())
    l=list(map(int,input().split()))
    
    freq = {}
    first = {}
    last = {}
    
    for i in range(n):
        if l[i] not in freq:
            freq[l[i]] = 0
            first[l[i]] = i
        freq[l[i]] += 1
        last[l[i]] = i
    
    mx = max(freq.values())
    ans_l, ans_r = 0, n-1
    
    for x in freq:
        if freq[x] == mx:
            if last[x] - first[x] < ans_r - ans_l:
                ans_l = first[x]
                ans_r = last[x]
    
    print(ans_l+1, ans_r+1)

except:
    pass