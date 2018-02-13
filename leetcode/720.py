

class Solution:
    def helper(self,words):

        sort = [[] for i in range(30)]
        copy = [[] for i in range(30)]



        result = []
        for s in words:
            sort[len(s)].insert(0,s)
            copy[len(s)].insert(0,s)


        for index in range(len(sort)-1,-1,-1):
            if not sort[index]:
                continue
            for j in sort[index]:
                f = self.DPS(index-1,j[:-1],copy,sort)
                if f :
                    result.append(j)

        max = 0
        S = ""
        for s in result:
            if len(s) > max or (s <S and len(s) == max):
                max = len(s)
                S = s
        return S




    def DPS(self,i,subStr,copy,search):
        if i == 0:
            return True

        if subStr in copy[i]:
            if subStr in search[i]:
                 search[i].remove(subStr)
            return self.DPS(i-1,subStr[:-1],copy,search)
        return False


    def helper2(self,words):
        words, resword, res = sorted(words), '', set() #排序是关键
        for word in words:
            if len(word) == 1 or word[:-1] in res:
                res.add(word)
                resword = word if resword == '' else word if len(word) > len(resword) else resword
        return resword

            


s = Solution()
print(s.helper(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
print(s.helper2(["a", "banana", "app", "appl", "ap", "apply", "apple","bc"]))







