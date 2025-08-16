from abc import ABC,abstractmethod

class Parent(ABC):
    def meth1(self):
        print("Parent method 1")

    @abstractmethod
    def meth2(self):
        pass

class Child(Parent):
    def meth3(self):
        print('Child method 3')

    def meth2(self):
        print('Child implementation 2')
        
c = Child()
c.meth2()