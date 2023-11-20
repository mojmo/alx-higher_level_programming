#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists."""

    result_list = []
    for i in range(0, list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_result = 0
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            result_list.append(div_result)
    return (result_list)
