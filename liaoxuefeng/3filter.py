

def not_empty(s):
    return s and str.strip(s)

print(list(filter(not_empty,['a','',' b b ','cccc ','   '])))



def is_odd(n):
    return  n % 2 ==1

print(list(filter(is_odd,[0,1,2,3,4,5,6,7,9])))



str = "123abcrunoob321"
s2 = '123abcrunoob312'
print (str.strip( '12' ))  # 字符序列为 12
print (s2.strip( '12' ))