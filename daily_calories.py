from food_variables import *
from datetime_my import delta_days
from colorama import Fore
from datetime import date  # datetime
from functions_food import percent, sum_macronutrients


sunday_time = "13:00-17:20"
monday_time = "11:30-22:30"
tuesday_time = "08:00-11:20 AND 16:30-22:30"
wednesday_time = "08:00-16:20"
thursday_time = "08:00-11:20 AND 16:30-22:30"
friday_time = "08:30-17:00"
# import the variable "delta_days" from datetime_draft

days_no_G = delta_days

daily = pro_coffee_25_no_light, yogurt_10alm_10gcran_10gco, silan_9g, ss



Supplements = 0

# Calculation of all the calories I ate today
# separated into the total number of calories for the amount of protein, carbohydrates and proteins
for food in daily:
    calories += food[0]
    protein_cal += food[1] * 4
    carbs_cal += food[2] * 4
    fat_cal += food[3] * 9
courses_of_pro_left = round((600 - protein_cal) / 80, 1)
if date.today().weekday() == 6:
    day_info = Fore.CYAN + f'Sunday {date.today()} {sunday_time}  | tomorrow: {monday_time}'
elif date.today().weekday() == 0:
    day_info = Fore.CYAN + f'Monday {date.today()}  {monday_time}   | tomorrow: {tuesday_time}'
elif date.today().weekday() == 1:
    day_info = Fore.CYAN + f'Tuesday {date.today()}  {tuesday_time}   | tomorrow: {wednesday_time}'
elif date.today().weekday() == 2:
    day_info = Fore.CYAN + f'wednesday {date.today()}  {wednesday_time}   | tomorrow: {thursday_time}'
elif date.today().weekday() == 3:
    day_info = Fore.CYAN + f'Thursday {date.today()}  {thursday_time}   | tomorrow: {friday_time}'
elif date.today().weekday() == 4:
    day_info = Fore.CYAN + f'Friday {date.today()}  {friday_time}'
else:
    day_info = Fore.BLUE + ("Saturday " + str(date.today())) + f' | tomorrow:\
 {sunday_time}'
print(Fore.YELLOW + f'calories today: {round(calories + Supplements)} | {day_info} | {days_no_G} days G free'.upper())
if 25 <= round(protein_cal * 100 / calories) < 33:
    print(Fore.GREEN + f'{round(protein_cal)} PROTEIN ({round(protein_cal * 100 / calories)}%) [500-650]\
({courses_of_pro_left})')
if round(protein_cal * 100 / calories) >= 33:
    print(Fore.RED + f'{round(protein_cal)} PROTEIN ({round(protein_cal * 100 / calories)}%) [500-650]\
({courses_of_pro_left})')
if round(protein_cal * 100 / calories) < 25:
    print(Fore.RESET + f'{round(protein_cal)} PROTEIN ({round(protein_cal * 100 / calories)}%) [500-650]\
    ({courses_of_pro_left})')
if 45 <= round(carbs_cal * 100 / calories) <= 55:
    print(Fore.GREEN + f'{round(carbs_cal)} CARBS   ({round(carbs_cal * 100 / calories)}%) [45-55]')
if round(carbs_cal * 100 / calories) > 55:
    print(Fore.RED + f'{round(carbs_cal)} CARBS   ({round(carbs_cal * 100 / calories)}%) [45-55]')
if round(carbs_cal * 100 / calories) < 45:
    print(Fore.RESET + f'{round(carbs_cal)} CARBS   ({round(carbs_cal * 100 / calories)}%) [45-55]')
if 20 <= round(fat_cal * 100 / calories) <= 30:
    print(Fore.GREEN + f'{round(fat_cal)} FATS    ({round(fat_cal * 100 / calories)}%) [20-30]')
if round(fat_cal * 100 / calories) > 30:
    print(Fore.RED + f'{round(fat_cal)} FATS    ({round(fat_cal * 100 / calories)}%) [20-30]')
if round(fat_cal * 100 / calories) < 20:
    print(Fore.RESET + f'{round(fat_cal)} FATS    ({round(fat_cal * 100 / calories)}%) [20-30]')
