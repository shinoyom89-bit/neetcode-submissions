# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        snap=[]
        for nodes in lists:
            curr=nodes
            while curr:
                snap.append(curr.val)
                curr=curr.next
        snap.sort()
        merge=ListNode()
        dummy=merge
        for n in snap:
            dummy.next=ListNode(n)
            dummy=dummy.next
        return merge.next