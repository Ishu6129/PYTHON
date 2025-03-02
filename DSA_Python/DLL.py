class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if self.start is None:
            self.start = n
        else:
            self.start = n
            self.start.next.prev = self.start.next

    def insert_at_last(self, data):
        n = Node(None, data)
        if self.start is None:
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
            temp.next.prev = temp.next

    def search_item(self, data):
        temp = self.start
        while temp:
            if temp.item == data:
                return temp
            temp = temp.next

    def insert_after(self, value, data):
        temp = self.start
        while temp:
            if temp.item == value:
                n = Node(None, data, temp.next)
                temp.next = n
                temp.next.prev = temp.next
            temp = temp.next

    def delete_start(self):
        if self.start is not None:
            self.start.next.prev = None
            self.start = self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp is not None:
                if temp.next.next is None:
                    temp.next = None
                temp = temp.next

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.item == data and self.start.next is None:
            self.start=None
        else:
            temp=self.start
            if self.start.item==data:
                self.start=self.start.next
                self.start.prev=None
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

    def print_item(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
        print()
    def __iter__(self):
        return DLLIterator(self.start)
class DLLIterator:
    def __init__(self,data):
        self.current=data
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is not None:
            data=self.current.item
            self.current=self.current.next
            return data
        else:
            raise StopIteration


mylist = DLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.delete_item(20)
mylist.print_item()
for i in mylist:
    print(i)