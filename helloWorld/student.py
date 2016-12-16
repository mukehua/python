class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_age(self):
        print("%s:%s" % (self.name, self.age))

mukehua = Student("mukehua", 26)
mukehua.print_age()
