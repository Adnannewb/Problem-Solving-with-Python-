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
    #brute force approach to reverse linked list
    def reverse_linked_list(self):
        temp=self.head
        stack=[]
        while temp is not None:
            stack.append(temp.value)
            temp=temp.next
        temp=self.head
        while temp is not None:
            e=stack.pop()
            temp.value=e
            temp=temp.next
        return self.head
    #optimized approach to reverse linked list
    def reverse_linked_list_optimized(self):
        temp=self.head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        self.head=prev
        return self.head 
sl1=SinglyLinkedlist()
sl1.append(10)
sl1.append(34)
sl1.append(143)
sl1.append(56)
sl1.append(78)
print("Linked list before reversing:")
temp=sl1.head
while temp is not None:
    print(temp.value, end=" ")
    temp=temp.next
print("None")

# sl1.reverse_linked_list()
sl1.reverse_linked_list_optimized()

print("Linked list after reversing:")
temp=sl1.head
while temp is not None:
    print(temp.value, end=" ")
    temp=temp.next
print("None")