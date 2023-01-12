import time

class user ():

    def __init__(self,name,weapon,health,beans,maxhealth,weapons):
        
        self.name = name        #user name
        self.weapon = weapon    #user weapon
        self.health = health    #user health
        self.beans = beans      #user beans (currency)
        self.conditiontime = 0  #user condition timer
        self.condition = ''     #user condition
        self.inventory = ['Rusty Sword']    #user inventory
        self.permcondition = ''     #user perm condition
        self.maxhealth = maxhealth #user max health
        self.exp = 0    #user exp
        self.weapons = weapons  #weapons info

    def __repr__(self):
        return self.name + '\n' +'Health: ' + str(self.health) + '\n'

    def get_inventory(self):
        #prints user inventory
        count = 1
        for i in self.inventory:
            print(count ,'. ',i + ' - ' + (self.weapons[i]['weaponrating']))
            count += 1

    def acquire(self, item):
        #adds item to user inventory
        self.inventory.append(item)
        print('you acquired the ', str(item))

    def equip(self,item):
        #equips item
            if int(item) == 0:
                raise Exception('nope')
            self.weapon = self.inventory[int(item) - 1]
            print(str(self.inventory[int(item) - 1]) , 'equipped')


    def gain_beans(self,beans):
        #increases self.beans by beans
        self.beans += beans

    def get_health(self):
        #returns user health
        return self.health

    def gain_health(self,health):
        #increases user health by health unless at max
        self.health += health
        if self.health > self.maxhealth:
            self.health = self.maxhealth
            print('You are at maximum health')
            return
        elif health != 0:
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

    def get_beans(self):
        return self.beans

    def get_name(self):
        return self.name

    def get_weapon(self):
        return self.weapon

    def take_damage(self,damage):
        # user takes damage
        self.health -= damage
        if damage > 0:
            print('You take ', damage, ' damage')
        if self.health < 1:
            self.death()

    def death(self):
        #print death message and raise error

        time.sleep(1)
        print("")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("")
        print("Alas your journey has ended \n")
        time.sleep(1)
        print("These struggles and triumphs suffered for naught\n")
        time.sleep(1)
        print("History has been washed clean of your mortal stain\n")
        time.sleep(1)
        raise ValueError('Death...')
        


    def print(self):
        #prints user info mid battle
        time.sleep(1)
        print('')
        print('<><><><><><><><><><>')
        print(self.name)
        print('Health: ', str(self.health))
        


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
        #prints user conditions
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
        #resets user conditions and condition timer
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
        #checking for perm conditions
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
        #checking for damage modifying conditions
        if self.condition == 'weak':
            damage -= 5
            return int(damage)
        elif self.condition == 'enraged':
            damage += 10
            return int(damage)
        else :
            return damage

    def condition_check_attackC(self,chance):
        #checking for chance modifying conditions
        if self.condition == 'focus':
            chance += 10
            return int(chance)
        elif self.condition == 'slowed':
            chance -= 10
            return int(chance)
        else :
            return chance

    def next_turn(self):
        #advancing condition timer
        self.conditiontime -= 1