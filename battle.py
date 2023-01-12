
import time
import random

class battle():

    

    def __init__(self, user, monster,monsterinstance):
        self.monster = monster #monster type
        self.user = user #user
        self.monsterinstance = monsterinstance #monster instance

    def __str__(self):
        return str(self.user.get_name()) + ' vs. '+ str(self.monsterinstance.get_name() + ' the ' + str(self.monsterinstance.type))

    def get_monster(self):
        return str(self.monsterinstance)

    def get_attack(self):
        #gets attack from weapon options and returns it
        print('')
        print('*-*-*-*-* *-*-*-*-* *-*-*-*-* ATTACK *-*-*-*-* *-*-*-*-*' )
        time.sleep(1)

        print('')
        print('Choose your attack')
        print(self.user.weapons[self.user.get_weapon()]['attacklist'])
        print('')
        while True:
            choice = input('Select an attack: ')
            if choice in self.user.weapons[self.user.get_weapon()]['attacklist']:
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
        if (self.user.weapons[self.user.weapon][attack]['conditions'][0]) != '':
            if self.user.weapons[self.user.weapon][attack]['conditions'][0] == 'enraged' or self.user.weapons[self.user.weapon][attack]['conditions'][0] == 'focused':
                self.user.set_condition((self.user.weapons[self.user.weapon][attack]['conditions'][0]),
                                        (self.user.weapons[self.user.weapon][attack]['conditions'][1]))
                self.user.print_condition()
            else:
                self.monsterinstance.set_condition((self.user.weapons[self.user.weapon][attack]['conditions'][0]),
                                                   (self.user.weapons[self.user.weapon][attack]['conditions'][1]))
                self.monsterinstance.print_condition()
        if (self.user.weapons[self.user.weapon][attack]['conditions'][0]) != '':
            if (self.user.weapons[self.user.weapon][attack]['conditions'][0]) == 'bleeding':
                self.monsterinstance.set_perm_condition('bleeding',(self.user.weapons[self.user.weapon][attack]['conditions'][1]))
            if (self.user.weapons[self.user.weapon][attack]['conditions'][0]) == 'burning':
                self.monsterinstance.set_perm_condition('burning',(self.user.weapons[self.user.weapon][attack]['conditions'][1]))
    
    def hit_print(self,hit,damage,heal):
        #prints hit message
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
        damage/chance/text etc are all inherited from user class accessing the self.user.weapons dictionary
        :return: no return statement necessary
        """
        ####get attack stats below
        
        damage = self.user.weapons[self.user.get_weapon()][attack]['damage']
        chance = self.user.weapons[self.user.get_weapon()][attack]['chance']
        text = self.user.weapons[self.user.get_weapon()][attack]['text']
        heal = self.user.weapons[self.user.get_weapon()][attack]['heal']
        hit = self.user.weapons[self.user.get_weapon()][attack]['hit']
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
                if self.user.weapons[self.user.get_weapon()]['name'] == 'Staff of Chaos':
                    x = random.randint(-2,4)
                    damage = damage * x
                #succesful hit below
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
            if self.user.weapons[self.user.get_weapon()]['name'] == 'Staff of Chaos':
                x = random.randint(-2, 4)
                damage = damage * x
            print('')
            #succesful hit below
            self.hit_print(hit,damage,heal)
            self.user.gain_health(heal)
            self.condition_application_check(attack)
            self.monsterinstance.take_damage(damage)
            self.monsterinstance.print()
            self.user.print()


    def defense(self):
        #gives the user an oppurtunity to select defensive moves, calculates hit, prints and applies outcome
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
            print(self.user.weapons[self.user.get_weapon()]['deflist'])
            print('')
            #determines defensive move
            while True:
                choice = input('Select a defense: ')
                if choice in self.user.weapons[self.user.get_weapon()]['deflist']:
                    break
            damage = (self.monster)[attack]['damage'][self.monsterinstance.level-1]
            heal = (self.monster)[attack]['heal'][self.monsterinstance.get_level()-1]
            aim = (self.monster)[attack]['aim']
            chance = (self.user.weapons[self.user.weapon][choice]['chance']) - aim
            damage = self.monsterinstance.condition_check_attackD(damage)
            chance = self.user.condition_check_attackC(chance)
            response = (self.user.weapons[self.user.weapon][choice]['damage'])
            x = random.randint(0, 100)
            time.sleep(1.5)
            if x < chance:
                print('')
                print('Your attempt was successful!')
                damage = int(damage * (self.user.weapons[self.user.weapon][choice]['damagetaken']))
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
                #user takes damage/ aquires conditions
                self.condition_application_from_monster(attack)
                self.user.take_damage(damage)
                self.monsterinstance.heal(heal)
                self.user.print()
        else:
            #if the user can not block
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
        #rewards user after a succesful battle
        self.user.set_condition('',0)
        self.user.set_perm_condition('', 0)
        time.sleep(1)
        time.sleep(1)
        print('')
        print('  ------------------------------')
        print(' |       |              |       |')
        print(' |----------[  <()>  ]----------|    ')
        print(' |       |              |       |')
        print(' |       |              |       |')
        print('| _______|______________|_______ |')
        input('press enter to open...')
        
        print('')
        time.sleep(1)
        self.user.acquire(self.monsterinstance.reward)
        self.user.gain_beans(self.monsterinstance.get_beans())
        self.user.gain_exp(self.monsterinstance.get_exp(),self.user.exp)
        time.sleep(1)