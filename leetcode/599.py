class Solution:

    #time : l1 +l2*x
    def helper(self, list1, list2):

        map = {}

        result = {}
        for index, e in enumerate(list1):
            map[e] = index

        min = float("inf")
        for i in map:

            if i in list2:
                map[i] = map[i] + list2.index(i)
                if map[i] not in result:
                    result[map[i]] = [i]

                else:
                    result[map[i]].append(i)
                if min > map[i]:
                    min = map[i]



        return result[min]


    def helper2(self,list1,list2):


        map = {}

        result = []
        for index, e in enumerate(list1):
            map[e] = index

        min = float("inf")

        for index,e in enumerate(list2):
            if e in map:


                map[e] = map[e]+index

                if min>map[e]: #如果当前min大于map[e],则说明找到了更小的和索引的感兴趣的值，则应将之前的result清空
                    result.clear()
                    result.append(e)
                    min = map[e]
                elif min == map[e]:
                    result.append(e)


        return result








s = Solution()
l1 = ["Shogun","Tapioca Express","Burger King","KFC"]
l2 = ["KFC","Shogun","Burger King"]
print(s.helper(l1, l2))
print(s.helper2(l1, l2))
