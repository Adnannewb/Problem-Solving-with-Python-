class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SinglyLinkedlist:
    def __init__(self):
        self.head=None
    #append in singly linked list 
    def append(self,value):
        new_node=Node(value)
        if(self.head==None):
            self.head=new_node
        else:
            current=self.head
            while(current.next is not None):
                current=current.next
            current.next=new_node
    #brute force approach to find middle of linked list
    def middle_of_linked_list(self):
        n=0
        temp=self.head
        while temp is not None:
            n+=1
            temp=temp.next
        temp=self.head
        for i in range(n//2):
            temp=temp.next
        return temp.value
    #optimized approach to find middle of linked list
    def middle_of_linked_list_optimized(self):
        slow_ptr=self.head
        fast_ptr=self.head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
        return slow_ptr.value

sl1=SinglyLinkedlist()
sl1.append(10)
sl1.append(34)
sl1.append(143)
sl1.append(56)
sl1.append(78)
print("Brute force approach:", sl1.middle_of_linked_list())
print("Optimized approach:", sl1.middle_of_linked_list_optimized())