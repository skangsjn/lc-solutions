# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        start = curr = head
        prev = None
        count = 0

        while curr:
            count += 1
            if count > n:
                prev = start
                start = start.next
            curr = curr.next
        
        if prev:
            prev.next = start.next
        else:
            head = head.next

        return head