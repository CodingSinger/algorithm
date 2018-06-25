from leetcode.tree import TreeNode

# 按树高从上到下打印整颗树
class Solution:
    def helper(self, root):
        d = {}

        def dfs(node, deep):

            if not node:
                return
            if deep not in d:
                d[deep] = []
            d[deep].append(node.val)
            dfs(node.left,deep+1)
            dfs(node.right,deep+1)
        dfs(root,0)
        for i in range(max(d.keys())+1):
            print(" ".join([str(s) for s in d[i]]),end=" ")

    #双端队列，打印父节点，如果有子节点，则pushback到末尾，并从前面依次取出节点，继续前面的操作。
    def helper2(self,root):
        pass

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.left.left.left = TreeNode(6)
s.helper(root)
