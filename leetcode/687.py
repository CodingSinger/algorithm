
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



#递归的思想

class Solution:
    def helper(self,root):
        self.maxResult = 0

        self.DFS(root)
        return self.maxResult




    #该题目和求树的高度思想差不多，都是递归到最底层然后一层一层累加


    def DFS(self,root):

        #递归的终结条件就是root为None
        if not root:
            return 0


        # 由题意得出当前节点左子树和右子树的最长相同高度是必须算出来的，并且在该层递归需要，所以需要变量接收
        left_length = self.DFS(root.left)
        right_length = self.DFS(root.right)


        # 考虑上本层节点之后的最长相同高度 不同则为0，相同则在下层节点结果上进行加1
        left_now = right_now = 0
        if root.left and root.val == root.left.val:
            left_now = left_length+1
        if root.right and root.val == root.right.val:
            right_now = right_length+1

        #考虑题中例子2的情况，对于本节点root来说，可以使用左右子树的长度和，所以需要计算左子树和右子树长度和的结果
        self.maxResult = max(self.maxResult,left_now+right_now)
        # 返回只需返回最长的单边
        return max(left_now,right_now)




    def helper2(self,root):

        self.result2 = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            left_now = right_now =  0
            if node.val == node.left.val:
                left_now = left+1
            if node.val == node.right.val:
                right_now = right+1

            self.result2 = max(self.result2,left_now+right_now)
            return max(left,right)


    def helper3(self,root):
        self.res = 0



        def dfs(node):

            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            left_now = right_now = 0
            if node.left.val == node.val:
                left_now = left+1
            if node.right.val == node.val:
                right_now = right+1

            self.res = max(self.res,left_now+right_now)
            return max(left,right)


        dfs(root)
        return self.res







root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)
s = Solution()
print(s.helper(root))






