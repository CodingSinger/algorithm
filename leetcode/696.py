
#思路：题目让我们求01出现次数相同并且0，1连续的子串，形如 k*0+k*1 或者k*1+k*0，
# 因此为每个0，1记录连续的次数，例如“001100011”，则记录成group = [2，2，3，2],因为可以01和10，可以知道每相邻的两个group元素都可以提供结果的一部分，并且由其中的小的决定子串的最多0或者1的个数，其个数就是
# 子串的数量，举例来说 00011 记录成3，2 则可以提供子串01，0011，而不能00011，所以result = result +min(group[i],group[i+1]).

class Solution:
    def helper(self,s):
        group = [1]
        lcount = 0
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                group.append(1)
                lcount+=1
            else:
                group[lcount] = group[lcount]+1


        result = 0
        for i in range(1,len(group)):
            result +=min(group[i],group[i-1])


        return result

#思路二：就是在思路一的基础上不用额外的group列表来保存，而只用last和cur这两个变量来保存当前遍历的索引i的上两个元素的连续出现次数
    def helper2(self,s):
        last ,cur ,result = 0,1,0
        for i in range(1,len(s)):

            if s[i]!= s[i-1]:

                result += min(cur,last)
                last = cur
                cur = 1


            else:
                cur = cur+1

        return result+min(cur,last)



s = Solution()
print(s.helper("00110011"))
print(s.helper2("10101"))

