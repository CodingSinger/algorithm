class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 这题很简单 就是维护一个字典，选出每层的最大值 深度遍历
    def helper(self, root):

        d = {}

        def dfs(node, depth):
            if not node:
                return
            pre = d.setdefault(depth, node.val)
            if pre < node.val:
                d[depth] = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return list(d.values())

    # 广度遍历 选出每一层的最大值
    def helper2(self, root):
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue) #当前层在数组的界限
            maxi = float("-inf")
            for i in range(size):
                cur = queue.pop(0)
                maxi = max(maxi,cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.append(maxi)

        return res


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(5)
print(s.helper(root))
print(s.helper2(root))