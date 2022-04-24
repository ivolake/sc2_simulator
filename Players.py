# TODO: сделать СИСТЕМУ ПРИКАЗОВ
#  добавить панель приказов(координаты move),
# 3.1. send_unit_cmd - функция, описывающее доставку до юнита определенной команды. Оперирует объектами класса Unit и их полями current_command.
# 3.2 send_unit_move, send_unit_attack - подвиды функции отправки команды, отправляющие конкретные команды юниту.


class Player:
    """
    Нужен для связи пользователей с юнитами
    """
    def __init__(self, name: str):
        """
        Определение ника игрока
        """
        self.player_name = self.verify_nickname(name)

    def verify_nickname(self, nick: str):
        """
        Проверка ника
        """
        banlist_of_letters = ["\\", ":"]
        if len(nick) > 15:
            print(f"Слишком длинный ник, замена на {nick[:15]}.")
            nick = nick[:15]

        for letter in banlist_of_letters:
            if letter in nick:
                raise ValueError(f"Запрещённые символы в нике: '{letter}'.")

        return nick


class Command:
    """
    Класс команд, все команды прописаны здесь
    """
    list_of_commands = [
        "move",  # бежать к точке(юниту)
        "attack",  # бежать к точке(юниту) с атакой
        "idle",  # стоять (когда нет приказов)
        "hold",  # не сдвигаться с места
        "patrol",  # ряд attack по нескольким точкам
        "ability"  # использовать способность
    ]

    def __init__(self, unit_type: object):
        """
        Определяем тип юнита и его способности
        """
        pass
