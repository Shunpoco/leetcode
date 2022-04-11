# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descs: List[List[int]]) -> Optional[TreeNode]:
        memory = {}
        parent = set()
        child = set()
        
        for desc in descs:
            if memory.get(desc[0]):
                v = memory[desc[0]]
            else:
                v = TreeNode(desc[0])
                memory[desc[0]] = v
                
            if memory.get(desc[1]):
                c = memory[desc[1]]
            else:          
                c = TreeNode(desc[1])
                memory[desc[1]] = c

            if desc[2] == 1:
                v.left = c
            else:
                v.right = c

            parent.add(desc[0])
            child.add(desc[1])
        
        root = list(parent-child)[0]
        
        # print(memory)
        # print(root)

        return memory[root]
