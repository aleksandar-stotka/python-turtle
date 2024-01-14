FONT = ("Courier", 24, "normal")

night_of_coding = 33

def day_of_units(day):
    if day > 0:
     return f"i need {day} day of coding and {night_of_coding} night of coding"
    else:
        return "not valid number"

user_input = input("how many day of coding and night you need\n")

user_number = int(user_input)




calculated_value = day_of_units(user_number)

print(calculated_value)






class Scoreboard:
    pass
