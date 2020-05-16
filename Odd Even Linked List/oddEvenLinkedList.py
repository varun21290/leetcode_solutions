# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (head is None or head.next is None): return head
        node=head
        temp1=node.next
        temp2=node.next
        node.next=temp2.next
        if(node.next is not None):
            node=node.next
            temp1.next=node.next
            while(node.next is not None):
                temp2=node.next
                node.next=temp2.next
                if(node.next is None): break
                node=node.next
                temp2.next=node.next

        node.next=temp1
        temp2.next=None
        return head
        
