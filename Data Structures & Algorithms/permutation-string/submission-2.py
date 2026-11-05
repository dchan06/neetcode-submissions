class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): 
            return False
        
        s1_count, s2_count = [0] * 26, [0] * 26
        # populate the first 3 chars of each string in the string counts
        for i in range(len(s1)): 
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1    # first 3 char
        
        matches = 0 
        l = 0
        for i in range(26): 
            matches += (1 if s1_count[i] == s2_count[i] else 0)

        for r in range(len(s1), len(s2)): 
            if matches == 26: 
                return True
            char_ind = ord(s2[r]) - ord('a')
            s2_count[char_ind] += 1
            if s2_count[char_ind] == s1_count[char_ind]: 
                matches += 1
            elif s1_count[char_ind] + 1 == s2_count[char_ind]: 
                matches -= 1
            
            char_ind = ord(s2[l]) - ord('a')
            s2_count[char_ind] -= 1
            if s2_count[char_ind] == s1_count[char_ind]: 
                matches += 1
            elif s1_count[char_ind] - 1 == s2_count[char_ind]:
                matches -= 1

            l += 1
        
        return matches == 26
        
