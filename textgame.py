import random

def attack(enemy_health):
    damage = random.randint(5, 15)
    enemy_health -= damage
    print(f"You attacked the enemy for {damage} damage.")
    return enemy_health

def defend():
    print("You chose to defend. Damage will be reduced next turn.")
    return True

def heal(player_health):
    heal_amount = random.randint(8, 12)
    player_health += heal_amount
    print(f"You healed yourself for {heal_amount} health.")
    return player_health

def enemy_attack(player_health, is_defending):
    damage = random.randint(5, 15)
    if is_defending:
        damage //= 2  
    player_health -= damage
    print(f"The enemy attacked you for {damage} damage.")
    return player_health

def game():
    player_health = 100
    enemy_health = 100
    is_defending = False

    while player_health > 0 and enemy_health > 0:
        print(f"\nPlayer Health: {player_health}, Enemy Health: {enemy_health}")
        choice = input("Choose your action: Attack (a), Defend (d), Heal (h): ").lower()

        if choice == 'a':
            enemy_health = attack(enemy_health)
            is_defending = False
        elif choice == 'd':
            is_defending = defend()
        elif choice == 'h':
            player_health = heal(player_health)
            is_defending = False
        else:
            print("Invalid choice.")
            is_defending = False

        if enemy_health <= 0:
            print("Congratulations! You've defeated the enemy.")
            break

        player_health = enemy_attack(player_health, is_defending)

        if player_health <= 0:
            print("You were defeated by the enemy. Game over.")
            break

game()
