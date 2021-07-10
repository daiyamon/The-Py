# This is a sample Python script.
from math import*
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("Paycheck Calculator")

hourly_rate1 = input("Enter the hourly rate of the first job: $")
hourly_rate2 = input("Enter the hourly rate of the second job: $")
hours = input("How many hours do you plan on working weekly: ")
print("Choose a time frame: ")
time_frame = input("week, month, year : ")

def calculate_check(num1, num2, time):
    realtime = 1
    if time == "week":
        realtime = 1
    if time == "month":
        realtime = 4
    if time == "year":
        realtime = 52

    check = (float(num1) * float(num2)) * int(realtime)
    return check
def calculate_difference(num1, num2):

    if num1 > num2:
        difference = float(num1) - float(num2)
        pays_more = "first"


    if num2 > num1:
        difference = float(num2) - float(num1)
        pays_more = "second"

    conclusion = "The " + pays_more + " job pays $" + str(difference) + " more."

    return conclusion
check1 = float(calculate_check(hourly_rate1, hours, time_frame))
check2 = float(calculate_check(hourly_rate2, hours, time_frame))

print("The first job will pay $" + str(check1) + " every " + time_frame)
print("The second job will pay $" + str(check2) + " every " + time_frame)
print(calculate_difference(float(check1), float(check2)))