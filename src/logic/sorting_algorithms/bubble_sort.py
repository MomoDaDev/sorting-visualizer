from ..helper import Helper as h

def bubble_sort(p):
    if p == True:
        print('Bubble Sort: ', '\n')
    """
    Bubble sort algorithm
    """
    for i in range(0, len(h.arr_num)):
        for j in range(0, len(h.arr_num) - 1):
            # Switch numbers if the number with the lower index is bigger
            if h.arr_num[j] > h.arr_num[j + 1]:
                # Switch numbers
                x = h.arr_num[j]
                h.arr_num[j] = h.arr_num[j + 1]
                h.arr_num[j + 1] = x