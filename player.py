from items import *
from enemy import *


class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._cur_xp = 1
        self._base_hp = 10
        self.cur_hp = 10
        self._items = []
        self.alive = True

    def get_lives(self):
        return self._lives

    def set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def get_level(self):
        return self._level

    def set_level(self):
        cur_level = self._level
        wrkin_level = self._level
        level_map = [1, 500, 1200, 2100, 3400]
        if wrkin_level >= 1:
            # delta = level - self._level
            xp = self._cur_xp
            # self._level = level
            j = 0
            for i in level_map:
                if i <= xp:
                    j += 1
                    wrkin_level = j
                else:
                    break
                self._level = wrkin_level
            if cur_level != wrkin_level:
                print("You are now level {}!".format(self._level))
        else:
            print("Level cannot be below 1, how did this even happen?")

    lives = property(get_lives, set_lives)
    level = property(get_level, set_level)

    def _collect_item(self, itm_nm, itm_type='d', itm_hlpts=0, itm_atkpts=0, qnty=1):
        # if found in inventory, add to quantity
        # else add item to inventory
        if itm_nm in self._items:
            set_qnty(itm_nm)
        else:
            self._items.append(itm_nm)
            first_get(itm_nm, itm_hlpts, itm_atkpts, qnty, itm_type)

    def _use_item(self, itm_nm, target):
        # modify quantity and return item properties
        if itm_nm in self._items:
            itm_type = get_itm_type(itm_nm)
            if itm_type == 'd':
                if isinstance(target, Enemy):    # #todo get targeting to work
                    atkpts = get_atkpts(itm_nm)
                    target.take_damage(atkpts)
                if target == self:
                    hlpts = get_healpts(itm_nm)
                    self.heal_damage(hlpts)
            else:
                atkpts = get_atkpts(itm_nm)
                target.take_damage(atkpts)

            cur_qnty = get_qnty(itm_nm)
            if cur_qnty > 1:
                cur_qnty -= 1
                set_qnty(itm_nm, cur_qnty)
            elif cur_qnty == 1:
                last_use(itm_nm)
                x = self._items.index(itm_nm)
                self._items.pop(x)

        else:
            print("Sorry, you do not have that item")

    def take_damage(self, damage):
        remaining_points = self.cur_hp - damage
        if remaining_points > 0:
            self.cur_hp = remaining_points
            print("You took {} points damage and have {} left".format(damage, self.cur_hp))
        else:
            self.lives -= 1
            if self.lives >= 0:
                self.cur_hp = self._base_hp
                print("You lost a life. You have {0.lives} remaining.".format(self))

    def heal_damage(self, heal_pts):
        print("You have healed for {} points.".format(heal_pts))
        self.cur_hp += heal_pts

    def xp_get(self):
        return self._cur_xp

    def xp_set(self, xp_val):
        self._cur_xp += xp_val
        self.set_level()





    def __str__(self):
        return "Name: {0.name}, Lives {0._lives}, Level: {0._level}, XP: {0._cur_xp}".format(self)
