# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
# def main():
#     class Hero:
#         def __init__(self,health,power):
#             self.health=health
#             self.power=power
#         def __str__(self):
#             return 'Health:{} Power:{}'.format(self.health,self.power)    
#         # Hero attacks    
#         def attack(self,enemy):
#             enemy.health -= self.power
#             print("You do {} damage to the {}.".format(self.power,enemy))
#             if enemy.health <= 0:
#                 print("The {} is dead.".format(enemy))
#         def allive(self):
#             if self.health > 0:
#               return True 

#     class Goblin:
#         def __init__(self,health,power):
#            self.health=health
#            self.power=power
#         def  attack(enemy):
#            hero_health -= goblin_power
#            print("The goblin does {} damage to you.".format(goblin_power))
#            if hero_health <= 0:
#               print("You are dead.")

#         def allive(self):
#             if self.health > 0:
#               return True
            
#         def __str__(self):
#             return 'Health:{} Power:{}'.format(self.health,self.power)
#         while  sobha.allive() and John.alive():
#                 print("You have {} health and {} power.".format(sobha.health, sobha.power))
#                 print("The goblin has {} health and {} power.".format(John.health, John.power))
#                 print()
#                 print("What do you want to do?")
#                 print("1. fight goblin")
#                 print("2. do nothing")
#                 print("3. flee")
#                 print("> ",end=' ')
#                 raw_input = input()
#                 if raw_input == "1":
#                     # Hero attacks goblin
#                     goblin_health -= hero_power
#                     print("You do {} damage to the goblin.".format(hero_power))
#                     if goblin_health <= 0:
#                         print("The goblin is dead.")
#                 elif raw_input == "2":
#                     pass
#                 elif raw_input == "3":
#                     print("Goodbye.")
#                     break
#                 else:
#                     print("Invalid input {}".format(raw_input))
                
    
#     main()
#     sobha=Hero(20,5)
#     John=Goblin(10,2)
#     print(sobha)
#     print(sobha.health)
#     print(John)
#     sobha.allive()


def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    while goblin_health > 0 and hero_health > 0:
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin_health -= hero_power
            print("You do {} damage to the goblin.".format(self.power))
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")

main()

