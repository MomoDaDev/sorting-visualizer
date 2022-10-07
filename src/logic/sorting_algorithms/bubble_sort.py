from logic.interfaces.sorting_algorithm_base import play_change, switch_numbers
from ..helper import Helper as h
from facade.sorting_facade import SORT_DELAY

def bubble_sort():
    """
    Bubble sort algorithm
    """
    for i in range(0, len(h.arr_num)):
        for j in range(0, len(h.arr_num) - 1):
            # Switch numbers if the number with the lower index is bigger
            if h.arr_num[j] > h.arr_num[j + 1]:
                # Switch numbers
                switch_numbers(j, j + 1)
                play_change(SORT_DELAY)