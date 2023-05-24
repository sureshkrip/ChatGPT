import json

def count_children(json_object):
    if isinstance(json_object, dict):
        return {key: count_children(value) for key, value in json_object.items()}
    elif isinstance(json_object, list):
        return len(json_object)
    else:
        return 0  # Base case: if not dict or list, it has no children

def sum_values(nested_dict):
    if isinstance(nested_dict, dict):
        return {key: sum_values(value) for key, value in nested_dict.items()}
    else:
        return nested_dict

def traverse(data):
    counts = count_children(data)
    sums = sum_values(counts)
    return sums

# replace with your JSON string
json_string = '{"a": {"b": {"c": 1, "d": 2}, "e": [1, 2, 3]}, "f": {"g": 1}}'
data = json.loads(json_string)
print(traverse(data))
