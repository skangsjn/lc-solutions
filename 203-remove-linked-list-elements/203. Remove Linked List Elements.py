# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        curr, prev = head, ListNode(-1)
        while curr:
            if curr.val == val:
                dummy = curr
                while dummy and dummy.val == val:
                    dummy = dummy.next

                curr = dummy
                if prev.val == -1:
                    head = curr
                else:
                    prev.next = curr
            else:
                prev = curr
                curr = curr.next
        
        if prev.val == -1:
            return None
        # else:
        #     return prev
        
        print('prev', prev)
        print('dummy', curr)
        
        return head