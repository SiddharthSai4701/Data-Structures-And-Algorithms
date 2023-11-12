# Binary Search using iterative method

# l = list(map(int, input().split()))
# low = 0
# high = len(l)-1

# x = 4
# it = 1

# while high!=low:
    
#     mid = int((low+high)/2)
#     print(f"Iteration {it}")
#     print(f"x is: {x}")
#     print(f"mid is: {l[mid]}")
#     if x == l[mid]:
#         print( "Value found!")
#         break
        
#     elif x>l[mid]:
#         low = mid+1
        
#     else:
#         high = mid-1
        
#     it+=1
        
# Binary Search using recursive method

def BinarySearch(lst,search_value,low,high):
    if high>=low:
        mid = int((low+high)/2)
        if lst[mid] == search_value:
            return 1
        
        elif lst[mid]>search_value:
            return BinarySearch(lst, search_value, low, mid-1)
        
        else:
            return BinarySearch(lst, search_value, mid+1, high)
        
    else:
        return -1
    
l = list(map(int, input().split()))
x = 4

r = BinarySearch(l,4,0,l[-1])
print(r)