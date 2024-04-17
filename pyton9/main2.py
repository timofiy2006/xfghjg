def count_all_values(dictionary):
    count = 0
    if isinstance(dictionary, dict):
        for key in dictionary.keys():
            count += count_all_values(dictionary[key])
    else:
        count += 1
    return count

# Приклад виклику функції:
my_dict = {
    'key1': 'value1',
    'key2': {
        'key3': 'value3',
        'key4': 'value4'
    }
}
print(count_all_values(my_dict))
