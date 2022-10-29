import linecache

from player import Player
from enemies import Monster
from potions import Potion
from swords import Sword
import time
import random




# First 3

manticore_info = ' Мантикора — вымышленное существо, чудовище размером с лошадь, с головой человека, телом льва и хвостом' \
                 ' скорпиона.\n Мантикоры (лат. Manticora) — род жуков из семейства жужелиц (Carabidae)\n' \
                 ' подсемейство скакунов (Cicindelinae).'

wendigo_info = ' Вендиго/Виндиго - дух-людоед в мифологии алгонкинов. Первоначально воспринимался как символ ненасытного' \
               ' голода и голодной зимы,\n впоследствии стал служить предостережением против любых излишеств человеческого поведения.'

banshee_info = ' Банши — персонаж ирландского фольклора, чьи стоны и рыдания предвещают скорую смерть тому, кто их слышит.\n' \
               ' Когда банши можно увидеть, чаще всего она выглядит как прекрасная\n женщина с длинными светлыми волосами,' \
               ' нередко с серебряным гребнем в руке.'

Manticore = Monster('Мантикора', 100.0, 4.5, 1.1, manticore_info)
Wendigo = Monster("Вендиго", 100.0, 5, 1, wendigo_info)
Banshee = Monster('Банши', 100.0, 4.9, 1, banshee_info)


# Second 3

ghoul_info = 'Живые мертвецы, поднимающиеся из могил. Как и любые другие вампиры, вурдалаки пьют кровь и могут опустошать' \
             ' целые деревни.'

hamayun_info = 'Подобно Алконосту, божественная женщина-птица, основная функция которой — осуществление предсказаний.\n' \
               ' Хорошо известна присказка «Гамаюн — птица вещая». Также умела управлять погодой.\n Считалось,' \
               ' когда Гамаюн летит со стороны восхода, следом за ней приходит буря.'

kikimora_info = 'Злой дух (иногда — жена домового), предстающий в образе маленькой уродливой старушки.\n Если кикимора' \
                ' живет в доме за печкой или на чердаке,\n то постоянно вредит людям: шумит, стучит в стены, мешает спать,' \
                ' рвет пряжу, бьет посуду, травит скот.'

Ghoul = Monster('Вурдалак', 100.0, 25, 1.1, ghoul_info)
Hamayun = Monster('Гамаюн', 100.0, 29.5, 1.1, hamayun_info)
Kikimora = Monster('Кикимора', 100.0, 32, 1, kikimora_info)


# Third 3

draugr_info = 'в скандинавской мифологии души берсерков, умерших не в сражении или не сгоревших в погребальном костре.'

griffin_info = 'Этих крылатых чудовищ изображали с орлиной головой и туловищем льва.\n Греки называли их «собаками Зевса»,' \
               ' охранявшими сокровища в государстве гипербореев.'

ubor_info = 'Убор – болгарский вампир, который обладает очень скверным нравом. Он настолько труслив,\n' \
            ' что боится нападать на животных и людей. Из-за этого ему приходится питаться падалью и даже навозом.'

Draugr = Monster(' Драугр', 100.0, 45.1, 0.9, draugr_info)
Griffin = Monster('Грифон', 100.0, 55.5, 0.8, griffin_info)
Ubor = Monster('Убор', 100.0, 60, 0.6, ubor_info)


# objects Potion class
big_potion = Potion('(45.0$) зелье здоровья(б)', 75)
medium_potion = Potion('(30.0$) зелье здоровья(ср)', 50)
small_potion = Potion('(20.0$) зелье здоровья(м)', 25)

# objects Sword class
wooden_sword = Sword('деревянный меч', 7.0, 14.0)
sword = Sword('железный меч', 9.0, 17.0)
flamberg = Sword('фламберг', 12.0, 20.0)
espadon = Sword('эспадон', 15.0, 24.0)
claymore = Sword('клеймор', 19.0, 30.0)
violent_steel = Sword('буйная сталь', 24.0, 39.0)
goddess_contempt = Sword('презрение богини', 29.0, 44.0)
multicolor_eclipse = Sword('многоцветное затмение', 34.0, 49.0)
ichimonji = Sword('ичимондзи', 39.0, 57.0)
iron_mass = Sword('железная масса', 44.0, 63.0)
lefty = Sword('левша', 45.0, 60.0)
spooky_beak = Sword('жуткий клюв', 50.0, 68.0)
blade_of_the_seventh_sun = Sword('лезвие седьмого солнца', 54.0, 71.0)
brink_of_insanity = Sword('грань безумия', 57.0, 77.0)
excalibur = Sword('легендарный экскалибур', 87.0, 200.0)

swords_objects_array = [flamberg, espadon, claymore, violent_steel, goddess_contempt, multicolor_eclipse, ichimonji,
         iron_mass, lefty, spooky_beak, blade_of_the_seventh_sun, brink_of_insanity, excalibur]

# РЮКЗАК
backpack = {big_potion.name:big_potion.hill, medium_potion.name:medium_potion.hill, (sword.name+' '+str(sword.cost)+'$'):sword.damage,
            (wooden_sword.name+' '+str(wooden_sword.cost)+'$'):wooden_sword.damage}
# ТОРГОВЕЦ

dealer = {small_potion.name:small_potion.hill, medium_potion.name:medium_potion.hill, big_potion.name:big_potion.hill}

# Функция для заполнения лавки

def shop_filling(objet):
    dealer[objet.name+' '+str(objet.cost)+'$'] = objet.damage

for object in swords_objects_array:
    shop_filling(object)

# СПИСОК ПОБЕЖДЕННЫХ ЧУДОВИЩ
win_list = []


def player_menu():

      while True:

            print('\n1) Статы [', Hero.name, ']\n'
                    '2) Рюкзак\n'
                    '3) Торговец\n'
                    '4) Монеты\n'
                    '5) Снаряжение\n' 
                    '6) Очки прокачки\n'
                    '7) Список побед\n'
                    '8) Продолжить...')

            choice = input('-- ')

            if choice == '1':
                  Hero.show_stats()
                  input()

            elif choice == '2':

                  print(backpack)

                  backpack_item = input('Поменять/Использовать-(название)-- ')

                  if backpack_item in backpack:
                        # проверка на то, что он хочет использовать зелье
                        try:
                              if backpack_item.split().index('зелье') == 1:
                                  # Проверка, если при использования хила hp будет больше максимального
                                  healthpoints = Hero.hp + backpack[backpack_item]
                                  if healthpoints > Hero.max_hp:
                                      Hero.hp = Hero.max_hp
                                      del backpack[backpack_item]
                                      print('Максимальное здоровье', str(Hero.hp))
                                  # Иначе просто прибавить очки хила к hp
                                  else:
                                      Hero.hp += backpack[backpack_item]
                                      print('Использовано', backpack_item)
                                      del backpack[backpack_item]


                        # Иначе он берет меч
                        except ValueError:
                              Hero.attack = backpack[backpack_item]
                              Hero.damage_per_second = round(Hero.attack / Hero.attack_speed, 1)

                              # Важный функционал: когда берется оружие в руки из рюкзака, то после смены на другое оно
                              # не выбрасывается или исчезает, а возвращается в рюкзак
                              key = None
                              if Hero.weapon != {}:
                                    for k, v in Hero.weapon.items():
                                        backpack[k] = v
                                        key = k
                                    just_use = Hero.weapon.pop(key)
                              Hero.weapon[backpack_item] = backpack[backpack_item]
                              del backpack[backpack_item]


            elif choice == '3':

                  buy_or_sell = input("а)Купить\nб)Продать\n ")

                  # Купить
                  if buy_or_sell == 'а':
                      print('ТОРГОВЕЦ:\n')

                      for k, v in dealer.items():
                          print(k+':', v)

                      purchase_choice = input('\nВыбери зелье/оружие(название)-- ')

                      if purchase_choice in dealer:

                          try:
                              # Срезаем знак доллара
                              # Если покупает меч, проверяет это float()
                              cost = float(purchase_choice.split()[-1][:-1])
                              if Hero.money >= cost:
                                  backpack[purchase_choice] = dealer[purchase_choice]
                                  del dealer[purchase_choice]
                                  Hero.money -= cost
                              else:
                                  input('Не достаточно средств..')

                          except ValueError:
                              # Иначе покупает зелье
                              if Hero.money >= float(purchase_choice.split()[0][1:-2]):
                                  # В сумке должно быть максимум по 1-му виду зелий
                                  if purchase_choice in backpack:
                                      input('В сумке нет места для зелья такого типа, выбери другое')
                                  else:
                                      backpack[purchase_choice] = dealer[purchase_choice]
                                      Hero.money -= float(purchase_choice.split()[0][1:-2])

                  #  Продать
                  else:
                      print(Hero.weapon)
                      print(backpack)

                      sell = input('Что продать-- ')

                      # Если продаваемая вещь в рюкзаке
                      if sell in backpack:
                          # Если хотим продать зелье
                          if sell.split()[0][0] == '(':
                              Hero.money += float(sell.split()[0][1:-2])
                              del backpack[sell]
                          # Иначе продаём меч
                          else:
                              dealer[sell] = backpack[sell]
                              Hero.money += float(sell.split()[-1][:-1])
                              del backpack[sell]

                      # Если оружие не в рюкзаке, мы можем продать и то оружие, что в руках
                      elif sell in Hero.weapon:
                          dealer[sell] = Hero.weapon[sell]
                          Hero.money += float(sell.split()[-1][:-1])
                          del Hero.weapon[sell]

            elif choice == '4':
                  print(Hero.money)
                  input()

            elif choice == '5':
                  print(Hero.weapon)
                  input()

            elif choice == '6':
                  print("Неиспользованные очки:", str(Hero.upgrade_points))
                  if Hero.upgrade_points > 0:
                      spend_points = input("a) Обменять на монеты\nb) Повысить здоровье\n")

                      if spend_points == 'б':
                          # 1 очко == 1.5hp
                          Hero.max_hp += 1.5*Hero.upgrade_points
                          Hero.upgrade_points = 0
                          print('Максимальное здоровье повышено:', str(Hero.max_hp))
                      else:
                          Hero.money += Hero.upgrade_points * 10
                          Hero.upgrade_points = 0

                  input()

            elif choice == '7':
                print(win_list)
                input()

            else:
                  break



def monster_menu(clas1, clas2, clas3):

      print('Так, передо мной три комнаты. Наверное, монстры в них. Посмотрим кто там..')
      time.sleep(1)

      # Меню одного монстра (инфа, статы, в бой)
      def one_monster_info(name, clas):

            # Это условие, чтобы у побежденного чудовища не будет отображаться меню
            if clas.hp != 0:
                print('a) Инофрмация\nb) Статы', name+'\n'+'c) В бой!')

                choice3 = input('-- ')

                if choice3 == 'а':
                    print(clas.info)
                    input()

                elif choice3 == 'б':
                    clas.show_stats()
                    input()

                elif choice3 == 'с':
                    while True:
                        print('... идёт бой ...')
                        time.sleep(1)
                        Hero.hp -= clas.damage_per_second
                        clas.hp -= Hero.damage_per_second
                        if Hero.hp <= 0:
                            Hero.hp = 0
                            print('\nВы погибли...')
                            return False
                        elif clas.hp <= 0:
                            clas.hp = 0
                            print('\nВы победили!\n')
                            time.sleep(2)

                            # Случайное число для для обработки кол-ва получаемой награды
                            number = random.randint(4, 30)

                            Hero.money += number*1.5
                            Hero.upgrade_points += number//2.5
                            Hero.memories += 1

                            print('Ваша награда:\nмонеты:', str(number)+'\nочки прокачки:', str(Hero.upgrade_points)+'\n'
                                    'воспоминания:', '('+str(Hero.memories)+'/9)\n')

                            # Побежденное чудовище сохраняется в списке побед
                            win_list.append(clas.name)
                            return True



      while True:

            if clas1.hp != 0 or clas2.hp != 0 or clas3.hp != 0:
                 print('a)', clas1.name, '\tb)', clas2.name, '\t\tc)', clas3.name, '     ( #-панель игорока )')

                 choice = input('-- ')

                 if choice == 'а':

                     returned_value_for_exit = one_monster_info(clas1.name, clas1)
                     # Проверка для выхода из программы, если hp игрока 0
                     if returned_value_for_exit == False:
                         break

                 elif choice == 'б':

                     returned_value_for_exit = one_monster_info(clas2.name, clas2)
                     if returned_value_for_exit == False:
                         break

                 elif choice == 'с':

                     returned_value_for_exit = one_monster_info(clas3.name, clas3)
                     if returned_value_for_exit == False:
                         break

                 elif choice == '#':
                     player_menu()

            else:
                return True


choice = input('  Пропустить заставку?y/n-- ')

if choice == 'n':
    print("... Я вижу ты проснулся, незнакомец. Когда я нашёл тебя, ты был без сознания в разорванной одежде недалеко от"
      " берега реки.\n    Ты не из здешних мест...")

    Hero = Player(input('  Моё имя Велимдур... А твоё?... --  '), 100.0, 4.0, 1)

    time.sleep(1)

    print('\n Хм..', Hero.name + ", cейчас, наверное, ты не помнишь, что с тобой случилось, но странно, что ты помнишь своё"
                          " имя.\n Скорее всего часть твоих"
                          " воспоминаний украли чудища.. Велимдур расскажет, как все в этом месте устроено. Чтобы вернуть"
                          " утраченную память,\n тебе надо будет победить 9 страшных чудовищ, которые живут в этом месте."
                          " Так ты сможешь восстановить хотя бы часть воспоминаний..\n Велимдур тебе не говорил, что он"
                          " торговец, у него можно приобрести необходимое снаряжение и еще другие побрикушки..), но не"
                          "забесплатно, а за монеты.\n Их ты можешь получать, как награду, за убийства чудищ, а также"
                          " другие полезные предметы. Велимдур даст тебе некоторые вещи, чтобы выжить..\n Используй их"
                          " с умом.")

    time.sleep(2)


    print('\n -Ахх...голова болит...я ничего не помню, этот странный торговец прав, наверное,\n когда я одолею всех этих...'
      'монстров, то..верну свои воспоминания. Надо поспешить!\n')
    input()
else:
    Hero = Player(input('  Моё имя Велимдур... А твоё?... --  '), 100.0, 2.0, 1)


choice2 = input('Включить режим бога?(y/n)-- ')
if choice2 == 'y':
    Hero.hp = 1000
    Hero.damage_per_second = 100

player_menu()

time.sleep(1)
print('\t\t\t\t\t\tГЛАВА 1.(приспособление)\n')
time.sleep(3)
output1 = monster_menu(Manticore, Wendigo, Banshee)

if output1 == True:
    time.sleep(2)
    print('Это было нелегкая битва, но я справился. Осталось 6 чудовищ... я должен поспешить!\n')
    time.sleep(2)
    print('\t\t\t\t\t\t\tГЛАВА 2.(адаптирование)\n')
    time.sleep(3)
    output2 = monster_menu(Ghoul, Hamayun, Kikimora)

    if output2 == True:
        time.sleep(2)
        print('Хорошо... так хочется закусить.. я уже вернул большую часть своих воспоминаний.. но осталось еще 3 чудовища...'
              ' я должен поспешить!\n')
        time.sleep(2)
        print('\t\t\t\t\t\t\tГЛАВА 3.(принятие)\n')
        time.sleep(3)
        monster_menu(Draugr, Griffin, Ubor)


        time.sleep(3)
        print('Дхагхмзх...а-а..мои воспоминания вернулись, да-а-а-а-!! Это было непросто... все еще болит голова...'
              'я начинаю вспоминать кто я...ахгах...')
        for i in range(7):
            time.sleep(1)
            if i == 3:
                print('...я...')
            elif i == 6:
                print('   Абоба')
            else:
                print('... ...')

        time.sleep(1)





