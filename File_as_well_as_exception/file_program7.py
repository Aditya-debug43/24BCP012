import pickle
class Employee:
    def __init__(self, code, name, doj, salary):
        self.code = code
        self.name = name
        self.doj = doj
        self.salary = salary
e = Employee(1, "John", "2022-01-01", 50000)
with open("emp.dat", "wb") as f:
    pickle.dump(e, f)
with open("emp.dat", "rb") as f:
    obj = pickle.load(f)
    print(obj.code, obj.name, obj.doj, obj.salary)