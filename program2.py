# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)
import random
value_1 = random.randint(0,99)
value_2 = random.randint(0,99)
# Function for question 1
def question_1():
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    a_= int(input(f"1.){value_1} + {value_2}= "))
    if a_ == int(value_1 + value_2):
        print("Correct")
        a_ans = int(1)
    else:
        print("Wrong")
        a_ans = int(0)
    return a_ans

# Function for question 2
def question_2(a_ans):
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    b_= int(input(f"2.){value_1} + {value_2}= "))
    if b_ == int(value_1 + value_2):
        print("Correct")
        b_ans = int(a_ans +  1)
    else:
        print("Wrong")
        b_ans = int(a_ans +  0)
    return b_ans

# Function for question 3
def question_3(b_ans):
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    c_= int(input(f"3.){value_1} + {value_2}= "))
    if c_ == int(value_1 + value_2):
        print("Correct")
        c_ans = int(b_ans + 1)
    else:
        print("Wrong")
        c_ans = int(b_ans + 0)
    return c_ans

# Function for question 4
def question_4(c_ans):
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    d_= int(input(f"4.){value_1} + {value_2}= "))
    if d_ == int(value_1 + value_2):
        print("Correct")
        d_ans = int(c_ans + 1)
    else:
        print("Wrong")
        d_ans = int(c_ans + 0)
    return d_ans

# Function for question 5
def question_5(d_ans):
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    e_= int(input(f"5.){value_1} + {value_2}= "))
    if e_ == int(value_1 + value_2):
        print("Correct")
        e_ans = int(d_ans + 1)
    else:
        print("Wrong")
        e_ans = int(d_ans + 0)
    return e_ans

# Function for question 6
def question_6(e_ans):
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    f_= int(input(f"6.){value_1} + {value_2}= "))
    if f_ == int(value_1 + value_2):
        print("Correct")
        f_ans = int(e_ans + 1)
    else:
        print("Wrong")
        f_ans = int(e_ans + 0)
    return f_ans

# Function for question 7
def question_7(f_ans):
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    g_= int(input(f"7.){value_1} + {value_2}= "))
    if g_ == int(value_1 + value_2):
        print("Correct")
        g_ans = int(f_ans + 1)
    else:
        print("Wrong")
        g_ans = int(f_ans + 0)
    return g_ans

# Function for question 8
def question_8(g_ans):
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    h_= int(input(f"8.){value_1} + {value_2}= "))
    if h_ == int(value_1 + value_2):
        print("Correct")
        h_ans = int(g_ans + 1)
    else:
        print("Wrong")
        h_ans = int(g_ans + 0)
    return h_ans

# Function for question 9
def question_9(h_ans):
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    i_= int(input(f"9.){value_1} + {value_2}= "))
    if i_ == int(value_1 + value_2):
        print("Correct")
        i_ans = int(h_ans + 1)
    else:
        print("Wrong")
        i_ans = int(h_ans + 0)
    return i_ans

# Function for question 10
def question_10(i_ans):
    value_1 = random.randint(0,99)
    value_2 = random.randint(0,99)
    j_= int(input(f"10.){value_1} + {value_2}= "))
    if j_ == int(value_1 + value_2):
        print("Correct")
        j_ans = int(i_ans + 1)
    else:
        print("Wrong")
        j_ans = int(i_ans + 0)
    return j_ans

# Function for displaying the total score
def display(j_ans):
    print(f"You total score is {j_ans}/10")


print("Answer the following questions:")

# Questions
a_ans = question_1()
b_ans = question_2(a_ans)
c_ans = question_3(b_ans)
d_ans = question_4(c_ans)
e_ans = question_5(d_ans)
f_ans = question_6(e_ans)
g_ans = question_7(f_ans)
h_ans = question_8(g_ans)
i_ans = question_9(h_ans)
j_ans = question_10(i_ans)
# Displaying the total score
display(j_ans)

print("Thank you!")