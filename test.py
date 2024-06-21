name = "Patrick"
last_name = "Ryan"
age = 35 
found = False
print(name)
#you do not need to use semi colons to end scentences like in javascript

# if / else statement
if age > 36:
    print("You are old!")
elif age < 36:
    print("You are young!")
else:
    print("I dont know how old I am!") 

if  age == 35:
    print("But not for long!")

print("Thanks for coming!!!")



# functions


def sayhello():
    print("Hello there " + name + " " + last_name + "!")

sayhello()

# list - known as arrays in javascript
colors = ["black", "blue", "green", "yellow"]
#positions    0       1        2         3

#add to list
colors.append("purple")

#travel the list with a for loop
# for(i=0; i<colors.length; i++)
#{
#    let temp = colors[i
#    #console.log(temp)
#}
# python way -------

for x in colors:
    print(x)


print(colors)
# get a specific element
print(colors[1])


# dictionary
person = {
    "firstName": "Patrick",
    "lastName": "Ryan",
    "age": 35
}

print(person)

# modify the dictionary
person["age"] = 39

print(person)

# get the values
print(person["lastName"])







####################### class 2 ###########################



# create a  calculator using functions

def printMenu():
    print("[1]sum")
    print("[2]subtract")
    print("[3]multiplication")
    print("[4]division")


    #plain instructions
printMenu()
opt = input("Select the option: ")

number1=float(input("Please provide the first number: "))
number2=float(input("Please provide the second number: "))

if opt == "1":
    total = number1 + number2
    print("The total is: " + str(total))
elif opt == "2":
    total = number1 - number2
    print("The total is: " + str(total))
elif opt == "3":
    total = number1 * number2
    print("The total is: " + str(total))
elif opt == "4":
    if number2 ==  0:
        print("Dividing by zero is not permitted")
    else:
        total = number1 / number2
        print("The total is: " + str(total))