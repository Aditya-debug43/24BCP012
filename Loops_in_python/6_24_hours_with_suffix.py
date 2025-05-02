for i in range(24):
    if i == 0:
        print("12 AM - Midnight")
    elif i < 12:
        print(i, "AM")
    elif i == 12:
        print("12 PM - Noon")
    else:
        print(i-12, "PM")