

class User:
    def __init__(self, fname, lname, username, password):
        self.fname = fname
        self.lname = lname
        self._username = username
        self.__password = password
        self.name = "{} {}".format(fname, lname)
    
    def login(self):
        username = input("\nUsername:\n>>>")
        password = input("\nPassword:\n>>>")
        if (username == self._username and password == self.__password):
            print("Welcome back, {}".format(self.name))


if __name__ == "__main__":
    user1 = User("Angel", "Padilla","AjustinPadilla","12213")
    user1.login()