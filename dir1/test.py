name=['abc','qwe','rty']

def normalize(name):
    def zhuanhuan(s):
        return str.upper(s[0]) + str.lower(s[1:])
    return list(map(zhuanhuan,name))

print(normalize(name))

from functools import reduce
DIGITS ={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2float(s):
    def char2num(c):
        return DIGITS[c]

    l = s.split(sep='.')
    x = len(l[1])

    def fn(x,y):
        return x*10+y
    def fm(x):
        if x == 0:
            return 1
        if x >0:
            return 10 * fm(x-1)
    return reduce(fn,map(char2num,l[0]))+reduce(fn,map(char2num,l[1]))/fm(len(l[1]))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')





