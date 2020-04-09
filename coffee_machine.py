def menu():
    while True:
        action = input('Write action (buy, fill, take, remaining, exit):\n')
        print()
        if action == 'remaining':
            remaining(supply)
        elif action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        else:
            print('Unknown action.')
        print()


def buy():
    global supply
    global coffee_types
    check_supply = True

    coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
    if coffee_type == 'back':
        return

    coffee_type = int(coffee_type)

    for key, value in coffee_types[coffee_type].items():
        if supply[key] - value < 0:
            print(f'Sorry, not enough {key}!')
            check_supply = False
            break

    if check_supply:
        for key, value in coffee_types[coffee_type].items():
            supply[key] -= value
        print('I have enough resources, making you a coffee!')


def fill():
    global supply

    supply['water'] += int(input('Write how many ml of water do you want to add:\n'))
    supply['milk'] += int(input('Write how many ml of milk do you want to add:\n'))
    supply['coffee beans'] += int(input('Write how many grams of coffee beans do you want to add:\n'))
    supply['disposable cups'] += int(input('Write how many disposable cups of coffee do you want to add:\n'))


def take():
    global supply

    print(f"I gave you ${supply['money']}")
    supply['money'] = 0


def remaining(supply):
    print('The coffee machine has:')
    for key, value in supply.items():
        print(('$' if key == 'money' else '') + f'{value} of {key}')


supply = {'water': 400,
          'milk': 540,
          'coffee beans': 120,
          'disposable cups': 9,
          'money': 550}

coffee_types = {1: {'water': 250, 'coffee beans': 16, 'disposable cups': 1, 'money': -4},
                2: {'water': 350, 'milk': 75, 'coffee beans': 20, 'disposable cups': 1, 'money': -7},
                3: {'water': 200, 'milk': 100, 'coffee beans': 12, 'disposable cups': 1, 'money': -6}}

menu()




