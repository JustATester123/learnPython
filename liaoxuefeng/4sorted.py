
l = [1,-3,5,30,50,-7]
print(sorted(l))
print(sorted(l,key=abs))


s = ['hanxue','andi','Bobo','Tom']
print(sorted(s))
print(sorted(s,key=str.lower))
print(sorted(s,key=str.lower,reverse=True))


def by_name(L):
   return L[0]

def by_score(l):
    return l[1]

l =[('b',2),('a',1),('c',3)]


print(sorted(l,key=by_name))
print(sorted(l,key=by_score,reverse=True))

