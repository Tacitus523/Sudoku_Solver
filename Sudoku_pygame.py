import pygame
import numpy as np
from sudoku_solver import Sudoku, sudoku

#Initilaze
pygame.font.init()

#Screen settings
WIDTH,HEIGHT=600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")
#icon = "#"
#pygame.display.set_icon(icon)

def draw_field(sudoku):
    paper_size=(452,452)
    f_size=(paper_size[0]//9,paper_size[1]//9)
    paper=pygame.Surface(paper_size)
    
    fields=[
    [pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size)],
    [pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size)],
    [pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size)],
    [pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size)],
    [pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size)],
    [pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size)],
    [pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size)],
    [pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size)],
    [pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size),pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size), pygame.Surface(f_size)]     
    ]

    screen.fill((70,70,70))
    paper.fill((0,0,0))
    
    for sudoku_row, field_row in zip(sudoku.array, fields):
        for sudoku_entry, field_entry in zip(sudoku_row, field_row):
            field_entry.fill((240,240,240))

    number_org_font=pygame.font.SysFont('arial',32, True)
    number_font=pygame.font.SysFont('brushscriptkursiv',32)
    for row_index,row in enumerate(sudoku.array):
        for column_index,column in enumerate(row):
            if sudoku.original[row_index][column_index]:
                number_label=number_org_font.render(f"{sudoku.original[row_index][column_index]}",True,(0,0,0))
                fields[row_index][column_index].blit(number_label,(f_size[0]//2-number_label.get_width()//2,f_size[1]//2-number_label.get_height()//2))
            elif sudoku.array[row_index][column_index]:
                number_label=number_font.render(f"{sudoku.array[row_index][column_index]}",True,(0,0,0))
                fields[row_index][column_index].blit(number_label,(f_size[0]//2-number_label.get_width()//2,f_size[1]//2-number_label.get_height()//2))


    for x, field_row in zip(range(0,paper_size[0],f_size[0]), fields):
        for y, field_entry in zip(range(0,paper_size[0],f_size[0]), field_row):
            paper.blit(field_entry,(y,x))

    for x in range(0,paper_size[0],f_size[0]):
        for y in range(0,paper_size[1],f_size[1]):
            if (y/f_size[0])%3==0:
                pygame.draw.line(paper, (0,0,0), [0, y], [paper_size[0],y], 3)
            else:
                pygame.draw.line(paper, (0,0,0), [0, y], [paper_size[0],y], 1)
        if (x/f_size[0])%3==0:
            pygame.draw.line(paper, (0,0,0), [x,0], [x,paper_size[0]], 3)
        else:
            pygame.draw.line(paper, (0,0,0), [x,0], [x,paper_size[0]], 1)

    screen.blit(paper,(WIDTH//2-paper_size[0]//2,HEIGHT//2-paper_size[1]//2))
    pygame.display.update()

def get_input(sudoku):
    #rects
    paper_size=(452,452)
    f_size=(paper_size[0]//9,paper_size[1]//9)
    rects=[]
    for x in range((WIDTH-paper_size[0])//2, (WIDTH+paper_size[0]-3)//2, f_size[0]):
        for y in range((HEIGHT-paper_size[1])//2, (HEIGHT+paper_size[1]-3)//2, f_size[1]):
            rects.append(pygame.Rect((x,y),(f_size[0],f_size[1])))

    #filter events for KEYDOWN
    pygame.event.set_blocked([pygame.MOUSEMOTION,pygame.KEYUP])
    event = pygame.event.wait()
    pygame.event.set_allowed(pygame.MOUSEMOTION)
    mouse = pygame.mouse.get_pos()
    pygame.event.set_blocked([pygame.MOUSEMOTION,pygame.KEYUP])


    for rect in rects:
        if rect.collidepoint(pygame.mouse.get_pos()):
            index = rects.index(rect)
            if event.type==pygame.KEYDOWN and (event.key in [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]):
                if not sudoku.array[index%9][index//9]:
                    sudoku.array[index%9][index//9]=int(event.unicode)
                    #set new entry
                    if not sudoku.is_legit():
                        sudoku.array[index%9][index//9]=0
                        warning_font=pygame.font.SysFont('arial',24, True)
                        warning_label=warning_font.render("This can't be placed here",True,(0,0,0))
                        screen.blit(warning_label,((WIDTH-warning_label.get_width())/2,25))
                        pygame.display.update()
                        pygame.time.wait(500)
            if event.type==pygame.KEYDOWN and (event.key==pygame.K_0 or event.key==pygame.K_BACKSPACE or event.key==pygame.K_DELETE):
                #delete if not in original
                if not sudoku.original[index%9][index//9]:
                    sudoku.array[index%9][index//9]=0

def draw_solution(sudoku, row=0, column_element=0):
    if not sudoku.original[row][column_element]:
        for element in Sudoku.elements:
            if sudoku.legit_in(row,column_element,element):
                pygame.time.wait(25)
                draw_field(sudoku)
                if column_element!=8:
                    if draw_solution(sudoku,row,column_element+1):
                        return True
                elif row!=8:
                    if draw_solution(sudoku,row+1,0):
                        return True
                #all nines are placed,lesser numbers just need to be placed
                elif row==8:
                    pygame.time.wait(5000)
                    for column in sudoku.array:
                        for elements in Sudoku.elements:
                            if sudoku.legit_in(8,column,element):
                                sudoku.array[8][column]=element
                                draw_field(sudoku)
                                pygame.time.wait(1000)
                    if sudoku.is_solved():
                        draw_field(sudoku)
                        pygame.time.wait(5000)
                        return True
                        
            else:
                sudoku.array[row][column_element]=0
    else:
        if column_element!=8:
            if draw_solution(sudoku,row,column_element+1):
                return True
        elif row!=8:
            if draw_solution(sudoku,row+1,0):
                return True
        #all nines are placed,lesser numbers just need to be placed
        elif row==8:
            pygame.time.wait(5000)
            for column in sudoku.array:
                for elements in Sudoku.elements:
                    if sudoku.legit_in(8,column,elements):
                        sudoku.array[8][column]=elements
                        draw_field(sudoku)
                        pygame.time.wait(1000)
                    
    if sudoku.is_solved():
        draw_field(sudoku)
        pygame.time.wait(5000)
        return True
    
    

def play_sudoku():
    
    #zero settings   
    #sudoku=Sudoku(np.zeros((9,9),dtype=int))

    #set Clock
    FPS = 30
    clock = pygame.time.Clock()
    
    running=True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        draw_field(sudoku)

        get_input(sudoku)
        

#play_sudoku()
Sudoku(sudoku.original).draw()
draw_solution(sudoku)
Sudoku(sudoku.original).draw()
sudoku.draw()