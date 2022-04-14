#SC 2 classes
from random import randint

class Ground_Units:
    def __init__(self, hp):
        self.health_points = hp
    def recieve_damage(self, dp):
        self.health_points -= dp
    def show_hp (self):
        print("хп отсалось:", self.health_points)
    pass

class marines(Ground_Units):
    def say_something (self):
        texts = ["Кто на новенького?", "Кому навешать?", "В бой!"]
        print(texts[randint(0,2)])
    pass

class tanks(Ground_Units):
    pass

marine1 = marines(100)
marine1.show_hp()
marine1.recieve_damage(10)
marine1.show_hp()
marine1.say_something()