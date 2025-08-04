#position, name, age, level, salary
se1 = ["Software Engineer", "Ravi", 25, "Senior", 10000]
se2 = ["Software Engineer", "Shailu", 24, "Junior", 8000]


#class
class SoftwareEngineer:

    #class attribute
    alias = "Keyboard Magician"
    
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code...")

    def code_language(self, language):
        print(f"{self.name} is writing code in {language}")

    #dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}"
        return information
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25 :
            return 5000
        elif age < 30:
            return 7000
        else:
            return 9000
        

#instance
se1 = SoftwareEngineer("Ravi", 25, "Senior", 10000)
se2 = SoftwareEngineer("Shailu", 24, "Junior", 8000)
se3 = SoftwareEngineer("Shailu", 24, "Junior", 8000)

# output
# print(se1.name, se1.level, se1.salary, se1.alias)
# print(se2.name, se2.level, se2.salary, se2.alias)

# se1.code()
# se1.code_language("Python")

# print(se1)
# print(se2)

# print(se2 == se3)

print(se1.entry_salary(23))
print(SoftwareEngineer.entry_salary(27))

