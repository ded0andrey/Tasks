def find_in_nested_dict(nested_dict, keys):
    values = []
    if isinstance(nested_dict, dict):
        for key, value in nested_dict.items():
            if key in keys:
                values.append(value)
            if isinstance(value, dict):
                nested_values = find_in_nested_dict(value, keys)
                if nested_values:
                    values.extend(nested_values)
    return values

nested_dict = {'1': {'DEBUG': 'Tracemod'}, '2': {'PARAMS': 'Null pointer exception'},
           '4': {'DEBUG': 'sendAllert'}, '5': {'ERROR': 'No valid JSON'}}

keys = ['DEBUG', 'ERROR']

print(find_in_nested_dict(nested_dict, keys))