class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if n==0 or head==None:
            return None
        
        head1 = ListNode(0)
        head1.next = head
        head  = head1
        
        p = head
        q = head
        
        for i in xrange(0,n+1):
            if q!=None:
                q=q.next
            else:
                return None
        
        while q:
            p=p.next
            q=q.next
        
        p.next = p.next.next
        
        return head.next
