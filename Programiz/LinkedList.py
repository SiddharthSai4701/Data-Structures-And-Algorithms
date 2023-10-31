# -*- coding: utf-8 -*-
"""
Filename: 

About the program:

Created on Mon Oct 30 14:14:07 2023

@author: Siddharth Vijay Sai
"""
class Node:
    
    def __init__(self, item):
        
        self.item = item
        self.next = None
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        

ll1 = LinkedList()

ll1.head = Node(1)

node2 = Node(2)
node3 = Node(3)

ll1.head.next = node2
node2.next = node3

while ll1.head != None:
    print(ll1.head.item)
    ll1.head = ll1.head.next