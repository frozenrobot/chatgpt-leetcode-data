# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        middle = length // 2
        curr = head

        for _ in range(middle):
            curr = curr.next

        return curr
