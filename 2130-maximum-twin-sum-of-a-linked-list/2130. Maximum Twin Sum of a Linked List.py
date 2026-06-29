# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        count = ans = 0

        # find middle of LL
        while fast and fast.next:
            con = slow
            slow = slow.next
            fast = fast.next.next
            count += 1
        
        # reverse from middle to end
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        if con:
            con.next = prev
        else:
            head = prev

        # initialize second pointer n/2 ahead of first
        p1 = p2 = head
        for _ in range(count):
            p2 = p2.next
        
        # find max sum
        for _ in range(count):
            print(p1.val)
            curr = p1.val + p2.val
            ans = max(ans, curr)
            p1, p2 = p1.next, p2.next
                
        return ans