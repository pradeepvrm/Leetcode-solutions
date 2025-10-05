# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        node = None

        while mid:
            temp = mid.next
            mid.next = node
            node = mid
            mid = temp

        first = head
        second = node
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2

        


        