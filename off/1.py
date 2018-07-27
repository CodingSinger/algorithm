class Solution:
    def helper(self):

        temp = input()
        temp = temp.split(" ")
        N, M = int(temp[0]), int(temp[1])
        di, pi = [], []
        ai = []
        for i in range(N):
            s = input()
            temp = s.split(" ")
            di.append(temp[0])
            pi.append(temp[1])

        s = input()
        ai = s.split(" ")

        

        for i in range(M):
            cur = -1
            for j in range(N):
                if int(di[j]) <= int(ai[i]):
                    cur = max(cur, int(pi[j]))

            print(cur)




s = Solution()
s.helper()