import collections
import heapq


#这题和767题思路差不太多，需要注意的是间隔n时，则需要每次都取n+1个不同的，当取出来的元素个数小于n+1时，则需要补上空闲时间，
# 但是在最后末尾的则不需要补空闲时间，例如abcabca, n =2 ,最后一次只取出来1个a，因为结束了， 所以不需要加上n，只需要加上最后取出来的个数


class Solution:
    def helper(self,tasks,n):

        n = n+1
        m =  [(-tasks.count(x), x) for x in set(tasks)]
        heapq.heapify(m)
        least = 0

        temp = []
        while m:
            length = min(len(m),n)
            for i in range(length):
                count,ele = heapq.heappop(m)

                if count +1:
                    temp.append((count+1,ele))


            for i in temp:
                heapq.heappush(m,i)

            temp.clear()



            if len(m) == 0: #已经是末尾了，则只需加最后取出来的元素个数
                least += length
            else: #否则按n来加，(不管有没有取够n个，没取够填充空闲)
                least += n




        return least
s = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
print(s.helper(tasks,2))



