class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        counter = 0
        properties.sort(reverse=True)
        stack = [[properties[0][1], properties[0][0]]]
        
        for i in range(1, len(properties)):
            if properties[i][0] == stack[-1][1]:
                stack[-1][0] = max(stack[-1][0], properties[i][1])
                
                if len(stack) > 1 and stack[-2][0] > properties[i][1]:
                    counter += 1
            elif properties[i][1] < stack[-1][0]:
                counter += 1
                
            elif properties[i][1] > stack[-1][0]:
                stack.append([properties[i][1], properties[i][0]])
                
        return counter
