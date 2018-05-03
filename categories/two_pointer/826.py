
class Solution:


    # 超时 O(M*N)
    def helper(self,difficulty,profit,worker):

        length = len(difficulty)
        res = 0
        for w in worker:
            i = 0
            maxp = 0
            while i < length:
                if w>=difficulty[i]:
                    maxp = max(maxp,profit[i])
                i+=1
            res+=maxp

        return res

    # 和上面的代码看起来区别不大，但是上面的其实对每一个worker的对每一个difficulty进行遍历 时间复杂度为O(M*N) M为人数，N为工作数
    # 而下面的不然，对worker和difficulty进行排序之后，则保证后面遍历到的worker一定比之前的能力强。
    # 即前一个worker能做的收益最大的工作后一个worker一定也能做，保存了状态i，每一次只需从i开始遍历得到当前worker能做的最大收益的工作即可，而不需要从0开始遍历
    # 时间复杂度 O(NlogN+QlogQ)
    def helper2(self, difficulty, profit, worker):
        jobs = zip(difficulty, profit)
        jobs = sorted(jobs)
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
s = Solution()
print(s.helper(difficulty,profit,worker))
print(s.helper2(difficulty,profit,worker))