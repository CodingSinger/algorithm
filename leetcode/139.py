class solution:
    def helper(self, s, wordDict):
        length = len(wordDict)

        def cut(str, i):
            if i >= length:
                return False
            temp = str.replace(wordDict[i], "")
            if temp == "":
                return True
            if cut(temp, i + 1):
                return True
            # 回溯
            i += 1
            return cut(str, i)

        return cut(s, 0)

    def helper2(self, s, wordDice):
        d = [False] * len(s) #d[i]表示s[0..i]之前的都能在wordDice中找到对应的字符串序列，
        for i in range(len(s)):
            for w in wordDict:
                # 分两种情况判断 如果i+1 = len(w)，则s[i-len(w)+1:i+1] = s[0:i+1]，相等则记录d[i] = True
                # 另一种情况，如果d[i-len(w)]为真，则只要根据 s[i-len(w)+1:i+1] == w就可以判断d[i]是否为True ，例如leetcode ,["leet","code"]
                # 首先根据第一种情况判断d[3]为true,后续会根据d[3] = True,判断d[7]也为True，因为，s[i-len(w)+1:i+1] = s[7-4+1:8] == 'code'
                if (d[i-len(w)] or i+1 == len(w)) and s[i-len(w)+1:i+1] == w:
                    d[i] = True
        return d[-1]



s1 = solution()
s = ""
wordDict = ["car", "ca", "rs"]
print(s1.helper2(s, wordDict))
