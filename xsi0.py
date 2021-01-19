import pygame
import os
import sys
import time
from tkinter import *
pygame.init()
pygame.font.init()

numeJucatorX = ''
numeJucator0 = ''

root = Tk()
root.title('Interfata X si 0')
#Labelurile
labelJucatorX = Label(root, text='Jucator X')
labelJucatorX.grid(row=0, column=0)

labelJucator0 = Label(root, text='Jucator 0')
labelJucator0.grid(row=0,column=3)
#Entryurile
JucatorX_name = StringVar()
e2 = Entry(root, width=40, textvariable=JucatorX_name)
e2.insert(0, "Scrie-ti numele: ")
e2.grid(row=0, column=2)

Jucator0_name = StringVar()
e1 = Entry(root, width=40, textvariable=Jucator0_name)
e1.insert(0, "Scrie-ti numele: ")
e1.grid(row=0,column=4)

#Functii
def SetName():
    global numeJucator0, numeJucatorX
    if len(e1.get()) >= 3 and len(e1.get()) < 20 and len(e2.get()) >= 3 and len(e2.get()) < 20:
        numeJucatorX = e2.get()
        numeJucator0 = e1.get()
        return True
    else:
        return False

def DestroyElements():
    if SetName():
        labelJucatorX.destroy()
        labelJucator0.destroy()
        e2.destroy()
        e1.destroy()
        buttonAdd.destroy()
        root.destroy()
    else:
        SetName()

#Button add
buttonAdd = Button(root, text='Adauga numele', command=DestroyElements)
buttonAdd.grid(row=0, column=5)


root.mainloop()

root2 = Tk()
root2.title('Match history')

list = Listbox(root2, height=15, width=55)
list.grid(row=3, column=1, rowspan=9, columnspan=2)



WIDTH, HEIGHT, = 800, 500
BOX = 95, 95
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WINS_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 70)

FPS = 144

B1 = pygame.Rect(330, 90, 10, 310) #horizontal 1
B2 = pygame.Rect(440, 90, 10, 310) #horizontal 2
B3 = pygame.Rect(240, 190, 300, 10) #vertical 1
B4 = pygame.Rect(240, 290, 300, 10) #vertical 2

WinsX = 0
WinsO = 0


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('X si 0')

X_IMAGE = pygame.image.load(os.path.join('Assets', 'X.png'))
Ximagine = pygame.transform.scale(X_IMAGE, (BOX))
pygame.display.set_icon(X_IMAGE)
O_IMAGE = pygame.image.load(os.path.join('Assets', '0.png'))
Oimagine = pygame.transform.scale(O_IMAGE, (BOX))

def draw_window(B1, B2, B3, B4, WinsX, WinsO):

    pygame.draw.rect(WIN, BLACK, B1)
    pygame.draw.rect(WIN, BLACK, B2)
    pygame.draw.rect(WIN, BLACK, B3)
    pygame.draw.rect(WIN, BLACK, B4)

    xWins = WINS_FONT.render(numeJucatorX + ': ' + str(WinsX), 1, BLACK)
    oWins = WINS_FONT.render(numeJucator0 + ': ' + str(WinsO), 1, BLACK)
    WIN.blit(xWins, (WIDTH - xWins.get_width() - 10, 10))
    WIN.blit(oWins, (10, 10))
    pygame.display.update()

def draw_winner(winner_text):
    list.insert(END, current_time +' | '+ winner_text + " | " + str(WinsX) + '-' + str(WinsO))
    draw_text = WINNER_FONT.render(winner_text, 1, BLACK)
    WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() / 2, 400))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    global WinsX, WinsO, current_time
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    def check_pos(pos, X, O, listaX, listaO):
        # Sus stanga
        if pos[0] > 234 and pos[1] > 81 and pos[0] < 333 and pos[1] < 190 and Table[0] =='-':
            if len(listaO) < len(listaX):
                WIN.blit(Oimagine, (235, 95))
                listaO.append(O)
                Table[0] = 'O'
                pygame.display.update()
            else:
                WIN.blit(Ximagine, (235, 95))
                listaX.append(X)
                Table[0] = 'X'
                pygame.display.update()


        # Sus miljoc
        elif pos[0] > 334 and pos[1] > 81 and pos[0] < 433 and pos[1] < 190 and Table[1] =='-':
            if len(listaO) < len(listaX):
                WIN.blit(Oimagine, (340, 95))
                listaO.append(O)
                Table[1] = 'O'
                pygame.display.update()
            else:
                WIN.blit(Ximagine, (340, 95))
                listaX.append(X)
                Table[1] = 'X'
                pygame.display.update()
        # Sus dreapta
        elif pos[0] > 434 and pos[1] > 81 and pos[0] < 534 and pos[1] < 190 and Table[2] =='-':
            if len(listaO) < len(listaX):
                WIN.blit(Oimagine, (445, 95))
                listaO.append(O)
                Table[2] = 'O'
                pygame.display.update()
            else:
                WIN.blit(Ximagine, (445, 95))
                listaX.append(X)
                Table[2] = 'X'
                pygame.display.update()
        # Mijloc stanga
        elif pos[0] > 234 and pos[1] > 190 and pos[0] < 334 and pos[1] < 290 and Table[3] =='-':
            if len(listaO) < len(listaX):
                WIN.blit(Oimagine, (235, 195))
                listaO.append(O)
                Table[3] = 'O'
                pygame.display.update()
            else:
                WIN.blit(Ximagine, (235, 195))
                listaX.append(X)
                Table[3] = 'X'
                pygame.display.update()
        # Mijloc mijloc
        elif pos[0] > 334 and pos[1] > 190 and pos[0] < 433 and pos[1] < 290 and Table[4] =='-':
            if len(listaO) < len(listaX):
                WIN.blit(Oimagine, (340, 195))
                listaO.append(O)
                Table[4] = 'O'
                pygame.display.update()
            else:
                WIN.blit(Ximagine, (340, 195))
                listaX.append(X)
                Table[4] = 'X'
                pygame.display.update()
        # Mijloc dreapta
        elif pos[0] > 434 and pos[1] > 190 and pos[0] < 534 and pos[1] < 290 and Table[5] =='-':
            if len(listaO) < len(listaX):
                WIN.blit(Oimagine, (445, 195))
                listaO.append(O)
                Table[5] = 'O'
                pygame.display.update()
            else:
                WIN.blit(Ximagine, (445, 195))
                listaX.append(X)
                Table[5] = 'X'
                pygame.display.update()
        # Jos stanga
        elif pos[0] > 234 and pos[1] > 290 and pos[0] < 334 and pos[1] < 390 and Table[6] =='-':
            if len(listaO) < len(listaX):
                WIN.blit(Oimagine, (235, 295))
                listaO.append(O)
                Table[6] = 'O'
                pygame.display.update()
            else:
                WIN.blit(Ximagine, (235, 295))
                listaX.append(X)
                Table[6] = 'X'
                pygame.display.update()
        # Jos mijloc
        elif pos[0] > 334 and pos[1] > 290 and pos[0] < 433 and pos[1] < 390 and Table[7] =='-':
            if len(listaO) < len(listaX):
                WIN.blit(Oimagine, (340, 295))
                listaO.append(O)
                Table[7] = 'O'
                pygame.display.update()
            else:
                WIN.blit(Ximagine, (340, 295))
                listaX.append(X)
                Table[7] = 'X'
                pygame.display.update()
        # Jos dreapta
        elif pos[0] > 434 and pos[1] > 290 and pos[0] < 534 and pos[1] < 390 and Table[8] =='-':
            if len(listaO) < len(listaX):
                WIN.blit(Oimagine, (445, 295))
                listaO.append(O)
                Table[8] = 'O'
                pygame.display.update()
            else:
                WIN.blit(Ximagine, (445, 295))
                listaX.append(X)
                Table[8] = 'X'
                pygame.display.update()

    Table =  ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

    X = pygame.Rect(235, 90, 100, 100)
    O = pygame.Rect(335, 190, 100, 100)


    listaX = []
    listaO = []

    clock = pygame.time.Clock()
    WIN.fill(WHITE)
    draw_window(B1, B2, B3, B4, WinsX, WinsO)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                root2.mainloop()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                check_pos(pos, X, O, listaO, listaX)


        winner_text = ''
        if Table[0] == Table[1] == Table[2] != '-':
            if Table[0] == 'X':
                winner_text = numeJucatorX + ' a castigat!'
                WinsX += 1
            else:
                winner_text = numeJucator0 + ' a castigat!'
                WinsO += 1

        elif Table[3] == Table[4] == Table[5] != '-':
            if Table[3] == 'X':
                winner_text = numeJucatorX + ' a castigat!'
                WinsX += 1
            else:
                winner_text = numeJucator0 + ' a castigat!'
                WinsO += 1

        elif Table[6] == Table[7] == Table[8] != '-':
            if Table[4] == 'X':
                winner_text = numeJucatorX + ' a castigat!'
                WinsX += 1
            else:
                winner_text = numeJucator0 + ' a castigat!'
                WinsO += 1

            # Mai jos sunt verificarile pentru coloane
        elif Table[0] == Table[3] == Table[6] != '-':
            if Table[3] == 'X':
                winner_text = numeJucatorX + ' a castigat!'
                WinsX += 1
            else:
                winner_text = numeJucator0 + ' a castigat!'
                WinsO += 1

        elif Table[1] == Table[4] == Table[7] != '-':
            if Table[1] == 'X':
                winner_text = numeJucatorX + ' a castigat!'
                WinsX += 1
            else:
                winner_text = numeJucator0 + ' a castigat!'
                WinsO += 1

        elif Table[2] == Table[5] == Table[8] != '-':
            if Table[2] == 'X':
                winner_text = numeJucatorX + ' a castigat!'
                WinsX += 1
            else:
                winner_text = numeJucator0 + ' a castigat!'
                WinsO += 1
            # Mai jos sunt verificarile pentru diagonale
        elif Table[0] == Table[4] == Table[8] != '-':
            if Table[4] == 'X':
                winner_text = numeJucatorX + ' a castigat!'
                WinsX += 1
            else:
                winner_text = numeJucator0 + ' a castigat!'
                WinsO += 1

        elif Table[2] == Table[4] == Table[6] != '-':
            if Table[2] == 'X':
                winner_text = numeJucatorX + ' a castigat!'
                WinsX += 1
            else:
                winner_text = numeJucator0 + ' a castigat!'
                WinsO += 1

            # Mai jos este verificarea pentru egalitate
        elif Table[0] != '-' and Table[1] != '-' and Table[2] != '-' and Table[3] != '-' and Table[4] != '-' and Table[
            5] != '-' and Table[6] != '-' and Table[7] != '-' and Table[8] != '-':
            winner_text = 'Egalitate!'

        if winner_text != '':
            draw_winner(winner_text)
            break
    main()

if __name__ == '__main__':
    main()