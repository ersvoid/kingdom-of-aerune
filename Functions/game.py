choices = ["1. Attack", "2. Magic", "3. Items", "4. Run"]


def display_board(player, enemy):
    print("                HP           MP")
    print("{}   {}/{}        {}/{}".format(player.name, player.hp, player.maxhp, player.mp, player.maxmp))
    print("{}   {}/{}        {}/{}".format(enemy.name, enemy.hp, enemy.maxhp, enemy.mp, enemy.maxmp))


def death(char):
    if char.death_check():
        return True


def sleep_check(enemy, player):
    if death(enemy):
        return
    if enemy.sleep:
        print("The enemy is sleeping.")
        enemy.take_damage(10 + player.get_str())
        save = enemy.will()
        spell = player.get_wis()
        if save >= spell:
            print("Your opponent is still sleeping!")
        else:
            enemy.sleep = False
            print("Your opponent has woken up!")
            return enemy.sleep


def fire_check(enemy):
    if death(enemy):
        return
    save = enemy.reflex()
    if save > 15:
        enemy.fire = 0
        return enemy.fire
    if enemy.fire > 0:
        print("The enemy is on fire!")
        enemy.take_damage(5)
        enemy.fire -= 1
        return enemy.fire


def player_turn(player, enemy):
    if death(player) or death(enemy):
        return
    for c in choices:
        print(c)
    choice = input("Your turn: ")
    if choice == "1":
        if player.attack() > enemy.ac_rating():
            enemy.take_damage(player.damage())
        else:
            print(player.name, " missed!")
    elif choice == "2":
        c = 1
        for m in player.magic:
            print("{}. {}".format(c, m.name))
            c += 1
        choice = int(input("Choose spell: ")) - 1
        mana = player.magic[choice].cost
        if player.mp - mana < 0:
            print("Spell failed...")
        else:
            player.take_mp(mana)
            if player.magic[choice].type == "attack":
                if player.magic[choice].elem == "Fire":
                    enemy.fire = 5
                    enemy.take_damage(player.magic[choice].get_val())
                elif player.magic[choice].elem == "Death":
                    if enemy.will() < player.will():
                        enemy.hp = 0
                        print("A black ray pierces the heart of your enemy...")
                    else:
                        print("A black ray shoots from your fingers...")
                        enemy.take_damage(player.magic[choice].get_val())
                else:
                    enemy.take_damage(player.magic[choice].get_val())
            elif player.magic[choice].type == "heal":
                player.heal(player.magic[choice].val)
            elif player.magic[choice].type == "alter":
                if enemy.will() >= player.will():
                    print("Your opponent is unaffected by your spell.")
                else:
                    enemy.sleep += 5
                    print("The enemy is sleeping.")
    elif choice == "3":
        c = 1
        for i in player.items[1:]:
            print("{}. {} X {}".format(c, i.name, i.amt))
            c += 1
        choice = int(input("Choose an item: "))
        p_item = player.items[choice]
        if not p_item.check_item():
            print("You have no more of that item!")
        else:
            p_item.use_item()
            if p_item.type == "p":
                player.heal(p_item.item_value())
            elif p_item.type == "s":
                if p_item.elem == "Fire":
                    enemy.fire = 5
                    enemy.take_damage(p_item.item_value())
    elif choice == "4":
        print("You try to run but cannot escape!")
    else:
        choice = input("Your turn: ")


def enemy_turn(enemy, player):
    if death(enemy) or death(player):
        return
    if enemy.sleep:
        return
    if player.ac_rating() < enemy.attack():
        print(enemy.name, " attacks ", player.name)
        player.take_damage(enemy.damage())
    else:
        print(enemy.name, " missed!")


def battle(loc, player):
    global battle_on, _round
    enemy = loc.pop[0]
    print("{} has entered the arena.".format(enemy.name))
    player_init = player.ac_rating()
    enemy_init = enemy.ac_rating()
    _round = True
    while _round:
        display_board(player, enemy)
        if death(enemy) or death(player):
            break
        sleep_check(enemy, player)
        fire_check(enemy)
        if player_init > enemy_init:
            print("You are faster.")
            player_turn(player, enemy)
            if death(enemy):
                break
            enemy_turn(enemy, player)
        elif player_init < enemy_init:
            print("Your opponent is faster.")
            enemy_turn(enemy, player)
            if death(player):
                break
            player_turn(player, enemy)
    print("ROUND OVER!!!!")
    if player.hp <= 0:
        print("You are dead.")
        return False
    else:
        print("You have won this battle!")
        player.win_gold(enemy.money)
        player.get_xp(enemy.xp)
        print("You have gained {} XP.".format(enemy.xp))
        enemy.reset()
        return True


def continue_screen():
    print("\n")
    input("press any key to continue")
    print("\n")


def welcome_screen():
    print("""Welcome to the Kingdom of Aerune!  You have made your way to the outskirts of the empire, where wilderness 
and wonder await any brave adventurer.  You disembark from the carriage and set down the footpath towards the 
town in the distance.  The town is small, with no protective walls or towers.  These people are completely 
exposed to the elements and dangers of the wild.""")
    continue_screen()


def game_screen(loc):
    c = 1
    print("You stand on the dirt street.")
    for l in loc.lst:
        print("{}. {}".format(c, l.name))
        c += 1
    num = len(loc.lst) + 1
    print("{}. Leave town.".format(num))
    val = int(input("Choose one: ")) - 1
    while val < 0 or val > num:
        val = int(input("Choose: "))
    else:
        return val


def quest_func(loc, player):
    global battle_on
    print("\n")
    print(loc.i1)
    continue_screen()
    print(loc.i2)
    continue_screen()
    print(loc.i3)
    continue_screen()
    loc.__str__()
    battle_on = True
    print("\n")
    while battle_on:
        val = battle(loc, player)
        if val:
            player.quest += 1
            print(loc.o1)
            continue_screen()
            print(loc.o2)
            battle_on = False
            return battle_on
        else:
            break
    battle_on = False
    return battle_on


def shopping(loc, player):
    global shop_on
    loc.__str__()
    loc.pop[0].talk()
    print("You have " + str(player.money) + "gp.")
    print("1. Buy")
    print("2. Sell")
    print("3. Goodbye")
    val = int(input("'What\'ll it be then?' "))
    if val == 1:
        print("You have " + str(player.money) + "gp.")
        loc.pop[0].sell(player)
    elif val == 2:
        print("You have " + str(player.money) + "gp.")
        loc.pop[0].buy(player)
    elif val == 3:
        shop_on = False
        return shop_on
    else:
        int(input("'What did you say?' "))


def innkeeper(loc, player):
    global inn_on
    loc.__str__()
    loc.pop[0].talk()
    print("1. Yes")
    print("2. No")
    val = int(input("'Well?' "))
    if val == 1:
        print("'That'll be 25gp.'")
        if player.money < 25:
            print("'Get out of here!'")
            inn_on = False
            return inn_on
        else:
            print("'Here take this key. Give it back when you're done.'")
            player.spend_gold(25)
            player.reset()
            print("You spend the night at the inn and wake up feeling refreshed.")
            inn_on = False
            return inn_on
    elif val == 2:
        print("'Need any supplies?'")
        print("1. Yes")
        print("2. No")
        val = int(input("'Well?' "))
        if val == 1:
            print("You have " + str(player.money) + "gp.")
            loc.pop[0].sell(player)
        elif val == 2:
            print("The innkeeper waves goodbye.")
            inn_on = False
            return inn_on
        else:
            int(input("'What did you say?' "))
    else:
        int(input("'Well?' "))


def housing(loc):
    global house_on
    loc.__str__()
    loc.pop[0].talk()
    house_on = False
    return house_on


a1 = "'Please accept this bounty as a gift of our gratitude.'"
c1 = "'Thank you!'"
d1 = "'Thank you again for your help.'"


def mayor_hall(loc, player, dungeon, a=a1, b=100, c=c1, d=d1):
    global hall_on
    loc.__str__()
    if player.quest == 0:
        loc.pop[0].talk()
        print("1. Yes")
        print("2. No")
        val = int(input("'Well?' "))
        if val == 1:
            print(d)
            hall_on = False
            quest_func(dungeon, player)
            print(player.quest)
        elif val == 2:
            print("Goodbye.")
            hall_on = False
            return hall_on
        else:
            int(input("'Well?' "))
    elif player.quest == 20:
        print("'Thank you again for the help with the Wizard.'")
        hall_on = False
        return hall_on
    elif player.quest % 2 != 0:
        print(a)
        player.win_gold(b)
        print(player.quest)
        return True
    elif player.quest % 2 == 0:
        print(d)
        print(player.quest)
        loc.pop[0].talk()
        print("1. Yes")
        print("2. No")
        val = int(input("'Well?' "))
        if val == 1:
            print(c)
            hall_on = False
            quest_func(dungeon, player)
            print(player.quest)
            return hall_on
        elif val == 2:
            print("Goodbye.")
            hall_on = False
            return hall_on
        else:
            int(input("'Well?' "))


shop_on = False
inn_on = False
house_on = False
battle_on = False
hall_on = False
questing = False


def run_village(player, town, shop, inn, house, hall, dungeon):
    global shop_on, inn_on, house_on, battle_on, hall_on, questing
    val = game_screen(town)
    print("\n")
    if val == 0:
        shop_on = True
    elif val == 1:
        inn_on = True
    elif val == 2:
        house_on = True
    elif val == 3:
        hall_on = True
    elif val == 4:
        game_on = False
        return game_on
    else:
        int(input("Choose one: "))
    while shop_on:
        shopping(shop, player)
    while inn_on:
        innkeeper(inn, player)
    while house_on:
        housing(house)
    while hall_on:
        _bool = mayor_hall(hall, player, dungeon)
        if _bool:
            return True
    continue_screen()


def town_game(player, town, shop, inn, house, hall, dungeon):
    _bool = run_village(player, town, shop, inn, house, hall, dungeon)
    if _bool:
        return True


def dungeon_lvl(player):
    if player.quest < 2:
        return 0
    elif player.quest < 4:
        return 1
    elif player.quest < 6:
        return 2
    elif player.quest < 8:
        return 3
    elif player.quest < 10:
        return 4
    elif player.quest < 12:
        return 5
    elif player.quest < 14:
        return 6
    elif player.quest < 16:
        return 7
    elif player.quest < 18:
        return 8
    elif player.quest < 20:
        return 9


def game_stage(player, towns, shops, inns, houses, halls, dungeons):
    lvl = dungeon_lvl(player)
    game_on = True
    towns[0].__str__()
    print("\n")
    while game_on:
        _bool = town_game(player, towns[0], shops[0], inns[0], houses[0], halls[0], dungeons[lvl])
        if _bool:
            return True
