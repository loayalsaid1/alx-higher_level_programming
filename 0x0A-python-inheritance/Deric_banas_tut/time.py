class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        return f"{self.hour}:{self.minute:02d}:{self.second:02d}"

    def __add__(self, other_time):
        if not isinstance(other_time, Time):
            raise TypeError("Not an Time object")
        
        new_time = Time()
        seconds = other_time.second + self.second
        if seconds >= 60:
            new_time.minute += 1
        new_time.second = seconds % 60

        minutes = other_time.minute + self.minute
        if minutes >= 60:
            new_time.hour += 1
        new_time.minute += minutes % 60

        new_time.hour += (other_time.hour + self.hour ) % 24

        return new_time

time1 = Time(9, 32, 50)
print(time1)

time2 = Time(1, 30e, 50)
print(time2)

print(time1 + time2)
