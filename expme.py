class Val(object):
    __slots__ = ['value']
    def __init__(self, value = 0):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value
v = Val(1)
print(v)
assert v.eval() == 1

class Add(object):
    __slots__=['left','right']
    def __init__ (self,a,b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() + self.right.eval()


e = Add(Val(1),Val(2))
print(e.eval())
assert e.eval() == 3

e =Add(Val(1),Add(Val(2),Val(3)))
print(e.eval())

class Sub(object):
    __slots__=['left','right']
    def __init__ (self,a,b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() - self.right.eval()
e = Sub(Val(1),Val(2))
print(e.eval())
assert e.eval() ==-1
e= Sub(Val(1),Sub(Val(2),Val(3)))
print(e.eval())


class Mul(object):
    __slots__=['left','right']
    def __init__ (self,a,b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() * self.right.eval()
e = Mul(Val(1),Val(2))
print(e.eval())
assert e.eval() == 2





