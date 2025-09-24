import pandas as pd
import random

f_names = ["Billy", "Bob", "Lily", "Ben", "Bea", "Sam", "Max", "Lisa", "Dave", "Will", "Joe", "Tilly", "Ada", "Ian", "Zoe", "Luke", "Kai", "Eli", "Hugh", "Jess", "John"]
l_names = ["Cole", "Brown", "Smith", "Jones", "Doe", "Davis", "Miller", "Black", "Ford", "Reid", "Ross", "Pine", "Hill", "Lee", "Diaz", "Cruz", "Moore"]
years = []
pathways = []
names = []

for i in range(20000):
    names.append(f"{random.choice(f_names)} {random.choice(l_names)}")
    
print(names)