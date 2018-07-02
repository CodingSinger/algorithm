# 包含min函数的栈结构 min获取当前栈最小的元素 要求min时间复杂度是O(1)

# 思路渐进：
# 1. 临时变量x 保存最小值，每次push都比较是否更小 问题： 如果当前最小元素被弹出？需要保存第二小的元素，如果又被弹出呢？...
#  |
# \|/
# 2. 使用辅助栈，栈顶是最小元素，如果push的元素比栈顶还小，则放入辅助栈，pop的时候如果移除的是最小元素则从辅助栈顶也移除该元素。
class Solution:
    def __init__(self):
        self.arr = []
        self.support = []

    def min(self):
        return self.support[-1]

    def push(self, x):
        if not self.support or self.support[-1] >= x:
            self.support.append(x)
        self.arr.append(x)

    def pop(self):

        x = self.arr.pop()
        if x == self.support[-1]:
            self.support.pop()
        return x


s = Solution()
s.push(1)
s.push(2)
s.push(0)
print(s.arr)
print(s.min())
s.pop()
print(s.min())
print(s.arr)

