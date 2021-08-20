# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =  ListNode()
        cur =  dummy 
        while l1 and l2 : 
            if(l1.val <= l2.val) :
                cur.next =  ListNode(l1.val)
                l1 =  l1.next
            else :
                cur.next = ListNode(l2.val)
                l2 = l2.next 
            cur = cur.next
        while l1 :
            cur.next =  ListNode(l1.val)
            l1 =  l1.next
            cur = cur.next
        while l2 : 
            cur.next  =  ListNode(l2.val)
            l2 = l2.next 
            cur = cur.next
        return dummy.next
