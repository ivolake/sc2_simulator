from random import randint, random


class Condition:
    def __init__(self):
        pass

    def check(self):
        return randint(0, 1)


class Unit:
    def __init__(self):
        pass


class Command:
    def __init__(self):
        self.name = f"command{int(random()*100)}"
        self.id = 0

    def __repr__(self):
        print("command executed")

    def execute(self):
        print(f"command {self.name} executed")


class CommandBuffer:
    def __init__(self):
        self.cond1 = Condition()
        self.cond2 = Condition()
        self.cond3 = Condition()
        self.Queue = {}

    def add_command(self, *, unit, name: Command, id=0):
        name.id = id
        self.Queue.update({unit: name})


class UnitsContainer:
    def __init__(self):
        self.Container = []

    def add_unit(self, unit):
        self.Container.append(unit)


MyBuffer = CommandBuffer()

unit1 = Unit()
unit2 = Unit()
unit3 = Unit()

container = UnitsContainer()

container.add_unit(unit1)
container.add_unit(unit2)
container.add_unit(unit3)




#def Iteration(buffer, Container):
 #   for command in buffer.Queue.keys:


