# This file contains all the callback methods for the UI
from logic.helper import Helper

import dearpygui.dearpygui as dpg
import random as r
import importlib

SIMPLE_PLOT_NAME = 'number_plot'
COMBO_NAME = 'sorting_algorithm_combo'
COMBO_DEFAULT_VALUE = 'Bubble Sort'
SORT_DELAY = 0.001
VIEWPORT_NAME = 'Sorting Visualizer'

def reset_callback(sender):
    Helper.initialize_arr_num()
    update_simple_plot()

def shuffle_callback(sender):
    r.shuffle(Helper.arr_num)
    update_simple_plot()

def sort_callback(sender):
    key = dpg.get_value(COMBO_NAME)
    module = importlib.import_module('logic.sorting_algorithms.' + Helper.dic_algorithms[key])
    func = getattr(module, Helper.dic_algorithms[key])
    func()

def update_simple_plot():
    dpg.set_value(SIMPLE_PLOT_NAME, Helper.arr_num)
