import re

class Person(object):

    first_name = None
    last_name = None
    full_name = None

    def __init__(self,**kwargs):
        arguments_keys = kwargs.keys()
        if len(arguments_keys) == 2:
            self.join_name(kwargs)
        elif len(arguments_keys) == 1:
            self.break_name(kwargs)

    def break_name(self,kwargs):
        fullname = list(kwargs.values())[0]
        if re.search(r"\s",fullname):
            self.first_name = fullname[0]
            self.last_name = fullname[1]
            self.full_name = list(kwargs.values())[0]


    def join_name(self,kwargs):
        name = list(kwargs.values())
        self.first_name = name[0]
        self.last_name = name[1]
        self.full_name = name[0]+" "+name[1]

    def print_names(self):
        print("fname = ",self.first_name,"lname = ",self.last_name,"fullname = ",self.full_name)

        

b = Person(name="kaushil Rambhia")
b.print_names()


a = Person(first_name="kaushil",last_name="Rambhia")
a.print_names()