class MyType(type):
    def __init__(self,*args,**kwargs):
        print('xx')
        super(MyType,self).__init__(*args,**kwargs)

    def __call__(cls, *args, **kwargs):
        print('__call__')
        obj = cls.__new__(cls,*args, **kwargs)
        cls.__init__(obj,*args, **kwargs)
        print(cls)
        return obj

def with_metaclass(base):
    return MyType("MyType2",(base,),{})

# 方式一
class Foo(metaclass=MyType): # metaclass=MyType,即指定了由MyType创建Foo类，当程序运行，用到class Foo时，即调用MyType的__init__方法，创建Foo类
    def __init__(self,name):
        self.name = name


#方式二    在Flask的wtform的源码中用到过
# class Foo(with_metaclass(object)):
#     def __init__(self,name):
#         self.name = name

print(Foo.__call__)
a=Foo('name')