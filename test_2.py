class NavalBattle:
    playing_field = []

    def __init__(self, simbol):
        self.simbol = simbol

    @staticmethod
    def show():
        for i in NavalBattle.playing_field:
            string = ''
            for j in i:
                if j == 1 or j == 0:
                    string += '~'
                else:
                    string += str(j)
            string += '\n'
            print(string)

    def shot(self,x,y):
        if NavalBattle.playing_field[y-1][x-1] == 1:
            NavalBattle.playing_field[y-1][x-1] = str(self.simbol)
            print('попал')
        elif NavalBattle.playing_field[y-1][x-1] == 0:
            NavalBattle.playing_field[y-1][x-1] = 'о'
            print('мимо')
