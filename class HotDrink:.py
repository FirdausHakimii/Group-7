#Muhammad Firdaus Hakimi
#A20MJ5014


class HotDrink:
    def __init__(self, name, temperature, color):
        self.name = name
        self.temperature = temperature
        self.color = color

    def describe(self):
        return f"{self.name} - Temperature: {self.temperature}°C, Color: {self.color}"

class Coffee(HotDrink):
    def __init__(self, coffee_type, temperature, color):
        super().__init__("Coffee", temperature, color)
        self.coffee_type = coffee_type

    def describe(self):
        return super().describe() + f", Coffee Type: {self.coffee_type}"

class Tea(HotDrink):
    def __init__(self, tea_type, temperature, color):
        super().__init__("Tea", temperature, color)
        self.tea_type = tea_type

    def describe(self):
        return super().describe() + f", Tea Type: {self.tea_type}"

class HotChocolate(HotDrink):
    def __init__(self, chocolate_type, temperature, color):
        super().__init__("Hot Chocolate", temperature, color)
        self.chocolate_type = chocolate_type

    def describe(self):
        return super().describe() + f", Chocolate Type: {self.chocolate_type}"

coffee = Coffee(coffee_type="Espresso", temperature=75, color="Dark Brown")
tea = Tea(tea_type="Green Tea", temperature=80, color="Light Green")
hot_chocolate = HotChocolate(chocolate_type="Dark Chocolate", temperature=60, color="Brown")

drinks = [coffee, tea, hot_chocolate]
for drink in drinks:
    print(drink.describe())
