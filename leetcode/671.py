
#思路：树的下层节点的值一定大于等于上层节点，并且树的根节点是最小值，当树的节点值等于这个最小值时，则往下继续搜索，相当于所有节点组成的值集合中，除去树的根节点的值寻找一个最小值
#
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    def helper(self,root):
        self.ans = float('inf')
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1


    def helper2(self,root):
        one = root.val #one是这棵树的最小值
        self.two = float('inf') #正无穷
        def dfs(node):
            if not node:
                return
            if one < node.val < self.two:
                #大于根节点小于之前的最小值
                self.two = node.val
            elif node.val == one:
                #等于最小值 则往下遍历
                dfs(node.left)
                dfs(node.right)
            else:
                #大于self.two，则无需往下遍历，因为下层节点一定越来越大
                pass
        dfs(root)
        return self.two


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left=TreeNode(2)
root.left.right = TreeNode(2)
s = Solution()
print(s.helper(root))
print(s.helper2(root))

print(min(2,2))












