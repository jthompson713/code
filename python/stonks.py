stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

user_day = int(input('Enter which day(0 thru 19) to view the price: '))

def price_at(user_day):
  print('Stock prices on day',user_day,':', stock_prices[user_day])

price_at(user_day)

print('\n================================')

range_day1 = int(input('\nEnter day 1 of range(0 thru 19): '))
range_day2 = int(input('Enter day 2 of range(0 thru 19): '))

print('\n================================')

def max_price(range_day1, range_day2):
  print('\nThe maximum price from day', range_day1, 'to day', range_day2, 'is: ', max(stock_prices[range_day1 : range_day2]))

max_price(range_day1, range_day2)



def min_price(range_day1, range_day2):
  print('\nThe minimum price from day', range_day1, 'to day', range_day2, 'is: ', min(stock_prices[range_day1 : range_day2]))

min_price(range_day1, range_day2)