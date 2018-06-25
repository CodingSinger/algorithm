from leetcode.tree import TreeNode

# 因为题目中规定了路径是从根搜索到叶子，即一直往下的，则用深度搜索既可

class Solution:
    def helper(self, root, value):

        def dfs(node, sum, path):

            if not node:
                return
            path += " " + str(node.val) + " "
            cur = node.val + sum
            if not node.left and not node.right and cur == value: # 1
                # 打印
                print(path[1:])
                return
            dfs(node.left, cur,path)
            dfs(node.right, cur,path)

        dfs(root, 0, "")


    # 如果不规定路径需要从根节点开始并结束在叶子节点，思路也很简单，就是在上面的基础上，对该树每一个节点当作根节点进行调用上面的步骤，并且需要
    # 除去1处代码中对叶子节点的限制
    def helper1(self):
        pass



s = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
root.left.left = TreeNode(8)
root.left.right = TreeNode(7)
s.helper(root,22)