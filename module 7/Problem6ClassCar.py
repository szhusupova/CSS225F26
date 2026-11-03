# Sezimgul
# 2026-11-03
# Problem 6: Car class with extra attributes and methods
#
# Attribute vs method:
# An attribute is a variable inside a class that stores data about
# an object (for example self.model). A method is a function defined
# inside a class that performs an action, usually using the object's
# attributes (for example get_model()).


class car:
    def __init__(self, model, year, color, type, manufacturer):
        # Attributes: data stored for each car object
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    # Methods: actions that return the object's data
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return (self.model + ' ' + str(self.year) + ' ' + self.color
                + ' ' + self.type + ' ' + self.manufacturer)


car1 = car("Sports", 2012, "Blue", "Coupe", "Ford")
car2 = car("Sedan", 2020, "Black", "Sedan", "Toyota")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())
