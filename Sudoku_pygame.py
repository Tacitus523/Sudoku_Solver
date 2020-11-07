import pygame
import numpy as np
from sudoku_solver import Sudoku

#Initilaze
pygame.font.init()

#Screen settings
WIDTH,HEIGHT=600,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")
#icon = "#"
#pygame.display.set_icon(icon)

def draw_field(board):
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
    
    for board_row, field_row in zip(board, fields):
        for board_entry, field_entry in zip(board_row, field_row):
            field_entry.fill((240,240,240))

    number_font=pygame.font.SysFont('arial',32, True)
    for row_index,row in enumerate(board):
        for column_index,column in enumerate(row):
            if board[row_index][column_index]:
                number_label=number_font.render(f"{board[row_index][column_index]}",True,(0,0,0))
                fields[row_index][column_index].blit(number_label,(f_size[0]//2-number_label.get_width()//2,f_size[1]//2-number_label.get_height()//2))

    for x, field_row in zip(range(0,paper_size[0],f_size[0]), fields):
        for y, field_entry in zip(range(0,paper_size[0],f_size[0]), field_row):
            paper.blit(field_entry,(x,y))

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

def get_input(board,rects):
    mouse = pygame.mouse.get_pos()

    

    for rect in rects:
        if rect.collidepoint(pygame.mouse.get_pos()):
            index=rects.index(rect)
            for event in pygame.event.get():    
                if event.type==pygame.KEYDOWN:
                    if(event.key in [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9]):
                        print("event")
                        if not board[index%9][index//9]:
                            board[index%9][index//9]=event.unicode
                            if not Sudoku(board).is_legit():
                                board[index%9][index//9]=0
                                #warning_font=pygame.font.SysFont('arial',24, True)
                                #warning_label=warning_font.render("This can't be placed here",True,(0,0,0))
                                #screen.blit(warning_label,((WIDTH-warning_label.get_width())/2,50))
                if event.type==pygame.KEYDOWN and (event.key==pygame.K_0 or event.key==pygame.K_BACKSPACE or event.key==pygame.K_DELETE):
                    board[index%9][index//9]=0
            pygame.event.clear()




def play_sudoku():
    
    #zero settings   
    board=np.zeros((9,9),dtype=int)
    board[0][0]=1

    #rects
    paper_size=(452,452)
    f_size=(paper_size[0]//9,paper_size[1]//9)
    rects=[]
    for x in range((WIDTH-paper_size[0])//2, (WIDTH+paper_size[0]-3)//2, f_size[0]):
        for y in range((HEIGHT-paper_size[1])//2, (HEIGHT+paper_size[1]-3)//2, f_size[1]):
            rects.append(pygame.Rect((y,x),(f_size[0],f_size[1])))
    
    #filter events
    pygame.event.set_allowed([pygame.KEYDOWN,pygame.MOUSEMOTION])


    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        draw_field(board)
        get_input(board,rects)
        pygame.display.update()

play_sudoku()