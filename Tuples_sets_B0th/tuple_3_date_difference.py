from datetime import date
d1 = (2022, 5, 10)
d2 = (2022, 5, 25)
dt1 = date(*d1)
dt2 = date(*d2)
print((dt2 - dt1).days)