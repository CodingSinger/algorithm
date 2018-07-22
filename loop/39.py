from leetcode.tree import TreeNode

#思路 深度遍历，每往下一层+1，遍历到空返回0，返回节点左右叶子节点的大的那个数
class Solution:
    def helper(self, root):
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            return max(left, right)

        return dfs(root)


s = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(6)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(2)
print(s.helper(root))
