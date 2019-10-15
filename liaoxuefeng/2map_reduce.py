from functools import reduce

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2float(s):
    s1 = str.split(s,sep='.')
    l = len(s1[1])

    def fn(x,y):
        return 10*x+y

    def fm(x):
        if x ==0:
            return 1
        if x > 0:
            return 10*fm(x-1)

    def str2num(s):
        return DIGITS[s]

    return reduce(fn,map(str2num,s1[0]))+reduce(fn,map(str2num,s1[1])) / fm(len(s1[1]))

print('str2float(\'123.456\')=',str2float('123.456'))

if abs(str2float('123.456')-123.456) <0.00001:
    print('测试成功')
else:
    print('测试失败')