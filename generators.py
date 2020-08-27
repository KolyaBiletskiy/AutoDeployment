from OOP import inheritance



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




print('-------------------------')


def my_gen(n):
    for i in range(n):
        yield i**2


gen_object_square = my_gen(5)

for num in gen_object_square:
    print(num)

arra = ['1', 2, 3, 4, 5, 5, 6, 6]

arr_map = map(str, arra)

for i in arr_map:
    print(type(i))


nla = lambda x, y, z: 100 + x + 1 + y + z

print(nla(10, 20, 30))


def outer(x):
    lam = lambda y: x + y
    return lam(5)


print(outer(5))



test_l = ['aa', 'bb', 'ab']

for item in test_l:
    if item[0] == 'a':
        print(item)


print([w for w in test_l if w[0] == 'a'])


class Base:
    def a(self):
        print("Base_a")

class Inherited(Base):
    def a(self):
        # Base.a(self)
        # call base method here
        print("Inherited_a")



obj = Inherited()

# obj.a()
Base.a(obj.a())