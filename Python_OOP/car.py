class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = .12
        if price > 10000:
            self.tax = .15
        self.display_all()
    def display_all(self):
        print "Price:", str(self.price), "Speed:", self.speed, "Fuel:", self.fuel, "Mileage:", self.mileage, "Tax:", str(self.tax)

car1 = car(2000, "35mph", "Full", "15mpg")
car2 = car(2000, "5mph", "Not Full", "105mpg")
car3 = car(2000, "15mph", "Kind of Full", "95mpg")
car4 = car(2000, "25mph", "Full", "25mpg")
car5 = car(2000, "45mph", "Empty", "25mpg")
car6 = car(20000000, "35mph", "Empty", "15mpg")
