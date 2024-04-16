import random
import copy
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
        if NavalBattle.playing_field == []:
            print('игровое поле не заполнено')
        else:
            if NavalBattle.playing_field[y-1][x-1] == 1:
                NavalBattle.playing_field[y-1][x-1] = str(self.simbol)
                print('попал')
            elif NavalBattle.playing_field[y-1][x-1] == 0:
                NavalBattle.playing_field[y-1][x-1] = 'о'
                print('мимо')
            else:
                print('ошибка')

    @staticmethod
    def new_game():
        NavalBattle.playing_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ships = [4,3,2,1]
        for i in range(len(ships)):
            while ships[i] != 0:
                new_array = copy.deepcopy(NavalBattle.playing_field)
                x = random.randint(0,9)
                y = random.randint(0,9)
                if new_array[y][x] == 0:
                    direction = random.randint(0,1)
                    if direction == 0:
                        if x+i < 10:
                            for j in range(x,x+i+1):
                                new_array[y][j] += 1
                            if y-1 > -1:
                                for j in range(x, x + i + 1):
                                    new_array[y-1][j] += 1
                            if y+1<10:
                                for j in range(x, x + i + 1):
                                    new_array[y+1][j] += 1
                            if x+i+1<10:
                                new_array[y][x+i+1] +=1
                            if x-1>-1:
                                new_array[y][x-1] +=1
                            flag = True
                            for j in new_array:
                                if 2 in j:
                                    flag = False
                            if flag == True:
                                for j in range(x, x + i + 1):
                                    NavalBattle.playing_field[y][j] += 1
                                ships[i] -= 1

                        elif x - i > -1:
                            for j in range(x-i, x+1):
                                new_array[y][j] += 1
                            if y-1 > -1:
                                for j in range(x-i, x+1):
                                    new_array[y-1][j] += 1
                            if y+1<10:
                                for j in range(x-i, x+1):
                                    new_array[y + 1][j] += 1
                            if x+1<10:
                                new_array[y][x+1] +=1
                            if x-i-1:
                                new_array[y][x-i-1] +=1
                            flag = True
                            for j in new_array:
                                if 2 in j:
                                    flag = False
                            if flag == True:
                                for j in range(x-i,x+1):
                                    NavalBattle.playing_field[y][j] += 1
                                ships[i] -= 1
                    else:
                        if y+i < 10:
                            for j in range(y,y+i+1):
                                new_array[j][x] += 1
                            if x-1 > -1:
                                for j in range(y, y + i + 1):
                                    new_array[j][x-1] += 1
                            if x+1<10:
                                for j in range(y, y + i + 1):
                                    new_array[j][x+1] += 1
                            if y+i+1<10:
                                new_array[y+i+1][x] +=1
                            if y-1>-1:
                                new_array[y-1][x] +=1
                            flag = True
                            for j in new_array:
                                if 2 in j:
                                    flag = False
                            if flag == True:
                                for j in range(y,y+i+1):
                                    NavalBattle.playing_field[j][x] += 1
                                ships[i] -= 1
                        elif y - i > -1:
                            for j in range(y-i, y+1):
                                new_array[j][x] += 1
                            if x-1 > -1:
                                for j in range(y-i, y+1):
                                    new_array[j][x-1] += 1
                            if x+1<10:
                                for j in range(y-i, y+1):
                                    new_array[j][x+1] += 1
                            if y+1<10:
                                new_array[y+1][x] +=1
                            if y-i-1:
                                new_array[y-i-1][x] +=1
                            flag = True
                            for j in new_array:
                                if 2 in j:
                                    flag = False
                            if flag == True:
                                for j in range(y-i, y+1):
                                    NavalBattle.playing_field[j][x] += 1
                                ships[i] -= 1

