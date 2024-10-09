class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass

class Factory:
    def get_person(self, p_type):
        if p_type =='w':
            return Worker()
        elif p_type =='s':
            return Student()
factory = Factory()
factory.get_person("w")
factory.get_person("s")