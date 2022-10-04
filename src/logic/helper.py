class Helper:
    STANDARD_NUMBER_LENGTH = 0
    arr_num = []
    dic_algorithms = {}

    def __init__(self):
        Helper.STANDARD_NUMBER_LENGTH = 40

    def initialize_arr_num():
        for i in range(1, Helper.STANDARD_NUMBER_LENGTH + 1):
            Helper.arr_num.append(i)

    def initialize_dic_algorithms():
        Helper.dic_algorithms = {
            'Bubble Sort': 'bubble_sort'
        }