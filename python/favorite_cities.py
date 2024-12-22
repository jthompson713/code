class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

vacaville = City('Vacaville', 'USA', 1200345, 'Nut Tree, Pena Adobe, Lagoon Valley')

print(vars(vacaville))