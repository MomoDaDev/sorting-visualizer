from logic.helper import Helper
from ui.ui import *

def initialize_app():
    initialize_helper()
    initialize_ui()

def initialize_helper():
    Helper()
    Helper.initialize_arr_num()
    Helper.initialize_dic_algorithms()
    Helper.initialize_algo_list()

def initialize_ui():
    setup_ui()