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


import json

def count_children(json_object):
    if isinstance(json_object, dict):
        return sum(count_children(v) for v in json_object.values()) + len(json_object)
    elif isinstance(json_object, list):
        return sum(count_children(x) for x in json_object) + len(json_object)
    else:
        return 0  # Base case: if not dict or list, it has no children

# your provided JSON string
json_string = '{ "a": {"b": [{ "c":1, "b": [{"d": 2}], "e": [{"f": 3}] }]}}'
data = json.loads(json_string)

print(count_children(data))



import json

def count_keys(json_object):
    if isinstance(json_object, dict):
        return {k: count_keys(v) for k, v in json_object.items()}
    elif isinstance(json_object, list):
        return sum(count_keys(x) for x in json_object)
    else:
        return 0  # Base case: if not dict or list, it has no children

def sum_counts(nested_dict):
    if isinstance(nested_dict, dict):
        return {key: sum_counts(value) for key, value in nested_dict.items()}
    elif isinstance(nested_dict, int):
        return nested_dict
    else:  # it's a list
        return sum(nested_dict)

json_string = '{ "a": {"b": [{ "c":1, "b": [{"d": 2}], "e": [{"f": 3}] }]}}'
data = json.loads(json_string)

counts = count_keys(data)
sums = sum_counts(counts)

print(sums)

