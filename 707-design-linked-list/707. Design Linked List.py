class ListNode:
    def __init__(self, val):
        self.val = val
        self.next, self.prev = None, None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        # use sentinel nodes as psuedo-head and psuedo-tail
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.size += 1

        new_node = ListNode(val)
        first = self.head.next
        self.head.next, new_node.prev = new_node, self.head
        new_node.next, first.prev = first, new_node

    def addAtTail(self, val: int) -> None:
        self.size += 1

        new_node = ListNode(val)
        last = self.tail.prev
        self.tail.prev, new_node.next = new_node, self.tail
        new_node.prev, last.next = last, new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        if index < 0:
            index = 0

        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        self.size += 1
        to_add = ListNode(val)
        pred.next, to_add.prev = to_add, pred
        succ.prev, to_add.next = to_add, succ
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev

        self.size -= 1
        pred.next, succ.prev = succ, pred

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)