

    def removeDuplicates(self,head):
        c = head
        while True:
            try:
                if c.data == c.next.data:
                   c.next =  c.next.next
                else:  c  =  c.next
            except AttributeError: # final None has no data
                return head

