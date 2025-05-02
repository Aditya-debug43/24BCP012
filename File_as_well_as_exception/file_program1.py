import csv
data = [['Roll No', 'Name', 'Marks1', 'Marks2', 'Marks3']]
data.append([1, 'John', 78, 88, 90])
data.append([2, 'Alice', 80, 85, 82])
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)