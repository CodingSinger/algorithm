class Solution:
    def helper(self, nums, k):
        # sumList = []
        index = k
        sums = sum(nums[:k])
        # sumList.append(sums)



        temp = sums
        for num in nums[k:]:
            temp = temp - nums[index - k] + num
            sums = max(sums,temp)

            index += 1



        # maxSum = max(sumList)

        return (sums/ float(k))

    

l = [1,12,-5,-6,50,3]
s = Solution()
print(s.helper(l, 4))
