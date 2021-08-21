
""" Binary Search Algorithm 
----------------------------------------

"""

def binary_search(a_List, item):
    
    first = 0
    last = len(a_List) - 1 
    while first <= last:
        i = (first + last) / 2

        if a_List[i] == item:
            return 'found at position'.format(item=item , i=i)
        elif a_List[i] > item:
            last = i - 1 
        elif a_List[i] < item:
            first = i + 1
        else:
            return 'not found in the first ' .format(item=item)


a_List = [4,5,9,3,6]
item = 4
binary_search(a_List, item)
