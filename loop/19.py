# 二叉树的镜像
from leetcode.tree import TreeNode


class Solution:
    def help(self, root):
        def reverse(node):
            if not node:
                return

            tmp = node.right
            node.right = node.left
            node.left = tmp

            reverse(node.left)
            reverse(node.right)

        reverse(root)
        return root


s = Solution()

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
print(s.help(root))
