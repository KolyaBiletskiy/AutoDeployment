import time
# fact =3  then 1*2*3
f = 1
fact = 3

for i in range(1, fact+1):
    f = i * f

print(f)


a = [1,2,3]
b = [10,20,30]
ab = []
for i in a:
    num = i
    for i in b:
        ls = num*i
        ab.append(ls)
print(ab)





print(list(map(lambda x: x ** 2, a)))

print([x**2 for x in a])





start = time.time()
array = [1,2,3,4,5,6,-0,-6,-100]
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
print(min, max)
# 40 iterations
print(time.time() - start)


# for i in array:
#     if min is None:
#         min = i
#
#         for i in array:
#             if i < min:
#                 min = i
#     else:
#         break
#
# for i in array:
#     if max is None:
#         max = i
#
#         for i in array:
#             if i > max:
#                 max = i
#     else:
#         break
# 51 iteration
