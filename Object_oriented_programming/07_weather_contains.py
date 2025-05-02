class Weather:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return item in self.data

w = Weather(["rain", "sunny", "cloudy"])
print("rain" in w)
print("snow" in w)