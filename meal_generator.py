"""
Aman Arya

This is a basic algorithm for generating meal plans, simply adds food
for whichever count is low or high
"""

import random as r
from collections import defaultdict

class Food:
    "Basic class for Food information"
    def __init__(self, name, cal, attrib):
        self.name = name
        self.cal = cal
        self.attrib = attrib

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def getattrib(self):
        return self.attrib


# Basic made up data
low = 50
high = 250
data = [Food('LDLr1', r.randint(low, high), ['LDLr']),
        Food('HDLi1', r.randint(low, high), ['HDLi']),
        Food('Gi1', r.randint(low, high), ['Gi']),
        Food('HDLr1', r.randint(low, high), ['HDLr']),
        Food('LDLi1', r.randint(low, high), ['LDLi']),
        Food('Gr1', r.randint(low, high), ['Gr']),
        Food('LDLr2', r.randint(low, high), ['LDLr']),
        Food('HDLi2', r.randint(low, high), ['HDLi']),
        Food('Gi2', r.randint(low, high), ['Gi']),
        Food('HDLr2', r.randint(low, high), ['HDLr']),
        Food('LDLi2', r.randint(low, high), ['LDLi']),
        Food('Gr2', r.randint(low, high), ['Gr']),
        Food('LDLr3', r.randint(low, high), ['LDLr']),
        Food('HDLi3', r.randint(low, high), ['HDLi']),
        Food('Gi3', r.randint(low, high), ['Gi']),
        Food('HDLr3', r.randint(low, high), ['HDLr']),
        Food('LDLi3', r.randint(low, high), ['LDLi']),
        Food('Gr3', r.randint(low, high), ['Gr']),
        Food('LDLr4', r.randint(low, high), ['LDLr']),
        Food('HDLi4', r.randint(low, high), ['HDLi']),
        Food('Gi4', r.randint(low, high), ['Gi']),
        Food('HDLr4', r.randint(low, high), ['HDLr']),
        Food('LDLi4', r.randint(low, high), ['LDLi']),
        Food('Gr4', r.randint(low, high), ['Gr'])]


# really basic and simple way to group food items
food_map = defaultdict(list)
for d in data:
    for a in d.attrib:
        food_map[a].append(d)


def generate_meals(user_in, user_cal=1600):
    """
    This generates the meal plan for the day based on what the user's
    data and recommended calorie count (1600 default).
    :param user_in: dictionary that tells user levels for each factor
    :return: dictionary containing meal plans for the day and overall calorie count
    """

    bcal = 0.3 * user_cal
    lunch = bcal
    sn = 0.1 * user_cal
    dn = bcal

    s = {'b': bcal, 'l': lunch, 'sn': sn, 'dn': dn}

    user_map = defaultdict(list)
    for k, v in user_in.items():
        user_map[v].append(k)

    eaten = []
    meals = {}
    alt = True
    over = 0
    for k,v in s.items():
        count = 0
        meals[k] = []
        while count < v-100:

            if alt:
                for t in user_map[3]:
                    f = choose_meal(food_map[t+'r'], eaten)

                    eaten.append(f)
                    meals[k].append(f)
                    count += f.cal

                    if count > v-65:
                        alt = not alt
                        break

            else:
                for t in user_map[1]:
                    f = choose_meal(food_map[t + 'i'], eaten)

                    eaten.append(f)
                    meals[k].append(f)
                    count += f.cal

                    if count > v-65:
                        alt = not alt
                        break

            for t in user_map[2]:
                if alt:
                    f = choose_meal(food_map[t + 'i'], eaten)


                else:
                    f = choose_meal(food_map[t + 'r'], eaten)

                eaten.append(f)
                meals[k].append(f)
                count += f.cal

                if count > v-65:
                    alt = not alt
                    break

            alt = not alt

        over += count
        meals[k].append(count)

    meals['overall'] = over
    return meals



def choose_meal(m, eaten):
    while True:
        f = r.choice(m)
        if f not in eaten:
            return f


#sample user input
user_in = {'LDL':2, 'HDL':2, "G":2}

print generate_meals(user_in)




