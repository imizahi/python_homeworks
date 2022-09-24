class Toyota:
    gear = 0
    drive_position = 'stop'

    def __init__(self, name, engine, color):
        self.engine = engine
        self.color = color
        self.name = name
        print(f"Your car is {self.name}, {self.color}, {self.engine}")

    def drive(self, chose):
        if chose == 'y' and self.drive_position == 'stop':
            self.drive_position = "move"
            print("You moving")
            self.gear = 1

        elif chose == 'n' and self.drive_position == 'move':
            self.drive_position = "stop"
            print("You stopped")

        elif chose == 'n' and self.drive_position == 'stop':
            print("You already stopped\n")

        elif chose == 'y' and self.drive_position == 'move':
            print("You already moving\n")

    def shift_gear(self,gear_counter):
        if gear_counter == '+' or gear_counter == 'up':
            self.gear += 1
            if self.gear >= 7:
                self.gear = 6
                print("Gear can`t be more than 6\n")
            else:
                print(f"Your gear is {self.gear}")
        if gear_counter == '-' or gear_counter == 'down':
            self.gear -= 1
            if self.gear < -1:
                self.gear -= 1
                print("Gear can`t be less than reverse")
            else:
                print(f"Your gear is {self.gear}")

    def change_colour(self, color):
        self.color = color
        print(f"Your color is {self.color}\n")