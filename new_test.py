import random
from OOP import Polymorphism




print('Hash for 181 is:', hash(181))


yes_no = ['they will send you the offer', 'they will not send you the offer']

print(random.choice(yes_no))



levi_maxi = ['you will work at levi9', 'you will work at maxitech']

print(random.choice(levi_maxi))


for item in enumerate(range(24)):
    print(item)

a = 'http://google.com'

if '//' in a:
    print(a.split('//')[1].split('.')[0])
else:
    print(a.split('.')[1].split('.')[0])

def domain_name(url):
    if '//' in url:
        return url.split('/')[1].split('.')[0]
    else:
        return url.split('.')[1].split('.')[0]

print(domain_name('http://google.com'))


