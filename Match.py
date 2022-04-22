# TODO: Создать методы : "start"(Начало матча) - создание карты, как объекта Map и стартовых изменяющихся объектов
#  с их начальными параметрами;
#  "End"(Завершение матча) - ;
#  Связать систему приказов, юнитов и здания
#  Модель симуляции в Match.proceed - итерация по всем изменяющимся объектам на карте.
#  Для таких объектов создать класс Object (BasicObject, ...) от которого будут наследоваться все остальные
#  изменяющиеся объекты на карте: Unit, Building, Destroyable.
#  Изменяться они будут посредством накопленных в буффере в течение предыдущих итераций команд.

from sc2_simulator import Players


class ObjectBase:
    __hitPoints: int

    @property
    def HitPoints(self) -> int:
        return self.__hitPoints




class Match:
    __frequency: int
    Player_1 = Players.Player()
    Player_2 = Players.Player()

    def gameIteration(self):
        #цикл для перебора всех команд очереди, а также обновления состояния соответствующих объектов, задействованных в итерации
        pass


    def __init__(self):
        print("So, it begins")

    def refresh(self):
#Должны быть обновлены свойства юнитов в соответствии со стеком команд за данную итерацию
        pass

    def start(self):
        #Все стартовые свойства должны быть установлены на соответствующии значения
        #Все стартовые объекты с обоих сторон должны быть сгенерированы
        pass

    def proceed(self):
        Match.game_Iteration()

        pass

    def end(self):
        #условие завершения матча
        pass
