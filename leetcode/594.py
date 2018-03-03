import collections
from collections import Collection


class Solution:


    #思路:排序后用start每个子串的开始下标，其实nums[start]表示的就是子串中较小的值出现的第一个位置的下标，当nums[i] != nums[i-1]时更新new_start，当nums[i] - min =>1 时，则说明一个和谐子串结束了，则更新start为new_start,
    #因为new_start是上一个子串的最大值的第一个索引，但可能是下一个子串的较小值的索引，例如1 2 2 2 3，当遍历到3时，new_start = 1,start = 0,此时需要更新start = new_start.
    def helper(self, nums):
        # 1 2 2 2 3 3 5 7
        nums.sort()
        result = 0
        start, new_start = 0, 0

        for i in range(1, len(nums)):
            if nums[i] - nums[start] > 1:
                start = new_start
            if nums[i] != nums[i - 1]:
                new_start = i
            if nums[i] - nums[start] == 1:
                result = max(result, i - start + 1)
        return result

    #思路：我们知道最长的协调子串是相邻的两个数字的总个数。所以我们只需要统计每个数字的个数，并且遍历数组，统计i+1的个数，与之前的result相比取大值即可

    def helper2(self, nums):

        map = collections.Counter(nums)

        for i in map:
            if i+1 in map:
                result = max(result,map[i]+map[i+1])
        return result



s = Solution()
l1 = [1, 2, 2, 1]
l2 = [1, 1, 1, 1]
l3 = [1, 3, 5, 7, 9, 11, 13, 15, 17]
l4 = [1, 3, 2, 2, 2, 3, 5, 3, 7]
l5 = [1, 4, 1, 3, 1, -14, 1, -13]
l6 = [1, 2, 2, 3, 4, 5, 1, 1, 1, 1]
print(s.helper(l5))
print(s.helper(l3))
print(s.helper(l6))

print(s.helper(l2))
print(s.helper([1, 2, 3, 4]))
print(s.helper(l1))
print(s.helper(l4))

print(s.helper(l4))