def SimpleFunction():
    a=10
    b= 100
    c = 100/10
    print('Welcome to function')
    print("The divider of those numbers is :" + str(c))

print("This line is out of function") # as it is not in the functions block, so it is out of the function
SimpleFunction() # function must be called

def sum(var1, var2):
    sum = var1+var2
    print("Sum of those variable")
    print(sum)

sum(12,45.23)
sum("Our country name is ", "Bangladesh")

def wishCard(name, wish = "TaqabbalAllahu Minna wa Minkum "): # default parameter
    print(wish,name)

wishCard("Mahir") # it will use default parameter
wishCard("Faisal", "Eid Mubarok") # default parameter can be changed passing another value