menu = ['null', 'Cheeseburger', 'Fries', 'Soda', 'Ice Cream', 'Cookie']

price_cb = 5.47
price_f = 1.32
price_soda = 2.54
price_ic = 1.99
price_c = .99

def welcome():
  print("""Thank you for choosing McDonald's! Please choose
from our folliwing menu items.
           1.) Cheeseburger
           2.) Fries
           3.) Soda
           4.) Ice Cream
           5.) Cookie
  """)

welcome()

def get_item():
  item_1 = int(input('Enter the number you would like to order: '))
  print('You have added ', menu[item_1], 'to the cart.')

get_item()



