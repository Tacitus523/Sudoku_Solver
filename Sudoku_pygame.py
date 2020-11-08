import pygame
import time
import numpy as np
from sudoku_solver import Sudoku, choose_sudoku, solve_Sudoku
import os

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

    button_size=(90,30)
    button_surf=[pygame.Surface(button_size),pygame.Surface(button_size)]
    button_surf[0].fill((0,200,0))
    button_surf[1].fill((200,0,0))
    button_font=pygame.font.SysFont('arial', 24, True)
    hint_label=button_font.render("HINT",True,(0,0,0))
    solve_label=button_font.render("SOLVE",True,(0,0,0))
    button_surf[0].blit(hint_label,(button_size[0]//2-hint_label.get_width()//2,+button_size[1]//2-hint_label.get_height()//2))
    button_surf[1].blit(solve_label,(button_size[0]//2-solve_label.get_width()//2,+button_size[1]//2-solve_label.get_height()//2))
    screen.blit(button_surf[0],(WIDTH//2-paper_size[0]//3-button_size[0]//2,HEIGHT-50))
    screen.blit(button_surf[1],(WIDTH//2+paper_size[0]//3-button_size[0]//2,HEIGHT-50))

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
                if not sudoku.original[index%9][index//9]:
                    temp=sudoku.array[index%9][index//9]
                    sudoku.array[index%9][index//9]=int(event.unicode)
                    #set new entry
                    if not sudoku.is_legit(index%9,index//9,int(event.unicode)):
                        sudoku.array[index%9][index//9]=temp
                        warning_font=pygame.font.SysFont('arial',24, True)
                        warning_label=warning_font.render("This can't be placed here",True,(0,0,0))
                        screen.blit(warning_label,((WIDTH-warning_label.get_width())/2,25))
                        pygame.display.update()
                        pygame.time.wait(500)
            if event.type==pygame.KEYDOWN and (event.key==pygame.K_0 or event.key==pygame.K_BACKSPACE or event.key==pygame.K_DELETE):
                #delete if not in original
                if not sudoku.original[index%9][index//9]:
                    sudoku.array[index%9][index//9]=0

    button_size=(90,30)
    hint_button_pos=(WIDTH//2-paper_size[0]//3-button_size[0]//2,HEIGHT-50)
    solve_button_pos=(WIDTH//2+paper_size[0]//3-button_size[0]//2,HEIGHT-50)
    hint_button_rect=pygame.Rect(hint_button_pos,button_size)
    solve_button_rect=pygame.Rect(solve_button_pos,button_size)

    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==1 and hint_button_rect.collidepoint(pygame.mouse.get_pos()):
            hint(sudoku)
        
        if event.button==1 and solve_button_rect.collidepoint(pygame.mouse.get_pos()):
            sudoku.array=sudoku.original.copy()
            draw_solution(sudoku)
            

def draw_solution(sudoku):
    if not sudoku.get_empty():
        return True
    
    else:
        target_row_index, target_column_index = sudoku.get_empty()
        for element in Sudoku.elements:
            if sudoku.is_legit(target_row_index,target_column_index,element):
                sudoku.array[target_row_index][target_column_index] = element
                draw_field(sudoku)

                if draw_solution(sudoku):
                    return True

                sudoku.array[target_row_index][target_column_index]=0
    return False

def hint(sudoku):
    for row_index,row in enumerate(sudoku.array):
        for column_index,column in enumerate(row):
            if column and column!=sudoku.solution.array[row_index][column_index]:
                sudoku.original[row_index][column_index]=sudoku.solution.array[row_index][column_index]
                sudoku.array[row_index][column_index]=sudoku.solution.array[row_index][column_index]
                return
    
    for row_index,row in enumerate(sudoku.array):
        for column_index,column in enumerate(row):
            if not column:
                sudoku.original[row_index][column_index]=sudoku.solution.array[row_index][column_index]
                sudoku.array[row_index][column_index]=sudoku.solution.array[row_index][column_index]
                return


def play_sudoku(sudoku):
    if not sudoku.solution:
        solve_Sudoku(sudoku)

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        draw_field(sudoku)
        if not sudoku.get_empty():
            pygame.time.wait(5)
            running=False
        get_input(sudoku)

    if sudoku.get_empty():
        np.savetxt("save_sudoku.csv", sudoku.array, delimiter=",")
        np.savetxt("save_original.csv", sudoku.original, delimiter=",")
        np.savetxt("save_solution.csv", sudoku.solution.array, delimiter=",")
    else:
        os.remove("save_sudoku.csv")
        os.remove("save_original.csv")
        os.remove("save_solution.csv")


        
if __name__=='__main__':
    try:
        sudoku = Sudoku(np.genfromtxt('save_sudoku.csv', dtype=int, delimiter=','))
        sudoku.original = np.genfromtxt('save_original.csv', dtype=int, delimiter=',')
        sudoku.solution = Sudoku(np.genfromtxt('save_solution.csv', dtype=int, delimiter=','))
        
    except:
        sudoku=choose_sudoku()

    play_sudoku(sudoku)
