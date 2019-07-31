dicts = {'username':'wangjiong','password':12345}

print(dicts)

print(dicts.keys())

print(dicts.values())

dicts['age'] =28
for k,v in dicts.items():
    print('dicts key is: %r' %k)
    print("dicts value is: %r " %v)

dicts.pop('username')
print(dicts.items())

dicts["age"]=30
print(dicts)

