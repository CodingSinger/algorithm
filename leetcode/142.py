class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#         d2: distance from head to cycle entry E
#         d1: distance from E to X
#         l: cycle length

#                           _____
#                          /     \
#         head_____d2______E       \
#                         \       /
#                          X_____/

# 如果有回环的话，则将slow移动到head,此时，fast和slow每次往前走一步，再次相交的点就是环的起点

# 证明: 假设第一次相交的时候slow走的距离为x,则fast走的距离为2x，在相遇的时候，fast已经绕着环假设走了n圈，设圈长为l,则2x-x = nl,x = nl

#设交点到环起点为d1,设环起点到头结点距离为d2,则x = d1+d2 = nl ,即d1+d2 = (n-1)l+l,所以 d2 = (n-1)l+(l-d1) ,l-d1就是 交点到环另一侧的起点。（X->E）

# 双

class Solution:
    def helper(self,head):
        slow = fast = head



        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:

                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None


l = ListNode(10)
l1 = ListNode(5)
l.next = l1
l2 = ListNode(20)
l1.next = l2
l3 = ListNode(25)
l2.next = l3
l4 = ListNode(30)
l3.next = l4
l4.next = l2
s = Solution()
print(s.helper(l))




