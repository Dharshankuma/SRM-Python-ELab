# Binita was travelling from Chennai to Delhi in Rajdhani Express. 
# The train have arrived at the destination later than the estimated time. So, Binita wants to know the total number of hours and minutes 
# the train was delayed. Can you help Binita in finding the exact hour and time Rajdhani Express was delay on the day of Binita's journey?

def calculate_delay(totMin):
    hours = totMin / 60
    minutes = totMin % 60
    return hours,minutes

totMin = int(input())
hours,minutes = calculate_delay(totMin)
print(f"{int(hours)} Hours and {minutes} Minutes")