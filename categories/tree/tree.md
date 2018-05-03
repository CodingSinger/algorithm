
和树相关的题目，一般都需要用递归来解决问题，这个时候，我们需要清楚递归出口的设计，以及主要的逻辑操作
是需要在递归到最底层之前进行还是需要在递归到最底层之后进行。



关于用数组构造出一颗独一无二的树
叶子节点的子节点用#表示
can be represented as the serialization 1,2,#,#,3,4,#,#,5,#,#, which is a unique representation of the tree.



# 典型的树题和思考


```python

class Solution:
    def helper(self,root):

        self.res = 0
        def dfs(node, mathleft=None):
            if not node:
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                self.res += abs(left-right)

                return left+right+node.val #记住该是获取子树所有节点值的方法
        dfs(root)
        return self.res

```




```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归到最底(没有子节点)，如果最底层是0，则删除，然后往上移，如果该节点也是0，并且子节点都被移除了，则也移除，继续往上移动。依次递归
# 下层树先操作才能操作上层树的题目时，需要先左右深度遍历到最底层，然后进行操作，(操作在递归之后)，像该题中的判断删除操作，就放在dfs(node.left)和dfs(node.right)之后
class Solution:
    def helper(self, root):


        def dfs(node, parent, left):

            if not node:
                return
            dfs(node.left, node, True)
            dfs(node.right, node, False)
            if node.val == 0 and not node.left and not node.right:
                if left:
                    parent.left = None
                else:
                    parent.right = None

        dfs(root.left,root,True)
        dfs(root.right,root,False)
        return root

    def print(self, root):
        if not root:
            return
        self.print(root.left)
        print(root.val)
        self.print(root.right)



root = TreeNode(1)

root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
s = Solution()
root = s.helper(root)
s.print(root)



```




树的子节点和树的父节点在数组中的关系

```python


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

```