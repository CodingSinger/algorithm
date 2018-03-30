



#合理运用hashMap set等集合来处理能够使算法简单

#例如此题，将数字放入hashMap中，对重复的更新值为2。 然后遍历1-n,不存在map[i+1]的就为缺少的，存在map[i+1]==2的就是重复的
class Solution:

    def helper(self,nums):

        map = {}

        result = []
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] = 2
        for i in range(len(nums)):
            if i+1 not in map:
                result.insert(1, i + 1)
                continue
            if map[i+1] == 2:
                result.insert(0,i+1)


        return result

s = Solution()
print(s.helper([3,2,3,4,6,5]))


