



# def create_cubes(n):
#     result = []
#
#     for x in range(n):
#         result.append(x**3)
#
#     return print(result)
#
#
# create_cubes(10)


# convert to generator


def create_cubes(n):

    for x in range(n):
        if (x ** 3)%2 == 0:
            yield x



my_nums = create_cubes(10)

# # print(next(my_nums))
# # print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# print(next(my_nums))
#
for num in my_nums:
    print(num)
#
print(32%2)











