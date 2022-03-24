class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        temp = ""
        start = False
        for c in s:
            if c != " ":
                if start == False:
                    start = True
                temp += c
            else:
                if start:
                    if result == "":
                        result = temp
                    else:
                        result = temp + " " + result
                    temp = ""
                    start = False
                    
        if temp != "":
            if result == "":
                result = temp
            else:
                result = temp + " " + result
                
        return result
