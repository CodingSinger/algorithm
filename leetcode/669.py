
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, root, L, R):

        self.nroot = TreeNode(0)

        def dfs(node, parent):
            if node:
                if L <= node.val <= R:
                    if node.val > parent.val:
                        parent.right = node
                    else:
                        parent.left = node
                    dfs(node.left, node)
                    dfs(node.right, node)
                elif node.val < L:
                    parent.left = None
                    dfs(node.right,parent)
                else:
                    parent.right = None #需要注意这里需要置空，因为后面的不需要遍历了
                    dfs(node.left, parent) #需要注意这里依旧传入parent，而不是node，因为并未parent并未连接本次节点，继续传入下次递归
        dfs(root,self.nroot)
        return self.nroot.left if self.nroot.left else self.nroot.right

    def helper2(self,root,L,R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
s = Solution()
root = TreeNode(3)
root.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right = TreeNode(4)
n = s.helper2(root,1,3)
print(n)

root1 = TreeNode(1)
root1.left = TreeNode(0)
root1.right = TreeNode(2)

print(s.helper(root1,1,2))