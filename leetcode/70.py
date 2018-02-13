#coding=utf-8


# dp问题都是从解决局部到解决全部  从最底层开始一层层逼近最终答案 如题 要解决第n层的梯子步数 需要依次解决1~n-1层的步数 设想如果解决了第一层所需的步数为x,则第2层的走法就在第一层走法的基础上只需思考剩下的层数的走法
class Solution:
    def helper(self,n):

        ns = [ 0 for i in range(n+1)]

        ns[0] = 1 #每次只走一步的方法
        steps = [1,2]
        for i in range(1,n+1):
            for step in steps:
                if i-step>=0:

                    ns[i] = ns[i-step]+ns[i]

        return ns[n]

s = Solution()
print s.helper(3)


