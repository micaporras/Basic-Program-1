# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

# Function for question 1
def question_1():
    a_= int(input("1.) 4 + 5= "))
    if a_ == 9:
        print("Correct")
        a_ans = int(1)
    else:
        print("Wrong")
        a_ans = int(0)
    return a_ans

# Function for question 2
def question_2(a_ans):
    b_= int(input("2.) 7 + 9= "))
    if b_ == 16:
        print("Correct")
        b_ans = int(a_ans +  1)
    else:
        print("Wrong")
        b_ans = int(a_ans +  0)
    return b_ans

# Function for question 3
def question_3(b_ans):
    c_= int(input("3.) 14 + 13= "))
    if c_ == 27:
        print("Correct")
        c_ans = int(b_ans + 1)
    else:
        print("Wrong")
        c_ans = int(b_ans + 0)
    return c_ans

# Function for question 4
def question_4(c_ans):
    d_= int(input("4.) 19 + 16= "))
    if d_ == 35:
        print("Correct")
        d_ans = int(c_ans + 1)
    else:
        print("Wrong")
        d_ans = int(c_ans + 0)
    return d_ans

# Function for question 5
def question_5(d_ans):
    e_= int(input("5.) 13 + 15= "))
    if e_ == 28:
        print("Correct")
        e_ans = int(d_ans + 1)
    else:
        print("Wrong")
        e_ans = int(d_ans + 0)
    return e_ans

# Function for question 6
def question_6(e_ans):
    f_= int(input("6.) 20 + 21= "))
    if f_ == 41:
        print("Correct")
        f_ans = int(e_ans + 1)
    else:
        print("Wrong")
        f_ans = int(e_ans + 0)
    return f_ans

# Function for question 7
def question_7(f_ans):
    g_= int(input("7.) 31 + 27= "))
    if g_ == 58:
        print("Correct")
        g_ans = int(f_ans + 1)
    else:
        print("Wrong")
        g_ans = int(f_ans + 0)
    return g_ans

# Function for question 8
def question_8(g_ans):
    h_= int(input("8.) 17 + 28= "))
    if h_ == 45:
        print("Correct")
        h_ans = int(g_ans + 1)
    else:
        print("Wrong")
        h_ans = int(g_ans + 0)
    return h_ans

# Function for question 9
def question_9(h_ans):
    i_= int(input("9.) 12 + 24= "))
    if i_ == 36:
        print("Correct")
        i_ans = int(h_ans + 1)
    else:
        print("Wrong")
        i_ans = int(h_ans + 0)
    return i_ans

# Function for question 10
def question_10(i_ans):
    j_= int(input("10.) 23 + 67= "))
    if j_ == 90:
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