from logic.helper import Helper
from logic.sorting_algorithms import *

def initialize_app():
    initialize_helper()
    initialize_ui()

def initialize_helper():
    Helper()
    Helper.initialize_arr_num()
    Helper.initialize_dic_algorithms()

    test_all_algorithms()

def initialize_ui():
    pass

def test_all_algorithms():
    Helper.STANDARD_NUMBER_LENGTH = 40

    import random as r
    import importlib

    for key in Helper.dic_algorithms:
        module = importlib.import_module('logic.sorting_algorithms.' + Helper.dic_algorithms[key])
        func = getattr(module, Helper.dic_algorithms[key])
        r.shuffle(Helper.arr_num)
        print(Helper.arr_num)
        func(True)
        print(Helper.arr_num)