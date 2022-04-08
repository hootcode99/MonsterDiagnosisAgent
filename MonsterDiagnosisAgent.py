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
        print(name, vitamins)
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
        for disease in list(diseases.values()):
            convert_symbols(disease)

        # convert disease name values into their own array
        names_list = []
        for disease_name in list(diseases.keys()):
            names_list.append(disease_name)

        # convert disease names and values from dictionary to separate arrays
        names_list, values_list = self.create_value_arrays(diseases)
        print("Initial Values")
        print("---------------")

        print("namelist:", names_list)
        print("valuelist:", *values_list, sep='\n')
        print("patient", list(patient_vitamins.values()))
        print("\n")

        # check uncombined initial set for a match
        initial_diseases = dict(zip(names_list, values_list))
        current_match = check_match(initial_diseases, patient_vitamins)

        # while there is not a current match
        while current_match is None:

            # generate a new set of combinations
            combinations_dict = self.generate_combinations(values_list, names_list, list(initial_diseases.values()),
                                                           list(initial_diseases.keys()))
            print("\n")
            print("Loop Update")
            print("---------------")

            # update the working values
            values_list = list(combinations_dict.values())
            print("VLIST", *values_list, sep='\n')
            names_list = list(combinations_dict.keys())

            print(names_list)

            # check for a match in the generated combinations
            current_match = check_match(combinations_dict, patient_vitamins)
        print("MATCH FOUND")
        diagnosis = current_match.split(", ")
        return diagnosis

    def create_value_arrays(self, disease_dict):
        name_array = []
        value_array = []
        for name, vitamins in disease_dict.items():
            name_array.append(name)
            value_array.append(list(vitamins.values()))

        return name_array, value_array

    def generate_combinations(self, values_list, names_list, initial_values, initial_names):
        print("Generate Combinations")
        print("----------------------")
        values_combine = []
        names_combine = []

        # find value combinations
        # values_combine = combinations(values_list, 2)
        print("ivalues", *initial_values, sep='\n')
        for pair in product(values_list, initial_values):
            if pair[1] != pair[0]:
                values_combine.append(pair)
        # print(*values_combine, sep='\n')

        # get corresponding name combinations
        # names_combine = combinations(names_list, 2)

        for pair in product(names_list, initial_names):
            if pair[1] not in pair[0]:
                names_combine.append(pair)

        comb_dict = {}

        for name_pair in names_combine:
            index = names_combine.index(name_pair)
            comb_name = name_pair[0] + "," + name_pair[1]
            comb_dict[comb_name] = sum_values(values_combine[index][0], values_combine[index][1])

        # show generated combinations
        for key, value in comb_dict.items():
            print(key, value)

        return comb_dict
