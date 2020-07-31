import csv

steps_file = open('./Steps_data.csv', 'r', encoding='utf-8-sig')
reader = csv.reader(steps_file)
employee_list = []


class Calc:

    def calculatebmi(self,feet, inches, lbs):
        # convert feet to inches and add with remaining inches
        heightinches = (float(feet) * 12) + float(inches)
        # in order to convert to bmi we must square the height in inches
        denominator = float(heightinches) ** 2
        # divide the weight in pounds by the height squared
        numerator = float(lbs) / float(denominator)
        # multiply by 703 to get final bmi
        bmi = round(numerator * 703, 1)
        return bmi

    def calculatefuturebmi(self, feet, inches, lbs, amount_of_steps):
        # convert steps into calories ( avg person burns .04 calories per step)
        calories = float(amount_of_steps) * .04
        # convert calories into lbs of fat lost
        fat_lost_lbs = round(float(calories) / float(3500), 2)
        # minus lost pounds by current weight in lbs
        new_weight = round(float(lbs) - fat_lost_lbs, 2)
        new_bmi = Calc.calculatebmi(self, feet, inches, new_weight)
        return new_bmi

    def calculateBonus(self, starting_bmi, amount_of_steps):
        # formula to calculate bonus is (bmi * steps )/10000
        numerator = float(starting_bmi) * float(amount_of_steps)
        denominator = float(10000)
        bonus_in_dollars = numerator / denominator
        return round(bonus_in_dollars, 2)

    def calculateExistingBonus(self, name_of_employee):
        steps_file = open('./Steps_data.csv', 'r', encoding='utf-8-sig')
        reader = csv.reader(steps_file)
        for row in reader:
            if name_of_employee == row[1]:
                # formula to calculate bonus is (bmi * steps )/10000
                numerator = float(row[3]) * float(row[2])
                denominator = float(10000)
                bonus_in_dollars = numerator / denominator
                return round(bonus_in_dollars, 2)


