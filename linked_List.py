#Linked List 
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
# node1=Node(5)
# node2=Node(10)
# node3=Node(7)
# node4=Node(8)
# node1.next=node2
# node2.next=node3
# node3.next=node4

# print(node4.next)


#Singly Linked List
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
    #traverse singly linked list
    def traverse(self):
        if not self.head:
            print("Linked List is empty")
        else:
            current=self.head
            while(current is not None):
                print(current.value,end=" ")
                current=current.next

    def insertion(self,value,position):
        new_node=Node(value)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev_node=None
            count=0
            while(current is not None and count<position):
                prev_node=current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.next=current
        
    def delete(self,value):
        temp=self.head
        if temp.next is not None:
            if temp.value==value:
                self.head=temp.next
                return
            else:
                found=False
                prev=None
                while temp is not None:
                    if(temp.value==value):
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                if(found):
                    prev.next=temp.next
                    return
                else:
                    print("Node Not found")

sl1=SinglyLinkedlist()
sl1.append(10)
sl1.append(34)
sl1.append(143)
sl1.insertion(32,1)
sl1.append(1)
print("Before Deletion:")
sl1.traverse()
sl1.delete(1)
print("\nAfter Deletion:")
sl1.traverse()
        
        