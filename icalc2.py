import pegpy
peg = pegpy.grammar('''
Expression = Product (^{ '+' Product #Add })*
Product = Value (^{ '*' Value #Mul })*
Value = { [0-9]+ #Int }
''')
parser = pegpy.generate(peg)

class Expr(object):
    @classmethod
    def new(cls, v):
        if isinstance(v, Expr):
            return v 
        return Val(v)


class Val(Expr):
    __slot__ = ['value']

    def__init__(self, value):
         self.value = value
            
    def__repr__(self):
        return f'Val({self.value})'

    def eval(self, env:dict):
        return self.value 

e = Val(0)
assert e.eval({}) == 0
    
class Binary(Expr):
    __slot__ = ['left','right']
        
    def__init__(self, left, right):
        self.left = Expr.new(left)
        self.right = Expr.new(right)
            
    def__repr__(self):
        classname = self.__class__.__name__
        returnf'{classname}({self.left},{self.right})'


class Add(Binary):
     __slot__ = ['left','right']
            
    def eval(self, env:dict):
        return self.left.eval(env) + self.right.eval(env)