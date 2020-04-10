class CoffeeMachine:
    coffee_types = {'espresso': {'water': 250, 'coffee beans': 16, 'disposable cups': 1, 'money': -4},
                    'latte': {'water': 350, 'milk': 75, 'coffee beans': 20, 'disposable cups': 1, 'money': -7},
                    'cappuccino': {'water': 200, 'milk': 100, 'coffee beans': 12, 'disposable cups': 1, 'money': -6}}

    def __init__(self, water, milk, c_beans, d_cups, money):
        self.supply = {'water': water,
                       'milk': milk,
                       'coffee beans': c_beans,
                       'disposable cups': d_cups,
                       'money': money}

    def user_input(self):
        return input()

    def menu(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            action = self.user_input()
            print()
            if action == 'remaining':
                self.remaining()
            elif action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'exit':
                break
            else:
                print('Unknown action.')
            print()

    def remaining(self):
        print('The coffee machine has:')
        for key, value in self.supply.items():
            print(('$' if key == 'money' else '') + f'{value} of {key}')

    def buy(self):
        check_supply = True
        number_of_coffee_type = {'1': 'espresso', '2': 'latte', '3': 'cappuccino'}

        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee_type = self.user_input()
        if coffee_type == 'back':
            return

        coffee_type = number_of_coffee_type[coffee_type]

        for key, value in CoffeeMachine.coffee_types[coffee_type].items():
            if self.supply[key] - value < 0:
                print(f'Sorry, not enough {key}!')
                check_supply = False
                break

        if check_supply:
            for key, value in CoffeeMachine.coffee_types[coffee_type].items():
                self.supply[key] -= value
            print('I have enough resources, making you a coffee!')

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.supply['water'] += int(self.user_input())
        print('Write how many ml of milk do you want to add:')
        self.supply['milk'] += int(self.user_input())
        print('Write how many grams of coffee beans do you want to add:')
        self.supply['coffee beans'] += int(self.user_input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.supply['disposable cups'] += int(self.user_input())

    def take(self):
        print(f"I gave you ${self.supply['money']}")
        self.supply['money'] = 0


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.menu()
