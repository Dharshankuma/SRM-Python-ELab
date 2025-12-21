# Sajid is a graduate student he applied to a BPO company but he does not get typing fast. So he wanted to increase his 
# typing speed for the job.His well-wisher suggested that he type the sentence "The quick brown fox jumps over the lazy dog" 
# repeatedly. This sentence is known as a pangram because it contains every letter of the alphabet. 
# After typing the sentence several times, Sajid needs to check whether the given number is a pangram.
# can you help him, whether the given sentence is a pangram or not
 
# Functional Description:
# The for loop reads character by character of the String and if the character is an alphabet then increment the total 
# if used[alphabet]=0 and it makes used[alphabet]=1 (increment for every new alphabet used between a to z. the alphabet count 
# should not exceed 26.

def alphabet_count(sentence):
    sentence = str(sentence)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    used = [0] * 26
    count = 0
    
    for ch in sentence:
        if ch.isalpha():
            ch = ch.lower()
            
            index = alphabet.index(ch)
            
            if(used[index] == 0):
                used[index] = 1
                count += 1
                
                if count == 26:
                    break
    
    if count == 26:
        return "panagram"
    else:
        return "not a panagram"
        
sentence = input()
print(alphabet_count(sentence))