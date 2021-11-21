def binary_search(values, value_to_find):
    left_value = 0
    right_value = len(values) - 1
    while left_value <= right_value:
        middle_value = (left_value + right_value) // 2
        if values[middle_value] == value_to_find:
            return middle_value
        elif value_to_find < values[middle_value]:
            right_value = values[middle_value] - 1
        elif value_to_find > values[middle_value]:
            left_value = values[middle_value] + 1
    return -1
