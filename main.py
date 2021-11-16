
#### Describe each datatype below:(4 marks)

## 4         = integer
## 5.7       =float
## True      =boolean
## Good Luck =string 

#### Which datatype would be useful for storing someone's height? (1 mark)
## Answer   the second(float)


#### Which datatype would be useful for storing someone's hair colour?(1 mark)
## Answer the fourth(string)


####Create a variable tha will store the users name.(1 mark)
#name=input(" type your number ")

####Create a print statement that will print the first 4 characters of the person's name.(3 marks)
#print(name[0:4])

####Convert the user's name to all uppercase characters and print the result
# nameup=name.upper()
# print(nameup)

####Find out how many times the letter A occurs in the user's name
#nameup.count("A")

#### Create a conditional statement to ask a user to enter their age. If they are older than 18 they receive a message saying they can enter the competition, if they are under 18, they receive a message saying they cannot enter the competition.
# age=int(input(" type your age "))
# if age<=18:
#   print(" you cannot enter the competition")
# else:
#   print(" ypu can enter the competition ")


#### Create an empty list called squareNumbers 
#squareNumbers=[]


#### Square numbers are the solutions to a number being multiplied by itself( example 1 is a square number because 1 X 1 = 1, 4 is a square number because 2 X 2 = 4 ). 

###Calculate the first 20 square numbers and put them in the list called squareNumbers. (With loop and .append 10 marks, without, Max 6 marks).
# for count in range(1,21):
#   num=count*count
#   squareNumbers.append(num)


# ####Print your list
# count=0
# while count<20:
#   print(squareNumbers[count])
#   count+=1
####Create a variable called userSquare that asks the user for their favourite square number
# userSquare=int(input(" type your favourite number "))


#### Add this variable to the end of your list called SquareNumbers
#squareNumbers.append(userSquare)


### Create a variable called choice. This variable should choose a random element from your list. Print the variable called choice.
#choice=squareNumbers.randit
#print(choice)


####Create another print statement that prints tha following output: The random square number is: XX, where XX is where the random square number chosen by the computer.(4 marks)
#print(" the random square number is : ",choice)