# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [(root, 0, None)]

        memo = defaultdict(dict)
        sums = [0]

        while len(queue) > 0:
            v, l, p = queue.pop(0)
            if l > 0:
                if memo.get(l) is None:
                    memo[l] = {}
                if memo[l].get(p) is None:
                    memo[l][p] = v.val
                else:
                    memo[l][p] += v.val

                if len(sums) - 1 < l:
                    sums.append(v.val)
                else:
                    sums[l] += v.val

            if v.left is not None:
                queue.append((v.left, l+1, id(v)))

            if v.right is not None:
                queue.append((v.right, l+1, id(v)))

        queue = [(root, 0, None)]

        while len(queue) > 0:
            v, l, p = queue.pop(0)

            if l == 0:
                v.val = 0
            else:
                v.val = sums[l] - memo[l][p]

            if v.left is not None:
                queue.append((v.left, l+1, id(v)))

            if v.right is not None:
                queue.append((v.right, l+1, id(v)))

        return root
