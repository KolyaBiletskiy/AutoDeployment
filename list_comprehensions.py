

mylist = [x**2 for x in range(10)]

print(mylist)


oo = 3
def test():
    if oo != 5:
        print('11111finally')
    if oo != 3:
        print("2222211111finally")
    if oo != 4:
        print('3333311111finally')
    else:
        print('44444411111finally')


test()
