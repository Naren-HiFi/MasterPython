################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# # Local Scope
def drink_potion():
     potion_strength = 2
     print(potion_strength)

drink_potion()
#print(potion_strength)

# Global Scope
player_health = 10

def game():
 def drink_wine():
     potion_strength = 4
     print(potion_strength)
 drink_wine()

game()
print(player_health)

#  There is no block scope in python

game_level = 3
def create_enemy():
    arch_rivals_list = ["Zombie","Alien","Skeletons"]
    if game_level < 6:
        new_enemy = arch_rivals_list[1]
    print(new_enemy)

create_enemy()

# Modifying global scope

anemies = 7

def increase_anemies():
    global anemies
    anemies += 1
    print(f"anemyes inside function: {anemies}")

increase_anemies()
print(f"anemyes outside function: {anemies}")

# Without modifying global scope

no_Of_memes = 90

def increase_memes():
  print(f"memes inside function: {no_Of_memes}")
  return no_Of_memes + 10

memes = increase_memes()
print(f"memes outside function: {memes}")

# Global Constants
PI = 3.14159
URL = "https://www.facebook.com"
TWITTER_HANDLE = "@yu_angela"

def call_global_consatants():
    print(URL)
    print(TWITTER_HANDLE)
    print(PI)

call_global_consatants()

i = 50


def foo():
    i = 100
    return i


foo()
print(i)