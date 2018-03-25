# 最小生成树算法


class Solution:
    def helper(self, graph):
        ls = len(graph)
        queue = [float("inf") for i in range(ls)] #初始化各个节点的键值为无穷大
        path = [-1 for i in range(ls)] #保存最小生成树的路径 例如path[i]= k表示最小生成树有路径i->k，

        removed = [] #另一棵子树
        tmp = 0
        while len(removed) < ls:

            mins = float("inf")


            #求出最小值
            for i, v in enumerate(queue):
                if i not in removed and v < mins:
                    mins = v
                    tmp = i

            #把i节点加入另一棵子树中
            removed.append(tmp)
            for index, n in enumerate(queue):
                if index in removed: #如果index节点已经在removed子树中
                    continue
                key = graph[tmp][index]
                if key != 0 and n > key:# tmp到index之间有通路，并且之前连接两棵树的距离大于现在的tmp-index之间的距离
                    queue[index] = key #更新距离
                    path[index] = tmp #更新index到另一棵子树的路径

        return path


s = Solution()

graph = [
    [0, 15, 7, 10, 0, 0, 0, 0],
    [15, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 9, 12, 5, 0],
    [10, 0, 0, 0, 0, 0, 8, 3],
    [0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 12, 0, 0, 0, 6, 0],
    [0, 0, 5, 8, 0, 6, 0, 14],
    [0, 0, 0, 3, 0, 0, 14, 0]
]

print(s.helper(graph))
