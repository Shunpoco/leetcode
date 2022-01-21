class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            if h.get(sorted_s):
                h[sorted_s].append(s)
            else:
                h[sorted_s] = [s]
                
        result = []
        
        for vals in h.values():
            result.append(vals)
            
        return result
