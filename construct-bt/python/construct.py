from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        rootVal = preorder[0]

        root = TreeNode(rootVal)

        if len(preorder) == 1:
            return root

        rootIdxIn = inorder.index(rootVal)

        leftIn = inorder[:rootIdxIn]
        if len(inorder)-1 == rootIdxIn:
            rightIn = []
        else:
            rightIn = inorder[rootIdxIn+1:]
            
        if len(leftIn) == 0:
            leftPre = []
            leftIdxPre = 0
        else:
            leftIdxPre = len(leftIn)
            leftPre = preorder[1:leftIdxPre+1]
        if len(preorder) == leftIdxPre+1:
            rightPre = []
        else:
            rightPre = preorder[leftIdxPre+1:]


        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)

        return root
