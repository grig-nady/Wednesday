import pygame
import time
pygame.init()
back = (10, 15, 40)
mw = pygame.display.set_mode((500,500))
mw.fill(back)

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color=color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
    def colliderect(self,rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
'''
sssr = Picture('photo_1_2023-04-01_12-17-25.jpg', 25, 25, 50, 50)
teresh = Picture('imgonline-com-ua-Resize-V55c6v1MY60R.jpg', 25, 25, 50, 50)
vost = Picture('imgonline-com-ua-Resize-1WNBz9uIUuQ.jpg', 25, 25, 50, 50)
ciol = Picture('photo_2_2023-04-01_12-17-25.jpg', 25, 25, 50, 50)
zvez = Picture('photo_3_2023-04-01_12-17-25.jpg', 25, 25, 50, 50)
venanduran = Picture('imgonline-com-ua-Resize-QjXHQWdXxLh.jpg', 25, 25, 50, 50)
colich = Picture('photo_2_2023-04-01_12-17-04.jpg', 25, 25, 50, 50)
almazi = Picture('photo_3_2023-04-01_12-17-04.jpg', 25, 25, 50, 50)
plan = Picture('imgonline-com-ua-Resize-73pG7Lr3SBN22W.jpg', 25, 25, 50, 50)
agaaa= Picture('imgonline-com-ua-Resize-DNI2C5b1u0KIU5.jpg', 25, 25, 50, 50)
bib= Picture('imgonline-com-ua-Resize-7eixtM7Ktlva.jpg', 25, 25, 50, 50)
kuku= Picture('photo_1_2023-04-01_12-17-04.jpg', 25, 25, 50, 50)
vavav= Picture('imgonline-com-ua-Resize-zjlglQtnMoHrbE.jpg', 25, 25, 50, 50)
jooo= Picture('imgonline-com-ua-Resize-DCoUQGcBttlqWexA.jpg', 25, 25, 50, 50)'''
questions = ['1. Установите соответствие между физическими величинами и единицами этих величин в СИ: к каждому элементу первого столбца подберите соответствующий элемент из второго столбца и запишите в таблицу выбранные цифры под соответствующими буквами.? Ответ: СССР',
    '2. Кто является первой женщиной-космонавтом? Ответ: Валентина Терешкова',
    '3. На каком корабле Юрий Гагарин совершил первый полёт в космос? Ответ: Восток ',
    '4. Какой ученый изобрёл космическую ракету? Ответ: Циолковский',
    '5. В переводе с греческого "комета" означает.....? Ответ: Хвостатая звезда',
    '6. Какие две планеты солнечной системы вращаются в противоположном направлении Земле? Ответ: Венера и Уран',
    '7. Сколько планет в солнечной системе? Ответ: 8',
    '8. На какой планете бывает дождь из алмазов? Ответ: Сатурн',
    '9. Какая планета находится ближе всего к Солнцу? Ответ: Меркурий',
    '10. Какой человек первый полетел в космос? Ответ: Юрий Гагарин',
    '11. Какой тип звезд самый распространённый  в Млечном Пути? Ответ: Красные карлики',
    '12. Какого цвета кажется Солнце? Ответ: глазам кажется белым',
    '13. Почему ночью Луна светится? Ответ: Это лишь отражение солнца',
    '14. Какой третий по яркости небесный объект в космосе? Ответ: Венера']

#начало
print('Вас приветсвует Надежда! Начать тест по физике? (да/нет, off - завершить)')
start = input('jjh')
start = start.lower()
while start != 'off':
    if start == 'да':
        count = 0
        one = input('Отлично, тогда начнём!\n1 вопрос:Установите соответствие между физическими величинами и единицами этих величин в СИ: к каждому элементу первого столбца подберите соответствующий элемент из второго столбца и запишите в таблицу выбранные цифры под соответствующими буквами. ')
        one = one.lower()
        sssr.fill()
        sssr.draw()
        pygame.display.update()
        if one == 'ссср':
            count +=1
        else:
            count +=0
        two = input('2 вопрос:\nКто является первой женщиной-космонавтом? ')
        two = two.lower()
        teresh.fill()
        teresh.draw()
        pygame.display.update()
        v = two.find('терешкова')
        if v == 0:
            count +=1
        else:
            count +=0
        three = input('3 вопрос:\nНа каком корабле Юрий Гагарин совершил первый полёт в космос?')
        three = three.lower()
        vost.fill()
        vost.draw()
        pygame.display.update()
        if three == 'восток':
            count +=1
        else:
            count +=0
        four = input('4 вопрос:\nКакой ученый изобрёл космическую ракету?')
        four = four.lower()
        ciol.fill()
        ciol.draw()
        pygame.display.update()
        if four == 'циолковский':
            count +=1
        else:
            count +=0
        five = input('5 вопрос:\nВ переводе с греческого "комета" означает.....?')
        five = five.lower()
        zvez.fill()
        zvez.draw()
        pygame.display.update()
        if five == 'хвостатая звезда':
            count +=1
        else:
            count +=0
        six = input('6 вопрос:\nКакие две планеты солнечной системы вращаются в противоположном направлении Земле?')
        six = six.lower()
        venanduran.fill()
        venanduran.draw()
        pygame.display.update()
        vv = six.find('венера и уран')
        if vv == 0:
            count +=1
        else:
            count +=0
        seven = input('7 вопрос:\nСколько планет в солнечной системе?')
        seven = seven.lower()
        colich.fill()
        colich.draw()
        pygame.display.update()
        if seven == '8':
            count +=1
        else:
            count +=0
        eight = input('8 вопрос:\nНа какой планете бывает дождь из алмазов?')
        eight = eight.lower()
        almazi.fill()
        almazi.draw()
        pygame.display.update()
        if eight == 'сатурн':
            count +=1
        else:
            count +=0
        nine = input('9 вопрос:\nКакая планета находится ближе всего к Солнцу?')
        nine = nine.lower()
        plan.fill()
        plan.draw()
        pygame.display.update()
        if nine == 'меркурий':
            count +=1
        else:
            count +=0
        ten = input('10 вопрос:\nКакой человек первый полетел в космос? ')
        ten = ten.lower()
        agaaa.fill()
        agaaa.draw()
        pygame.display.update()
        c = ten.find('гагарин')
        tena = ten.find('юрий гагарин')
        if c == 0 or tena ==0:
            count +=1
        else:
            count +=0
        eleven = input('11 вопрос:\nКакой тип звезд самый распространённый в Млечном Пути?')
        eleven = eleven.lower()
        bib.fill()
        bib.draw()
        pygame.display.update()
        if eleven == 'красные карлики' or eleven == 'красный карлик':
            count +=1
        else:
            count +=0
        tvelve = input('12 вопрос:\nКакого цвета кажется Солнце? ')
        tvelve = tvelve.lower()
        kuku.fill()
        kuku.draw()
        pygame.display.update()
        gg = tvelve.find('белым')
        ggg = tvelve.find('белое')
        if gg == 0 or ggg == 0:
            count +=1
        else:
            count +=0
        thirteen = input('13 вопрос:\nПочему ночью Луна светится?')
        thirteen = thirteen.lower()
        vavav.fill()
        vavav.draw()
        pygame.display.update()
        fuf = thirteen.find('отражение')
        fuft = thirteen.find('солнечное отражение')
        if fuf == 0 or fuft ==0:
            count +=1
        else:
            count +=0
        fourteen = input('14 вопрос:\nКакой третий по яркости небесный объект в космосе?')
        fourteen = fourteen.lower()
        jooo.fill()
        jooo.draw()
        pygame.display.update()
        if fourteen == 'венера':
            count +=1
        else:
            count +=0
        print('Викторина окончена! Вы ответили на', count, 'из 14')
        yes = input('Хотите проверить себя?')
        if yes == 'да':
            a = questions[0]
            b = questions[1]
            c = questions[2]
            d = questions[3]
            e = questions[4]
            f = questions[5]
            g = questions[6]
            h = questions[7]
            i= questions[8]
            j = questions[9]
            k = questions[10]
            l = questions[11]
            m = questions[12]
            n = questions[13]
            
            print(a,'\n',b,'\n',c,'\n',d,'\n',e,'\n',f,'\n',g,'\n',h,'\n',i,'\n',j,'\n',k,'\n',l,'\n',m,'\n',n)
            break
        else:
            print('Тогда удачи!')
            break
    if start == 'нет':
        print('Тогда в следующий раз.')
    else:
        print('Вы ввели что-то не то, попробуйте еще раз')
    start = input('Введите да — начать игру, off - завершить')
    