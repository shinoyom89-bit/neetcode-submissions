class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        pk = None

        # Check first k nodes
        check = curr
        for _ in range(k-1):
            if check is None:
                return head
            check = check.next

        while curr and check:
            prev = None
            first = curr

            # Reverse k nodes
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # First group
            if dummy.next is None:
                dummy.next = prev
            else:
                pk.next = prev

            # first is now the tail of this reversed group
            pk = first

            # Check next k nodes
            check = curr
            for _ in range(k-1):
                if check is None:
                    break
                check = check.next

        # Remaining nodes are less than k
        pk.next = curr

        return dummy.next