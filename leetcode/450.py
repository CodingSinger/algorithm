
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self,root,key):

        def delete(node,val):
            if not node:
                return None

            if node.val > val:
                node.left = delete(node.left,val)
            elif node.val < val:
                node.right = delete(node.right,val)
            else:

                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:

                    maxNode = findLeftMax(node.left) #从node.left中找到最大的值 替代当前node
                    node.val = maxNode.val
                    #从node.left中搜索出maxNode.val删除
                    node.left = delete(root.left,maxNode.val)

            return node




        def findLeftMax(node):

            while node.right:
                node = node.right
            return node

        return delete(root,key)

s = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root =  s.helper(root,3)
print(root)