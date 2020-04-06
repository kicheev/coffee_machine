def min_cups_from_supplies(dict):
    min_cups = dict['water']['supply remaining'] // dict['water']['one cup']
    current_cups = 0
    for value in dict.values():
        current_cups = value['supply remaining'] // value['one cup']
        if current_cups < min_cups:
            min_cups = current_cups
    return min_cups


def check_cups(user_need_cups, cups_remaining):
    if user_need_cups == cups_remaining:
        print('Yes, I can make that amount of coffee')
    elif user_need_cups < cups_remaining:
        print(f'Yes, I can make that amount of coffee (and even {cups_remaining - user_need_cups} more than that)')
    else:
        print(f'No, I can make only {cups_remaining} cups of coffee')


status_of_making_coffee = ['Starting to make a coffee',
                 'Grinding coffee beans',
                 'Boiling water',
                 'Mixing boiled water with crushed coffee beans',
                 'Pouring coffee into the cup',
                 'Pouring some milk into the cup',
                 'Coffee is ready!']

# one_cup_composition = {'water': [200, 'ml'],
#                        'milk': [50, 'ml'],
#                        'coffee beans': [15, 'grams']}

supplies = {'water': {'unit': 'ml', 'one cup': 200, 'supply remaining': 0},
            'milk': {'unit': 'ml', 'one cup': 50, 'supply remaining': 0},
            'coffee beans': {'unit': 'grams', 'one cup': 15, 'supply remaining': 0}}

for key, value in supplies.items():
    supplies[key]['supply remaining'] = int(input(f"Write how many {value['unit']} of {key} the coffee machine has:\n"))

user_need_cups = int(input('Write how many cups of coffee you will need:\n'))

check_cups(user_need_cups, min_cups_from_supplies(supplies))




