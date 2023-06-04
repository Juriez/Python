class user:
    name = ''
    email = ''
    password = ''
    login = False
    def login(self):
        password = input("Enter your password ") #procedure to input something
        email = input('Enter your mail address ')
        name = input("Enter your username ")
        if(password == self.password and email == self.email):
            print("Successfully loged in ")
            login = True

        else:
            print("Login Failed! ")
            login=False
    def logout(self):
        login = False
        print("You are logged out ")
    def isLogin(self):
        if(self.login):
            return True
        else:
            return False
    def profile(self):
        if self.isLogin():
            print(self.name,"\n",self.email)
        else:
            print("User is Loggedout")
user1 = user()
user1.name = 'Mahir'
user1.email= 'bsse1316@iit.du.ac.bd'
user1.password='12345'
user1.login()
user1.profile()