import random
import time


class Player:
    name = ""
    money = 0
    weapon = "Unarmed"
    armour = "Unarmed"
    health = 100
    index = 0


class Actions:
    explore = ["You take your axe and forage for a while, and earn ", "You head to the local pond and fish, and earn ",
               "You decide to head to the caves and mine, earning you "]
    exploreMoney = [5, 7, 9]
    shop = ["Unarmed", "Tirones' Rusty Dagger", "Veles' Old Spear", "Hastatus' Copper Blade", "Princeps' Gold Sword",
            "Centurion's Platinum War Axe", "Marcus Licinius Crassus' Fabled Hammer", "Agrimensor's Old Rags",
            "Celeres' Ancient Bronze Plate", "Decurion's Iron Armour", "Primus Ordinis' Sturdy Gold Armour",
            "Palatini's Massive Platinum Plating", "Julius Caesar's Mystical Robe"]
    shopMoney = [0, 30, 50, 70, 90, 130, 170, 30, 50, 70, 90, 130, 200]


def check_index(contents, index):
    if 0 <= index < len(contents):
        return True
    else:
        return False


def read_txt(txt):
    file = open(txt, 'r')
    content = file.readlines()
    return content
    file.close()


def add_txt(txt, text):
    file = open(txt, 'a')
    file.write(text)
    file.write('\n')
    file.close()
    return 'Success'


def edit_txt(txt, index, text):
    file = open(txt, 'r')
    items = file.readlines()
    items[int(index)] = (str(text) + "\n")
    file = open(txt, 'w')
    file.writelines(items)
    file.close()
    result = 'Success'
    return result


def find_index(word, items):
    if (str(word) + '\n') in items:
        index = items.index((word + '\n'))
        result = int(index)
    else:
        result = 'Fail'
    return result


def login():
    login_choice = int(input("[1] Login\n[2] Register\n$"))
    if login_choice == 1:
        user = str(input("Username: "))
        if find_index(user, read_txt("users.txt")) == 'Fail':
            print("Fail")
            time.sleep(2)
            login()
        else:
            print(f"Welcome, {user}")
            Player.name = user
            time.sleep(2)
    if login_choice == 2:
        user = str(input("Enter your desired username: "))
        users = read_txt("users.txt")
        if len(user) > 20 or len(user) < 0:
            print("Fail")
            time.sleep(2)
        elif find_index(user, users) == "Fail":
            add_txt("users.txt", user)
            add_txt("money.txt", "0")
            add_txt("weapon.txt", "Unarmed")
            add_txt("armour.txt", "Unarmed")
            print("Repeating process")
            time.sleep(2)
            login()


login()
names = read_txt("users.txt")
index = find_index(Player.name, names)
money_list = read_txt("money.txt")
armour_list = read_txt("armour.txt")
weapon_list = read_txt("weapon.txt")
Player.money = int(money_list[index].replace("\n", ""))
Player.armour = armour_list[index].replace("\n", "")
Player.weapon = weapon_list[index].replace("\n", "")
Player.index = index
print("Location: Ancient Rome\nDate & Time: Unknown\n\n_____\nPoverty grips the nation. As a peasant, try and make a "
      "living\nbecome a powerful gladiator for the Roman Colosseum. Try not to die in the process.\n\n\n")
time.sleep(3)
while Player.health > 0:
    print("Forum Romanum - Roman Forum (Hub)\n [1] Explorare (Explore)\n [2] Shop (Shop)\n [3] Gladiator (Gladiator)\n")
    move = int(input("$"))
    if move == 1:
        temp = random.randint(0, 2)
        loot = random.randint(Actions.exploreMoney[temp] + 3, Actions.exploreMoney[temp] + 5)
        print(f"{Actions.explore[temp]}{loot}$")
        Player.money += loot
        time.sleep(2)
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
                print(f"Successfully purchased {Actions.shop[buy]} for {Actions.shopMoney[buy]}! Gratulationes!"
                      f"\nYou have {Player.money} left.")
                # backup
                edit_txt("money.txt", Player.index, str(Player.money))
                edit_txt("weapon.txt", Player.index, Actions.shop[buy])
            if Player.money >= Actions.shopMoney[buy] and buy > 6 and buy <= 12 :
                Player.money -= Actions.shopMoney[buy]
                Player.armour = Actions.shop[buy]
                print(f"Successfully purchased {Actions.shop[buy]} for {Actions.shopMoney[buy]}! Gratulationes!"
                      f"\nYou have {Player.money} left.")
                # backup
                edit_txt("money.txt", Player.index, str(Player.money))
                edit_txt("armour.txt", Player.index, Actions.shop[buy])
