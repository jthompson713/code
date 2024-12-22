class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

bobs = Restaurant()
wing2go = Restaurant()
dennys = Restaurant()

dennys.name = 'Denny\'s'
dennys.category = 'Diner'
dennys.rating = 1.7
dennys.delivery = True

wing2go.name = 'Wings 2 Go'
wing2go.category = 'Chicken Wings'
wing2go.rating = 5.0
wing2go.delivery = True

bobs.name = 'Bob\'s Burgers'
bobs.category = 'American Diner'
bobs.rating = 4.7
bobs.delivery = False

print(vars(bobs))
print(vars(wing2go))
print(vars(dennys))