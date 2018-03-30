import collections
import heapq


class Solution:
    def helper(self,S):

        #将S中元素计数并存入字典
        m = collections.Counter(S)

        #获得值最大的对应的键
        v = max(m,key=m.get)

        if m[v] > (len(S)+1)//2:
            return ""

        queue = [ i for i in S]

        start = 0
        temp = ","
        l = len(S)
        while len(temp) <= l:
            if temp[-1] == queue[start]:

                queue.append(queue[start])
            else:
                temp+=queue[start]
            start+=1

        return temp[1:]




    def reorganizeString(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            # This code turns out to be superfluous, but explains what is happening
            # if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            # else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')
s = Solution()
print(s.reorganizeString("aaabbbcc"))
print(s.helper("vvvlo"))