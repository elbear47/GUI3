from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import csv
from calculations import Calc

steps_file = open('./Steps_data.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(steps_file)

root = Tk()
root.title('Metrics for Health Step Tracker')
root.geometry("400x200")

c = Calc()


age_bmi_list = []
age_steps_list = []
age_bonus_list = []
for row in reader:
    # add ages and bmi data to a list
    age_bmi_list.append([row[5], row[3]])
    age_steps_list.append([row[5], row[4]])
    age_bonus_list.append([row[5], c.calculateExistingBonus(row[1])])

# sort the list in asc order using age
sorted_age_bmi_list = sorted(age_bmi_list)
sorted_age_steps_list = sorted(age_steps_list)
sorted_age_bonus_list = sorted(age_bonus_list)

# this section will be for bmi by age
ages = []
bmi_data = []
for element in sorted_age_bmi_list:
    ages.append(int(element[0]))
    bmi_data.append(int(element[1]))
# this section will be for avg number of steps taken daily by age
ages2 = []
daily_steps = []
for element in sorted_age_steps_list:
    ages2.append(int(element[0]))
    daily_steps.append(float(element[1]))

# this section will be for bonus by age
ages3 = []
bonus = []
for element in sorted_age_bonus_list:
    ages3.append(int(element[0]))
    bonus.append(float(element[1]))


# graph bmi by age
def graph_bmi_by_age():
    plt.bar(ages, bmi_data)
    plt.xlabel('Ages')
    plt.ylabel('BMI')
    plt.title('BMI by Age')
    plt.show()


# graph avg number of daily steps by age
def graph_steps_by_age():
    plt.bar(ages2, daily_steps)
    plt.xlabel('Ages')
    plt.ylabel('Avg Num Of Daily Steps')
    plt.title('Avg Number of Daily Steps by Age')
    plt.show()


# graph bonus by age
def graph_bonus_by_age():
    plt.bar(ages3, bonus)
    plt.xlabel('Ages')
    plt.ylabel('Bonus(USD)')
    plt.title('Bonuses in Dollars by Age')
    plt.show()


myBtn = Button(root, text='View BMI by Age', command=graph_bmi_by_age)
myBtn.pack()
myBtn2 = Button(root, text='View Avg Number of Steps taken daily by Age', command=graph_steps_by_age)
myBtn2.pack()
myBtn3 = Button(root, text='View Bonuses by Age', command=graph_bonus_by_age)
myBtn3.pack()

root.mainloop()
