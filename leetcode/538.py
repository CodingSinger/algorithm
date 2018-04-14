class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root):

        self.vals = []

        # 中序遍历 因为是二叉搜索树 所以遍历结果是个从小到大的有序数组
        def dfs(node):
            if node:
                dfs(node.left)
                self.vals.append(node.val)
                dfs(node.right)

        self.sums = 0

        def restructure(root): # 从最大的节点进行重新计算节点值，因此新节点值为老节点值加上之前已经遍历过的节点值的和
            if root:
                restructure(root.right)
                root.val = self.sums = self.sums + self.vals.pop()
                restructure(root.left)

        dfs(root)
        restructure(root)

    @staticmethod
    def show(node):

        if node:
            Solution.show(node.left)
            print(node.val)

            Solution.show(node.right)


    #思路2：也是从最大节点开始遍历，累加已经遍历过的节点值，根据累加值来更新当前节点值
    def helper2(self, root):

        self.sums2 = 0
        def dfs(node):
            if node:
                dfs(node.right)
                self.sums2 += node.val
                node.val = self.sums2

                dfs(node.left)
        dfs(root)
        return root


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
s = Solution()
# s.helper(root)
# Solution.show(root)

Solution.show(s.helper2(root))