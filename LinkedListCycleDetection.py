#create a class for ListNode
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



#Brute force Solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head              # Current node we're examining
        node_set = set()         # Set to store visited nodes
        
        while temp is not None:
            if temp in node_set: # Check if we've seen this node before
                return True      # Found a cycle!
            node_set.add(temp)   # Remember this node for future
            temp = temp.next     # Move to the next node
        
        return False            # Reached end, no cycle found

#Optimal Solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head          # Slow pointer (tortoise) - moves 1 step
        fast = head          # Fast pointer (hare) - moves 2 steps

        while fast is not None and fast.next is not None:
            slow = slow.next      # Move slow pointer 1 step
            fast = fast.next.next # Move fast pointer 2 steps
            
            if slow == fast:      # Pointers met - cycle detected!
                return True

        return False             # Fast reached end - no cycle