

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:



    #思路：由题意得出二维数组的宽度由树的高度决定，并且高度h和宽度w的关系为w = (2^h)-1
    #因此先求出树的高度。初始化数组，然后我们需要思考如何得到每个节点在数组中的坐标arr[x][y],x很好确定，就是每往下递归一层就进行加1
    #规律可得左子树节点的坐标和当前节点的坐标(a,b)的关系为x = a+1,y = (low+b)//2 ,右子树关系为x = a+1,y=(b+high)//2
    # low 和high初始为0和数组宽度w.一直二分下去。

    def helper(self,root):
        def getMaxDeep(node):
            if not node:
                return 0
            left = getMaxDeep(node.left)+1
            right = getMaxDeep(node.right)+1
            return max(left,right)
        maxDeep = getMaxDeep(root)

        breadth = pow(2,maxDeep)-1
        array = [[""]*breadth for i in range(maxDeep)]
        # 需要知道每个node在数组的下标
        # 刚开始根节点的下标为(0,(2^deep-1)//2)
        def print(deep,node,low,high):
            if not node:
                return
            mid = (low+high)//2
            array[deep][mid] = str(node.val)

            print(deep+1,node.left,low,mid) #左子树节点的位置应该在当前节点位置和low节点的中间

            print(deep+1,node.right,mid,high) #右子树的位置应该在当前节点位置和high节点中间

        print(0,root,0,breadth)
        return array


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
s = Solution()
print(s.helper(root))






