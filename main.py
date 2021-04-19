from player import *
from enemy import *
from items import *
import random
import time


casey = Player("Casey")
jimbo = Peasant("Jimbo")
jumbo = Infantry("Jumbo")
# broadsword = weapon()
# axe = weapon()
# health_vial = disposable()
casey._collect_item('broadsword', itm_atkpts=3, qnty=-1, itm_type='w')
casey._collect_item('axe', itm_atkpts=4, qnty=2, itm_type='w')
casey._collect_item('health vial', itm_hlpts=5, qnty=1, itm_type='d')
# print(casey._items)

def sleep(int):
    return time.sleep(int)

def fancy_print(string):
    for each in string:
        time.sleep(.1)
        print(each, end='')

def RFI():
    return random.randint(1, 20)


def check_alive(target):
    if target.lives > 0 and target.cur_hp > 0:
        return True
    else:
        return False


def player_turn(player, enemy):

    print("Your items are: ", end='')
    print()

    for each in player._items:
        print(each, end=' ')
    used_item = input("\nWhich item would you like to use? ")
    while used_item not in player._items:
        used_item = input("I'm sorry, which item would you like to use?")
    itm_type = get_itm_type(used_item)
    if itm_type == 'd':
        target = player
    else:
        target = enemy
    sleep(1)
    player._use_item(used_item, target)
    if not check_alive(enemy):
        fancy_print("{} has been vanquished!\n".format(enemy.name))
        enemy.alive = False
        xp_val = enemy.xp_val
        # level = player.get_level()
        player.xp_set(xp_val)
    return enemy.alive



def enemy_turn(player):
    sleep(1)
    casey.take_damage(jimbo.deal_damage())
    if not check_alive(player):
        fancy_print('You have vanquished to the void. My condolences')
        player.alive = False
    return player.alive




def Combat(player, enemy):

    player_initiative = RFI()
    enemy_inititative = RFI()

    while player.alive and enemy.alive:

        if player_initiative >= enemy_inititative:
            if player.alive == True:
                enemy.alive = player_turn(player, enemy)
            if enemy.alive == True:
                player.alive = enemy_turn(player)
            print('*' * 55, '\n')
        else:
            if enemy.alive == True:
                player.alive = enemy_turn(player)
            if player.alive == True:
                enemy.alive = player_turn(player, enemy)
            print('*' * 55, '\n')

            # player attack enemy
            # print
            # check alive
            # enemy attack player
            # print
            # check alive

if __name__ == '__main__':
    Combat(casey, jimbo)
    Combat(casey, jumbo)
    # print(casey)
    # print(jimbo)
    # for i in range(1, 33):
    #     jimbo.take_damage(1)
