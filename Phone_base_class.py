class Phone:
    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Name: {self.name}\nBrand: {self.brand}\nYear: {self.year}")


class Smartphone(Phone):
    def __init__(self, name, brand, year, os):
        super().__init__(name, brand, year)
        self.os = os

    def display_info(self):
        super().display_info()
        print(f"Operating System: {self.os}")


class BasicPhone(Phone):
    def __init__(self, name, brand, year, is_touch_screen):
        super().__init__(name, brand, year)
        self.is_touch_screen = is_touch_screen

    def display_info(self):
        super().display_info()
        print(f"Touch Screen: {'Yes' if self.is_touch_screen else 'No'}")


# Example usage:
iphone = Smartphone("iPhone 13", "Apple", 2021, "iOS")
nokia = BasicPhone("3310", "Nokia", 2000, False)
galaxy = Smartphone("Galaxy S23", "Samsung", 2023, "Android")
poco = Smartphone("Poco F5", "POCO", 2021, "Android")
motorola = BasicPhone("MOTO XT702", "Motorola", 2009, False)
ericsson = BasicPhone("Sony Ericsson W715", "Sony Ericsson", 2009, False)
nothing = Smartphone("Nothing Phone 2", "Nothing", 2023, "Android")
xiaomi = Smartphone("Xiaomi 14 Pro", "Xiaomi", 2023, "Android")
honor = Smartphone("Honor X9b", "Honor", 2023, "Android")


iphone.display_info()
print("\n")
nokia.display_info()
print("\n")
galaxy.display_info()
print("\n")
poco.display_info()
print("\n")
motorola.display_info()
print("\n")
ericsson.display_info()
print("\n")
nothing.display_info()
print("\n")
xiaomi.display_info()
print("\n")
honor.display_info()
