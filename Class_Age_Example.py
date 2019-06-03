class Person:
    def __init__(self, initial_age):
        self.initial_age = initial_age
        if self.initial_age < 0:
            print("Age is not valid, setting age to 0.")
            self.initial_age = 0

    def am_i_old(self):
        if self.initial_age < 13:
            print("You are young.")
        elif 13 < self.initial_age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def year_passes(self):
        self.initial_age += 1
