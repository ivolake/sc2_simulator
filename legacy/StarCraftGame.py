

#unit editor
class Unit(Player):
    def __init__(self, hp):
        self.health_points = hp
    def __init__(self, armor):
        self.armor_points = armor
    def recieve_damage(self, dp):
        self.health_points -= dp
    def Grade_List(self):
        pass
    pass

class Grades():
    def list_of_grades(self):
        list_of_grades = []
    pass



