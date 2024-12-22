class Pokemon():
    def __init__(self, entry, name, types, description, is_caught):
      self.entry = entry
      self.name = name
      self.types = types
      self.description = description
      self.is_caught = is_caught
    def speak(self):
      print(self.name)
      print(self.name)
    def display_details(self):
      print('Entry Number: ', self.entry)
      print('Name: ', self.name)
      print('Type: ', self.types)
      print('Description: ', self.description)
      if self.is_caught == True:
        print(self.name ,'has already been caught!')
      else:
        print(self.name ,'has not been caught.')

      

pikachu = Pokemon('#025', 'Pikachu', 'Electric', 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', 'True')
pidgy = Pokemon('#016', 'Pidgy', 'Flying', 'Pidgey is a small, plump-bodied avian Pokémon. It is primarily brown with a cream-colored face, underside, and flight feathers.', 'False')
squirtle = Pokemon('#007', 'Squirtle', 'Water', 'Squirtle is a small, light-blue Pokémon with an appearance similar to a turtle. ', 'False')

pidgy.speak()
pidgy.display_details()