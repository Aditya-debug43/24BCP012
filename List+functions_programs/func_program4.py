def sum_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg
print(sum_avg([70, 80, 90, 85, 75]))