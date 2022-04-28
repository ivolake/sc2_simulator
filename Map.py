# TODO: current_state карты (обращается к координатам каждого юнита)
class Platform:
	def __init__(self, lvl, points):
		self.lvl = lvl
		self.list_of_points = points


# This is class Map is used like an API
class Map:
	def __init__(self, LOB, LOU, LOP):
		self.__objects = {'Units': LOU, 'Buildings': LOB}
		# Levels Of Platforms
		self.LvlOP = {plt.lvl: plt.list_of_points for plt in LOP}

	def add(self, unit):
		self.__objects['Units'].append(unit)

	def build(self, building):
		self.__objects['Buildings'].append(building)

	def delete(self, obj):
		try:
			ind = self.__objects['Units'].index(obj)
			self.__objects['Units'].pop(ind)
			return 'Unit was deleted.'
		except ValueError:
			try:
				ind = self.__objects['Buildings'].index(obj)
				self.__objects['Buildings'].pop(ind)
				return 'Building was deleted.'
			except ValueError:
				return 'Not found.'

	def get_pos(self, obj):
		try:
			ind = self.__objects['Units'].index(obj)
			return self.__objects['Units'][ind].pos
		except ValueError:
			try:
				ind = self.__objects['Buildings'].index(obj)
				return self.__objects['Buildings'][ind].pos
			except ValueError:
				return 'Not found.'

	# Дает юниту понять, продолжать путь по прежнему пути или нет, который вернул метод find_way
	def keep_way(self)->bool:
		return True

	# Проблема видимости игроками строений
	def find_way(self, obj, point):
		list_of_points = []

		tuple_of_points = tuple(list_of_points)
		return tuple_of_points