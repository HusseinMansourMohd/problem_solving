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
    def create_linked_list(arr):
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    def print_linked_list(head):
        current = head
        while current is not None:
            print(current.val, end="->"
        
   