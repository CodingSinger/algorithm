class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def helper(self, head):

        if not head and not head.next:
            return False
        slow = head.next
        fast = head.next.next

        while fast:

            if fast == slow:
                return True
            if fast.next and fast.next.next:
                fast = fast.next.next

                slow = slow.next

            else:
                return False


    #用set来做，如果有环则会出现已经在set的情况 ，时间复杂度O(n),空间复杂度O(n)
    def helper2(self, head):

        s = set([head])
        while head:
            head = head.next
            if head in s:
                return True
            else:
                s.add(head)

        return False

    # 一个快一个慢，如果有环则肯定会相遇，时间复杂度O(n),空间复杂度O(1)
    def helper3(self,head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


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
print(s.helper2(l))
print(s.helper3(l))
