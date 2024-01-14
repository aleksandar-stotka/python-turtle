FONT = ("Courier", 24, "normal")

night_coding = 33

def day_curse(day):
    if day > 0:
      return f"i need {day} day of coding and {night_coding} nights  "
    else:
        return f"not valid" 
    
   

  
user_inputDays = input("hey user hoe many day you need\n") 

new_value = int(user_inputDays)


day_curse(new_value)

calculate_value = day_curse(new_value)
print(calculate_value)





class Scoreboard:
    pass
