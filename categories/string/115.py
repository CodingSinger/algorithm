
class Solution:



    # 动态规划，可以拆分成子问题，并且全局解包含局部解
    # mem[i+1][j+1]表示S[0..j]中包含T[0..i]中的子序列的次数

    # 动态转化方程：
    #    mem[i + 1][j + 1] = mem[i][j] + mem[i + 1][j] if T[i] == S[j] else  mem[i + 1][j + 1] = mem[i + 1][j];
    #
    def helper(self, S, T):
        ls = len(S)
        lt = len(T)
        mem = [[1] * (ls+1) if i == 0 else [0] * (ls+1) for i in range(lt + 1)]

        for i in range(lt):
            for j in range(ls):

                if T[i] == S[j]: #如果相等，则次数应该是S[0..j-1]中包含的T[0..i-1]的次数加上之前S[0...j-1]中包含S[0..i]的次数
                                #举个例子 S = babgbag T = bag,当遍历到T中的a和S中的第二个a时，则相同子序列子树应该为S子串babgb中出现b的次数加上babgb中出现的ba的次数
                    mem[i + 1][j + 1] = mem[i][j] + mem[i + 1][j];
                else:
                    mem[i + 1][j + 1] = mem[i + 1][j]

        print(mem)
        return mem[lt][ls]


        #类似的题目还有球最大公共子序列
S = "babgbag"
T = "bag"
s = Solution()
print(s.helper(S, T))
