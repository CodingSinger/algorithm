import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:


    def __init__(self):
        self.__h = 100

    # 错误解法 无法解决是否是根节点的问题，即数组化的树可能有多种可实现的树结构

    # 低效解法 O(n3)
    def helper(self, root):

        arr = []

        def dfs(node):
            if node:
                arr.append(node.val)
                dfs(node.left)
                dfs(node.right)

        res = []
        dfs(root)

        count = -1
        length = len(arr)
        for i in range(length - 1):
            for k in range(i + 1, length):
                temp1 = i
                temp2 = k
                if arr[temp1] == arr[temp2]:
                    res.append([])
                    count += 1
                while arr[temp1] == arr[temp2]:
                    res[count].append(arr[temp1])
                    temp1, temp2 = temp1 + 1, temp2 + 1
                    if temp2 >= length:
                        break

        return res


    # 需要解决数组化树的唯一性，即一个数组只能构造出一颗树

    #并且不进行循环比较来判断是否存在相同的子树，而是根据字典的计数根据是否有相同的序列判断之前是否有相同结构的子树出现
    def helper2(self,roo):
        count = collections.Counter()
        ans = []

        def collect(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans


    def helper3(self,root):
        print(self.__h)
        trees = collections.defaultdict()
        print(trees.__len__())
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []

        def lookup(node):
            # if not node:
                # print("s")
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                # print(node.val)
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(2)


s = Solution()
print(s.helper2(root))
print(s.helper3(root))