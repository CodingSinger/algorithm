import operator


class Solution:
    def helper(self,nums):

        for i,num in enumerate(nums[:-1]):
            if i == 0 or (nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                new = nums[:i]+nums[i+1:]
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                new = nums[:i]+nums[i+1:]
            else:
                continue

            sl = sorted(new)
            if  sl == new:
                return True

        return len(nums) == 1 or nums[:-1] == sorted(nums[:-1])


    # 2 6 7 4 8
    # 遍历整个数字，如果当前数字比前面的数字小，那么这个数字是一定要改变的。需要考虑的是，把当前的数字改成多少才合适。
    #
    # 因为要得到的序列是非递减的，意味着相邻的元素可以是相同的，那么我们就可以将需要改变的数字改为前面的那个数字，当然我们也可以把前面的那个数字改成当前的这个数字。
    #
    # 当决策有两种的时候，我们只需要考虑其中一种较为简单的情况需要符合的条件。条件之外就是另一种情况。
    #
    # 这里我们考虑把前面的数字变成当前的数字的情况，当前面的数字再前面没有数字，那么无疑改前面的数字是最好的，不会影响后面。如果前面的数字再前面还有数字，并且要是小于关系，那么改前面这个数字也是对后面没影响的。
    #
    # 我们只要按照这种方法进行数字的修改，直至遍历完成，如果修改次数小于等于1，那么返回true，否则返回false。


    def helper3(self,nums):


        count = 0
        for i in range(1,len(nums)):


            if nums[i] < nums[i-1]:
                if i <2 or nums[i-2] < nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]

                count += 1

        return count<=1










    # limit exceeded 遍历删除一个元素组合成新数组 然后排序比较是否和新数组一致 如果一致则说明移除某个元素能使得剩下的有序 则返回True
    def helper2(self,nums):

      for i in range(len(nums)):
          l = nums[0:i]+nums[i+1:]
          if l == sorted(l):
              return True

      return False






s = Solution()
l = [4,2,1]
print(s.helper(l))
print(s.helper3(l))
print(s.helper2([1,3,2]))
