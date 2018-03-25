class Solution:
    def helper(self, words):
        res = []
        for i, e2 in enumerate(words):
            for k, e1 in enumerate(words):

                if i == k or [i, k] in res or [k, i] in res:
                    continue
                if e2[::-1] == e1:
                    res.append([i, k])
                    res.append([k, i])
                else:
                    if len(e2) > len(e1):
                        temp = e1[::-1]

                        # 截取前面

                        if temp == e2[0:len(temp)]:
                            testlast = words[i][len(temp):]
                            if testlast[::-1] == testlast:
                                res.append([i, k])

                        # 对len(temp) == 0的情况需要在这里特殊处理


                        if len(temp) == 0:
                            if e2[::-1] == e2:
                                res.append([k, i])
                        elif e2[-len(temp):] == temp:

                            testpre = e2[:-len(temp)]
                            if testpre[::-1] == testpre:
                                # 如果成立 则words[k]+words[i]是回文
                                res.append([k, i])

        return res

    def helper2(self, words):
        res = []
        for i, e in enumerate(words):
            for k in range(i + 1, len(words)):
                if len(words[i]) >= len(words[k]):
                    temp1, temp2 = words[k][::-1], words[i]

                    min1,max1 = k,i

                else:
                    temp1, temp2 = words[i][::-1], words[k]
                    min1,max1 = i,k


                if temp1 == temp2[:len(temp1)]:
                    testlast = temp2[len(temp1):]
                    if testlast[::-1] == testlast:
                        res.append([max1, min1])

                        # 对len(temp) == 0的情况需要在这里特殊处理

                if len(temp1) == 0:
                    if temp2[::-1] == temp2:
                        res.append([min1, max1])
                elif temp2[-len(temp1):] == temp1:

                    testpre = temp2[:-len(temp1)]
                    if testpre[::-1] == testpre:
                        # 如果成立 则words[k]+words[i]是回文
                        res.append([min1,max1])

        return res


    def helper3(self,words):
        def is_palindrome(check):
            return check == check[::-1]

        words = {word:i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back], k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals



    def helper4(self,words):

        words = {word:i for i,word in enumerate(words)}
        res = []
        for key,value in words.items():

            for i in range(len(key)+1):

                #根据索引拆分
                pref = key[:i]
                suff = key[i:]

                #判断是否有回文的

                if pref[::-1] == pref:
                    temp = suff[::-1]
                    #检测temp是否在words temp != key是为了避免 abc 拆分成 "aaa" 和 "" 而造成的干扰
                    if temp != key and temp in words:
                        #此时temp应该是连在key前面的
                        if [words[temp],value] not in res:
                            res.append([words[temp],value])
                if suff[::-1] == suff:
                    temp = pref[::-1]
                    if key\
                            != temp and temp in words:
                        if [value,words[temp]] not in res:
                            res.append([value,words[temp]])


        #如上的算法 在"acd" "dca"这种回文的情况下会被重复添加两次
        return res




s = Solution()
l = ["abcd", "dcba", "lls", "s", "sssll"]
l1 = ["a", ""]
l2 = ["a", "abc", "aba", ""]
print(s.helper(l))
print(s.helper2(l))
print(s.helper3(l))
print(s.helper4(l1))
l3 = [0 for i in range(10)]

m = {"3":545,"sdf":345}
