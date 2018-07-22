
# 排序数列 求和为k的两个数，

class Solution:

    # 思路1：遍历每个数x，再遍历数组，对每一个数x+y是不是为k 时间复杂度O(n^2)
    def helper(self,arr,x):
        pass

    # 既然我们第一次遍历x，则我们只需要找到k-x，则可以用二分法查找 时间复杂度O(nlogn)
    def helper2(self,arr,x):
        pass

    #双指针思路
    # 头指针和尾指针，当头尾指针所在数和大于k,则移动尾指针向前，否则移动头指针向前，找到之后，移动头尾指针，寻找下一组
    def helper3(self,arr,x):

        head,tail = 0,len(arr)-1

        while head <tail:

            if arr[head]+arr[tail] == x:
                print(arr[head]," ",arr[tail])
                head,tail = head+1,tail-1
            elif arr[head]+arr[tail] >x:
                tail-=1
            else:
                head+=1

s = Solution()
print(s.helper3([1,2,5,6,7,8,9,10,12,15],15))
