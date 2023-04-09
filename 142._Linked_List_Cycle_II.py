# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
###
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return None
        #####
        # Initialize the slow and fast pointers
        slow = head
        fast = head
        
        # Move the slow pointer one step at a time and the fast pointer two steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If the pointers meet at a node in the cycle, break out of the loop
            if slow == fast:
                break
        
        # If the fast pointer reached the end of the linked list, there is no cycle
        if not fast or not fast.next:
            return None
        
        # Reset the slow pointer to the head of the linked list
        slow = head
        
        # Move both pointers one step at a time until they meet again
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        # Return the node where the cycle begins
        return slow
