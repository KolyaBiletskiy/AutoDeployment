
import random

mylist = [x**2 for x in range(10)]

print(mylist)

a = ['aa', 'bb', 'ab']

#return strings that starts from "a"

b = [w for w in a if w[0] == "a"]

print(b)

temps = [221,230,245,255]


lc = [item/10 for item in temps if item != 255]

print(lc)



c = ['1','1','3']
a = list(map(int, c))

print(a)

