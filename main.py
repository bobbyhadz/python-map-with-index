# Get access to the Index in the map() function in Python

my_list = ['Bobby', 'Hadz', 'Com']


def example_func(idx_and_item):
    index, item = idx_and_item

    return item + str(index)


result = list(map(example_func, enumerate(my_list)))

print(result)  # 👉️ ['Bobby0', 'Hadz1', 'Com2']