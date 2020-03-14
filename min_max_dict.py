
test_dict = {}

testlist = [1, 2, 3, 4, -5, 100, 0, 1, 11, -300]

def min_max(testlist):
    min_value = None
    max_value = None
    for i in testlist:
        if min_value is None:
            min_value = i
        for i in testlist:
            if i < min_value:
                min_value = i
        if max_value is None:
            max_value = i
        for i in testlist:
            if i > max_value:
                max_value = i
    return test_dict.update({'min_value': min_value, 'max_value': max_value})

min_max(testlist)

print(test_dict.items())
print(test_dict.keys())
print(test_dict.values())


