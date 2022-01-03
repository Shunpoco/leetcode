class Solution:
    pairs = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        result = [""]
        
        for d in digits:
            pair = self.pairs[d]
            temp = []
            for p in pair:
                for r in result:
                    temp.append(f"{r}{p}")
                
            result = temp
            
        return result
