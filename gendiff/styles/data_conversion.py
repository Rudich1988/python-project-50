from gendiff.diff.diff_names import (IN_2_FILES, IN_FILE1, IN_FILE2,
                                     DIFF_TYPES_VALUES, DIFF_VALUES)


def get_new_key_value(value):
    if isinstance(value[0], dict):
        new_value_1 = value[0]
        new_value_2 = data_conversion(value[1])
    elif isinstance(value[1], dict):
        new_value_1 = data_conversion(value[0])
        new_value_2 = value[1]
    else:
        new_value_1 = data_conversion(value[0])
        new_value_2 = data_conversion(value[1])
    return (new_value_1, new_value_2)


def check_description_data(key, value):
    if IN_FILE1 in value:
        return '- ' + key
    return '+ ' + key


def data_conversion(data):
    if not isinstance(data, dict):
        return str(data)
    final_data = {}
    for key, value in data.items():
        if IN_FILE1 in value or IN_FILE2 in value:
            new_key = check_description_data(key, value)
            final_data[new_key] = value[0]
        elif IN_2_FILES in value or DIFF_VALUES in value:
            final_data[key] = data_conversion(value[0])
        elif DIFF_TYPES_VALUES in value:
            new_value = get_new_key_value(value[:-1])
            final_data['- ' + key] = new_value[0]
            final_data['+ ' + key] = new_value[1]
    return final_data
