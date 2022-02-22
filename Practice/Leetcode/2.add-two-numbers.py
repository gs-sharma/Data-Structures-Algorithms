#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode()
        head = result
        while l1 or l2 :
            if l1 is None:
                data = l2.val + carry
                result.next = ListNode(data % 10)
                result = result.next
                carry = data // 10
                l2 = l2.next
            elif l2 is None:
                data = l1.val + carry
                result.next = ListNode(data % 10)
                result = result.next
                carry = data // 10
                l1 = l1.next
            else:
                data = l1.val + l2.val + carry
                result.next = ListNode(data % 10)
                result = result.next
                carry = data // 10
                l1 = l1.next
                l2 = l2.next

        if carry != 0:
            result.next = ListNode(carry)
        
        return head.next

            
# @lc code=end

