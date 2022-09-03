import os
import time


class Player:
    name = ""
    money = 0
    weapon = "Unarmed"
    armour = "Unarmed"
    health = 100
    index = 0
    skillArmour = 0
    skillWeapon = 0
    skill = 0


class Actions:
    explore = ["You take your axe and forage for a while, and earn ", "You head to the local pond and fish, and earn ",
               "You decide to head to the caves and mine, earning you "]
    exploreMoney = [3, 4, 5]
    shop = ["Unarmed", "Tirones' Rusty Dagger", "Veles' Old Spear", "Hastatus' Copper Blade", "Princeps' Gold Sword",
            "Centurion's Platinum War Axe", "Marcus Licinius Crassus' Fabled Hammer", "Agrimensor's Old Rags",
            "Celeres' Ancient Bronze Plate", "Decurion's Iron Armour", "Primus Ordinis' Sturdy Gold Armour",
            "Palatini's Massive Platinum Plating", "Julius Caesar's Mystical Robe"]
    shopMoney = [0, 30, 50, 70, 90, 130, 170, 30, 50, 70, 90, 130, 200]
    enemies = [

    ]


def load_save():
    names = read_txt("users.txt")
    index = find_index(Player.name, names)
    money_list = read_txt("money.txt")
    armour_list = read_txt("armour.txt")
    weapon_list = read_txt("weapon.txt")
    skillWeapon_list = read_txt("skillWeapon.txt")
    skillArmour_list = read_txt("skillArmour.txt")
    skill_list = read_txt("skill.txt")
    Player.money = int(money_list[index].replace("\n", ""))
    Player.armour = armour_list[index].replace("\n", "")
    Player.weapon = weapon_list[index].replace("\n", "")
    Player.skillWeapon = int(skillWeapon_list[index].replace("\n", ""))
    Player.skillArmour = int(skillArmour_list[index].replace("\n", ""))
    Player.skill = float(skill_list[index].replace("\n", ""))
    Player.index = index


def fake_load():
    input("Gladiator RPG Game!!!\nPress to start\n$")
    print("Authenticating...")
    time.sleep(0.8)
    print("Syncing progress...")
    time.sleep(0.6)
    print("Complete!")
    time.sleep(0.8)


def calculate_skill():
    Player.skill = (Player.skillWeapon + Player.skillArmour) / 10


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
    os.system("clear")
    login_choice = int(input("[1] Login\n[2] Register\n$"))
    if login_choice == 1:
        user = str(input("Username: "))
        if find_index(user, read_txt("users.txt")) == 'Fail':
            print("Invalid username.")
            time.sleep(2)
            os.system("clear")
            login()
        else:
            print(f"Authentication successful. Welcome back, {user}")
            Player.name = user
            time.sleep(2)
    if login_choice == 2:
        user = str(input("Enter your desired username: "))
        users = read_txt("users.txt")
        if len(user) > 20 or len(user) < 0:
            print("Too long / Too short.")
            os.system("clear")
            login()
            time.sleep(2)
        elif find_index(user, users) == "Fail":
            add_txt("users.txt", user)
            add_txt("money.txt", "0")
            add_txt("weapon.txt", "Unarmed")
            add_txt("armour.txt", "Unarmed")
            add_txt("skill.txt", "0")
            add_txt("skillWeapon.txt", "0")
            add_txt("skillArmour.txt", "0")
            os.system("clear")
            print("Registration successful. Welcome to RPG game. Restarting Process...")
            time.sleep(2)
            os.system("clear")
            login()