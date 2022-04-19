# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode0(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB and headB not in s:
            headB = headB.next
        return headB

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        def lens(node):
            res = 0
            while node:
                res, node = res+1, node.next
            return res
        lenA, lenB = lens(headA), lens(headB)
        if lenA < lenB:
            headA, headB, lenA, lenB = headB, headA, lenB, lenA
        for _ in range(lenA - lenB):
            headA = headA.next
        while headA and headA != headB:
            headA, headB = headA.next, headB.next
        return headA

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
