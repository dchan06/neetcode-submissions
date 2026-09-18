class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if  len(s) != len(t): 
            return False 
        a = {} 
        b = {}
        for i in s: 
            if i not in t: 
                return False
            if i not in a: 
                a[i] = 0
            a[i] += 1
        for j in t: 
            if j not in b:
                b[j] = 0
            b[j] += 1
        if a == b: 
            return True
        return False


        