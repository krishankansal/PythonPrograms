class MyClass:
    
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    
    @staticmethod
    def staticmethod():
        return 'static method called'

# print(MyClass().method())
# print(MyClass.classmethod())
# print(MyClass.staticmethod())
# print(MyClass().classmethod())
# print(MyClass().staticmethod())
print(MyClass().__class__)
print(MyClass().__class__.classmethod())