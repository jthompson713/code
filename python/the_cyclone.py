height = int(input("Enter your height in cm: "))
credits = int(input("Enter the amount of credits you have: "))

if height > 137 and credits > 10:
  print("Enjoy the ride!")
elif height < 137:
  print("You are not tall enought to ride.")
elif credits < 10:
  print("You don't have enough credits")
else:
  print("You have not met either requirment to ride the ride.")