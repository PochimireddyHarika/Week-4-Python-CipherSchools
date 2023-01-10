class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def phone_name(self):
        return f"{self.brand} {self.modelname}"
    def __str__(self):
        return f'{self.brand} {self.model} and price is {self.price}'

    def __rep__(self):
        return f'Phone({self.brand},{self.price}, {self.price})'
    def __len__(self):
        return len(self.phone_name())
    def __add__(self,other):
        return self.price + other.price
    def __mul__(self,other):
        return self.price * other.price

my_phone = Phone('nokia', '1100', 1000)
my_phone2 = Phone('nokia', '1600', 1200)
print(my_phone +  my_phone2)
print(my_phone * my_phone2)
print(my_phone.__repr__())
print(len(my_phone))


class SmartPhone(Phone):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)
        self.camera = camera
    def phone_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    def __len__(self):
        return self.price

my_smartPhone = SmartPhone('oneplus', '5t',33000,'16MP')
print(my_smartphone.phone_name())
print(my_phone.phone_name())
print(len(my_smartphone))
print(len(my_phone))


l = [1,2,3]
print(len(l))
t = (1,2,3)
s = "harika"
print(len(t))
print(len(s))