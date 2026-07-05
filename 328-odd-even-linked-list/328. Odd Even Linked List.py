# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        con = head.next
        prev_odd = ListNode(1)
        prev_even = ListNode(2)

        while curr and curr.next:
            next_node = curr.next
            next_odd = curr.next.next
            
            prev_odd.next = curr
            prev_even.next = next_node

            prev_odd = curr
            prev_even = curr.next

            curr = next_odd
        
        if curr:
            last_odd = prev_even.next
            prev_odd.next = last_odd
            prev_even.next = None
            last_odd.next = con
        else:
            prev_odd.next = con
        
        return head