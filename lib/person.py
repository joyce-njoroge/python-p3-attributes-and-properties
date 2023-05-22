#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
class Person:
    def __init__(self, name="Guido", job="Sales"):
       self.name = name
       self.job = job

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value == "":
            print("Name must be string between 1 and 25 characters.")
        
        elif len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.__name = value.title()

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self.__job = value

def main():
    guido = Person()
    guido.name = "Guido"
    guido.job = "Sales"
    print(guido.name)

main()    

#class Person:
    #def __init__(self, name="Guido", job=None):
        #self.job = job
        #if not isinstance(name, str) or name == "":
            #print("Name must be string between 1 and 25 characters.")
        
        #elif len(name) > 25:
            #print("Name must be string between 1 and 25 characters.")
        #else:
            #self.name = name.title()

        #if job not in APPROVED_JOBS:
            #print("Job must be in list of approved jobs.")
        #else:
            #self.job = job    
        
#guido = Person(name="Guido", job="Sales")           





            
