# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

lenght = len(names)
index = random.randint(0, lenght-1)
value = names[index]



print(f"{value} is paying the bill today.")