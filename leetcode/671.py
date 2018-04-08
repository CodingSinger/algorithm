
#思路：树的下层节点的值一定大于等于上层节点，并且树的根节点是最小值，当树的节点值等于这个最小值时，则往下继续搜索，相当于所有节点组成的值集合中，除去树的根节点的值寻找一个最小值
#
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:



    def helper(self,root):
        self.ans = float('inf') #保存之前的节点
        min1 = root.val #根节点是最小的

        def dfs(node):
            if node:
                if min1 < node.val < self.ans: #如果当前节点大于最小的根节点并且小于之前保存的最小节点
                    self.ans = node.val #更新第二小的节点数值 不需要往下遍历了，因为后面的肯定比该rnode.val大
                elif node.val == min1: #当前节点可最小节点相等，则继续往下遍历。
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





    def helper3(self,root):

        def dfs(root):

            if not root.left:
                return float('inf')

            #如果左边的大于右边的，则第二小的值可能为由边
            if root.left.val>root.right.val:
                second = root.right.val
                third = root.left.val
                if second == root.val: #如果左边的等于root.val，则还得继续往下搜索，
                    search = dfs(root.right)  #找到右子树最小的 但可能这个最小的比之前兄弟节点上的值要大
                else:
                    return second
            elif root.left.val < root.right.val:
                second = root.left.val
                third = root.right.val
                if second == root.val:
                    search = dfs(root.left)
                else:
                    return second
            else:
                return min(dfs(root.left),dfs(root.right))

            if search == root.val:
                return third
            second = min(search,third) #比较一边子树的最小值和兄弟节点最小值谁才是这课子树第二小的
            if second == root.val:
                return -1
            return second


        return dfs(root)




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
print(s.helper3(root))
print(min(2,2))












