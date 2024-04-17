def print_values_for_key(dictionary, target_key):
    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            if key == target_key:
                print(value)
            else:
                print_values_for_key(value, target_key)

# Приклад виклику функції:
my_dict = {
    'key1': 'value1',
    'key2': {
        'key3': 'value3',
        'key4': 'value4'
    }
}
print_values_for_key(my_dict, 'key2')
