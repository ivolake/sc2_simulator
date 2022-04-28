# TODO: сделать СИСТЕМУ ПРИКАЗОВ
#  добавить панель приказов(координаты move),
#  перенести список комманд в docs
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
        if set(nick) == {' '} or nick == "":
            raise ValueError("Ник не может быть пустым.")

        nick = nick.split()
        nick = " ".join(nick) #убирает много пробелов

        if len(nick) > 15:
            if nick[14] == " ": #проверка на последний пробел в нике
                print(f"Слишком длинный ник, замена на {nick[:14]}.")
                nick = nick[:14]
            else:
                print(f"Слишком длинный ник, замена на {nick[:15]}.")
                nick = nick[:15]

        banlist_of_letters = r"\/,{}:;`~"
        banlist_of_letters = set(banlist_of_letters)
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

    def __init__(self,
                 command_type: str,
                 unit_type: object
                 ):
        """
        Определяем тип юнита и его способности
        """
        self.command_type = command_type
        self.unit_type = unit_type

    # def set_params(self):
    #     pass

    def run(self, **kwargs):
        if self.command_type == "move":
            return self.__move(**kwargs)
        elif self.command_type == "":
            pass
        else:
            print("try another command...")

    def move(self,
             x: int,
             y: int
             ):
        #while x y юнита не= заданным, то примитив движения в нужную сторону
        pass


class PrimitiveCommand:

    def __init__(self,
                 command_type: str,
                 unit_type: object
                 ):
        """
        Определяем тип юнита и его способности
        """
        self.command_type = command_type
        self.unit_type = unit_type
        if command_type == "move":
            pass

    # def set_params(self):
    #     pass

    def run(self, **kwargs):
        if self.command_type == "move":
            return self.__move(**kwargs)
        elif self.command_type == "":
            pass
        else:
            print("try another command...")

    def move(self,
             x: int,
             y: int
             ):
        # while x y юнита не= заданным, то примитив движения в нужную сторону
        pass
