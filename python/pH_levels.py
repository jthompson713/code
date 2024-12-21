user_pH = float(input("Enter a pH to test: "))
if user_pH > 7:
  print("Basic")
elif user_pH < 7 :
  print("Acidic")
else:
  print("Neutral")