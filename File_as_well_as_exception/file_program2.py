import csv
d = {}
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        roll = row[0]
        name = row[1]
        marks = list(map(int, row[2:]))
        total = sum(marks)
        d[roll] = [name, marks, total]
print(d)