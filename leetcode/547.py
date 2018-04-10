import collections


class Solution:

    ## 深度遍历方法：
    # 1. 遍历每个节点的所有连接节点k, 并依次深度搜索下去。将该节点所有连接节点进行加入同一个组，途中注意需要判断该节点是否已经被遍历过了，如1-》2，则由2-》1重复遍历，需要判断1是否已经在该组中
    def helper(self, M):

        groups = collections.defaultdict(list)

        def dfs(node, group):

            for i in range(len(M)):
                if M[node][i] == 1 and i not in groups[group]:  # 有连接并且这个点之前没有加入该组
                    groups[group].append(i)
                    dfs(i, group)

                    nodes.remove(i) #从待遍历节点中移除该点，这样的话nodes中的元素都将是没有加入组的节点

        nodes = list(range(len(M) - 1, -1, -1))

        group = 0
        while nodes:
            node = nodes.pop() #弹出一个点进行遍历
            groups[group].append(node) #弹出的点肯定是没有加入任何组的
            dfs(node, group) #深度遍历
            group += 1

        return group


s = Solution()
M = [[1,1,0],[1,1,0],[0,0,1]]
print(s.helper(M))
