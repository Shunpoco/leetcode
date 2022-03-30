class Solution:
    def calculate(self, s: str) -> int:
        self.stack = []
        self.rev_stack = []
        
        idx = 0
        while idx < len(s):
            # print(self.stack)
            if s[idx].isdigit():
                t = 2
                while s[idx:idx+t].isdigit() and idx+t <= len(s):
                    t += 1                
                self.stack.append(s[idx:idx+(t-1)])
                idx += t-1
                
            elif s[idx] == "(":
                self.stack.append(s[idx])
                idx += 1

            elif s[idx] == ")":
                while self.stack[len(self.stack)-1] != "(":
                    self.rev_stack.append(self.stack.pop())
                self.stack.pop()
                self.calc()
                
                idx += 1
            
            elif s[idx] == "+":
                self.stack.append(s[idx])
                idx += 1
            elif s[idx] == "-":
                self.stack.append(s[idx])
                idx += 1
                
            else:
                idx += 1
         
        # print(self.stack)
        while len(self.stack) > 0:
            self.rev_stack.append(self.stack.pop())
        self.calc()
        
        if len(self.stack) == 2:
            return -1 * int(self.stack[1])
        else:
            return int(self.stack[0])
    
    def calc(self):
        result = 0
        
        minus = False
        while len(self.rev_stack) > 0:
            v = self.rev_stack.pop()
            if v.isdigit():
                if minus:
                    result -= int(v)
                else:
                    result += int(v)
                minus = False
            elif v == "-":
                minus = not minus
                
        if result < 0:
            self.stack.append("-")
            result *= -1
        self.stack.append(str(result))
