print("Welcome to love calculator")
your_name = input("What is your name ? \n")
their_name = input("What is their name ? \n")

your_name = your_name.lower()
their_name = their_name.lower()

combined_string = your_name + their_name

lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}. You are like coke mentos together.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, You are alright together.")
else:
    print(f"your score is {love_score}.")