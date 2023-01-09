import random
import time

from GAME1 import lettergame

# BEAN WORLD REMASTERED - Lev Roland-Kalb
# Run Program and follow along below to play the game
# Last updated: 1/9/2023

class monster():
    def __init__(self,type,name,health,beans,exp,level,reward):
        """
        :param type: type of creature ()
        :param name: name of the monster
        :param health:
        :param beans: beans awarded upon victory
        :param exp:
        level = level for damage/heal
        """
        self.level = level
        self.name = name
        self.attacks = monsterattacks[type]
        self.health = health
        self.beans = beans
        self.exp = exp
        self.type = type
        self.conditiontime = 0
        self.condition = ''
        self.permcondition = ''
        self.reward = reward


    def next_turn(self):
        self.conditiontime -= 1

    def get_level(self):
        return self.level

    def get_health(self):
        return self.health

    def get_beans(self):
        return self.beans

    def get_exp(self):
        return self.exp

    def get_name(self):
        return self.name

    def take_damage(self,damage):
        self.health -= damage


    def print(self):
        print('<><><><><><><><><><><><><><><>')
        print("Monster: " , str(self.name), ' the ', str(self.type))
        print("Health: ", str(self.health))

    def heal(self,heal):
        if heal > 0:
            print('the opponent heals ', heal, ' HP')
        self.health += heal

    def random_attack(self):
        ####generates a random attack 
        return random.choice(monsterattacks[str(self.type)]['attacklist'])

    def set_condition(self,condition,permanence):
        """
        :param condition:
        :param permanence: how many turns
        :return:
        """
        self.condition = condition
        self.conditiontime = permanence

    def print_condition(self):
        #prints conditions
        if self.conditiontime > 0:
            print('')
            print('Your opponent is ' , str(self.condition), 'for the next ' , str(self.conditiontime) ,' turns')
        elif self.conditiontime > 1000:
            print('')
            print('Your opponent is ', str(self.condition), ' until the end of time')
        else:
            print('')
            print('The opponent has no lasting conditions')

    def get_condition(self):
        return [self.condition,self.conditiontime]

    def heal_user(self,heal):
        self.user.health += heal

    def condition_check_attackD(self, damage):
        if self.condition == 'weak':
            damage -= 5
            return int(damage)
        elif self.condition == 'enraged':
            damage += 10
            return int(damage)
        else:
            return damage

    def condition_check_attackC(self, chance):
        if self.condition == 'focus':
            chance += 10
            return int(chance)
        elif self.condition == 'slowed':
            chance -= 10
            return int(chance)
        else:
            return chance
    def set_perm_condition(self,condition,time):
        ### changed to not perm
        self.permcondition = condition
        self.conditiontime = time

    def condition_check_perm(self):
        if self.permcondition == 'burning' and self.conditiontime > 0:
            self.take_damage(10)
            print('The opponent take 10 burning damage')
            self.print()
        elif self.permcondition == 'bleeding' and self.conditiontime > 0:
            self.take_damage(5)
            print('The opponent take 5 bleeding damage')
            self.print()




class user ():
    def __init__(self,name,weapon,health,beans,maxhealth):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.beans = beans
        self.conditiontime = 0
        self.condition = ''
        self.inventory = ['Rusty Sword']
        self.permcondition = ''
        self.maxhealth = maxhealth
        self.exp = 0

    def __repr__(self):
        return self.name + '\n' +'Health: ' + str(self.health) + '\n'



    def get_inventory(self):
        count = 1
        for i in self.inventory:
            print(count ,'. ',i + ' - ' + (userweapons[i]['weaponrating']))
            count += 1

    def acquire(self, item):
        self.inventory.append(item)
        print('you acquired the ', str(item))

    def equip(self,item):
            if int(item) == 0:
                raise Exception('nope')
            self.weapon = self.inventory[int(item) - 1]
            print(str(self.inventory[int(item) - 1]) , 'equipped')


    def gain_beans(self,beans):
        self.beans += beans

    def get_health(self):
        return self.health

    def gain_health(self,health):
        self.health += health
        if self.health > self.maxhealth:
            self.health = self.maxhealth
            print('You are at maximum health')
            return
        if health > 0:
            print('*-*-* ',str(self.name), ' + ', str(health), " hp *-*-*")

    def gain_exp(self,exp,prev):
        """
        :param exp: experience gained
        :param prev: experience before gaining
        :return: player gains experience and levels up if necessary
        """
        self.exp += exp
        if 150 < self.exp <= 300 :

            if prev < 150:
                print('Level up !!!')
                print('')
                time.sleep(1)
                print('you have reached level 2')
                print('')
                self.health = 120
                self.maxhealth = 120
            else:
                print('Level 2')
                print('Max Health: 120')
                self.maxhealth = 120
        if 300 < self.exp <= 600:
            if prev < 300:
                print('Level up !!!')
                print('')
                time.sleep(1)
                print('you have reached level 3')
                print('')
                print('Max Health increased to 150')
                print('')
                self.health = 150
                self.maxhealth = 150
            else:
                print('Level 3')
                print('Max Health: 150')
                self.maxhealth = 150
        if 600 < self.exp <= 1000:

            if prev < 600:
                print('Level up !!!')
                print('')
                time.sleep(1)
                print('you have reached level 4')
                print('')
                print('Max Health increased to 200')
                print('')
                self.health = 200
                self.maxhealth = 200
            else:
                print('Level 4')
                print('Max Health: 200')
                self.maxhealth = 200

    def get_beans(self):
        return self.beans

    def get_name(self):
        return self.name

    def get_weapon(self):
        return self.weapon

    def take_damage(self,damage):
        self.health -= damage
        if damage > 0:
            print('You take ', damage, ' damage')
        if self.health < 1:
            death()


    def print(self):
        time.sleep(1)
        print('')
        print('<><><><><><><><><><>')
        print(self.name)
        print('Health: ', str(self.health))
        print("Weapon: " , str(self.weapon))


    def get_condition(self):
        return [self.condition,self.conditiontime]

    def set_condition(self,condition,permanence):
        """
        :param condition:
        :param permanence: how many turns
        :return:
        """
        self.condition = condition
        self.conditiontime = permanence

    def print_condition(self):
        if self.conditiontime > 0:
            print('')
            print('You are ' , str(self.condition), 'for the next ' , str(self.conditiontime) ,' turns')
        elif self.conditiontime > 1000:
            print('')
            print('You are ', str(self.condition), ' until the end of time')
        else:
            print('')
            print('You have no lasting conditions')

    def reset_conditions(self):
        self.conditiontime = 0
        self.condition = 0
        self.permcondition = ''

    def set_perm_condition(self,condition,time):
        """
        :param condition: condition being inflicted
        :param time: permanence
        :return: void
        """
        self.permcondition = condition
        self.conditiontime = time

    def condition_check_perm(self):
        ### changed from perm to not
        time.sleep(1)
        if self.permcondition == 'burning' and self.conditiontime > 0:
            self.take_damage(10)
            print('** burning **')
            self.print()
        elif self.permcondition == 'bleeding' and self.conditiontime > 0:
            self.take_damage(5)
            print('** bleeding **')
            self.print()

    def condition_check_attackD(self,damage):
        if self.condition == 'weak':
            damage -= 5
            return int(damage)
        elif self.condition == 'enraged':
            damage += 10
            return int(damage)
        else :
            return damage

    def condition_check_attackC(self,chance):
        if self.condition == 'focus':
            chance += 10
            return int(chance)
        elif self.condition == 'slowed':
            chance -= 10
            return int(chance)
        else :
            return chance

    def next_turn(self):
        self.conditiontime -= 1


class battle():
    def __init__(self, user, monster,monsterinstance):
        self.monster = monster
        self.user = user
        self.monsterinstance = monsterinstance

    def __str__(self):
        return str(self.user.get_name()) + ' vs. '+ str(self.monsterinstance.get_name() + ' the ' + str(self.monsterinstance.type))

    def get_monster(self):
        return str(self.monsterinstance)

    def get_attack(self):
        print('')
        print('*-*-*-*-* *-*-*-*-* *-*-*-*-* ATTACK *-*-*-*-* *-*-*-*-*' )
        time.sleep(1)

        print('')
        print('Choose your attack')
        print(userweapons[self.user.get_weapon()]['attacklist'])
        print('')
        while True:
            choice = input('Select an attack: ')
            if choice in userweapons[self.user.get_weapon()]['attacklist']:
                break
        return choice
    def condition_application_from_monster(self,attack):
        # checks who the condition from monster attack is supposed to be applied to and applies it
        if (self.monster)[attack]['conditions'][0] != '':
            if (self.monster)[attack]['conditions'][0] == 'enraged' or (self.monster)[attack]['conditions'][0] == 'focused':
                self.monsterinstance.set_condition((self.monster)[attack]['conditions'][0],
                                                   (self.monster)[attack]['conditions'][1])
                self.monsterinstance.print_condition()
            else:
                self.user.set_condition((self.monster)[attack]['conditions'][0],
                                        (self.monster)[attack]['conditions'][1])
                self.user.print_condition()
        if (self.monster)[attack]['conditions'][0] != '':
            if (self.monster)[attack]['conditions'][0] == 'bleeding':
                self.user.set_perm_condition('bleeding', (self.monster)[attack]['conditions'][1])
            if (self.monster)[attack]['conditions'][0] == 'burning':
                self.user.set_perm_condition('burning', (self.monster)[attack]['conditions'][1])

    def condition_application_check(self, attack):
        #checks who the condition from user weapon is supposed to be applied to and applies it
        if (userweapons[self.user.weapon][attack]['conditions'][0]) != '':
            if userweapons[self.user.weapon][attack]['conditions'][0] == 'enraged' or userweapons[self.user.weapon][attack]['conditions'][0] == 'focused':
                self.user.set_condition((userweapons[self.user.weapon][attack]['conditions'][0]),
                                        (userweapons[self.user.weapon][attack]['conditions'][1]))
                self.user.print_condition()
            else:
                self.monsterinstance.set_condition((userweapons[self.user.weapon][attack]['conditions'][0]),
                                                   (userweapons[self.user.weapon][attack]['conditions'][1]))
                self.monsterinstance.print_condition()
        if (userweapons[self.user.weapon][attack]['conditions'][0]) != '':
            if (userweapons[self.user.weapon][attack]['conditions'][0]) == 'bleeding':
                self.monsterinstance.set_perm_condition('bleeding',(userweapons[self.user.weapon][attack]['conditions'][1]))
            if (userweapons[self.user.weapon][attack]['conditions'][0]) == 'burning':
                self.monsterinstance.set_perm_condition('burning',(userweapons[self.user.weapon][attack]['conditions'][1]))
    def hit_print(self,hit,damage,heal):
        if damage > 0:
            print(hit, damage, 'damage')
            if heal > 0:
                print('The spell heals ', heal, 'health')
        elif damage < 0:
            print('uh oh')
        elif heal > 0 :
            print(hit, heal, 'health')
        else:
            print(hit)


    def attack(self,attack):
        """
        :param attack: gets attack from get_attack
        damage/chance/text etc are all inherited from user class accessing the userweapons dictionary
        :return: no return statement necessary
        """
        ####get attack stats below
        if 'True':
            damage = userweapons[self.user.get_weapon()][attack]['damage']
            chance = userweapons[self.user.get_weapon()][attack]['chance']
            text = userweapons[self.user.get_weapon()][attack]['text']
            heal = userweapons[self.user.get_weapon()][attack]['heal']
            hit = userweapons[self.user.get_weapon()][attack]['hit']
            chance = self.user.condition_check_attackC(chance)
            damage = self.user.condition_check_attackD(damage)

        print('')
        print(text)
        x = random.randint(0,100)
        time.sleep(1.5)
        ####this is checking if the opponent confused
        if (self.monsterinstance.get_condition()[0] != 'confused' or self.monsterinstance.get_condition()[1] < 1):
            if x < chance:
                print('')
                print('Your attempt was successful!')
                print('')
                if userweapons[self.user.get_weapon()]['name'] == 'Staff of Chaos':
                    x = random.randint(-2,4)
                    damage = damage * x
                self.hit_print(hit,damage,heal)
                self.monsterinstance.take_damage(damage)
                self.condition_application_check(attack)
                self.user.gain_health(heal)
                self.monsterinstance.print()
                self.user.print()
            else:
                print('')
                print('You missed :(')
        else:
            print('')
            print('Your attempt was successful!')
            if userweapons[self.user.get_weapon()]['name'] == 'Staff of Chaos':
                x = random.randint(-2, 4)
                damage = damage * x
            print('')
            self.hit_print(hit,damage,heal)
            self.user.gain_health(heal)
            self.condition_application_check(attack)
            self.monsterinstance.take_damage(damage)
            self.monsterinstance.print()
            self.user.print()


    def defense(self):
        time.sleep(1.5)
        print('')
        print('*-*-*-*-* *-*-*-*-* *-*-*-*-* DEFENSE *-*-*-*-* *-*-*-*-*')
        attack = self.monsterinstance.random_attack()
        if self.monsterinstance.get_condition()[0] == 'frozen' and self.monsterinstance.get_condition()[1] > 0:
            print('The enemy is frozen')
        elif ((self.monster)[attack]['blockable'] == True) and (self.user.get_condition()[0] != 'confused' or self.user.get_condition()[1] < 1):
            print('')
            print((self.monster)[attack]['text'])
            print('')
            print('Choose your defense')
            print(userweapons[self.user.get_weapon()]['deflist'])
            print('')
            while True:
                choice = input('Select an defense: ')
                if choice in userweapons[self.user.get_weapon()]['deflist']:
                    break
            damage = (self.monster)[attack]['damage'][self.monsterinstance.level-1]
            heal = (self.monster)[attack]['heal'][self.monsterinstance.get_level()-1]
            aim = (self.monster)[attack]['aim']
            chance = (userweapons[self.user.weapon][choice]['chance']) - aim
            damage = self.monsterinstance.condition_check_attackD(damage)
            chance = self.user.condition_check_attackC(chance)
            response = (userweapons[self.user.weapon][choice]['damage'])
            x = random.randint(0, 100)
            time.sleep(1.5)
            if x < chance:
                print('')
                print('Your attempt was successful!')
                damage = int(damage * (userweapons[self.user.weapon][choice]['damagetaken']))
                self.user.take_damage(damage)
                self.monsterinstance.take_damage(response)
                if response > 0:
                    print('The enemy takes ', response, ' damage')
                self.user.print()
                self.monsterinstance.print()
                print('')
            else:
                print('')
                print('Your ', choice , ' failed')
                print('')
                self.condition_application_from_monster(attack)
                self.user.take_damage(damage)
                self.monsterinstance.heal(heal)
                self.user.print()
        else:
            time.sleep(1.5)
            print('')
            print((self.monster)[attack]['text'])
            print('')
            damage = (self.monster)[attack]['damage'][self.monsterinstance.level-1]
            heal = (self.monster)[attack]['heal'][self.monsterinstance.get_level()-1]
            damage = self.monsterinstance.condition_check_attackD(damage)
            print('')


            self.user.take_damage(damage)
            self.condition_application_from_monster(attack)
            self.monsterinstance.take_damage
            self.monsterinstance.heal(heal)
            self.user.print()
            self.monsterinstance.print()

    def reward(self):
        self.user.set_condition('',0)
        self.user.set_perm_condition('', 0)
        time.sleep(1)
        chest(self.monsterinstance.reward)
        self.user.gain_beans(self.monsterinstance.get_beans())
        self.user.gain_exp(self.monsterinstance.get_exp(),self.user.exp)
#class bossbattle(battle):
   # def __str__(self):
   #     return "Final Battle: \n " + str(self.user.get_name()) + ' vs. ' + str(self.monsterinstance.get_name() + ' the ' + str(self.monsterinstance.type))


def battlesequence(battle):
    print('')
    battleintro(battle)
    print('')
    time.sleep(1.5)
    while battle.monsterinstance.get_health() > 0:
        if (battle.user.get_condition()[0] != 'frozen' or battle.user.get_condition()[1] < 1):
            battle.attack(battle.get_attack())
            if battle.monsterinstance.get_health() <= 0:
                break
        battle.defense()
        if battle.user.get_health() <= 0:
            death()
        battle.user.condition_check_perm()
        battle.monsterinstance.condition_check_perm()
        if battle.user.get_health() <= 0:
            death()
        if battle.monsterinstance.get_health() <= 0:
            break
        battle.user.print_condition()
        battle.monsterinstance.print_condition()
        battle.user.next_turn()
        battle.monsterinstance.next_turn()
    time.sleep(1.5)
    print('')
    battle.reward()
    battlefinish(battle)





rustysword = {'name':'Rusty Sword', 'attacklist':['heavy','light'],'deflist':['parry','dodge'], 'hands':1,
              'heavy':{'conditions':['enraged',0],'damage':18,'chance':45, 'heal':0,
                     'text':'You lunge forward swinging the rusty blade with all your might',
                       'hit':'Your heavy attack hits for '},
              'light':{'conditions':['',0],'damage':10,'chance':70, 'heal':0,
                     'text':'With a quick step you thrust the blade at your opponent',
                       'hit':'Your light attack hits for '},
              'parry':{'damagetaken':0,'chance':35,'damage':5}, 'dodge':{'damagetaken':0,'chance':50,'damage':0},
              'weaponrating':"1 star",'basedamage':'10 hp'}

SharpenedBlade = {'name':'Sharpened Blade', 'attacklist':['heavy','light'],'deflist':['parry','dodge'], 'hands':1,
              'heavy':{'conditions':['',0],'damage':25,'chance':50, 'heal':0,
                     'text':'With expert precision, you jab forward with the sharpened blade',
                       'hit':'Your heavy attack hits for '},
              'light':{'conditions':['',0],'damage':15,'chance':70, 'heal':0,
                     'text':'With a quick step you thrust the blade at your opponent',
                       'hit':'Your light attack hits for '},
              'parry':{'damagetaken':0,'chance':35,'damage':10}, 'dodge':{'damagetaken':0,'chance':50,'damage':0},
              'weaponrating':"2 stars",'basedamage':'15 hp'}

FlameStaff = {'name':'Flame Staff', 'attacklist':['fireball','heal'],'deflist':['pray for safety','dodge'], 'hands':1,
              'fireball':{'conditions':['burning',2],'damage':15,'chance':50, 'heal':0,
                     'text':'Flames shoot from the end of the staff as you recite the ancient words',
                       'hit':'The fireball hits for '},
              'heal':{'conditions':['',0],'damage':0,'chance':60, 'heal':8,
                     'text':'Green light floods the room as you recite the ancient words',
                       'hit':'Your spell lands for '},
              'pray for safety':{'damagetaken':0.2,'chance':60,'damage':0}, 'dodge':{'damagetaken':0,'chance':50,'damage':0},
              'weaponrating':"2.5 stars",'basedamage':'20 hp'}

SwordofFocus = {'name':'Sword of Focus', 'attacklist':['concentrate','attack'],'deflist':['think','dodge','parry'], 'hands':1,
              'concentrate':{'conditions':['focused',3],'damage':5,'chance':60, 'heal':5,
                     'text':'Blood gushes from your ears as you think harder than you have ever thunk',
                       'hit':'the spell hits for'},
              'attack':{'conditions':['',0],'damage':25,'chance':50, 'heal':0,
                     'text':'Calm and composed, you swing the hefty blade with purpose',
                       'hit':'Your attack lands for '},
              'think':{'damagetaken':0.5,'chance':100,'damage':0}, 'dodge':{'damagetaken':0,'chance':50,'damage':0},
                'parry':{'damagetaken':0,'chance':40,'damage':10},'weaponrating':"2.5 stars",'basedamage':'25 hp'}


MalletofMalice = {'name':'Mallet of Malice', 'attacklist':['fear','terrorize'],'deflist':['headstrong','dodge'], 'hands':1,
              'fear':{'conditions':['enraged',3],'damage':0,'chance':80, 'heal':0,
                     'text':'Your blood boils as you begin to feel the rage taking over',
                       'hit':'Anger Consumes you'},
              'terrorize':{'conditions':['',0],'damage':30,'chance':50, 'heal':0,
                     'text':'With a bloodcurdling scream you charge the opponent',
                       'hit':'Your vicious attack lands for '},
              'headstrong':{'damagetaken':0.4,'chance':100,'damage':0}, 'dodge':{'damagetaken':0,'chance':50,'damage':0},
              'weaponrating':"3 stars",'basedamage':'30 hp'}

SanguineSword = {'name':'Sanguine Sword', 'attacklist':['bloodlust','prick'],'deflist':['parry','dodge'], 'hands':1,
              'bloodlust':{'conditions':['',0],'damage':30,'chance':50, 'heal':0,
                     'text':'The blade emits a dull red glow as you swing it towards your foe',
                       'hit':'The attack hits for '},
              'prick':{'conditions':['bleeding',2],'damage':5,'chance':80, 'heal':0,
                     'text':'With quick hands you reach for the opponent with the sharp tip of the blade',
                       'hit':'Sometimes a tiny poke is all it takes, the attack hits for '},
              'parry':{'damagetaken':0,'chance':45,'damage':10}, 'dodge':{'damagetaken':0,'chance':60,'damage':0},
              'weaponrating':"3 stars",'basedamage':'30 hp'}

StaffofChaos = {'name':'Staff of Chaos', 'attacklist':['unleash','entropy'],'deflist':['parry','dodge'], 'hands':1,
              'entropy':{'conditions':['enraged',2],'damage':5,'chance':60, 'heal':0,
                     'text':'Something is wrong',
                       'hit':'Yes something was very wrong, '},
              'unleash':{'conditions':['',0],'damage':20,'chance':70, 'heal':0,
                     'text':'reality fractures as the staff slams against the floor, something is wrong',
                       'hit':'The attack hits for  '},
              'parry':{'damagetaken':0,'chance':45,'damage':10}, 'dodge':{'damagetaken':0,'chance':60,'damage':0},
              'weaponrating':"? stars",'basedamage':'40 hp'}

SwordofBloodandFlame =  {'name':'Sword of Blood and Flame', 'attacklist':['bleed','enflame'],'deflist':['parry','dodge'], 'hands':1,
              'bleed':{'conditions':['bleeding',2],'damage':35,'chance':50, 'heal':0,
                     'text':'Your eyes go blood-shot as the blade flies from your hand with a mind of it\'s own',
                       'hit':'The attack hits for '},
              'enflame':{'conditions':['burning',1],'damage':40,'chance':45, 'heal':0,
                     'text':'The metal turns red hot as you lunge forward with the weapon',
                       'hit':'The attack hits for  '},
              'parry':{'damagetaken':0,'chance':50,'damage':15}, 'dodge':{'damagetaken':0,'chance':60,'damage':0},
              'weaponrating':"4 stars",'basedamage':'35 hp'}

SwordandShield = {'name':'Sword and Shield', 'attacklist':['heavy','light'],'deflist':['parry','block'], 'hands':1,
              'heavy':{'conditions':['',0],'damage':40,'chance':50, 'heal':0,
                     'text':'With expert precision, you jab forward with the sharpened blade',
                       'hit':'Your heavy attack hits for '},
              'light':{'conditions':['',0],'damage':25,'chance':70, 'heal':0,
                     'text':'With a quick step you thrust the blade at your opponent',
                       'hit':'Your light attack hits for '},
              'parry':{'damagetaken':0,'chance':45,'damage':20},'block':{'damagetaken':0,'chance':100,'damage':0},
              'weaponrating':"4 stars",'basedamage':'40 hp'}

ShadowDagger = {'name':'Shadow Dagger', 'attacklist':['backstab','puncture'],'deflist':['run','hide'], 'hands':1,
              'backstab':{'conditions':['bleeding',2],'damage':35,'chance':60, 'heal':0,
                     'text':'With cat-like speed you dart around the opponent, blindsiding them with a quick stab',
                       'hit':'Your backstab hits for '},
              'puncture':{'conditions':['bleeding',1],'damage':25,'chance':70, 'heal':0,
                     'text':'With a quick step you thrust the blade at your opponent',
                       'hit':'The attack hits for '},
              'run':{'damagetaken':0,'chance':50,'damage':0},'hide':{'damagetaken':0,'chance':60,'damage':0},
              'weaponrating':"3 stars",'basedamage':'25 hp'}

LavaStaff = {'name':'Lava Staff', 'attacklist':['incinerate','heal'],'deflist':['pray for safety','dodge'], 'hands':1,
              'incinerate':{'conditions':['burning',3],'damage':35,'chance':50, 'heal':0,
                     'text':'Flames shoot from the end of the staff as you recite the ancient words',
                       'hit':'The fireball hits for '},
              'heal':{'conditions':['',0],'damage':0,'chance':60, 'heal':20,
                     'text':'Green light floods the room as you recite the ancient words',
                       'hit':'Your spell lands for '},
              'pray for safety':{'damagetaken':0.2,'chance':60,'damage':0}, 'dodge':{'damagetaken':0,'chance':50,'damage':0},
              'weaponrating':"3.5 stars",'basedamage':'35 hp'}



#userweapons is a dictionary of weapons
userweapons = {'Rusty Sword':rustysword,'Sharpened Blade':SharpenedBlade,
               'Flame Staff':FlameStaff,'Sword of Focus':SwordofFocus,
               'Mallet of Malice':MalletofMalice,'Sanguine Sword':SanguineSword,
               'Staff of Chaos':StaffofChaos,'Sword of Blood and Flame':SwordofBloodandFlame,
               'Sword and Shield':SwordandShield, 'Lava Staff':LavaStaff,'Shadow Dagger':ShadowDagger}


#########monsters


Goblin = {'Scavenge':{'damage':[0,0,0], 'blockable':False, 'heal':[4,6,8], 'aim':0, 'conditions':['',0],
            'text':'The goblin scampers around the room, collecting little bits of filth from off of the floor'},
         'Claw':{'damage':[5,8,10], 'blockable':True, 'heal':[0,0,0], 'aim':0, 'conditions':['',0],
            'text':'The goblin growls and lunges with its claws outstretched'}, 'attacklist':['Scavenge','Claw']}

Beast = {'Rampage':{'damage':[6,10,12], 'blockable':True, 'heal':[0,0,0], 'aim':-10, 'conditions':['bleeding',1],
            'text':'The beast roars and charges forward chaotically'},
         'Snarl':{'damage':[4,6,8], 'blockable':True, 'heal':[0,0,0], 'aim':0, 'conditions':['',0],
            'text':'The beast flashes a toothy grin and snaps down with its massive jaws'}, 'attacklist':['Rampage','Snarl']}


Cockatrice = {'Peck':{'damage':[8,11,16], 'blockable':True, 'heal':[0,0,0], 'aim':0, 'conditions':['bleeding',2],
            'text':'The bird squacks and chirps as it attacks'},
         'Lay':{'damage':[0,0,0], 'blockable':False, 'heal':[6,8,10], 'aim':0, 'conditions':['weak',1],
            'text':'The Cockatrice takes a deep breath and lays a massive egg'}, 'attacklist':['Peck','Lay']}

Wraith = {'Haunt':{'damage':[0,0,0], 'blockable':True, 'heal':[0,0,0], 'aim':0, 'conditions':['frozen',2],
            'text':'The monster floats up into the air while crooning a haunting tune'},
         'Nightmare':{'damage':[8,12,16], 'blockable':False, 'heal':[6,8,10], 'aim':0, 'conditions':['weak',1],
            'text':'The ghoul penetrates your mind castle, assaulting your very existence'}, 'attacklist':['Haunt','Nightmare']}

FrozenGolem = {'Smash':{'damage':[15,20,22], 'blockable':True, 'heal':[0,0,0], 'aim':0, 'conditions':['',0],
            'text':'The beast leans back before smashing both of it\'s massive fists into the ground'},
         'Freeze':{'damage':[0,0,0], 'blockable':True, 'heal':[0,0,0], 'aim':0, 'conditions':['frozen',2],
            'text':'A cloud of white fog materializes around the Golem and wafts towards you'},
               'Frostbite':{'damage':[5,6,8], 'blockable':True, 'heal':[0,0,0], 'aim':0, 'conditions':['frozen',1],
            'text':'The monster floats up into the air while crooning a haunting tune'}, 'attacklist':['Smash','Freeze','Frostbite']}

Demon = {'Sin':{'damage':[15,20,25], 'blockable':True, 'heal':[0,0,0], 'aim':0, 'conditions':['',0],
            'text':'The demon lifts its hood to show an unbelievably gruesome scene of gore'},
         'Sacrifice':{'damage':[0,0,0], 'blockable':False, 'heal':[-5,-8,-15], 'aim':0, 'conditions':['bleeding',3],
            'text':'The demon begins to cough, spewing blood and guts accross the floor'}, 'attacklist':['Sin','Sacrifice']}

FireSpirit = {'Incinerate':{'damage':[12,18,24], 'blockable':True, 'heal':[0,0,0], 'aim':0, 'conditions':['burning',2],
            'text':'The spirit lifts a molten arm as blue flame shoots from it\'s fingertips'},
         'Explosion':{'damage':[18,22,25], 'blockable':True, 'heal':[0,0,0], 'aim':-25, 'conditions':['burning',1],
            'text':'The spirits eyes roll back as a thunderous sound fills the room'}, 'attacklist':['Incinerate','Explosion']}

monsterattacks = {'Goblin':Goblin,"Beast":Beast,'Cockatrice':Cockatrice,'Wraith':Wraith,'Frozen Golem':FrozenGolem,'Demon':Demon,'Fire Spirit':FireSpirit}

####monsterinstances
################### type      name   health  beans, exp level reward
monster1 = monster('Goblin','Reginald',50,35,50,1,'Sharpened Blade')
monster2 = monster('Beast', 'Archibald',60,45,75,1,'Flame Staff')
monster3 = monster('Cockatrice', 'Chesmund',65,60,80,1,'Sword of Focus')
monster4 = monster('Wraith', 'Buford',80,50,90,1,'Mallet of Malice')
monster5 = monster('Frozen Golem', 'Winston',80,75,100,1,'Sanguine Sword')
monster6 = monster('Demon', 'Martin',100,90,100,2,'Sword of Blood and Flame')
monster7 = monster('Wraith', 'Alfred',110,100,110,2,'Lava Staff')
monster8 = monster('Fire Spirit','Bartholomew', 90,100,100,1,'Shadow Dagger')
monster9 = monster('Goblin','Gerald',100,80,150,3, 'Sword and Shield')
monster10 = monster('Cockatrice','Baxter',130,120,140,2,'reward')

###playerinstance
player1 = user('Borgus','Rusty Sword',100,0,100)

battle1 = battle(player1,Goblin,monster1)
battle2 = battle(player1,Beast,monster2)
battle3 = battle(player1,Cockatrice,monster3)
battle4 = battle(player1,Wraith,monster4)
battle5 = battle(player1,FrozenGolem,monster5)
battle6 = battle(player1,Demon,monster6)
battle7 = battle(player1,Wraith,monster7)
battle8 = battle(player1,FireSpirit,monster8)
battle9 = battle(player1,Goblin,monster9)
battle10 = battle(player1,Cockatrice,monster10)

####letter game instances

letters1 = lettergame('refried beans',5)
letters2 = lettergame('jack and the beanstalk',5)
letters3 = lettergame('is a chickpea a bean',5)





options = ['stats','Stats','save','Save','intro','Intro','1','2','3','4','5','6','7','8','9','10','11','12','Inventory','inventory','Reset','reset']
closed = {'1':False,'2':False,'3':False,'4':False,'5':False,'6':False,'7':False,'8':False,'9':False,'10':False,'11':False,'12':False}
#print(player1.get_weapon())


def battleintro(battle):
    print('Let the battle begin!')

def battlefinish(battle):
    print('Victory!')


def equipmentcheck ():
    player1.get_inventory()
    while True:
        try:
            player1.equip(input("select the number of the weapon you wish to equip: "))
            break
        except:
            continue
    print('')
    time.sleep(2)

def chest(item):
    time.sleep(1)
    print('')
    print('  ------------------------------')
    print(' |       |              |       |')
    print(' |----------[  <()>  ]----------|    ')
    print(' |       |              |       |')
    print(' |       |              |       |')
    print('| _______|______________|_______ |')
    input('press enter to open...')

    player1.acquire(item)
    print('')
    time.sleep(1)

def title():
    input('press enter')
    print('')
    print(
        '******************************************************************************************************************* ')
    time.sleep(.2)
    print(
        '******************************************************************************************************************* ')
    time.sleep(.2)
    print(
        '**                                                                      **                                       **')
    time.sleep(.2)
    print(
        '** BBBBBBBBBB      EEEEEEEEEEE        AAAA           NNNN        NNN    **       22222222222222222               ** ')
    time.sleep(.2)
    print(
        '** BBB     BBB     EEEE             AAA  AAA         NNNNN       NNN    **      22222222222222222222             ** ')
    time.sleep(.2)
    print(
        '** BBB      BBB    EEE             AAA    AAA        NNNNNN      NNN    **                    22222222           ** ')
    time.sleep(.2)
    print(
        '** BBB     BBB     EEEE           AAA      AAA       NNN  NNN    NNN    **                        222222         ** ')
    time.sleep(.2)
    print(
        '** BBBBBBBBB       EEEEEEEEEEE    AAAAAAAAAAAA       NNN   NNN   NNN    **                          222222       ** ')
    time.sleep(.2)
    print(
        '** BBB     BBB     EEEE           AAAAAAAAAAAA       NNN    NNN  NNN    **                            22222      ** ')
    time.sleep(.2)
    print(
        '** BBB      BBB    EEE            AAA      AAA       NNN     NNN NNN    **                            222222     ** ')
    time.sleep(.2)
    print(
        '** BBB     BBB     EEEE           AAA      AAA       NNN      NNNNNN    **                           222222      ** ')
    time.sleep(.2)
    print(
        '** BBBBBBBBBB      EEEEEEEEEEE    AAA      AAA       NNN       NNNNN    **                          222222       ** ')
    time.sleep(.2)
    print(
        '**************************************************************************                        222222         ** ')
    time.sleep(.2)
    print(
        '**************************************************************************                      222222           ** ')
    time.sleep(.2)
    print(
        '**    QQQQQQQQQ         UU     UU    EEEEEEE     SSSSSSSSS   TTTTTTTTT  **                    222222             ** ')
    time.sleep(.2)
    print(
        '**  QQQ       QQQ       UU     UU    EEE        SSSSSSSSS    TTTTTTTTT  **                  2222222              ** ')
    time.sleep(.2)
    print(
        '** QQQ          QQQ     UU     UU    EE         SSS             TTT     **               222222                  ** ')
    time.sleep(.2)
    print(
        '** QQQ           QQQ    UU     UU    EEE        SSS             TTT     **           2222222                     ** ')
    time.sleep(.2)
    print(
        '** QQQ     QQQ   QQQ    UU     UU    EEEEEEE    SSSSSSSSS       TTT     **         222222                        ** ')
    time.sleep(.2)
    print(
        '**  QQQ     QQQ QQQ     UU     UU    EEE        SSSSSSSSS       TTT     **      222222                           ** ')
    time.sleep(.2)
    print(
        '**   QQQ      QQQQ      UU     UU    EE                SSS      TTT     **    222222                             **  ')
    time.sleep(.2)
    print(
        '**     QQQQQQQQQQQ      UUU   UUU    EEE         SSSSSSSSS      TTT     **    2222222222222222222222222222       ** ')
    time.sleep(.2)
    print(
        '**              QQQ       UUUUU      EEEEEEE     SSSSSSSSS      TTT     **    2222222222222222222222222222       ** ')
    time.sleep(.2)
    print(
        '**                                                                      **                                       **')
    time.sleep(.2)
    print(
        '******************************************************************************************************************* ')
    time.sleep(.2)
    print(
        '*******************************************************************************************************************')
    print('')
    print('')
    print('start or credits:')
    start = input(str())
    while start != 'start' or 'credits':
        if start == 'start':
            print('')
            print('entering bean world...')
            time.sleep(.5)
            print('')
            print('...')
            time.sleep(.5)
            print('')
            print('...')
            print('')
            player1.name = input('Enter your Name: ')
            break
        elif start == 'credits':
            print('')
            print('-BeanQuest 2-')
            time.sleep(1)
            print('A game by Lev')
            time.sleep(1.5)
            print('')
            print('start or credits:')
            start = input(str())
        else:
            print('')
            print('start or credits:')
            start = input(str())

def scene1():
    print('')
    time.sleep(2)
    print('suddenly you awake in a massive room, it\'s walls covered in intricate carvings')
    print('')
    time.sleep(2)
    print('Twelve doors'
          ' stand before you with their numbers carved deep into black granite')
    print('')
    time.sleep(2)
    print('The strangest part is that there is no furniture')
    print('')
    time.sleep(2)
    print('500 feet from wall to wall there is nothing but empty space')
    print('')
    time.sleep(2)
    print('The only object you can see is a rusty sword laying a few feet in front of where you stand')
    print('')
    time.sleep(2)
    print('You acquired: Rusty Sword')
    print('')
    time.sleep(2)

def intro():
    print('')
    print('')
    time.sleep(2)
    print('welcome', player1.name + ', to the treacherous kingdom of beanworld')
    time.sleep(2.5)
    print('')
    print('It has been 14 years since the chosen one fought valiantly against the beast of the forgotten hellscape')
    time.sleep(3)
    print('')
    print('since that time, the kingdom has been ravaged by famine, fascism, and general monotony')
    time.sleep(3)
    print('')
    print('It would seem that when the beast was destroyed, it took with it something essential to the fabric of our world')

    print('')
    time.sleep(3.5)
    print('for without chaos, there can be no compassion')
    print('')
    time.sleep(3)
    print('nor good, without evil')
    time.sleep(3)
    print('')
    print('')
    print('the ancient ones speak of a hero which will one day restore balance to our empty lives')
    time.sleep(3)
    print('')
    print('one which will finally oppose the reign of the wretched king limus wetbeanicus')
    print('')
    time.sleep(3)
    print('all across the countryside the rumors have spread like beans on toast')
    print('')
    time.sleep(3)
    print('each village home to their own cast of would-be heroes ')
    print('')
    time.sleep(2.5)
    print('and yours is no different')
    print('')
    time.sleep(2.5)
    print('and you are no different')
    print('')
    print('')
    time.sleep(2.5)
    input('press enter to begin your adventure...')

    scene1()

def check_room_completion():
    """
    :return: used in the waiting room function to XX out doors
    which have been completed
    """
    for x in range (1,13):
        if closed[str(x)] == False:
            x = '    '
        else:
            x = '[XX]'

        print(''.join(('-*| ', x ,' |*-')),end='')
    print('')

#def check_game_completion()  ######needs work
   # if roomscompleted > 0
     #   final

def waiting_room():
    print('#**#' * 36)
    print(('# # # # ' * 4) +'# ' + '[ Inventory ] ' + (' # # # # '  * 2) + '[ Reset ]' +(' # # # # '  * 2) + ' [ Stats ]' + ( '# '  * 21))
    print('*##*' * 36)
    print('#[]#' * 36)
    print('*##*' * 36)
    print('#*** /\ ***#' * 12)
    print('#**#/  \#**#' * 8 + '#**#/^^\#**#' + '#**#/  \#**#' * 3)
    print('#* /    \ *#' * 8 + '#* / || \ *#' + '#* /    \ *#' * 3)
    print('#*|*#||#*|*#' * 12)
    print('\ **#||#** /' * 12)
    print(' \**#||#**/ ' * 12)
    print('#**##||##**#' * 12)
    print('#***/##\***#' * 12)
    print('*##******##*' * 12)
    print(''.join([('-**/  ' + str(x) + ' \**-') for x in range(1,10)]) \
          + ''.join([('-**/ ' + str(x) + ' \**-') for x in range(10,13)]))
    print('-*|      |*-' * 12)
    check_room_completion()
    check_room_completion()
    print('--|      |--' * 12)
    print('#***####***#' * 12)
    print('*##******##*' * 12)
    print(('# # # # ' * 5) + '[ Save ] ' + (' # # # # '  * 5) + ' [ Intro ]' + ( '# '  * 21))
    print('*##******##*' * 12)

def entrance(room):
    room = str(room)
    if len(str(room))== 1:
        room = room + ' '
    print( '#####**********#####'*3 )
    print('*-##-/        \-##-*'*3)
    print('*-#-/          \-#-*'*3)
    print('---/     **     \---'+'---/     ',room,'   \---'+'---/     **     \---')
    print('--*I<          >I*--'*3)
    print('--*[I          I]*--'*3)
    print('--*[I          I]*--'* 3)
    print('--*[I          I]*--'* 3)
    print('--*[I          I]*--'*3)
    print('___________________'*3)
    input('Press enter to enter ')
    print('')


def letters():
    wins = 0
    if letters1.game():
        wins += 1
    if letters2.game():
        wins += 1
    if letters3.game():
        wins += 1
    if wins >= 2:
        chest('Staff of Chaos')
    else:
        potion(-20)
        player1.maxhealth -= 20
        'Hahahahaha  not good enough'



def potion(health):
    print('')
    print('before you sits a glass with a heart on it\'s label')
    print('probably shouldn\'t drink something you just found on the ground...')
    print('')
    time.sleep(1)
    print('               ----')
    print('               |  |         ')
    print('               |  |         ')
    print('              /    \         ')
    print('             /      \        ')
    print('            (   <3   )    ')
    print('             \      /    ')
    print('              ------   ')
    print('')
    time.sleep(1)
    player1.gain_health(health)
    print('')
    print('Press enter to drink')
    print('')
    print('You gain ' + str(health) + ' health')




def death():
    raise Exception('hahahaha you died')

def maingame():
    def complete_stats():
        print('')
        print('Rooms Completed: ' + str(roomscompleted))
        print('')
        print('  Character Stats')
        print('  *-*-*-*-*-*-*-*')
        print('')
        print('Current Health: ', player1.get_health())
        print('Maximum Health: ', player1.maxhealth)
        print('  Damage Taken: ', damagetaken)
        print('  *-*-*-*-*-*-*-*  ')
        print('         Beans: ', player1.get_beans())
        print('    Experience: ', player1.exp)
        print(' ')
        print(' ')
        input('Press enter to return...')

    def room_complete(room,roomscompleted):
        options.remove(str(room))
        closed[str(room)] = True
        return roomscompleted + 1

    roomscompleted = 0
    damagetaken = 0
    title()
    intro()



    while True:
        waiting_room()
        print('')
        x = None
        while x not in options:
            print('')
            x = input('Make your Selection: ')
            if x in options:
                break
        if x == '1':
            entrance(1)
            print(battle1)
            battlesequence(battle1)
            roomscompleted = room_complete(1,roomscompleted)
        elif x == '2':
            entrance(2)
            print(battle2)
            battlesequence(battle2)
            roomscompleted = room_complete(2,roomscompleted)
        elif x == '3':
            entrance(3)
            letters()
            roomscompleted = room_complete(3,roomscompleted)
        elif x == '4':
            entrance(4)
            print(battle3)
            battlesequence(battle3)
            roomscompleted = room_complete(4,roomscompleted)
        elif x == '5':
            entrance(5)
            print(battle4)
            battlesequence(battle4)
            potion(25)
            roomscompleted = room_complete(5,roomscompleted)
        elif x == '6':
            entrance(6)
            print(battle5)
            battlesequence(battle5)
            roomscompleted = room_complete(6, roomscompleted)
        elif x == '7':
            entrance(7)
            print('Time winds back and you find yourself back in the main room')
            print('That was Strange...')
            roomscompleted = room_complete(7, roomscompleted)
        elif x == '8':
            entrance(8)
            print(battle6)
            battlesequence(battle6)
            roomscompleted = room_complete(8, roomscompleted)
        elif x == '9':
            entrance(9)
            print(battle7)
            battlesequence(battle7)
            roomscompleted = room_complete(9, roomscompleted)
        elif x == '10':
            entrance(10)
            print(battle10)
            battlesequence(battle8)
            roomscompleted = room_complete(10, roomscompleted)
        elif x == '11':
            entrance(11)
            print(battle9)
            battlesequence(battle9)
            roomscompleted = room_complete(11, roomscompleted)
        elif x == '12':
            entrance(12)
            print(battle10)
            battlesequence(battle10)
            roomscompleted = room_complete(12, roomscompleted)
            print('room 12')
        elif x == 'Save' or x == 'save':
            print('This feature has yet to be implemented')
            print('Please try again soon :)')
        elif x == 'Stats' or x == 'stats':
            complete_stats()
        elif x == 'Intro' or x == 'intro':
            intro()
        elif x == 'Inventory' or x == 'inventory':
            equipmentcheck()
        elif x == 'Reset' or x == 'reset':
            print('This feature has yet to be implemented')
            print('Please try again soon :)')


maingame()



