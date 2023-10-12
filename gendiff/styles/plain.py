def check_value(value):
    if value in ['false', 'true', 'null'] or type(value) is int:
        return value
    elif type(value) is dict:
        return '[complex value]'
    return f"'{value}'"


def create_description_diff(path, data):
    if 'in file1' in data and len(data) == 2:
        return f"Property '{path}' was removed\n"
    elif 'diff types values' in data:
        return (f"Property '{path}' was updated. "
                f"From {check_value(data[0])} to {check_value(data[1])}\n")
    elif 'in 2 files' in data:
        return '\n'
    elif 'diff values' in data:
        return get_string(data[0], path)
    else:
        return (f"Property '{path}' was "
                f"added with value: {check_value(data[0])}\n")


def get_string(data, path_value=''):
    if type(data) is not dict:
        description = create_description_diff(path_value, data)
        return description
    final_string = ''
    for key, value in data.items():
        result = str(get_string(value, path_value + '.' + key))
        final_string += f'{result}'
    return final_string


def get_plain_style(diff_files_data):
    final_string = ''
    for key, value in diff_files_data.items():
        result = f'{get_string(value, key)}\n'
        if result != '':
            final_string += result
    show_result = ''
    for row_of_differences in final_string.split('\n'):
        if row_of_differences != '':
            show_result += f'{row_of_differences}\n'
    return show_result[:-1]
