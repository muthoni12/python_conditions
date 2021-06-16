'''
Conditional statement
    - an expression that checks if a condition is met or not
    - it checks if an expression is either true or false
'''

age = 45
if age >= 45:
    print("You are eligible")


age = 18
if age >= 45:
    print("You are eligible")
else:
    print("You are too young")


age = 40
if age > 40:
    print("You are eligible")
elif age == 40:
    print("Yes you are 40, but it's a bit early")
else:
    print("You are too young")