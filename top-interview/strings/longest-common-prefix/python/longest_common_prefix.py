class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minStr = strs[0]
        
        for s in strs:
            if len(s) < len(minStr):
                minStr = s
                
        minPref = ''
        for i in range(len(minStr)):
            for j in range(len(strs)):
                s = strs[j]
                if minStr[i] != s[i]:
                    return minPref
                if j == len(strs)-1:
                    minPref += minStr[i]
                    
        return minPref
