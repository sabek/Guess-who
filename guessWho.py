from people import HiddenPeople

peoplelist = HiddenPeople()
guesslist = HiddenPeople()

guess = input("Please choose an attribute: ")
print("------")
peoplelist.removeperson(guess)

peoplelist.printpeople()
