status_of_making_coffee = ['Starting to make a coffee',
                 'Grinding coffee beans',
                 'Boiling water',
                 'Mixing boiled water with crushed coffee beans',
                 'Pouring coffee into the cup',
                 'Pouring some milk into the cup',
                 'Coffee is ready!']

one_cup_composition = {'water': (200, 'ml'),
                       'milk': (50, 'ml'),
                       'coffee beans': (15, 'g')}

cups_amount = int(input('Write how many cups of coffee you will need:\n'))
print('For 25 cups of coffee you will need:')
for key, value in one_cup_composition.items():
    print(value[0] * cups_amount, value[1], 'of', key)
