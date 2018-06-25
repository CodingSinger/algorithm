# 给一棵树和一个数组 看这个数组是否是这棵树或者这棵树的子树的后序遍历
from leetcode.tree import TreeNode


class Solution:
    def helper(self, root, arr):
        temp = []

        def afterTraverse(node):
            if not node:
                temp.append(-1)
                return
            afterTraverse(node.left)
            afterTraverse(node.right)
            temp.append(node.val)


        afterTraverse(root)

        t = temp[temp.index(arr[0]):temp.index(arr[-1])+1]
        if t.count(-1) >= len(t)-t.count(-1): #该序列在此树中不是一颗子树
            return False
        t= list(filter(lambda a:a!=-1,t))
        if t:
            if set(arr).issubset(t):
                return True
        return False

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.left.left.left = TreeNode(6)
arr = [2,3,1]
print(s.helper(root,arr))

