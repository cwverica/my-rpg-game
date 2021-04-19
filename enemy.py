import random

class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1, xp_val=10, atk_pts=1):
        self.name = name
        self.cur_hp = hit_points
        self.lives = lives
        self.xp_val = xp_val
        self.base_hp = hit_points
        self.atk_pts = atk_pts
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.cur_hp - damage
        if remaining_points > 0:
            self.cur_hp = remaining_points
            print("{} took {} points damage and have {} left".format(self.name, damage, self.cur_hp))
        else:
            if self.lives >= 1:
                self.lives -= 1
                if self.lives >= 0:
                    self.cur_hp = self.base_hp
            else:
                print("{} is already dead, why beat a dead horse?".format(self.name))

    def deal_damage(self):
        return self.atk_pts

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.cur_hp}".format(self)

class Peasant(Enemy):
    # basic enemy unit, quick, but low attack and hit points
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=10, xp_val=100)

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("Cowardly fool stumbled back and avoided your swing.")
            return True
        else:
            return False

    def misses(self):
        if random.randint(1, 5) <= 2:
            print("The peasant actually landed a hit!")
            return False
        else:
            print("The peasant missed it's attack!")
            return True

class Infantry(Enemy):
    # a bit tougher than the peasant, smarter, slightly slower and harder hitting
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=20, xp_val=500, atk_pts=2)

    def dodges(self):
        if random.randint(1, 6) == 6:
            print(" A skillful sidestep made you miss this attack")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)



class Knight(Enemy):

    # armored and slow, very low intelligence, but high hit points and deadly when a hit lands
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=50, xp_val=500, atk_pts=5)

    def dodges(self):
        if random.randint(1, 20) == 20:
            print("Through sheer luck, the tin-man stumbled out of your reach")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            dmg = ((damage * random.randint(2, 4))/4)
            if dmg < damage:
                print("The knights armor absorbed some of the blow!")
            super().take_damage(int(dmg))

    def misses(self):
        if random.randint(1, 7) <= 5:
            print("The knight lands a savage blow!")
            return False
        else:
            print("The knight barely missed you!")
            return True