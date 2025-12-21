# Selvan is working as a QC in a reputed Multinational Conglmerate. 
# His task is to check if the given Keyboard has a valid alphabets. 
# But since many Keyboards are need to be verified, he is finding is difficult to finish the task. 
# Can you automate the checking process and reduce his work load?


def is_alphabet(ch):
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ch in alphabets

ch = input()
if is_alphabet(ch):
    print("ALPHABET")
else:
    print('NOT AN ALPHABET')