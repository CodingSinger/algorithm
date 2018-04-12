
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