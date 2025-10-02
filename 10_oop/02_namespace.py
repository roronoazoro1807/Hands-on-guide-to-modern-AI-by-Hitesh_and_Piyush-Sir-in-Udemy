class Messi:
    origin = "Argentina"


print(Messi.origin)
print(type(Messi.origin))

Messi.is_goat = True
print(Messi.is_goat)
print(type(Messi.is_goat))

# Creating Objects from class Messi

la_masia_player = Messi()


# la_masia_player=Messi Messi() → calls the class constructor (__init__) and creates a new object (instance).

# la_masia_player will hold a Messi object.

print(la_masia_player.origin)
print(la_masia_player.is_goat)
