from itertools import combinations, product
import numpy as np


# convert patient vitamin values to integers
# patient_vitamins = convert_symbols(patient)
# convert disease vitamin values to integers
# for disease in list(diseases.values()):
#     convert_symbols(disease)
# convert disease name values into their own array
# names_list = []
# for disease_name in list(diseases.keys()):
#     names_list.append(disease_name)

def convert_symbols(disease_dict):
    for key, value in disease_dict.items():
        if value == '0':
            disease_dict[key] = 0
        elif value == '+':
            disease_dict[key] = 1
        elif value == '-':
            disease_dict[key] = -1

    return disease_dict


def combo_2(disease_combos):
    combine_dict = {}
    for item in disease_combos:

        name_a = item[0][0]
        name_b = item[1][0]
        values_a = item[0][1]
        # print(list(values_a.values()))
        values_b = item[1][1]
        # print(list(values_b.values()))

        sum_dict = {}
        c_value = ''
        for key, value in values_a.items():
            # combination rules for positive vitamin
            if value == '+':
                if values_b.get(key) == '+':
                    c_value = '+'
                elif values_b.get(key) == '0':
                    c_value = '+'
                elif values_b.get(key) == '-':
                    c_value = '0'
            # combination rules for neutral vitamins
            elif value == '0':
                if values_b.get(key) == '+':
                    c_value = '+'
                elif values_b.get(key) == '0':
                    c_value = '0'
                elif values_b.get(key) == '-':
                    c_value = '-'
            # combination rules for negative vitamins
            elif value == '-':
                if values_b.get(key) == '+':
                    c_value = '0'
                elif values_b.get(key) == '0':
                    c_value = '0'
                elif values_b.get(key) == '-':
                    c_value = '-'
            # build the sum dictionary for the combination
            sum_dict[key] = c_value
            # add the new dictionary as the value for the combination
            combine_dict.update({name_a + "-" + name_b: sum_dict})
    # print dictionary
    for k, v in combine_dict.items():
        print(k, '->', v)

    return combine_dict



def check_match(combine_dict, patient):
    solution = ''
    for combo_name, vitamin_list in combine_dict.items():
        # print(combo_name, vitamin_list)
        # print("Patient", patient)
        if patient == vitamin_list:
            print("------------MATCH FOUND--------------")
            solution = combo_name.split('-')
            return solution

    return None


class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, diseases, patient):
        diagnosis = None

        # # print dictionary
        # for k, v in diseases.items():
        #     print(k, '->', v)
        # # check with initial values
        # diagnosis = check_match(diseases, patient)
        #
        # # check combinations of 2
        # if diagnosis is None:
        #     disease_combos = combinations(list(diseases.items()), 2)
        #     combine_dict = combo_2(disease_combos)
        #     diagnosis = check_match(combine_dict, patient)

        # check combinations of 3
        if diagnosis is None:
            disease_combos = combinations(list(diseases.items()), 3)
            print(*list(disease_combos), sep='\n')
            # combine_dict = combo_2(disease_combos)
            # diagnosis = check_match(combine_dict, patient)


        return diagnosis
