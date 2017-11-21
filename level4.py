# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:

    def split(self, A):
        slow = A
        fast = A.next
        while fast:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next
        last_half = slow.next
        slow.next = None
        return last_half

    def reverse(self, l):
        current = l
        prev = None
        next = None
        while(current is not None):
            next = current.next
            current.next = prev
            prev=current
            current = next
        return prev

    def print(self, l):
        i = 0
        while (l is not None):
            i+=1
            if (l.next is None):
                print(str(l.val)+' at '+str(i))
            else:
                print(str(l.val)+' at '+str(i)+' -> ', end='')
            l = l.next

    def concat(self, l_a, l_b):
        #concats linked list in order of a then b
        a = l_a
        while (a.next is not None):
            a = a.next
        a.next = l_b
        return l_a
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        a = None
        total_count = 0
        if A is None:
            return A
        if A.next is None:
            return A

        #print('A:', end='')
        #self.print(A)
        head = A
        tail = self.split(A)
        #print('split half:')
        #self.print(tail)
        #print('A after split:')
        #self.print(A)

        rev_tail = self.reverse(tail)
        #print('reversed tail:')
        #self.print(rev_tail)
        #print('how about tail:')
        #self.print(tail)
        current = rev_tail
        while(current is not None):
            #print('head.val:' + str(head.val) + ' current.val:'+ str(current.val))
            head.val = current.val - head.val
            head = head.next
            current = current.next
        tail = self.reverse(rev_tail)
        result = self.concat(A, tail)

        return result
