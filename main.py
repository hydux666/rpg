import random
from cogs import *

login()
os.system("cls")
load_save()
fake_load()
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
                print(f"Successfully purchased {Actions.shop[buy]} for {Actions.shopMoney[buy]}! Gratulationes!"
                      f"\nYou have {Player.money} left.")
                os.system("cls")
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
                print(f"Successfully purchased {Actions.shop[buy]} for {Actions.shopMoney[buy]}! Gratulationes!"
                      f"\nYou have {Player.money} left.")
                # backup
                edit_txt("money.txt", Player.index, str(Player.money))
                edit_txt("armour.txt", Player.index, Actions.shop[buy])
                edit_txt("skillArmour.txt", Player.index, Actions.shopMoney[buy])
                edit_txt("skill.txt", Player.index, Player.skill)
        elif final == "N":
            print("Returning to forum now...")
            time.sleep(2)
        else:
            print("NT, NT.\n Now wait for 4 seconds as a punishment")
            time.sleep("4")
    elif move == 3:
        print(f"""
                Viewing stats:
                Name : {Player.name}
                Money : {Player.money}$
                Weapon : {Player.weapon}
                Armour : {Player.armour}
                Skill : {Player.skill}
        """)
        time.sleep(1.2)
