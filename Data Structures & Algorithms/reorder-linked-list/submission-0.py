# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        m = {}
        virtual = ListNode()
        virtual.next = head
        cursor = head
        nid = 0

        while cursor:
            m[nid] = cursor
            cursor = cursor.next
            nid += 1
        
        numNodes = nid

        def outputSeq(n):
            i = 0
            j = n - 1

            while True:
                yield i
                i += 1

                if i > j:
                    break

                yield j
                j -= 1

                if i > j:
                    break
        
        cursor = head
        for nid in outputSeq(numNodes):
            if nid == 0:
                continue

            cursor.next = m[nid]
            cursor = cursor.next
        cursor.next = None
        return         

