class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a += 1
        # print(x)
        # print(self.a)
        return x
p1 = MyNumbers()
myiter = iter(p1)
mynext=next(p1)
            print(x)



        

    