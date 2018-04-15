class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    #思路：用s树中的每个节点的子树和t进行比较。一旦相等就返回True
    def helper(self,s,t):


        # 比较s的每一个节点 和node的根节点，

        def result(node1,node2):

            if not node1:
                return False

            if compare(node1,node2):
                return True
            return result(node1.left,node2) or result(node1.right,node2)



        # 比较node1和node2两棵树是否相同，一层层往下比较
        def compare(node1,node2):
            if (not node1 and node2 ) or (node1 and not node2):
                return False
            if not node1 and not node2:
                return True

            if node1.val == node2.val :
                return compare(node1.left,node1.left) and compare(node1.right,node2.right)
            else:
                return False
        return result(s,t)





root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left = TreeNode(5)
root.left.right.left= TreeNode(0)
s = Solution()

root1 = TreeNode(2)
root1.left = TreeNode(5)
root1.right = TreeNode(4)
print(s.helper(root,root1))
