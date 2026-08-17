from functions import *
import time

enemy_health = enemy_health()
enemy_atk = enemy_atk()
enemy_def = enemy_def()

mc_health = int(input("What is your health (1-20): "))
mc_atk = int(input("What is your attack power (1-10)"))
mc_def = int(input("What is your defense (1-10): "))

time.sleep(1)

print(f"This is the enemies health: {enemy_health}.")
print(f"This is the enemies attack power: {enemy_atk}.")
print(f"This is the enemies defense: {enemy_def}.")

time.sleep(5)

print("The battle starts.\n")

while mc_health > 0 and enemy_health > 0:
    mc_attack = mc_atk - enemy_def
    if mc_attack < 0:
        mc_attack == 0
        mc_atk += 1
        
    enemy_health -= mc_attack
    print(f"You attacked by {mc_attack} and the enemies health is now {enemy_health}.")
    