first_name = input("Type your first name: ")
last_name = input("Type your last name: ")
bonus = input("Write the number in total of your sales here: ")
money = float(bonus)
x = 13 
y = 100 # I made this two variables in order to calculate a percent

extra_pay = money * x
extra_pay2 = extra_pay / y # with 'y' and 'x' variable we calculate a percent
value = round(extra_pay2, 2)
total = value

print(f"Your first name is:  {first_name} \nYour last name is:  {last_name} \nYour number of total sales is: {bonus} \nYour extra pay is: {total}")