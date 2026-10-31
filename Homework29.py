class carbrands:

    #Class Attributes
    Cars = "Luxury car brands"

    #Instance attribute
    def __init(self, brand, fuel, max_speed):
        self.brand = brand
        self.fuel = fuel
        self.max_speed = max_speed

#Instantaniate the carbrand class
BMW = carbrands("BMW", 300, 150)
Ferrari = carbrands("Ferrari", 200, 300)

#Access the class attributes
print("BMW is a {}:".format(BMW.Cars))
print("Ferrari is a {}:".format(Ferrari.Cars))

#Access the instance attributes
print("{} are {} with {} of range and {} of speed.".format(BMW.brand, BMW.fuel, BMW.max_speed))
print("{} are {} with {} of range and {} of speed.".format(Ferrari.brand, Ferrari.fuel, Ferrari.max_speed))