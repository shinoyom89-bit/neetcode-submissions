class Solution:
    def mergeTwoLists(self, list1, list2):
        l1 = list1
        l2 = list2
        dummy=ListNode()
        head=dummy
        while l1 and l2:
            if l1.val<=l2.val:
                dummy.next=l1
                dummy=dummy.next
                l1=l1.next
            else:
                dummy.next=l2
                dummy=dummy.next
                l2=l2.next
        if l1 :
            dummy.next=l1
        else:
            dummy.next=l2
        return head.next