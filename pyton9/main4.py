def count_occurrences(dictionary, target_value):
    count = 0
    if isinstance(dictionary, dict):
        for value in dictionary.values():
            count += count_occurrences(value, target_value)
    elif dictionary == target_value:
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
print(count_occurrences(my_dict, 'value3'))
