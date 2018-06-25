class Solution:
    def helper(self, heights):



        # 3，4，5，6，7,5
        # 3，4，5，6，7入栈，因为7大于5，则不入栈，此时以7为高的面积是肯定知道的，7*1，弹出7之后继续比较栈顶和5的大小，此时6也是大于5，则此时以6为高的面积也肯定是确定的，
        # 6 *2(2怎么计算来的，是由此时5的下标和6的下标之间的距离得到的。
        # https://www.cnblogs.com/boring09/p/4231906.html
        heights.append(0)
        maxArea, stack = 0, []
        for i in range(len(heights)):
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
            else:
                while  stack and heights[stack[-1]] > heights[i]:
                    low = stack.pop()

                    h = heights[low]

                    w = i if len(stack) == 0 else i - stack[-1]-1

                    maxArea = max(maxArea, h * w)
                stack.append(i)

        return maxArea


s = Solution()
height = [4,5,6,7,8,5]
print(s.helper(height))