# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

class Airplane():
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        message_take = f'{self.make} {self.model} is take off'
        return message_take
    
    def fly_up(self):
        if self.odometer < 30:
            self.odometer = self.odometer + 15
        message_fly = f'{self.make}  is flying on speed {self.odometer}'
        return message_fly
    
    def fly_down(self):
        if self.odometer > 0:
            self.odometer = self.odometer - 15
        else:
            pass
        message_fly = f'{self.make}  is flying on speed {self.odometer}'
        return message_fly 

    def land(self):
        self.is_flying = False
        message_land = f'{self.make} is stopped'
        return message_land


    def description(self):
        return f'{self.make}, {self.model}, {self.year} , {self.max_speed}'

airbus = Airplane('Boeing', '747', '2017', 1200)
print(airbus.description())
print(airbus.take_off())
print(airbus.fly_up())
print(airbus.fly_up())
print(airbus.fly_up())
print(airbus.fly_down())
print(airbus.fly_down())
print(airbus.fly_down())
print(airbus.land())
