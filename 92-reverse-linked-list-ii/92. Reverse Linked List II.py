# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:
            return None

        curr, prev = head, None
        while left > 1:
            prev = curr
            curr = curr.next
            left, right = left - 1, right - 1
        
        tail, con = curr, prev

        while right:
            third = curr.next
            curr.next = prev
            prev = curr 
            curr = third
            right -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr

        return head

        # curr = head
        # dummy = ListNode(0)
        # dummy.next = head
        # before_range = after_range = prev = None
        # right_node = left_node = None
        # count = 0

        # if left == right:
        #     return head

        # while curr:
        #     count += 1
        #     print('count', count)

        #     if count == left - 1:
        #         before_range = curr

        #     if count == right + 1:
        #         after_range = curr
                
        #         break

        #     if count >= left and count <= right:

        #         print(curr.val)

        #         if count == left:
        #             left_node = curr

        #         if count == right:
        #             right_node = curr
                    
        #         next_node = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = next_node
        #         continue
            
        #     curr = curr.next

        
        # left_node.next = after_range

        # if left == 1:
        #     dummy.next = right_node
        # else:
        #     before_range.next = right_node
        

        # return dummy.next
