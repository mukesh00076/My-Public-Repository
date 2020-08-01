class employee:
    test = "TEST"
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = "f{fname}.{lname} + @email.com"
        
    def fullname(self):
        return self.fname + " " + self.lname