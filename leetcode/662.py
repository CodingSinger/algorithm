class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def helper(self,root):
        d = {}
        self.res = 0

        #设父节点的position为x,则左子树的position为2x，右子树的2x+1
        def dfs(node,depth,pos):
            if node:
                #记录下第一个在该层的节点的位置
                if depth not in d:
                    d[depth] = pos
                self.res = max(self.res,pos-d[depth]+1) #每到一个键都需要更新最大跨度
                dfs(node.left,depth+1,pos*2)
                dfs(node.right,depth+1,pos*2+1)


        dfs(root,0,0)
        return self.res


root = TreeNode(10)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.left = TreeNode(3)
s = Solution()
print(s.helper(root))



