print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
together_names =name1+name2
lower_names = together_names.lower()#lower() method to use lower the names
t = lower_names.count("t")#count() method to use to count the letter occurances
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit =t+r+u+e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l+o+v+e

score = int(str(first_digit)+str(second_digit))#(type conversion used to convert string to integer)
if score<10 or score>=90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score <=50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  


