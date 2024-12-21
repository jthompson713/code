Hufflepuff = 0
Slytherin = 0
Ravenclaw = 0
Gryffindor = 0

answer = int(input("Q1)Do you like Dawn or Dusk?\n 1) Dawn\n 2) Dusk\n\n"))
if answer == 1:
  Gryffindor+= 1  
  Ravenclaw += 1
elif answer == 2:
  Hufflepuff += 1  
  Slytherin += 1
else:
  print("Wrong Input.")


answer2 = int(input("\nQ2)When I'm dead, I want people to remember me as:\n 1.) The Good\n 2.) The Great\n 3.) The Wise\n 4.) The Bold\n\n"))
if answer2 == 1:
  Hufflepuff += 2
elif answer2 == 2:
  Slytherin += 2
elif answer2 == 3:
  Ravenclaw += 2
elif answer2 == 4:
  Gryffindor += 2
else:
  print("Wrong Input.")

answer3 = int(input("\nQ3)Which kind of instrument most pleases your ear?\n 1.) The violin\n 2.) The trumpet\n 3.) The piano\n 4.) The drum\n\n"))
if answer3 == 1:
  Slytherin += 4
elif answer3 == 2:
  Hufflepuff += 4
elif answer3 == 3:
  Ravenclaw += 4
elif answer3 == 4:
  Gryffindor += 4
else:
  print("Wrong Input.")

print("\nGryffindor: ")
print(Gryffindor)
print("Slytherin: ")
print(Slytherin)
print("Hufflepuff: ")
print(Hufflepuff)
print("Ravenclaw: ")
print(Ravenclaw)

if Gryffindor > max(Slytherin, Hufflepuff, Ravenclaw):
  print("\nYour house is Gryffindor.")
elif Slytherin > max(Gryffindor, Hufflepuff, Ravenclaw):
  print("\nYour house is Slytheirn.")
elif Hufflepuff > max(Gryffindor, Slytherin, Ravenclaw):
  print("\nYour house is Hufflepuff.")
else:
  print("\nYour house is Ravenclaw.")