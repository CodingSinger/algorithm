class Solution:
    # 题目的意思比较装逼了，其实很简单，就是给一个数组，让你找到两个下标i,j是的min(a[i],a[j])*(j-1)最大(短板效应)
    # 最简单的思路就是讲所有情况都求出来，然后求最大值，这种做法的时间复杂度为O(n*n)的
    #Time Limit Exceeded
    def helper(self,height):
        res = float("-inf")
        length = len(height)
        for i in range(length):
            for j in range(i,length):
                res = max(min(height[i],height[j])*(j-i),res)

        return res

    # 更优的做法是：使用头尾指针 。
    # 假设(start,end)表示选下标为start和end时候的装水容量
    # 因为短板效应，我们假设height[start]<height[end],则此时我们没必要去求start和end处在(start,end)之间的这种情况，
    # 因为短板start已经确定了,end往左移只会使(end-start)更小从而容量更小，所以此种情况下，我们应该让start往右移,同理，当height[start]> height[end]的情况下，我们应该使end往左移
    # 该算法下时间复杂度为O(n)
    def helper1(self, height):
        start, end, res = 0, len(height) - 1, float("-inf")
        while start < end:
            res = max(min(height[start], height[end]) * (end - start),res)
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1

        return res


s = Solution()
print(s.helper([2, 3, 5, 10, 3, 5, 3]))
print(s.helper1([2, 3, 5, 10, 3, 5, 3]))