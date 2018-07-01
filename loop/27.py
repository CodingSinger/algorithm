from leetcode.tree import TreeNode

# 1.核心是中序遍历的非递归算法。
# 2.修改当前遍历节点与前一遍历节点的指针指向。
class Solution:
    def helper(self, root):
        self.pre = None
        def ans(root):
            if not root:
                return None
            dfs(root)
            tmp = root
            while tmp.left:
                tmp = tmp.left
            return tmp



        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            cur.left = self.pre
            if self.pre:
                self.pre.right = cur
            self.pre = cur
            dfs(cur.right)



        return ans(root)


s = Solution()
root = TreeNode(10)
root.left = TreeNode(6)
root.left.left = TreeNode(4)
root.right = TreeNode(14)
root.left.right = TreeNode(8)
print(s.helper(root))
