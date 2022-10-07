from ..helper import Helper
from facade.sorting_facade import update_simple_plot

import time

def switch_numbers(index_a, index_b):
    Helper.arr_num[index_a], Helper.arr_num[index_b] = Helper.arr_num[index_b], Helper.arr_num[index_a]

def play_change(delay):
    time.sleep(delay)
    update_simple_plot()