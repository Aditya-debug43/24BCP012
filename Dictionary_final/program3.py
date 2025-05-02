data = {
    'HR': [(101, 50000), (102, 60000)],
    'IT': [(201, 70000), (202, 55000)],
    'Finance': [(301, 45000), (302, 47000)]
}
for dept in data:
    salaries = [salary for _, salary in data[dept]]
    print(dept, "Min:", min(salaries), "Max:", max(salaries))