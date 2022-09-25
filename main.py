from models import Toyota
while True:
    print(
        '1. Add new car\n'
        '2. Quit\n'
    )
    flag = input("Chose menu item\n")

    if flag == '1':
        name_car = input("Name of car ")
        engine = input("What is engine ")
        color = input("What car`s color? ")
        new_car = Toyota(name_car, engine, color)
        while True:
            flag_option = input('What you want do with car?\n'
                                '1. Gear option\n'
                                '2. Move option\n'
                                '3. Color option\n'
                                '4. Quit\n')
            if flag_option == '1':
                gear_counter = input("+ shift or - shift\n")
                new_car.shift_gear(gear_counter)
            elif flag_option == '2':
                chose = input("Do you want move, y or n\n")
                new_car.drive(chose)
            elif flag_option == '3':
                color = input("input color\n")
                new_car.change_colour(color)
            elif flag_option == '4' or 'q':
                break
    if flag == '2':
        break
        