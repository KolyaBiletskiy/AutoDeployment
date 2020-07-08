
test_dict = {}

testlist = [1, 2, 3, 4, -5, 100, 0, 1, 11, -300]

def min_max(array):
    min = None
    max = None
    for i in array:
        if min is None:
            min = i
        elif i < min:
            min = i
        if max is None:
            max = i
        elif i > max:
            max = i
    return test_dict.update({'min_value': min, 'max_value': max})
    # return test_dict_new = {'min_value': min_value, 'max_value': max_value}

min_max(testlist)

print(test_dict.items())
print(test_dict.keys())
print(test_dict.values())

