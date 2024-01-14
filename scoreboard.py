FONT = ("Courier", 24, "normal")

night_of_coding = 33
user_input = input("how many")
def day_of_units(day):
    return f"i need {day} day of coding and {night_of_coding} night of coding"

def validate_user_input():
    try:
        user_number = int(user_input)
        if user_number > 0:
            calculate_value = day_of_units(user_number)
            print(calculate_value)
        elif user_number == 0:
            print("Please enter a positive number.")
    except ValueError:
        print("Your input is not a valid number.")
        


validate_user_input()











class Scoreboard:
    pass
