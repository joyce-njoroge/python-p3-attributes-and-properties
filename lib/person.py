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
    def __init__(self, name="Guido", job=None):
        self.job = job
        if not isinstance(name, str) or name == "":
            print("Name must be string between 1 and 25 characters.")
        
        elif len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name.title()

        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self.job = job    
        
guido = Person(name="Guido", job="Sales")           
            
