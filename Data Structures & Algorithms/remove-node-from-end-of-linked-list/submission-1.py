# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev,curr=None,head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        dummy=ListNode()
        dummy.next=prev
        i=1
        del_curr=dummy
        while i<n:
            del_curr=del_curr.next
            i+=1
        del_curr.next=del_curr.next.next
        prev,curr=None,dummy.next
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev