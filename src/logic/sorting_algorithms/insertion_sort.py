from facade.sorting_facade import SORT_DELAY
from logic.interfaces.sorting_algorithm_base import play_change
from ..helper import Helper as h

def insertion_sort():
    # Traverse through 1 to len(h.arr_num)
    for i in range(1, len(h.arr_num)):
 
        key = h.arr_num[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < h.arr_num[j] :
                h.arr_num[j+1] = h.arr_num[j]
                play_change(SORT_DELAY)
                j -= 1
        h.arr_num[j+1] = key
        play_change(SORT_DELAY)
