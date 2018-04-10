import collections


class Solution:


    #Time Limit Exceeded
    def helper(self, accounts):

        res = []

        for account in accounts:

            flag = False
            for i, r in enumerate(res):

                if account[0] == r[0]:
                    t1 = set(r[1:]).intersection(account[1:])  # 取交集
                    if t1:
                        temp = list(set(r[1:]).union(set(account[1:])))  # 取并集
                    # temp = sorted(temp)


                        index = len(res) - 1
                    # 对并集继续匹配res中的，看是否与其他元素还有交集，有的话取并
                        while index >= 0:
                            if account[0] == r[0]:
                                l = res[index]
                                t = list(set(l).intersection(set(temp)))
                                if t:
                                    del res[index]
                                    temp = list(set(l).union(set(temp)))

                            index -= 1

                        temp = sorted(temp)
                        # temp.insert(0, account[0]) #加上名字
                        res.append(temp)

                        flag = True
            if not flag:
                res.append(sorted(set(account)))

        return res




    #Union-find算法

    #将相同的用户的email分到相同的group中，类似于连通分量的计算
    def accountsMerge(self, accounts):
        class DSU:
            def __init__(self):
                self.p = list(range(10001))

            def find(self, x):
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)

        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]


s = Solution()
a=[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(s.helper(a))
print(s.accountsMerge(a))