print("((Disclamer)This Is A Game Chose What You Want)")
print()
print()
print(
  "If The Story ever stops press enter to continue! or we will ask like this:")
input("Press Enter To Continue")
print("ETERNITY THE GAME")
print("Depending On What You Choose The Entire Storyline Will Change")
print()
input("Press Enter To Continue")
GoodEvil = input("Are You Good Or Evil? ")
print("")
if GoodEvil == "Good":
  print("What Religon Are You?")
  print()
  print("A. Christan")
  print()
  print("B. Norse")
  print()
  print("C. Greek")
  print()
  print("D. Muslim")
  print()
  print("E. Roman")
  print()
  gamestart = input("Which One? (A,B,C,D,E) ")
  if gamestart == "A":
    import Heaven
  elif gamestart == "B":
    import Vahalla
  elif gamestart == "C":
    import Elysium
  elif gamestart == "D":
    import Jannah
  elif gamestart == "E":
    import Elysian

elif GoodEvil == "Evil":
  print("What Religon Are You?")
  print()
  print("A. Christan")
  print()
  print("B. Norse")
  print()
  print("C. Greek")
  print()
  print("D. Muslim")
  print()
  print("E. Roman")
  print()

  gamestart = input("Which One? (A,B,C,D,E) ")
  if gamestart == "A":
    import Hell
  elif gamestart == "B":
    import HellHeim
  elif gamestart == "C":
    import Underworld
  elif gamestart == "D":
    import Jahannam
  elif gamestart == "E":
    import Underworld
