# -*- coding: utf-8 -*-
"""
Filename: 

About the program:

Created on Sat Jul  8 13:12:05 2023

@author: Siddharth Vijay Sai
"""

class Node:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    
    def __init__(self):
        self.head = None
        
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def display(self):
        if self.head is None:
            print("Empty")
            
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '----->'
            itr = itr.next
            
        print(llstr)
        
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
        
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
            
        return count
            
        
        
ll = SingleLinkedList()
# ll.insert_at_end(5)
# ll.insert_at_end(89)

# ll.insert_at_end(79)
ll.insert_values([1,2,3,4,5,6,7,8,9,10])
ll.display()
print("Length: ",ll.get_length())