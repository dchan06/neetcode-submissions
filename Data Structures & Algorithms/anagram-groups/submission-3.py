class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matched = defaultdict(list)
        for s in strs: 
            alphabetical_s = ''.join(sorted(s))
            matched[alphabetical_s].append(s) 
        return list(matched.values()) 
