class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myFunc(self):
        print(f"Hello my name is {self.name}")
        
p1=Person("john", 35)
p1.myFunc()
p1.age=40
print(p1.age)




