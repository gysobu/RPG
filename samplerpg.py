def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2
    class charecter:
        def __init__(self,health,power):
            self.health=health
            self.power=power
            print('character class' + str(self.health))
        def __str__(self):
            return "Health:{} power:{}".format(self.health,self.power)
        
        def alive(self):
            if self.health >0:
                return True 
        

    class Hero(charecter):
        def print_status(self):
            print("You have {} health and {} power.".format(self.health, self.power)) 
        def attack(self,enemy):
            enemy.health -= self.power
            print("You do {} damage to the goblin.".format(self.power))
            if enemy.health <= 0:
                print("The goblin is dead.")
    class Goblin(charecter):  
        def print_status(self):
            print("The goblin has {} health and {} power.".format(self.health, self.power))
        def attack(self,enemy):
            enemy.health -= self.power
            print("The goblin does {} damage to you.".format(self.power))
            if enemy.health <= 0:
                print("You are dead.")
    sobha=Hero(10,5)
    john=Goblin(6,2)
    while sobha.alive() and john.alive():
        sobha.print_status()
        john.print_status()
        
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            sobha.attack(john)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if john.health > 0:
            # Goblin attacks hero
           john.attack(sobha)
main()


