# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        second_half=slow.next
        slow.next=None
        prev=None
        while second_half:
            temp=second_half.next
            second_half.next=prev
            prev=second_half
            second_half=temp
        l1,l2=head,prev
        while l2:
            l1next,l2next=l1.next,l2.next
            l1.next,l2.next=l2,l1next
            l1=l1next
            l2=l2next





