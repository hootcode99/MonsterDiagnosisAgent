from itertools import combinations, product
import numpy as np


# # print dictionary
# for k, v in diseases.items():
#     print(k, '->', v)

def generate_combinations(disease_combos, pair_count):
    combine_dict = {}
    print("LENGTH", pair_count)
    # print("Disease Combos")

    # print(*list(disease_combos), sep="\n")
    # for each combination in the set
    for item in disease_combos:

        # access the first two sets of values
        disease_a_name = item[0][0]
        disease_b_name = item[1][0]
        vitamins_a = item[0][1]
        vitamins_b = item[1][1]

        # sum the first two pairs
        sum_dict = {}
        combined_value = ''
        # for each vitamin-level pair in disease_A
        for vitamin, level in vitamins_a.items():
            # combination rules for positive vitamin
            if level == '+':
                if vitamins_b.get(vitamin) == '+':
                    combined_value = '+'
                elif vitamins_b.get(vitamin) == '0':
                    combined_value = '+'
                elif vitamins_b.get(vitamin) == '-':
                    combined_value = '0'
            # combination rules for neutral vitamins
            elif level == '0':
                if vitamins_b.get(vitamin) == '+':
                    combined_value = '+'
                elif vitamins_b.get(vitamin) == '0':
                    combined_value = '0'
                elif vitamins_b.get(vitamin) == '-':
                    combined_value = '-'
            # combination rules for negative vitamins
            elif level == '-':
                if vitamins_b.get(vitamin) == '+':
                    combined_value = '0'
                elif vitamins_b.get(vitamin) == '0':
                    combined_value = '0'
                elif vitamins_b.get(vitamin) == '-':
                    combined_value = '-'

            # store the summed dictionary values
            sum_dict[vitamin] = combined_value

            # add the sum dictionary as the value for the combination
            combine_dict.update({disease_a_name + "-" + disease_b_name: sum_dict})


    print("Combine Dict")
    print(*list(disease_combos), sep="\n")

    # if there were more than two pairs
    if pair_count > 2:
        # rebuild array

        # call this function recursively
        print("NEXT ROUND")
        generate_combinations(list(combine_dict.items()), pair_count - 1)

    # otherwise
    else:
        # return the results
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
        pass

    def solve(self, diseases, patient):

        # check with initial values
        diagnosis = check_match(diseases, patient)

        # increment the number of combinations
        combo_counter = 2

        # until a diagnosis is found
        while diagnosis is None:

            # arrange combinations
            disease_combos = combinations(list(diseases.items()), combo_counter)
            # print("DISEASE COMBOS")
            # print(*list(disease_combos), sep="\n")

            # perform combinations
            combine_dict = generate_combinations(disease_combos, combo_counter)

            # evaluate combinations
            diagnosis = check_match(combine_dict, patient)

            # move to next combo if the answer has not been found
            combo_counter += 1
            print("NEXT COMBO", combo_counter)

            # temporary stop
            if combo_counter == 4:
                break

        return diagnosis
