import pandas as pd
import random

f_names = ["Billy", "Bob", "Lily", "Ben", "Bea", "Sam", "Max", "Lisa", "Dave", "Will", "Joe", "Tilly", "Ada", "Ian", "Zoe", "Luke", "Kai", "Eli", "Hugh", "Jess", "John"]
l_names = ["Cole", "Brown", "Smith", "Jones", "Doe", "Davis", "Miller", "Black", "Ford", "Reid", "Ross", "Pine", "Hill", "Lee", "Diaz", "Cruz", "Moore"]
years = ["Freshman", "Sophmore", "Junior", "Senior", "Vic lap"]
pathways = ["CS", "Criminal Justice", "Biomed", "Culinary", "Marketing", "Business", "Engineering", "Early College", "Early Childhood Education"]
names = []

for i in range(20000):
    names.append(f"{random.choice(f_names)} {random.choice(l_names)}")
    
data = {
    "Name": names,
    "Age": [random.randint(14,19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.5),2) for _ in names],
    "Credits Completed": [random.randint(0,60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathways": [random.choice(pathways) for _ in names]
}

pennData = pd.DataFrame(data)
print(pennData)

pennData.to_csv("pennData.csv", index=False)