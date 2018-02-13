

class Splution:
    def helper(self,nums):

        result = nums[0]
        sum = nums[0]

        for index in range(1,len(nums)):
           sum = max(nums[index],sum+nums[index])
           result = max(result,sum)
        return result



    def helper2(self,A):
        if not A:
            return 0


        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum


s = Splution()
a = [3,4]

print s.helper([-2,1,-3,4,-1,2,1,-5,4])
