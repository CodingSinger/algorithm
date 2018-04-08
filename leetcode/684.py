import collections


class Solution:


    #基本思路 通过union-found算法，将节点存储到数组中，通过一个节点搜索到最底部的节点，然后判断两个节点是否通过相同节点相连。
    def helper(self,edges):

        temp = [i for i in range(1000)]

        def find(key):
            if temp[key] != key: # 如果key是temp[key]的子节点
                return find(temp[key])
            #已经是根节点了
            return key
        for e in edges:
            k1, k2 = e[0], e[1]
            t1,t2 = find(k1),find(k2) #找到k1,k2的最终子节点
            #如果最终子节点相同 则说明k1,k2节点会通过该最终子节点连接
            if t1 == t2:
                return e
            else:
                temp[t1] = t2
        return None


    def helper2(self,edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])


        #把所有边按点到点的方向进行存储，即{1：{2，3}}表示1到2和1到3有通路
        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v): #判断是否点u和点v是否有一条路径能连接 即u和v是否能连通
                return u, v
            graph[u].add(v)
            graph[v].add(u)

s = Solution()
l = [[1,2],[1,3],[2,3]]
print(s.helper(l))
print(s.helper2(l))
