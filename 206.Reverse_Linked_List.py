Class ListNode:
    def __init__(self, val = 0, next = None):
        val = self.val
        next = self.next
Class Solution:
    def reverseList(self , head: Optional[ListNode] ) -> Optional[ListNode] :
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def reverseList (self , head : Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
   