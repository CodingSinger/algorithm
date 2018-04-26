import time


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    # 超时
    def helper(self,root):
        def robHouse(node):
            if not node:
                return 0

            val = 0
            if node.left:
                val += robHouse(node.left.left) + robHouse(node.left.right)
            if node.right:
                val += robHouse(node.right.left) + robHouse(node.right.right)

            return max(node.val + val, robHouse(node.left) + robHouse(node.right))

        return robHouse(root)

    #因为一层一层往下递归，回去的时候node.left就是上一层的node.left.left，所以保存起来，避免二次计算
    def helper2(self,root):

        d = {}
        def robHouse(node):
            if not node:
                return 0
            if node in d:
                return d[node]
            val = 0
            if node.left:
                val += robHouse(node.left.left) + robHouse(node.left.right)
            if node.right:
                val += robHouse(node.right.left) + robHouse(node.right.right)

            val = max(node.val + val, robHouse(node.left) + robHouse(node.right))

            d[node] = val
            return val

        return robHouse(root)


root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

s = Solution()
print(s.helper(root))
print(s.helper2(root))

