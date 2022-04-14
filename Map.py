# This is class Map is used for storing info about all objects in match except players
class Map:
	def __init__(self):
		self.__objects = {'Units': [], 'Buildings': []}
		# Levels Of Platforms
		self.lop = {0: [], 1: [], 2: [], 3: []}

	def add(self, obj):
		# Пока так, но я что-то поменял для коммита
		self.__objects['Units'].append(obj)
