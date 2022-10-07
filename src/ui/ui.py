from facade.sorting_facade import *
from logic.helper import Helper

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

def setup_ui():

    dpg.create_context()

    with dpg.window(tag='Primary Window'):
        # Set Label
        dpg.add_text('Sorting Visualizer by Moritz Troestl')

        # Reset Button
        dpg.add_button(label='Reset', callback=reset_callback)

        # Shuffle Button
        dpg.add_button(label='Shuffle', callback=shuffle_callback)

        # Sort Button
        dpg.add_button(label='Sort', callback=sort_callback)

        # Sorting Algorithm Combo
        dpg.add_combo(items=Helper.algo_list, label="Sorting Algorithms", 
        height_mode=dpg.mvComboHeight_Small, tag=COMBO_NAME, 
        default_value=COMBO_DEFAULT_VALUE)

        # Plot to visualize numbers
        dpg.add_simple_plot(label='Numbers', default_value=Helper.arr_num, width=400, height=200, histogram=True, tag=SIMPLE_PLOT_NAME)


    dpg.create_viewport(title=VIEWPORT_NAME, width=800, height=700)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window('Primary Window', True)
    dpg.start_dearpygui()
    dpg.destroy_context()