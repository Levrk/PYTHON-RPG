import random
import time

class monster():

    def __init__(self,type,name,health,beans,exp,level,reward,monsterattacks):
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
        ##self.attacks = monsterattacks[type]
        self.health = health
        self.beans = beans
        self.exp = exp
        self.type = type
        self.conditiontime = 0
        self.condition = ''
        self.permcondition = ''
        self.reward = reward
        self.monsterattacks = monsterattacks


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
        ####
        return random.choice(self.monsterattacks[str(self.type)]['attacklist'])

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