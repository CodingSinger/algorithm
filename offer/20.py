# 顺时针打印二维数组


# 我们可以把矩阵想象成一个圈，然后从外到内一圈一圈打印
# 需要注意的是打印每一圈的时候需要考虑除去边界重复打印的值
class Solution:
    def helper(self, arr):
        height, weight = len(arr[0]), len(arr)
        count = 0

        while count < weight // 2:


            up, down = count, weight - count
            for i in range(count, height - count):
                print(arr[up][i], " ")
            left, right = count, height - count
            for i in range(count+1, weight - count):
                print(arr[i][right-1], " ")
            for i in range(height - count-2,count-1,-1):
                print(arr[down-1][i], " ")
            for i in range(weight - count-2,count,-1):
                print(arr[i][left], " ")
            count += 1




s = Solution()
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(s.helper(arr))
