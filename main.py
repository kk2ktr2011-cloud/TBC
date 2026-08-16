from functions import *

enemy_health = enemy_health()

mc_health = int(input("What is your health (1-20): "))
mc_atk = int(input("What is your attack power (1-10)"))
mc_def = int(input("What is your defense (1-10): "))

print(f"This is the enemies health: {enemy_health}")