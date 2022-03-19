import time

# Welcome
print("Welcome to the x-quiz, which you will be test out your mathematical ablity. Are you excited?")
time.sleep(2)

# Call and Name
name = input("What is your name")
while not name.isalpha():
  print("Please only enter your name in letter")
  time.sleep(2)
  name = input("What is your name")
time.sleep(2)
call = input("What do you want us to call you")
while not call.isalpha():
  print("Do you want to have letters in your call?")
  time.sleep(2)
  call = input("What do you want us to call you")

print("Hello {} {}, welcome to our game".format(call, name))

point = 0

# Functions
# If the user got selected a choice that is not in letters during junior division or the first question in senior division, they will be notfied that and they will need to reenter the value.
def explain():
  print("This is not a valid solution, please only select number")
# If the user got selected a choice that is not the required alphabet, they will be notified by this and they will need to reenter the value.
def letter():
  print("Please only select between the choice of a,b,c,d")
# If they got it correct in the first ten questions of either division, they will get one point added.
def correct_point_easy():
  global point
  point += 1
# If they got it correct in the last ten questions, they will get two points added.
def correct_point_hard():
  global point
  point += 2
# If they got any question wrong, they will not get any points.
def wrong_point():
  global point
  point += 0
# This is the only possible question in question that involves choice.
def a_valid_solution():
  ["a","b","c","d"]

# Junior quiz function
def junior_quiz():
  junior_1 = input(question_list_junior[0]).strip().lower()
  while not junior_1.isalpha():
    explain()
  while junior_1 not in a_valid_solution():
    letter()
  if junior_1 == "c":
    correct_point_easy()
  else:
    correct_point_hard()
    
  junior_2 = input(question_list_junior[1]).strip().lower()
  while not junior_2.isalpha():
    explain()
    junior_2 = input(question_list_junior[1]).strip().lower()
  while junior_2 not in a_valid_solution():
    letter()
    junior_2 = input(question_list_junior[1]).strip().lower()
  if junior_2 == "a":
    correct_point_easy()
  else:
    wrong_point()
    
  junior_3 = input(question_list_junior[2]).strip().lower()
  while not junior_3.isalpha():
    explain()
    junior_3 = input(question_list_junior[2]).strip().lower()
  while junior_3 not in a_valid_solution():
    letter()
    junior_3 = input(question_list_junior[2]).strip().lower()
  if junior_3 == "a":
    correct_point_easy()
  else:
    wrong_point()
  

  junior_4 = input(question_list_junior[3]).strip().lower()
  while not junior_4.isalpha():
    explain()
    junior_4 = input(question_list_junior[3]).strip().lower()
  while junior_4 not in a_valid_solution():
    letter()
    junior_4 = input(question_list_junior[3]).strip().lower()
  if junior_4 == "d":
    correct_point_easy()
  else:
    wrong_point()
 
  junior_5 = input(question_list_junior[4]).strip().lower()
  while not junior_5.isalpha():
    explain()
    junior_5 = input(question_list_junior[4]).strip().lower()
  while junior_5 not in a_valid_solution():
    letter()
    junior_5 = input(question_list_junior[4]).strip().lower()
  if junior_5 == "b":
    correct_point_easy()
  else:
    wrong_point()

  junior_6 = input(question_list_junior[5])
  while not junior_6.isalpha():
    explain()
    junior_6 = input(question_list_junior[5])
  while junior_6 not in a_valid_solution():
    letter()
    junior_6 = input(question_list_junior[5]).strip().letter()
  if junior_6 == "b":
    correct_point_easy()
  else:
    wrong_point()

  junior_7 = input(question_list_junior[6]).strip().lower()
  while not junior_7.isalpha():
    explain()
    junior_7 = input(question_list_junior[6]).strip().lower()
  while junior_7 not in a_valid_solution():
    letter()
    junior_7 = input(question_list_junior[6]).strip().lower()
  if junior_7 == "a":
    correct_point_easy()
  else:
    wrong_point()

  junior_8 = input(question_list_junior[7]).strip().lower()
  while not junior_8.isalpha():
    explain()
    junior_8 = input(question_list_junior[7]).strip().lower()
  while junior_8 not in a_valid_solution():
    letter()
    junior_8 = input(question_list_junior[7]).strip().lower()
  # There are two correct answers in this choice
  if junior_8 in ["a","c"]:
    correct_point_easy()
  else:
    wrong_point()

  junior_9 = input(question_list_junior[8]).strip().lower()
  while not junior_9.isalpha():
    explain()
    junior_9 = input(question_list_junior[8]).strip().lower()
  while junior_9 not in a_valid_solution():
    letter()
    junior_9 = input(question_list_junior[8]).strip().lower()
  if junior_9 == "a":
    correct_point_easy()
  else:
    wrong_point()

  junior_10 = input(question_list_junior[9]).strip().lower()
  while not junior_10.isalpha():
    explain()
    junior_10 = input(question_list_junior[9]).strip().lower()
  while junior_10 not in a_valid_solution():
    letter()
    junior_10 = input(question_list_junior[9]).strip().lower()
  if junior_10 == "b":
    correct_point_easy()
  else:
    wrong_point()
# Now the question is getting harder and is now worth two points
  junior_11 = input(question_list_juniorplus[0]).strip().lower()
  while not junior_11.isalpha():
    explain()
    junior_11 = input(question_list_juniorplus[0]).strip().lower()
  while junior_11 not in a_valid_solution():
    letter()
    junior_11 = input(question_list_juniorplus[0]).strip().lower()
  if junior_11 == "b":
    correct_point_hard()
  else:
    wrong_point()

  junior_12 = input(question_list_juniorplus[1]).strip().lower()
  while not junior_12.isalpha():
    explain()
    junior_12 = input(question_list_juniorplus[1]).strip().lower()
  while junior_12 not in a_valid_solution():
    letter()
    junior_12 = input(question_list_juniorplus[1]).strip().lower()
  if junior_12 == "a":
    correct_point_hard()
  else:
    wrong_point()

  junior_13 = input(question_list_juniorplus[2]).strip().lower()
  while not junior_13.isalpha():
    explain()
    junior_13 = input(question_list_juniorplus[2]).strip().lower()
  while junior_13 not in a_valid_solution():
    letter()
    junior_13 = input(question_list_juniorplus[2]).strip().lower()
  if junior_13 == "b":
    correct_point_hard()
  else:
    wrong_point()

  junior_14 = input(question_list_juniorplus[3]).strip().lower()
  while not junior_14.isalpha():
    explain()
    junior_14 = input(question_list_juniorplus[3]).strip().lower()
  while junior_14 not in a_valid_solution():
    letter()
    junior_14 = input(question_list_juniorplus[3]).strip().lower()
  if junior_14 == "a":
    correct_point_hard()
  else:
    wrong_point()

  junior_15 = input(question_list_juniorplus[4]).strip().lower()
  while not junior_15.isalpha():
    explain()
    junior_15 = input(question_list_juniorplus[4]).strip().lower()
  while junior_15 not in a_valid_solution():
    letter()
    junior_15 = input(question_list_juniorplus[4]).strip().lower()
  if junior_15 == "a":
    correct_point_hard()
  else:
    wrong_point()

  junior_16 = input(question_list_juniorplus[5]).strip().lower()
  while not junior_16.isalpha():
    explain()
    junior_16 = input(question_list_juniorplus[5]).strip().lower()
  while junior_16 not in a_valid_solution():
    letter()
    junior_16 = input(question_list_juniorplus[5]).strip().lower()
  if junior_16 == "d":
    correct_point_hard()
  else:
    wrong_point()

  junior_17 = input(question_list_juniorplus[6]).strip().lower()
  while not junior_17.isalpha():
    explain()
    junior_17 = input(question_list_juniorplus[6]).strip().lower()
  while junior_17 not in a_valid_solution():
    letter()
    junior_17 = input(question_list_juniorplus[6]).strip().lower()
  if junior_17 == "a":
    correct_point_hard()
  else:
    wrong_point()

  junior_18 = input(question_list_juniorplus[7]).strip().lower()
  while not junior_18.isalpha():
    explain()
    junior_18 = input(question_list_juniorplus[7]).strip().lower()
  while junior_18 not in a_valid_solution():
    letter()
    junior_18 = input(question_list_juniorplus[7]).strip().lower()
  if junior_18 == "a":
    correct_point_hard()
  else:
    wrong_point()

  junior_19 = input(question_list_juniorplus[8]).strip().lower()
  while not junior_19.isalpha():
    explain()
    junior_19 = input(question_list_juniorplus[8]).strip().lower()
  while junior_19 not in a_valid_solution():
    letter()
    junior_19 = input(question_list_juniorplus[8]).strip().lower()
  if junior_19 == "a":
    correct_point_hard()
  else:
    wrong_point()

  junior_20 = input(question_list_juniorplus[9]).strip().lower()
  while not junior_20.isalpha():
    explain()
    junior_20 = input(question_list_juniorplus[9]).strip().lower()
  while junior_20 not in a_valid_solution():
    letter()
    junior_20 = input(question_list_juniorplus[9]).strip().lower()
  if junior_20 == "a":
    correct_point_hard()
  else:
    wrong_point()

#Quizbank in junior division that is going to be given to the user.
  junior_quizbank =       [junior_1,junior_2,junior_3,junior_4,junior_5,junior_6,junior_7,junior_8,junior_9,junior_10,junior_11,junior_12,junior_13,junior_14,junior_15,junior_16,junior_17,junior_18,junior_19,junior_20]

# Question in senior division
def senior_division():
  senior_1 = input(question_list_senior[0]).strip().lower()
  while not senior_1.isalpha():
    explain()
    senior_1 = input(question_list_senior[0]).strip().lower()
  while senior_1 not in a_valid_solution():
    letter()
    senior_1 = input(question_list_senior[0]).strip().lower()
  if senior_1 == "a":
    correct_point_easy()
  else:
    wrong_point()

  senior_2 = input(question_list_senior[1]).strip().lower()
  while not senior_2.isalpha():
    explain()
    senior_2 = input(question_list_senior[1]).strip().lower()
  while senior_2 not in a_valid_solution():
    letter()
    senior_2 = input(question_list_senior[1]).strip().lower()
  if senior_2 == "a":
    correct_point_easy()
  else:
    wrong_point()
    
  senior_quizbank = ["senior_1","senior_2","senior_3","senior_4","senior_5","senior_6","senior_7","senior_8","senior_9","senior_10","senior_11","senior_12","senior_13","senior_14","senior_15","senior_16","senior_17","senior_18","senior_19","senior_20"]

# Asking for their age to then allocate them into different division.
try:
  age = int(input("How old are you?"))
except ValueError:
  print("You are not enter a value number")
  age = int(input("How old are you?"))

if age < 10:
  print("This might be too difficult for you")
  continue_ = input("Do you want to continue? Please answer in y/n").strip().lower()
  if continue_ == "n":
    print("See you in the future!")
  elif continue_ not in ["n","y"]:
    print("Please select between y/n")
    continue_ = input("Do you want to continue? Please answer in y/n")
  elif continue_ == "y":
    print("Enjoy your game!")
elif 10 <= age <= 14:
  print("You are in junior division!")
  junior_quiz()
elif 15 <= age <= 18:
  print("You are in senior division!")
elif age > 18:
  print("You are too old to attend this quiz")
  exit()
  
# The quizs
  # Simple questions, only worth one marks
question_list_junior = ["What is 3 * 5 + 4? a)32 b)27 c)19 d)23", #1
                       "What is the sum of angle in a triangle? a)180 b)90 c)270 d)360?", #2
                       """Which of the following statement is correct? 
                   a)Angles in a square sum to 360 degrees
                   b)Angles in a circle sum to 180 degrees
                   c)Vertically opposite angles sum to 180 degrees
                   d)Shapes with two side are called a triangle""", #3
                       "What is 10 squared? a)10 b)20 c)1 d)100", #4
                       """Which of them is first in calculations?
                   a)Multiplication and Division
                   b)Addition and Subtraction""", #5
                       "What is the longest side in a right angle triangle? a)adjacent b)hypotenuse c)opposite d)I am not sure", #6
                       "What is the highest power in a linear function? a)1 b)2 c)3 d)4", # 7
                       "What is square root of 4? a)2 b)4 c)-2 d)-4", # 8
                       "What is sine 30 degrees? a)0.5 b)1 c)sqrt(2)/3 d)0", # 9
                       """What is the definition of sine?
                    a)Opposite side over adjacent side
                    b)Opposite side over hypotenuse side
                    c)adjacent side over hypotenuse side
                    d)adjacent side over the opposite side"""] #10

question_list_senior = ["""What is the FORMAL definition of ellipse?
                        a)It has the same distance towards two focus from a certain point
                        b)The sum of the distance among two focus is 2a
                        c)The sum of the two focus is 2a
                        d)It has the same distance between two focus towards the center""",
                        """What is the FORMAL definition of parabola?
                        a)The distance between its focus and directrix toward the vertex is the same
                        b)The distance from a fixed point have the same distance towards the focus and directrix.
                        c)Vertex have to located at the origin
                        d)If the equation is y^2 = 4ax and the vertex is located on the center, the focus is located on (2a,0) and (-2a,0)""",
                        "What is the first deriative of function f(x)=2x^2? a)4x b)2x c)2x^2 d)4",
                        """If we are taking the deriative of a fraction, which method shall we apply?
                        a)Chain Rule
                        b)Product Rule
                        c)Quotient Rule
                        d)Number Rule""",
                        """If we are taking the deriative of a composite function, which method shall we apply?
                        a)Chain Rule
                        b)Product Rule
                        c)Quotient Rule
                        d)Number Rule""",
                       """What is a method we can use to calculate the equation of tangent line to a circle?
                        a)Implict differentation
                        b)Partial differentation
                        c)Algebraic differentation
                        d)Integration""",
                       """if z = a+bi, what is the value of z^2 if a = 2 and b = 1?
                       a)3+4i
                       b)4+3i
                       c)4-3i
                       d)3-4i""",
                       """What is sin(x+y)?
                       a)sin(x)cos(y)-cos(x)sin(y)
                       b)sin(x)sin(y)+cos(x)cos(y)
                       c)sin(x)cos(y)+cos(x)sin(y)
                       d)sin(x)sin(y)-cos(x)cos(y)""",
                       """What is In(-1)? Plese give in a complex solution
                       a)i(pi)
                       b)-i
                       c)-i(pi)
                       d)ei"""]
                        
                        
                        

# Those part of questions have a higher difficulties than the other question.
question_list_juniorplus = ["""What is a unit circle?
                             a)Circle with a circumfenrence of 1
                             b)Circle with a radius of 1
                             c)Circle with a center at the origin
                             d)Circle with no radius""",
                            "How many degrees is in pi? a)180 b)360 c)90 d)0",
                            """Solve for x is x^2 = -4?
                            a)-2 b)No real solution c)2 d)2""",
                            """What is the formal definition of circle?
                           a)The shape that has the same distance between its circumference and center
                           b)A shape that has 360 degrees
                           c)A roundy shape
                           d)A shape that has the same distance between its focus and directrix.""",
                           """What is the same as x square root?
                           a)x to the power of 1/2
                           b)x to the power of 1/3
                           c)x to the power of 2
                           d)x to the power of -1""",
                           "What is the tangent 90 degrees? a)0 b)1 c)-1 d)Not Exist",
                           "What is log 10? a)1 b)0 c)10 d)-1",
                           "What is In e? a)1 b)0 c)10 d)-1",
                           """What is m mean in a linear equation of y = mx+c?
                           a)Gradient
                           b)Y-intercept
                           c)X-intercept
                           d)Rise/Run""",
                           "What is the gradient of line y = x+3 a)1 b)2 c)3 d)-1"]

# This need an input
question_list_seniorplus = ["Calculate the deriative of 2(x-5)^2",
                           "Calculate the deriative of (x^2 - 3) / x+5",
                           "Calculate the integral from 0 to 1, 2x dx",
                           "Is f(x) = 12x + x^2 a maximum or a minimum? Please enter your value in max or min",
                           "Calculate the value of the X-COORDINATE of the focus in the equation of parabola y^2 = 8x",
                           "Calculate the vertex of the hyperbola in the equation 4x^2 - 9y^2 = 36. You just need to have one answer",
                           "If Z = 1.56, calculate the value of p(x) in the normal distribution",
                           "Please write the equation of the parabola if it has the x-intercept at -3 and 3. PLEASE WRITE THEM in terms of y",
                           "Solve the x in exponetial equation of 3^(x-5) = 81",
                           "Calculate the value of log 20 + log 5, leave this as a number."]
                    

  
                        
                        
                        
