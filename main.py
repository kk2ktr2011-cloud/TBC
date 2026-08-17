from functions import *

enemy_health = enemy_health()
enemy_atk = enemy_atk()
enemy_def = enemy_def()

mc_health = int(input("What is your health (1-20): "))
mc_atk = int(input("What is your attack power (1-10)"))
mc_def = int(input("What is your defense (1-10): "))

print(f"This is the enemies health: {enemy_health}.")
print(f"This is the enemies attack power: {enemy_atk}.")
print(f"This is the enemies defense: {enemy_def}.")