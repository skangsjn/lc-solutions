# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        power = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            power += 1
        if fast:
            power = power*2
        else:
            power = (power*2) - 1
        
        curr = head
        ans = 0
        while power >= 0:
            print(curr, power)
            if curr.val == 1:
                ans += (2 ** power)
            curr = curr.next
            power -= 1
        
        return ans