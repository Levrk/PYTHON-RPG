class lettergame():

    def __init__(self,word,lives):
        self.word = word
        self.letterdict = None
        self.letterlist = []
        self.nummoves = 1
        self.lives = ['X' for i in range(lives)]

    def create_list(self):
        letterlist = []
        for i in range (len(self.word)):
            if self.word[i] not in letterlist:
                letterlist.append(self.word[i])
        self.letterlist = letterlist

    def check_for_loss(self):
        if self.lives == []:
            return True

    def check_for_win(self):
        for i in self.letterdict.keys():
            if self.letterdict[i] == False:
                return False
        return True

    def create_dict(self):
        letterdict = {}
        for i in self.letterlist:
            letterdict[str(i)] = False
            if i == ' ':
                letterdict[str(i)] = True
        self.letterdict = letterdict


    def correct(self,letter):
        self.letterdict[letter.lower()] = True

    def print(self):
        for i in range (len(self.word)):
            print('-*-*-', end='')
        print('')
        for i in range (len(self.word)):
            if self.letterdict[self.word[i]] == True:
                x = str(self.word[i])
            else:
                x = ' '
            print(' ',x ,' ', end='')
        print('')
        for i in range (len(self.word)):
            if self.word[i] == ' ':
                print('     ', end='')
            else:
                print(' ___ ', end='')
        print('')
        print('Lives Remaining: ', self.lives)
    def print_answer(self):
        for i in range (len(self.word)):
            print('-*-*-', end='')
        print('')
        for i in range (len(self.word)):
            x = str(self.word[i])
            print(' ',x ,' ', end='')
        print('')
        for i in range (len(self.word)):
            if self.word[i] == ' ':
                print('     ', end='')
            else:
                print(' ___ ', end='')
        print('')
        print('Lives Remaining: ', self.lives)

    def move(self):
        print('')
        print('')
        print('Move # ',str(self.nummoves))
        print('*-*-*-*-*')
        while True:
            print('')
            letter = input('select a letter: ')
            if letter == self.word:
                return True
            if str.isalpha(letter) and len(letter) == 1:
                break


        #### this in __________________ is my problem
        if letter.lower() in self.letterlist:
            print('')
            print('Good guess')
            print('')
            self.correct(letter)
            self.nummoves += 1

        else:
            print('')
            print('Nope')
            print('')
            self.lives.pop(0)
            self.nummoves += 1



    def game(self):
        self.create_list()
        self.create_dict()
        while True:
            self.print()
            x = self.move()
            if self.check_for_win() or x == True:
                self.print_answer()
                print('You won in ', self.nummoves, 'Moves')
                return True
            elif self.check_for_loss():
                print('You lost in ', self.nummoves, 'Moves')
                return False


letters1 = lettergame('refried beans',10)
letters2 = lettergame('jack and the beanstalk',10)
letters3 = lettergame('is a chickpea a bean',10)


#letters3.game()