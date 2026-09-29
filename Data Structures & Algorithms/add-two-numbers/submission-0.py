class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        carry = 0
        list1 = l1
        list2 = l2
        while list1 or list2:
            l1_val = list1.val if list1 else 0
            l2_val = list2.val if list2 else 0
            total = l1_val + l2_val + carry
            add_val = total % 10
            carry = total // 10
            new_node = ListNode(add_val)
            if head is None:
                head = new_node
            else:
                curr = head
                while curr.next:
                    curr = curr.next
                curr.next = new_node
            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next
        if carry:
            new_node = ListNode(carry)
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        return head