#21. Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:       
    def mergeTwoLists(self, list1: Optional[ListNode] ,list2: Optional[ListNode]) -> Optional[ListNode]:
         # Create a dummy node and a current node pointer
        dummy = ListNode()
        #####
        current = dummy

        # Iterate through both lists until either list is empty
        while list1 and list2:
            # Compare the current values of list1 and list2
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move the current pointer to the next node
            current = current.next

        # If either list still has elements, append it to the end of the merged list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next