from leetcode.tree import TreeNode


class Solution:
    def helper(self, root):

        def dfs(root):

            if root:
                return root.val + dfs(root.left) + dfs(root.right)
            else:
                return 0

        return dfs(root)

    def helper2(self, root):

        def dfs(root):
            if root.left:
                if not root.left.left and not root.left.right:
                    return root.left.val + dfs(root.right)
                else:
                    return dfs(root.right) + dfs(root.left)
            return 0

        return 0 if not root else  dfs(root)

    def helper3(self, root):

        def dfs(root):

            if not root:
                return 0
            if root.left and not root.left.left and not root.left.right:# 如果左子树是叶子，则返回叶子的值加上右子树继续递归的值
                return root.left.val + dfs(root.right)
            else:

                return dfs(root.right) + dfs(root.left) #否则左子树和右子树继续递归

        return 0 if not root else  dfs(root)


s = TreeNode(10)
s.left = TreeNode(5)
s.right = TreeNode(-3)
s.left.left = TreeNode(3)
s.left.right = TreeNode(2)
s.left.left.left = TreeNode(3)
s.left.left.right = TreeNode(-2)
s.left.right.right = TreeNode(1)
s.right.right = TreeNode(11)

s1 = TreeNode(1)
s1.right = TreeNode(2)
s1.right.right = TreeNode(3)
s1.right.right.right = TreeNode(4)
s1.right.right.right.right = TreeNode(5)

s2 = TreeNode(3)
s2.left = TreeNode(9)
s2.right = TreeNode(20)
s2.right.left = TreeNode(15)
s2.right.right = TreeNode(7)
h = Solution()
print(h.helper(s1))
print(h.helper2(s1))
print(h.helper2(s2))
print(h.helper3(s2))
