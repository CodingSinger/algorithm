class Solution:

    # https://www.jianshu.com/p/218c1e4f0891
    def helper(self, m, start, end):

        maxnum = float("inf")
        res = [0 if start == i else maxnum for i in
               range(len(m))]  # 表示从start出发到 点i的最短路径 算出出发点到每个点的最小路径 因为从start->end的路径中的每个点到start的路径一定是最优的，

        # 这句话的意思是从start->end的路径任取一个点mid,当前的start->(A,..) -> mid路径一定是最短的那一条，不可能存在另一条路径从start -> (B...) -> mid比当前这条短,(A.. B..为中途路径)否则的话当前最短路径start - > end一定不是最优路径

        def solve_path(start, end):
            if start == end:
                return
            for i, e in enumerate(m[start]):
                if e != 0:
                    # 路径不为0 则表示有连接 start->i
                    res[i] = min(res[i], res[start] + e)
                    solve_path(i, end)

        solve_path(start, end)
        return res[8]

    def h(self, i):

        self.n = 10
        l = [1, 2, 3]

        def inside():
            i = 11
            l[1] = "sas"
            print(i)

            print(self.n)
            self.n = 100

        inside()
        print(l)
        print(i)
        print(self.n)


m = [[0 for i in range(9)],
     [0, 0, 1, 2, 3, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 4, 0, 0, 0],
     [0, 0, 0, 0, 0, 5, 4, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 6, 0],
     [0, 0, 0, 0, 0, 0, 6, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

s = Solution()
s.h(2)
print(s.helper(m, 1, 8))
