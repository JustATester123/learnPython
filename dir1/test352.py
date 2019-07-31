class myClass(object):

    def sayHello(self,name):
        return("hello,"+name)

mc = myClass()
print(mc.sayHello('wangjiong'))


class A:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a +self.b

c=A('2',5.2)
print(c.add())

class B(A):
    def sub(self):
        return self.a-self.b
d=B(5,1)

print(d.add())
print(d.sub())

