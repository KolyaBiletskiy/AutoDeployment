# f = "hello"
#
# print(f[:-1])
#
#
# a = "TESTBOX PDM, TRAILER, 589567 TESTBOX PDM, TRAILER, 589567 "
#
#
#
# if "TRAILE" in a:
#     print("hppray")
# else:
#     print("--------bad")
#
#
# a = ['df']
#
# if not a:
#     print("hello111")
# elif a:
#     print("yes")
#
#
# print("    xyz     d".rstrip())
#
# a = 2
#
# if a == 2:
#     print("sdd")
#
# print("end")
#
#
# aaa = [1,2,3,4,5]
#
# for el in aaa:
#     if el == 2:
#         print("sadsad")
#     print(el)
#
#
# de = ['hello hhh', 'no']
#
#
# if "no" in de:
#     print("DA")
#
#
# f = []
#
# for el in f:
#     if "dd" not in f[0]:
#         print("hello1111111")
#
# values = [' ','sda','asdsa',' ']
#
#
#     # catch the first non-empty value
# str_list = [name for name in values if name.strip()]
#
# print(str_list[0])
# print(type(str_list[0]))
#
#
# print(range(5))
#
# for el in range(5):
#     print(el)
#
#
# a = "hello "
#
# v = a.rstrip()
#
# print(a.count(" "))
# print(v.count(" "))
#
# print(a[-3:])
# print(a)
# print(a.rstrip())
#
# av = ['hello']
# cd = av[-2:]
# print(cd)
#
# elements = ['first', 'second', 'third']
#
# elements_second = ['just']
#
# values = []
#
# index = 0
#
# if elements_second:
#     for el in elements:
#         if index == 0:
#             continue
#         values.append(elements[index])
#         index = index + 1
#
# print(values)
#
#
#
# print("12345678"[:4])

# def square_digits(num):
#     a = str(num)
#     c = ""
#     for i in a:
#         b = str(int(i)**2)
#         c = c + b
#
#     return int(c)

# def get_sum(a,b):
#     if a == b:
#         return a
#     elif a > b:
#         return sum(range(b, a+1))
#     else:
#         return sum(range(a,b+1))
#
# print(get_sum(435, 2))
#
#
# def accum(s):
#     index = 0
#     word = ""
#     for letter in s:
#         index = index + 1
#         letter = letter * index
#         if index == 1:
#             item = "".join(letter.title())
#         else:
#             item = "-" + "".join(letter.title())
#         word = word + item
#
#     return word
#
# print(accum("aaaaz"))
#
# array =[1,1,1,12,11]
#
# def find_uniq(arr):
#     # a,b = set(arr)
#     a = list(set(arr))
#     print(a)
#     b = [i for i in a if arr.count(i) == 1]
#     # for i in a:
#     #     if arr.count(i) == 1:
#     #         b = i
#     # return a if arr.count(a) == 1 else b
#     for i in b:
#         b = f"{i}"
#     return b
#
# print(find_uniq(array))


def removeDuplicates(nums):
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
    return print(arr)


removeDuplicates([1, 2, 3, 3, 3, 3])

test_arr = [1, 1, 1, 1, 2, 3, -1, 100]

min = None
max = None

for i in test_arr:
    if min is None:
        min = i
    elif min < i:
        min = i
    if max is None:
        max = i
    elif max > i:
        max = i
print(min, max)


def outer(x):
    obj_lam = lambda y: x + y
    return obj_lam(x)


print(outer(5))

num = 5
if num // 2 == 2:
    print(num)


def first_non_repeating_letter(string):
    index = 0
    before_format = string
    string = string.lower()
    if string:
        for l in string:
            after_l = string[index + 1:]
            before_l = string[:index]
            if l not in after_l and l not in before_l:
                return before_format[index]
            index = index + 1
        else:
            return ''
    else:
        return ''


print('++++++++++')

print(first_non_repeating_letter('sTreSS'))

q = 'helloh'

print(list(enumerate(q)))


def check_unique(string):
    lower_str = string.lower()
    for i, letter in enumerate(lower_str):
        if q.count(letter) == 1:
            return string[i]
    return ''


print(check_unique('helloh'))



dup = [1,1,1,1,2,3,3,3,3,4]


un = []
for i in dup:
    if i not in un:
        un.append(i)

print(un)
