def outer(x,y):
    return lambda y,x: x + y


my = outer(6567567, 989)

print(my(10,5))


"""

lambda arguments : expression

The power of lambda is better shown when you use them as an anonymous function inside another function.


"""

x = lambda a, b: a + 100 + a + b
print(x(5,2))


with open("/Users/nick/Downloads/photo.txt") as f:
    for lines in enumerate(f):
        print(lines)
    # content = f.readlines()

# for lines in content:
#     print(en)


