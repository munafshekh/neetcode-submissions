# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        if head is None:
            return None

        if head.next == None:
            return head

        curr_node = head
        previous_node = None

        while curr_node:
            temp_node = curr_node.next
            curr_node.next = previous_node
            previous_node = curr_node
            curr_node = temp_node

        head = previous_node

        return head
