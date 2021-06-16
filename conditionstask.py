'''
Write a function that checks if a number given by the user is even or odd.
'''
def findoddoreven():
    number = int(input("Enter a number: "))
    x = number % 2
    if x == 0 :
        print("the number is even")
    else:
        print("number is odd")

findoddoreven()


'''
Write the same function for a list of numbers.

numbers = [207, 106, 86, 45]
for x in numbers:
    if x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
'''
def findoddoreven(numbers):
    for x in numbers:
        if x % 2 == 0:
            print(str(x) + " is even")
        else:
            print(str(x) + " is odd")    
findoddoreven([207, 106, 86, 45])


'''
Write a function that prints all the vowels form a sentence provided by the user.
'''
def findvowels():
    sentence = (input("Enter a sentence: "))
    vowels = ["a", "e", "i", "o", "u"] in sentence
    if vowels:
        print(vowels)

findvowels()


'''
Write the same function for a given sentence.
'''
sentence = "i am hungry"
for letter in sentence:
    if letter == "a":
        print("a")
    if letter == "e":
        print("e")
    if letter == "i":
        print("i")
    if letter == "o":
        print("o")
    if letter == "u":
        print("u")



sentence = "i love you"
vowels = ["a", "e", "i", "o", "u"]
for letters in sentence:
    if letters in vowels:
        print(letters)



