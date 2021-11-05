# 1. Match - сущность, объединяющая игроков (Player) и карту (Map).
# Поля игроков (player1, player2) и карты (map)- свойства класса.
# Матч может начинаться (start), проистекать (proceed) и заканчиваться (end).
# TODO: прописать сигнатуры всех методов и объявления полей
# TODO: аннотировать все объекты в проекте
# TODO: документация в форматие numpy
#  1) найти в пучурме настройку формата документации для питона (по умолчанию нампай)
#  2) задокументировать все объекты в проекте




class Map:
    def __init__(self, name):
        self.name = name

    def __repr__(self):  # сигнатура метода класса мап
        return self.name


class Player:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Match:
    def __init__(self, map_obj: Map):
        self.map = map_obj

    def __repr__(self) -> str:
        return f"Match(map={repr(self.map)})"

