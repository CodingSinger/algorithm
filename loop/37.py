
# 求两个链表的第一个公共节点
# 因为是单向链表，所以第一个公共节点之后，之后都是一样的，即这两个链表形状类似于Y。
# 最简单的思路就是 一次遍历比较两个链表 各个节点 直到第一次相同，这样做时间复杂度为n^2
# 第二个思路那就是借助hash字典，能够有效地判断节点是否在不在该字典，比如我们先将A链表依次放入字典，然后遍历B链表查看B节点是否在字典中，找到第一个在的，时间复杂度为n
# 借助栈，将A和B都放入各自的栈，知道尾部，然后依次弹出，如果是有交点的，则我们一直弹，直到最后栈顶是不相同的。时间复杂度也是n
# 最后一种做法就是得到A和B的长度，加入是4和6，那么我们舍弃掉B的前两个节点，以相同长度的起点开始走，直到走到共同点。该做法不需要额外的空间
class Solution:
    def helper(self,A,B):
        pass




s = Solution()
print(s.helper())