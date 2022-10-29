class Monster():

    def __init__(self, name, hp, attack, attack_speed, info):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.attack_speed = attack_speed
        self.info = info
        self.damage_per_second = round(self.attack / self.attack_speed, 1)

    def show_stats(self):
        print("\nПАРАМЕТРЫ [" + self.name + "]:", '\nздоровье:', self.hp, "\nатака:", self.attack, '\nскорость атаки:',
              self.attack_speed, '\nурон в секунду:', self.damage_per_second)