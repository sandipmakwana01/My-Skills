class a:
    a = 10

    def fun1(self):
        self.b=10
        print(self.b+self.a)

obj=a()

print(obj.a)

obj.fun1()