class Solution:
    # 暴力法
    def helper(self, index):

        def isUgly(x):
            while x % 2 == 0:
                x = x / 2
            while x % 3 == 0:
                x = x / 3
            while x % 5 == 0:
                x = x / 5
            return x == 1

        now, num = 0, 2

        while True:
            if isUgly(num):
                now += 1
                if now == index:
                    return num
            num += 1



    # 该思路直接跳过那些不可能是丑数的数，因为我们知道，一个丑数肯定是当前已经存在丑数集合的某一个丑数的2、3、5倍
    def helper2(self, index):

        now, num = 0, 1
        muply2, muply3, muply5 = num, num, num
        uglys = [1]
        while True:
            now += 1
            uglys.append(min(muply3 * 3, muply2 * 2, muply5 * 5))
            if now == index:
                return uglys[now]
            # 记录下下次立马能超过当前丑数的最小值 下次直接乘即可
            while muply2 * 2 <= uglys[now]:
                muply2 += 1
            while muply3 * 3 <= uglys[now]:
                muply3 += 1
            while muply5 * 5 <= uglys[now]:
                muply5 += 1


s = Solution()
print(s.helper(3))
print(s.helper2(5))
