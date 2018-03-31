class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def helper(self, head):

        if not head:
            return False
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        h = 0
        t = len(vals)-1
        while h != t:
            if vals[h] != vals[t]:
                return False
            h += 1
            t -= 1
        return True


    # 思路：首先还是一快一慢指针 当快指针到达尾端时，慢指针到达中点。在这过程中我们把链表前半段的next域反转过来指。这样的话，我们可以从中点向两侧开始遍历比较是否相同
    # 同理，我们可以把后半段的next域反转过来
    def helper2(self,head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
s = Solution()
