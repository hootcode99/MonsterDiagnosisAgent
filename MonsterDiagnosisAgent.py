
from itertools import combinations


def check_match(combine_array, patient):
    solution = ''
    for item in combine_array:
        vitamin_list = item[1]
        # print(item[0], vitamin_list)

        # print("Patient", patient)
        if patient == vitamin_list:
            print("------------MATCH FOUND--------------")
            solution = item[0].split('-')
            return solution

    return None


def combine(tuple1, tuple2) -> tuple:
    """
    Combine 2 tuples
    Ex. ('x', 0), ('y', 1) -> ('xy', 1)
    """
    element1 = tuple1[0] + "-" + tuple2[0]
    sum_dict = {}
    vitamins_a = tuple1[1]
    vitamins_b = tuple2[1]
    for vitamin, level in vitamins_a.items():
        # print(vitamin, level)
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
                combined_value = '-'
            elif vitamins_b.get(vitamin) == '-':
                combined_value = '-'

        # store the summed dictionary values
        sum_dict[vitamin] = combined_value

    element2 = sum_dict
    return element1, element2


def simplify_tuple(bag: tuple):
    """
    Simplify a tuple of tuples (a bag) into eventually 1 tuple
    Ex. [(('x', 0), ('y', 1), ('z', 2)), (('a', 3), ('b', 4), ('c', 5))]
    -> [(('xy', 1), ('z', 2)), (('ab', 7), ('c', 5))]
    -> [('xyz', 3), ('abc', 12)].
    """
    combine_array = []
    output_array= []
    # Simplest case: Only 1 tuple in each tuple
    for stuff in bag:
        # For each tuple in the bag, combine the first two nested tuples recursively
        while len(stuff) != 1:
            if len(stuff) > 2:
                # print("Before combo ", stuff)
                # slice list to recombine
                sliced = tuple(stuff[2:])  # everything after index 2
                # print("Sliced stuff ", sliced)

                new_tuple = combine(stuff[0], stuff[1]) # Now combine first two elements

                temp = [new_tuple]  # turn tuple into list so we can use clear func
                # add each tuple in sliced tuple to the list
                for single in sliced:
                    temp.append(single)
                stuff = tuple(temp)  # turn back into a tuple

                # print("After combo ", stuff)

            else:
                # print("Before combo ", stuff)
                new_tuple = combine(stuff[0], stuff[1])

                temp = [new_tuple]  # turn tuple into list so we can use clear func
                stuff = tuple(temp)  # turn back into a tuple

                # print("After combo ", stuff)
                combine_array.append(stuff)

    for item in combine_array:
        for line in item:
            output_array.append(line)

    return output_array


class MonsterDiagnosisAgent:
    def __init__(self):
        pass

    def solve(self, diseases, patient):
        # print("PATIENT", patient)
        # check with initial values
        diagnosis = check_match(list(diseases.items()), patient)

        # increment the number of combinations
        combo_counter = 2

        # until a diagnosis is found
        while diagnosis is None:
            # print("PAIR", combo_counter)
            # arrange combinations
            disease_combos = combinations(list(diseases.items()), combo_counter)

            # perform combinations
            combine_array = simplify_tuple(list(disease_combos))

            # evaluate combinations
            diagnosis = check_match(combine_array, patient)

            # move to next combo if the answer has not been found
            combo_counter += 1

            if combo_counter == 8:
                break

        if diagnosis is None:
            diagnosis = []

        return diagnosis
