class ConstructorTest:
    def __init__(self):
        print("I am a constructor")
    def fun1(self):
        print("I am a function")
    def fun2(self):
        print("I am another function")

ob = ConstructorTest()
ob.fun1() #it will also execute the constractor & print the corresponding output
ob.fun2()