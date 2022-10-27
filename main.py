import random
from cogs import *

login()
os.system("cls")
load_save()
fake_load()
if Player.alive != 1:
    print(f"{Player.name} has died. This character is inaccessible.")
    Player.health = 0
while Player.health > 0:
    os.system("cls")
    print("Forum Romanum - Roman Forum (Hub)\n [1] Explorare (Explore)\n [2] Shop (Shop)\n [3] View Stats"
          "\n [4] Gladiator (Gladiator)\n")
    move = int(input("$"))
    if move == 1:
        temp = random.randint(0, 2)
        loot = random.randint(Actions.exploreMoney[temp] + 3, Actions.exploreMoney[temp] + 5)
        print(f"{Actions.explore[temp]}{loot}$")
        Player.money += loot
        time.sleep(1.2)
        print(f"You now have {Player.money}$")
        # backup
        edit_txt("money.txt", Player.index, str(loot + Player.money))
    elif move == 2:
        print("Aaron Armoury\n Weapons\n  1. Tirones' Rusty Dagger\n  2. Veles' Old Spear\n  3.  Hastatus' Copper Blade"
              "\n  4. Princep's Gold Sword\n  5. Centurion's Platinum War Axe\n  6. Marcus Licinius Crassus' Fabled "
              "Hammer\n Armour\n  7. Agrimensor's Old Rags\n  8. Celeres' Ancient Bronze Plate\n  9. Decurion's Iron "
              "Armour\n  10. Primus Ordinis' Sturdy Gold Armour\n  11. Palatines Massive Platinum Plating"
              "\n  12. Julius Caesar's Mystical Robe (Some say its cursed, with the spirit of Caesar still in it)"
              "\n Enter index for price")
        buy = int(input("$"))
        print(f"Do you want to buy {Actions.shop[buy]} for {Actions.shopMoney[buy]}$? Y/N")
        final = str(input("$"))
        if final == "Y":
            if Player.money >= Actions.shopMoney[buy] and buy <= 6:
                Player.money -= Actions.shopMoney[buy]
                Player.weapon = Actions.shop[buy]
                Player.skillWeapon = Actions.shopMoney[buy]
                calculate_skill()
                print(f"Successfully purchased {Actions.shop[buy]} for {Actions.shopMoney[buy]}$! Gratulationes!"
                      f"\nYou have {Player.money}$ left.")
                os.system("cls")
                time.sleep(1.2)
                # backup
                edit_txt("money.txt", Player.index, str(Player.money))
                edit_txt("weapon.txt", Player.index, Actions.shop[buy])
                edit_txt("skillWeapon.txt", Player.index, Actions.shopMoney[buy])
                edit_txt("skill.txt", Player.index, Player.skill)
            if Player.money >= Actions.shopMoney[buy] and 6 < buy <= 12:
                Player.money -= Actions.shopMoney[buy]
                Player.armour = Actions.shop[buy]
                Player.skillArmour = Actions.shopMoney[buy]
                calculate_skill()
                print(f"Successfully purchased {Actions.shop[buy]} for {Actions.shopMoney[buy]}$! Gratulationes!"
                      f"\nYou have {Player.money}$ left.")
                time.sleep(1.2)
                # backup
                edit_txt("money.txt", Player.index, str(Player.money))
                edit_txt("armour.txt", Player.index, Actions.shop[buy])
                edit_txt("skillArmour.txt", Player.index, Actions.shopMoney[buy])
                edit_txt("skill.txt", Player.index, Player.skill)
            if Player.money < Actions.shopMoney[buy]:
                print("Not enough cash.")
                time.sleep(1.2)
        elif final == "N":
            print("Returning to forum now...")
            time.sleep(2)
    elif move == 3:
        print(f"""
                Viewing stats:
                Name : {Player.name}
                Money : {Player.money}$
                Weapon : {Player.weapon}
                Armour : {Player.armour}
                Skill : {Player.skill}
        """)
    elif move == 4:
        print("Are you sure that you want to enter the arena? Y/N")
        decision = str(input("$"))
        if decision == "Y":
            if Player.skill <= 10:
                sindex = random.randint(0, 3)
            elif Player.skill <= 18:
                sindex = random.randint(4, 7)
            elif Player.skill <= 26:
                sindex = random.randint(8, 11)
            elif Player.skill <= 37:
                sindex = random.randint(12, 16)
            enemy = Enemies.names[sindex]
            enemySkill = Enemies.skill[sindex]
            enemyHealth = enemySkill * 10
            defper = 1
            print(f"\nYou will be battling against... {enemy}!\n Enemy Health: {enemyHealth}\n Enemy Skill: {enemySkill}"
                  f"\nPress any key to continue")
            input("$")
            while Player.health > 0 and enemyHealth > 0:
                os.system("clear")
                print(
                    f"Your health: {Player.health}\nEnemy health: {enemyHealth}\n 1. Attack with {Player.weapon}\n "
                    f"2. Defend with {Player.armour}\n 3. Heal up")
                move = int(input("$"))
                os.system("clear")
                if move == 1:
                    damage = random.randint(((Player.skill * 3) - 2), ((Player.skill * 3) + 2))
                    enemyHealth -= damage
                    edamage = random.randint(round(enemySkill * 0.75 - 3), round(enemySkill * 0.75 + 3)) * defper
                    Player.health -= edamage
                    print(
                        f"You did {damage} to {enemy}, leaving him at {enemyHealth} health!\nThe {enemy} did {edamage} "
                        f"to you"
                        f", leaving you at {Player.health} health!")
                elif move == 2:
                    defper -= 5 / 100
                    edamage = random.randint(round(enemySkill * 0.75 - 3), round(enemySkill * 0.75 + 3)) * defper
                    Player.health -= edamage
                    sdefper = 1 - defper
                    print(f"You utilised your armour, gaining 5% damage reduction! You now have {sdefper} damage"
                          f" reduction\n {enemy} did"
                          f"{edamage} to you, leaving you at {Player.health} health!")
                elif move == 3:
                    edamage = random.randint(round(enemySkill * 0.75 - 3), round(enemySkill * 0.75 + 3)) * defper
                    Player.health -= edamage
                    chance = random.randint(1, 4)
                    if chance != 1:
                        heal = random.randint(Player.skill - 5, Player.skill + 2)
                        Player.health += heal
                        print(
                            f"{enemy} did {edamage} to you, however you managed to heal yourself for {heal} health,"
                            f"leaving you at {Player.health} health")
                    elif chance == 1:
                        print(f"{enemy} did {edamage} to you\nYou tried to heal, but failed in the process. You"
                              f" were left with {Player.health} health")

                time.sleep(3)
            if enemyHealth <= 0:
                earn = random.randint(Enemies.skill[sindex] - 3, Enemies.skill[sindex] + 3)
                Player.money += earn
                # backup
                edit_txt("money.txt", Player.index, str(Player.money))
                print(f"You defeated {enemy} in a bloody battle!\n The crowds cheer and you earn {earn}$\n Your "
                      f"money: {Player.money}$")
            if Player.health <= 0:
                print(f"{enemy} mercilessly swings his weapon, and you crumble to the ground.\nThis marks the "
                      f"end of your career. This account will now be inaccessible.")
                edit_txt("alive.txt", Player.index, "0")

        elif decision == "N":
                print("Leaving the arena...")
                time.sleep(2)

    time.sleep(5)
