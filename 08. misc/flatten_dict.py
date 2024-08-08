'''Write a function flatten_dict that converts a nested dictionary into a flat dictionary with keys as tuples representing the path to the value.'''

nested_dict = {
    'a': {
        'b': {
            'c': 1
        }
    },
    'd': 2
}


def flatten_dict(d, current_path=()):
    items = []
    for k, v in d.items():
        new_key = current_path + (k,)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key).items())
        else:
            items.append((new_key, v))
    return dict(items)


print(flatten_dict(nested_dict))
