{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class calc:\n",
    "    def sub(a, b):\n",
    "         return a - b\n",
    "    def mul(a, b):\n",
    "        return a * b\n",
    "    def div(a, b):\n",
    "        return a  / b\n",
    "    def add(a, b):\n",
    "        return a + b   \n",
    "\n",
    "z = calc()\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myfun(a, b):\n",
    "    print(f\"{a},  {b}\")\n",
    "\n",
    "myfun(\"Hello\", \"Mukesh\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class myclass:\n",
    "    def add(a, b):\n",
    "        print(\"Addition:\")\n",
    "        return a + b\n",
    "\n",
    "x = 10\n",
    "y = 20\n",
    "myclass.add(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class myclass:\n",
    "    def __init__(self, x, y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "    def myfun_add(self):\n",
    "        return self.x + self.y\n",
    "\n",
    "obj = myclass(10, 20)\n",
    "obj.myfun_add()\n",
    "#print(obj.a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Employee:\n",
    "    def emp_details():\n",
    "        fname = 'Mukesh'\n",
    "        lname = 'Patil'\n",
    "        email = 'mukesh.patil@gmail.com'\n",
    "        pay = 1000\n",
    "        print(\"email address: {}.{}@gmail.com\".format(fname, lname))\n",
    "\n",
    "Employee.emp_details()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#1# Simple function\n",
    "def emp_detail():\n",
    "    fname = 'Mukesh'\n",
    "    lname = 'Patil'\n",
    "    print(\"email address: {}.{}@gmail.com\".format(fname, lname))\n",
    "\n",
    "emp_detail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2# Simple function with return\n",
    "def emp_detail():\n",
    "    fname = 'Mukesh'\n",
    "    lname = 'Patil'\n",
    "    return (\"email address: {}.{}@gmail.com\".format(fname, lname))\n",
    "\n",
    "emp_detail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#3# Simple function - parametr accepts\n",
    "def emp_detail(f_name, l_name):\n",
    "    return (\"email address: {}.{}@gmail.com\".format(f_name, l_name))\n",
    "\n",
    "fname = 'Mukesh'\n",
    "lname = 'Patil'\n",
    "emp_detail(fname, lname)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#4# Simple class\n",
    "class Employee:\n",
    "    def emp_detail():\n",
    "        fname = 'Mukesh'\n",
    "        lname = 'Patil'\n",
    "        return (\"email address: {}.{}@gmail.com\".format(fname, lname))\n",
    "\n",
    "Employee.emp_detail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#3# Simple class - accept parameter\n",
    "class Employee:\n",
    "    def emp_detail(f_name, l_name):\n",
    "          return (\"email address: {}.{}@gmail.com\".format(f_name, l_name))\n",
    "\n",
    "fname = 'Mukesh'\n",
    "lname = 'Patil'\n",
    "Employee.emp_detail(fname, lname)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#3# Simple OOPS - used construtor/initializer or instance of class\n",
    "\n",
    "class Employee:\n",
    "   \n",
    "    def __init__(self, fname, lname, pay):\n",
    "        self.fname = fname\n",
    "        self.lname = lname\n",
    "        self.pay = pay\n",
    "        \n",
    "    def email(self):\n",
    "        return (f\"email address: {self.fname}.{self.lname}@gmail.com\") \n",
    "    \n",
    "    def fullname(self):\n",
    "        return (f\"Full Name: {self.fname} {self.lname}\")\n",
    "\n",
    "emp_1 = Employee('Mukesh', 'Patil', 5000)\n",
    "emp_2 = Employee('Rupa', 'Patil', 15000)\n",
    "\n",
    "print(emp_1.fullname())\n",
    "print(emp_1.email())\n",
    "print(\"Pay:\", emp_1.pay)\n",
    "\n",
    "print(emp_2.fullname())\n",
    "print(emp_2.email())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#4# OOPS - used construtor/initializer or instance of class\n",
    "\n",
    "class Employee:\n",
    "    pay_raise = 4.50\n",
    "    \n",
    "    def __init__(self, fname, lname, pay):\n",
    "        self.fname = fname\n",
    "        self.lname = lname\n",
    "        self.pay = pay\n",
    "        \n",
    "    def email(self):\n",
    "        return (f\"email address: {self.fname}.{self.lname}@gmail.com\") \n",
    "    \n",
    "    def fullname(self):\n",
    "         return (\"Full Name: {} {} and Pay: {}\".format(self.fname, self.lname, self.pay_raise))\n",
    "         return (\"Pay: \", self.pay_raise)\n",
    "\n",
    "emp_1 = Employee('Mukesh', 'Patil', 5000)\n",
    "emp_2 = Employee('Rupa', 'Patil', 15000)\n",
    "\n",
    "emp_1.pay_raise = 10\n",
    "print(\"Avg. Raise :\", Employee.pay_raise)\n",
    "print(emp_2.fullname())\n",
    "print(emp_1.pay_raise)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#5#classmethods and staticmethods\n",
    "class Employee:\n",
    "    pay_raise = 4.50\n",
    "    \n",
    "    def __init__(self, fname, lname, pay):\n",
    "        self.fname = fname\n",
    "        self.lname = lname\n",
    "        self.pay = pay\n",
    "        \n",
    "    @classmethod\n",
    "    def set_raise_amt(cls, amount):\n",
    "        cls.raise_amt = amount \n",
    "        return amount\n",
    "    \n",
    "    @staticmethod\n",
    "    def is_workday(day):\n",
    "        if day.weekday() == 5 or day.weekday() == 6:\n",
    "            return False\n",
    "        return True\n",
    "\n",
    "import datetime\n",
    "my_date = datetime.date(2016, 7, 10)\n",
    "print(Employee.is_workday(my_date))\n",
    "\n",
    "    \n",
    "emp_1 = Employee('Mukesh', 'Patil', 5000)\n",
    "emp_2 = Employee('Rupa', 'Patil', 15000)\n",
    "\n",
    "print(Employee.set_raise_amt(1.05)) # class method - class variable = 1.05\n",
    "emp_1.pay_raise = 10\n",
    "print(\"Avg. Raise :\", Employee.pay_raise)\n",
    "print(emp_1.raise_amt)\n",
    "print(emp_2.raise_amt)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#6# Inheritance - Creating Subclasses\n",
    "class Employee:\n",
    "    raise_pay = 1.05\n",
    "    def __init__(self, fname, lname, pay):\n",
    "        self.fname = fname\n",
    "        self.lname = lname\n",
    "        self.pay = pay\n",
    "    \n",
    "    def emp_raise(self):\n",
    "        return int(self.pay * self.raise_pay) \n",
    "    \n",
    "    def __add__(self, other):\n",
    "        return self.pay + other.pay \n",
    "\n",
    "class Developer(Employee):\n",
    "        raise_pay = 1.20\n",
    "        def __init__(self, first, last, pay, prog_lang):\n",
    "            super().__init__(first, last, pay) #Pass the variable to Employee class and no need to have separate \n",
    "            self.prog_lang = prog_lang     #initialize method for Developer class\n",
    "\n",
    "emp1 = Employee('Mukesh', 'Patil', 50000)\n",
    "emp2 = Employee('Rahul', 'Agarwal', 60000)\n",
    "print(emp1 + emp2) #Operator overloading ref Employee method __add__(self, other)\n",
    "\n",
    "print(emp1.emp_raise())\n",
    "\n",
    "dev1 = Developer('Rupali', 'Patil', 50000, 'Python')\n",
    "print(dev1.prog_lang, dev1.emp_raise())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python Program to perform addition of two complex numbers using binary + operator overloading. \n",
    "\n",
    "class complex: \n",
    "    def __init__(self, a, b): \n",
    "        self.a = a \n",
    "        self.b = b \n",
    "\n",
    "# adding two objects \n",
    "    def __add__(self, other): \n",
    "        return self.a + other.a, self.b + other.b \n",
    "\n",
    "    def __str__(self): \n",
    "        return self.a, self.b \n",
    "\n",
    "Ob1 = complex(1, 2) \n",
    "Ob2 = complex(2, 3) \n",
    "Ob3 = Ob1 + Ob2 \n",
    "print(Ob3) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Python program to overload a comparison operators \n",
    "\n",
    "class A: \n",
    "\tdef __init__(self, a): \n",
    "\t\tself.a = a \n",
    "\tdef __gt__(self, othe): \n",
    "\t\tif(self.a>othe.a): \n",
    "\t\t\treturn True\n",
    "\t\telse: \n",
    "\t\t\treturn False\n",
    "ob1 = A(2) \n",
    "ob2 = A(3) \n",
    "if(ob1>ob2): \n",
    "\tprint(\"ob1 is greater than ob2\") \n",
    "else: \n",
    "\tprint(\"ob2 is greater than ob1\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rupali\n",
      "Mukesh.Patil@gmail.com\n",
      "Rupali Patil\n"
     ]
    }
   ],
   "source": [
    "#Why do we need gatter and setter in Python, the below example first name chaged but didnt changed the email address\n",
    "class Employee:\n",
    "    def __init__(self, first, last):\n",
    "        self.first = first\n",
    "        self.last = last \n",
    "        self.email = \"{}.{}@gmail.com\".format(self.first, self.last)\n",
    "\n",
    "    def fullname(self):\n",
    "        return '{} {}'.format(self.first, self.last)\n",
    "\n",
    "emp_1 = Employee('Mukesh', 'Patil')\n",
    "emp_1.first = 'Rupali'\n",
    "\n",
    "print(emp_1.first)\n",
    "print(emp_1.email) \n",
    "print(emp_1.fullname())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rupali\n",
      "Rupali.Patil@gmail.com\n",
      "Rupali Patil\n"
     ]
    }
   ],
   "source": [
    "#Property Decorators - Getters, Setters, and Deleters\n",
    "#Why do we need gatter and setter in Python, the below example first name chaged but didnt changed the email address\n",
    "class Employee:\n",
    "    def __init__(self, first, last):\n",
    "        self.first = first\n",
    "        self.last = last \n",
    "    \n",
    "    @property   #Property decorator setter\n",
    "    def email(self):\n",
    "        return \"{}.{}@gmail.com\".format(self.first, self.last)\n",
    "\n",
    "    def fullname(self):\n",
    "        return '{} {}'.format(self.first, self.last)\n",
    "\n",
    "emp_1 = Employee('Mukesh', 'Patil')\n",
    "emp_1.first = 'Rupali'\n",
    "emp_2 = Employee('Ragav', 'Jain')\n",
    "\n",
    "print(emp_1.first)\n",
    "print(emp_1.email) # This is an attribute printing and not calling it as function to avoid impact to all users by recode above ex\n",
    "print(emp_1.fullname())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ashok\n",
      "Ashok.Deshmukh@gmail.com\n",
      "Ashok Deshmukh\n"
     ]
    }
   ],
   "source": [
    "#Property Decorators - Getters, Setters, and Deleters\n",
    "#Why do we need gatter and setter in Python, the below example first name chaged but didnt changed the email address\n",
    "class Employee:\n",
    "    def __init__(self, first, last):\n",
    "        self.first = first\n",
    "        self.last = last \n",
    "    \n",
    "    @property   #Property decorator setter\n",
    "    def email(self):\n",
    "        return \"{}.{}@gmail.com\".format(self.first, self.last)\n",
    "    @property\n",
    "    def fullname(self):\n",
    "        return '{} {}'.format(self.first, self.last)\n",
    "    \n",
    "    @fullname.setter \n",
    "    def fullname(self, name):\n",
    "        first, last = name.split(' ')\n",
    "        self.first = first\n",
    "        self.last = last\n",
    "\n",
    "emp_1 = Employee('Mukesh', 'Patil')\n",
    "emp_1.fullname = 'Ashok Deshmukh'  # Hash this comment and will get different / old output\n",
    "\n",
    "print(emp_1.first)\n",
    "print(emp_1.email) # This is an attribute printing and not calling it as function to avoid impact to all users by recode above ex\n",
    "print(emp_1.fullname)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ashok\n",
      "Ashok.Deshmukh@gmail.com\n",
      "Ashok Deshmukh\n",
      "Delet Name!\n"
     ]
    }
   ],
   "source": [
    "#Property Decorators - Getters, Setters, and Deleters\n",
    "#Why do we need gatter and setter in Python, the below example first name chaged but didnt changed the email address\n",
    "class Employee:\n",
    "    def __init__(self, first, last):\n",
    "        self.first = first\n",
    "        self.last = last \n",
    "    \n",
    "    @property   #Property decorator setter\n",
    "    def email(self):\n",
    "        return \"{}.{}@gmail.com\".format(self.first, self.last)\n",
    "    @property\n",
    "    def fullname(self):\n",
    "        return '{} {}'.format(self.first, self.last)\n",
    "    \n",
    "    @fullname.setter \n",
    "    def fullname(self, name):\n",
    "        first, last = name.split(' ')\n",
    "        self.first = first\n",
    "        self.last = last\n",
    "        \n",
    "    @fullname.deleter\n",
    "    def fullname(self):\n",
    "        print(\"Delet Name!\")\n",
    "        self.first = None\n",
    "        self.last = None\n",
    "\n",
    "emp_1 = Employee('Mukesh', 'Patil')\n",
    "emp_1.fullname = 'Ashok Deshmukh'  # Hash this comment and will get different / old output\n",
    "\n",
    "print(emp_1.first)\n",
    "print(emp_1.email) # This is an attribute printing and not calling it as function to avoid impact to all users by recode above ex\n",
    "print(emp_1.fullname)\n",
    "\n",
    "del emp_1.fullname"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Getting value\n",
      "Peter\n",
      "Setting value to Diesel\n",
      "Getting value\n",
      "Diesel\n",
      "Deleting value\n"
     ]
    }
   ],
   "source": [
    "# Python program to explain property() \n",
    "# function using decorator \n",
    "\n",
    "class Alphabet: \n",
    "\tdef __init__(self, value): \n",
    "\t\tself._value = value \n",
    "\t\t\n",
    "\t# getting the values\t \n",
    "\t@property\n",
    "\tdef value(self): \n",
    "\t\tprint('Getting value') \n",
    "\t\treturn self._value \n",
    "\t\t\n",
    "\t# setting the values\t \n",
    "\t@value.setter \n",
    "\tdef value(self, value): \n",
    "\t\tprint('Setting value to ' + value) \n",
    "\t\tself._value = value \n",
    "\t\t\n",
    "\t# deleting the values \n",
    "\t@value.deleter \n",
    "\tdef value(self): \n",
    "\t\tprint('Deleting value') \n",
    "\t\tdel self._value \n",
    "\n",
    "\n",
    "# passing the value \n",
    "x = Alphabet('Peter') \n",
    "print(x.value) \n",
    "\n",
    "x.value = 'Diesel'\n",
    "print(x.value) \n",
    "\n",
    "del x.value \n",
    "# print(x.value)  --> output - AttributeError: 'Alphabet' object has no attribute '_value'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
