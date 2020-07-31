from tkinter import *
from calculations import Calc
import csv
from plots import graph_bonus_by_age, graph_steps_by_age, graph_bmi_by_age

steps_file = open('./Steps_data.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(steps_file)
c = Calc()



root = Tk()
root.title("Step-Health Tracking Software")




def showCurrentBonus():
    myLabel = Label(root, text=c.calculateExistingBonus(clicked.get())).grid(row=2, column=1)


# FIRST SECTION (show current bonus for the year)

# get items we want to show in the menu
options = []
for row in reader:
    options.append(row[1])

current_bonus_lbl = Label(root, text='Select Name to View Current Bonus')
current_bonus_lbl.grid(row=0, column=1)

clicked = StringVar()  # define what type of variable for the menu items
clicked.set(options[0])  # set default
# Drop down boxes
drop = OptionMenu(root, clicked, *options)
drop.grid(row=1, column=1)

myButton = Button(root, text="Show Current Bonus", command=showCurrentBonus).grid(row=3, column=1, pady=10)

# NEXT SECTION ( project future bonus or BMI)

# create labels
heightLbl = Label(root, text='Enter Details to Project Future Bonus').grid(row=4, column=1, pady=20)
feetLbl = Label(root, text='Feet').grid(row=5, column=1, pady=5)
inchesLbl = Label(root, text='Inches').grid(row=6, column=1, pady=20)
weightLbl = Label(root, text='Weight in Lbs:').grid(row=7, column=1, pady=20)
avg_num_of_steps = Label(root, text='Enter average number of steps you plan to take each day:').grid(row=8, column=1,
                                                                                                     pady=20)
# create text boxes
feetTxt = Entry(root)
feetTxt.grid(row=5, column=2, pady=20)
inchestTxt = Entry(root)
inchestTxt.grid(row=6, column=2, pady=20)
weightTxt = Entry(root)
weightTxt.grid(row=7, column=2, pady=20)
avgStepsTxt = Entry(root)
avgStepsTxt.grid(row=8, column=2, pady=20)

# get input from text boxes and assign them to variables
feet = feetTxt.get()
inches = inchestTxt.get()
weight = weightTxt.get()
avgSteps = avgStepsTxt.get()


# show BMI if they stick to their step plan

def pressCalculateFutureBonus():
    futureBonusLbl = Label(root, text="Projected Next Year Bonus is: $" + str(c.calculateBonus(
        c.calculatebmi(feetTxt.get(), inchestTxt.get(), weightTxt.get()),
        int(avgStepsTxt.get()) * 365)))
    futureBonusLbl.grid(row=9, column=2, pady=20)


calcFutureBonusBtn = Button(root, text='Calculate Projected Bonus', command=pressCalculateFutureBonus)
calcFutureBonusBtn.grid(row=10, column=1, pady=20)

next_page_Lbl = Label(root, text='See Charts/Metrics')
next_page_Lbl.grid(row=11, column=1, pady=50)


myBtn = Button(root, text='View BMI by Age', command=graph_bmi_by_age)
myBtn.grid(row=12, column=1, pady=30)
myBtn2 = Button(root, text='View Avg Number of Steps taken daily by Age', command=graph_steps_by_age)
myBtn2.grid(row=13, column=1, pady=20)
myBtn3 = Button(root, text='View Bonuses by Age', command=graph_bonus_by_age)
myBtn3.grid(row=14, column=1, pady=20)

root.mainloop()
