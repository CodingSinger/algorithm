class Solution:
    def helper(self,S):

        result = [[""]]


        for index,s in enumerate(S):
            result.append([])
            if s.isalpha():
                l1 = list(map(lambda x:x+s.upper(),result[index]))
                l2 = list(map(lambda x:x+s.lower(),result[index]))


                result[index+1] = result[index+1]+l1+l2

            else:
                l3 = list(map(lambda x:x+s,result[index]))

                result[index+1] = result[index+1]+l3

        return result[len(S)]


s = Solution()
print(s.helper("33fg23"))


l = [2,4,5]



l = list(map(lambda x:x+1,l))
print(l)


