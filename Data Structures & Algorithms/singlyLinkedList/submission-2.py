class LinkedList:
    
    def __init__(self):
        self.virtual_head=Node()
        self.tail:Node=None
        self.length:int=0

    def get(self, index: int) -> int:
        if index>=self.length:
            return -1
        
        cursor = self.virtual_head.next
        current_index=0
        while current_index < index:
            cursor=cursor.next
            current_index +=1
        
        return cursor.value

    def insertHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.virtual_head.next
        self.virtual_head.next=new_node
        if self.length == 0:
            self.tail=new_node

        self.length+=1
        return

    def insertTail(self, val: int) -> None:
        new_node=Node(val)
        if self.length == 0:
            self.tail=new_node
            self.virtual_head.next=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return        

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        
        cursor = self.virtual_head.next
        previous=self.virtual_head
        current_index=0
        while current_index < index:
            previous=cursor
            cursor=cursor.next
            current_index+=1
        
        previous.next=cursor.next
        if current_index == self.length -1:
            self.tail=previous
        self.length-=1
        return True     

    def getValues(self) -> List[int]:
        cursor=self.virtual_head.next
        result=[]
        while cursor is not None:
            result.append(cursor.value)
            cursor=cursor.next
        return result

class Node:
    def __init__(self, value=None):
        self.value=value
        self.next:Node=None
        
