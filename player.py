class Player:

    def __init__(self, name, hp, attack, attack_speed):
        self.name = name
        # Для того чтобы хил не давал больше максимального hp
        self.max_hp = 100.0
        self.hp = hp
        self.attack = attack
        self.attack_speed = attack_speed
        self.damage_per_second = round(self.attack / self.attack_speed, 1)
        self.money = 0.00
        self.weapon = {}
        # Очки прокачки для максимального hp
        self.upgrade_points = 0
        # С каждым побежденным чудовищем игроку возвращается 1/9 утраченных воспоминаний
        self.memories = 0

    def show_stats(self):
        print("\nПАРАМЕТРЫ [", self.name + "]:", '\nздоровье:', self.hp, "\nатака:", self.attack, '\nскорость атаки:',
              self.attack_speed, '\nурон в секунду:', self.damage_per_second)