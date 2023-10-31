# -*- coding: utf-8 -*-
"""
Filename: 

About the program:

Created on Sat Jul  8 19:24:49 2023

@author: Siddharth Vijay Sai


Question 1

ALice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a
sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.

Technique: Binary Search

Problem:
    
    We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.

Inputs:
    1) cards - a list of numbers sorted in decreasing order
    2) query - a number, whose position in the array is to be determined
    
Output:
    position - The position of query in the list, cards. 
"""

def locate_card(cards, query):
    pass

# Test case -  always come up with test cases. Makes the job easier
cards = [13, 11, 10, 7, 4, 3, 1, 0]

# The number to be found
query = 7

# The index at which the element is found
output = 3

# Call the function and store the result
result = locate_card(cards, query)

# Compare the result with the query
result == query


"""
We will represent the test cases as dictionaries to make it easier to test them once we implement our function

Every test case will be represented as a dictionary containing two key - input and output
The input will again be a dictionary containing keys for each parameter of the function -  so here, cards and query
"""
test = {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query' : 7
            },
        'output' : 3 
        }

# Testing the function using the dictionary
locate_card(test['input']['cards'], test['input']['query']) == test['output']

# An alternate way of testing would be as follows

locate_card(**test['input']) == test['output']

# When we write ** and then pass a dictionary as an argument, python takes the keys of the given dictionary and uses the values of its keys as arguments in the function


"""
Our function should be able to handle any set of valid inputs we pass into it.
The possible scenarios that could occur are:
    
    1) The number, query, occurs in the middle of the list, cards.
    2) query is the first element
    3) query is the last element
    4) cards contains just one element that is query
    5) cards does not contain query
    6) cards is empty
    7) cards contains repeating numbers
    8) query occurs at more than one position/index in cards
    
    Edge Cases: Cases like empty list or query not occuring are called edge cases as they represent rare or extreme examples 
"""

# Create a list of test dictionaries

tests = []
tests.append(test)

# query occurs somewhere in the middle
tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query' : 1
            },
        'output' : 6 
    })


# query is the first element
tests.append({
        'input': {
            'cards': [4, 2, 1, -1],
            'query' : 4
            },
        'output' : 0
    })


# query is the last element
tests.append({
        'input': {
            'cards': [3, -1, -9, -127],
            'query' : -127
            },
        'output' : 3
    })

# cards contains just one element, query

tests.append({
    'input': {
        'cards': [6],
        'query': 6
        },
    'output': 0
    })

"""
The problem does not state what to do if cards does not contain query.

In an interview:
    1) Read the problem statement again, carefully.
    2) Look through the examples provided with the problem.
    3) Ask the interviewer/platform for clarification.
    4) Make a rasonable assumption, state it and move forward.
    
We will assume the function returns -1 incase cards does not contain query
"""

# cards does not contain 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
        },
    'output': -1
    })

# cards is empty

tests.append({
    'input': {
        'cards': [],
        'query': 7
        },
    'output': -1
    })

"""
# numbers can repeat in cards

In such a case we expect our function to return the index of the first occurence of query

While it may be acceptable for the function to return any position where query occurs, it would be slightly more difficult to test the function as the op is non deterministic
"""

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
        },
    'output': 2
    })

# print(tests)

"""
Easiest solution - brute force

Turn the cards over one by one until you find query.
If query isn't found, return -1
"""
# Brute Force Solution 1 -  throws error if list is empty

# def locate_card(cards, query):
    
#     position= 0
    
#     while True:
        
#         if cards[position] == query:
#             return position
            
        
#         position+=1
        
#         if position == len(cards):
#             return -1
        
# ans = locate_card(**test['input'])
# print(ans)


# Brute Force Solution 2 - my own

# def locate_card(cards, query):
    
#     for index, element in enumerate(cards):
        
#         if element == query:
#             return index
        
#     return -1

# Brute Force Solution 3

def locate_card(cards, query):
    position = 0
    while position<len(cards):
        if cards[position] == query:
            return position
        
        position+=1
    return -1
# # print(locate_card(**test['input']) == test['output'])

for index, dictionary in enumerate(tests):
    
    print(f"Test case {index+1}")
    print(locate_card(**dictionary['input']) == dictionary['output'])
    
    
# Always keep the brute force solution handy and implement it if you cannot figure out the optimal solution

