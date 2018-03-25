import sys

from leetcode.tree import TreeNode


class Solution:
    def __init__(self):
        self.x = 0


    def helper(self, root, sum):

        def dfs(root, now):
            if not root:
                return 0

            if root.val == 3:
                print("now" + str(now))
            if root.val + now == sum:
                self.x += 1
                print(str(now) + "---" + str(self.x))

            return (1 if now + root.val == sum else 0) + dfs(root.left, now + root.val) + dfs(root.right,
                                                                                                             now + root.val,
                                                                                                             )

        if root:
            return dfs(root, 0) + self.helper(root.left, sum) + self.helper(root.right, sum)

        return 0



    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target - root.val) + self.find_paths(root.right,
                                                                                                             target - root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int

        """

        if root:
            print(str(root.val) + "-----")
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0


sys.setrecursionlimit(1000000)  # 例如这里设置为一百万

s = TreeNode(10)
s.left = TreeNode(5)
s.right = TreeNode(-3)
s.left.left = TreeNode(3)
s.left.right = TreeNode(2)
s.left.left.left = TreeNode(3)
s.left.left.right = TreeNode(-2)
s.left.right.right = TreeNode(1)
s.right.right = TreeNode(11)

s1 = TreeNode(1)
s1.right = TreeNode(2)
s1.right.right = TreeNode(3)
s1.right.right.right = TreeNode(4)
s1.right.right.right.right = TreeNode(5)

h = Solution()
print(h.helper(s1, 3))

# print(h.pathSum(s1,3))
# print(h.pathSum(s, 8))
