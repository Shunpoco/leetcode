from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        memory = defaultdict(list)
        
        for path in paths:
            p = path.split(" ")
            
            parent = p[0]
            
            for i in range(1, len(p)):
                v = p[i].split("(")
                filename = v[0]
                content = v[1][:len(v[1])]
                
                filepath = parent + "/" + filename
                
                memory[content].append(filepath)
                
        result = []
        
        for _, v in memory.items():
            if len(v) > 1:
                result.append(v)
                
        return result
