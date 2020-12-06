import turtle
import time

fred = turtle.Turtle()
fred.shape("turtle")
fred.screen.bgcolor("light grey")
fred.screen.setup(550, 550)
MADSIZE = 14
MADFONT = ('Arial', MADSIZE, 'normal')
TITLESIZE = 16
TITLEFONT = ('Arial', MADSIZE, 'bold')

def defaultFred():
  fred.color("black")
  fred.width(1)

def erase():
  fred.penup()
  fred.goto(0,-100)
  fred.pendown()
  fred.width(1000)
  fred.color("light grey")
  fred.left(90)
  fred.forward(400)
  fred.right(90)
  fred.penup()
  defaultFred()

def madlib1(my_dict, num_choice):
  fred.penup()
  fred.goto(0,0)
  fred.write("Generating your madlib..", align = "center", font=MADFONT)
  fred.penup()
  fred.goto(0,-20)
  # ask for adjective
  adj = input("Enter adjective: ")
  print("Your adjective is: " + adj)
  # ask for word to scream
  scream = input("Enter scream: ")
  print("Your scream is " + scream)
  # ask for __adverb___
  adverb = input("Enter adverb: ")
  print("Your adverb is: " + adverb)
  # ask for noun
  noun = input("Enter noun: ")
  print("Your noun is: " + noun)
  erase()
  fred.penup()
  fred.goto(0,100)
  fred.write(my_dict[num_choice],move=False, align="center", font=TITLEFONT)
  fred.goto(0,0)
  fred.color("red")
  fred.write(scream + "! he said " + adverb + " as he jumped into his convertible " + noun + " \nand drove off with \nhis " + adj + " wife." ,move=False, align="center",font=MADFONT)
  fred.right(90)
  fred.forward(50)
  fred.left(90)
  time.sleep(5)
  erase()

def madlib2(my_dict, num_choice):
  fred.penup()
  fred.goto(0,0)
  fred.write("Generating your madlib..", align = "center", font=MADFONT)
  fred.penup()
  fred.goto(0,-20)
  # ask for adjective
  adj = input("Enter adjective: ")
  print("Your adjective is: " + adj)
  # ask for word to scream
  scream = input("Enter scream: ")
  print("Your scream is " + scream)
  # ask for __adverb___
  adverb = input("Enter adverb: ")
  print("Your adverb is: " + adverb)
  # ask for noun
  noun = input("Enter noun: ")
  print("Your noun is: " + noun)
  erase()
  fred.penup()
  fred.goto(0,100)
  fred.write(my_dict[num_choice],move=False, align="center", font=TITLEFONT)
  fred.goto(0,0)
  fred.color("red")
  fred.write(scream + "! he said " + adverb + " as he jumped into his convertible " + noun + " \nand drove off with his " + adj + " wife." ,move=False, align="center",font=MADFONT)
  fred.right(90)
  fred.forward(50)
  fred.left(90)
  time.sleep(5)
  erase()

def mainmenu():
  fred.write("Hi welcome to my madlib generator!", align = "center", font=MADFONT)
  fred.penup()
  fred.goto(0,-20)
  time.sleep(3)
  erase()

  user_choice = 0
  title_dict = {
    1 : "Madlib 1 in dictionary",
    2 : "Madlib 2 in dictionary"
  }
  while(user_choice != 9):
    fred.goto(0,0)
    fred.write("Choose the madlib you would like to create: \n 1. Madlib 1 \n 2. Madlib 2\n 9. Quit", align = "center", font=MADFONT)
    fred.penup()
    fred.goto(0,-20)
    try:  
      user_choice = int(input("Please enter your answer here!"))
      if user_choice == 1:
        erase()
        madlib1(title_dict,user_choice)
      elif user_choice == 2:
        erase()
        madlib2(title_dict,user_choice)
    except:
      print("That's not an integer number.")
  erase()
  fred.goto(0,0)
  fred.write("Thanks for playing :)", align = "center", 
  font=MADFONT)
  fred.goto(0,-20)
  
# End function definitions
mainmenu()

