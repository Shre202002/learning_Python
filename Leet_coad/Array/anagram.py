# 242. Valid Anagram
# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

def anagram(s:str,t:str): 

    # if len(s) != len(t):
    #     return False

    # return sorted(s) == sorted(t)

    if len(s) != len(t):
     return False
    lis = set(s)
    for i in lis:
     if s.count(i) != t.count(i):
        return False
    return True

print(anagram("anagram", "nagaram"))