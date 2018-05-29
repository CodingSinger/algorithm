# 最长上升子序列 1,7,5,4,3,8
class Solution:
    def helper(self, arr):
        lis = [1 for i in range(len(arr))]  # 状态 lis[i]表示第下标为arr[0..i]之间以arr[i]结尾的最长上升子序列
        res = 1                         # 状态转移方程为 lis[i] = max(lis[j]+1,lis[i] if arr[i]>arr[j]  j in [0..i)
        for i in range(len(arr)):
            for j in range(0, i):
                if arr[j] < arr[i]:
                    lis[i] = max(lis[j] + 1, lis[i])
            res = max(res, lis[i])
        return res


s = Solution()
print(s.helper([1, 3, 5, 4, 3, 8, 0]))
