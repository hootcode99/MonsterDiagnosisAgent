from itertools import combinations, product
import numpy as np


def convert_symbols(disease_dict):
    for key, value in disease_dict.items():
        if value == '0':
            disease_dict[key] = 0
        elif value == '+':
            disease_dict[key] = 1
        elif value == '-':
            disease_dict[key] = -1

    return disease_dict


def check_match(disease_combinations, patient_vitamins):
    print("\n")
    print("Check Match")
    print("---------------")
    patient_vitamins_values = list(patient_vitamins.values())
    match = None

    for name, vitamins in list(disease_combinations.items()):
        check_array = []

        for vitamin_value in vitamins:
            if vitamin_value > 1:
                check_array.append(1)
            elif vitamin_value < -1:
                check_array.append(-1)
            else:
                check_array.append(vitamin_value)
        print("check:", check_array)
        if check_array == patient_vitamins_values:
            match = name
            break
    print("\n")
    return match


def sum_values(list_a, list_b):
    a_numpy = np.array(list_a)
    b_numpy = np.array(list_b)
    output = np.add(a_numpy, b_numpy).tolist()
    return output


class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, diseases, patient):
        diagnosis = []

        # convert patient vitamin values to integers
        patient_vitamins = convert_symbols(patient)

        # convert disease vitamin values to integers
        # for disease in list(diseases.values()):
        #     convert_symbols(disease)

        # convert disease name values into their own array
        # names_list = []
        # for disease_name in list(diseases.keys()):
        #     names_list.append(disease_name)

        disease_combos = combinations(list(diseases.items()), 2)

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



        return diagnosis

