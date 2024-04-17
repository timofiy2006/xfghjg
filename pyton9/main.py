def print_all_keys(dictionary):
    if isinstance(dictionary, dict):
        for key in dictionary.keys():
            print(key)
            print_all_keys(dictionary[key])

# Приклад виклику функції:
my_dict = {
    'key1': 'value1',
    'key2': {
        'key3': 'value3',
        'key4': 'value4'
    }
}
print_all_keys(my_dict)
