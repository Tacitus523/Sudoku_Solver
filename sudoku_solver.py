import numpy as np
from random import choice



class Sudoku:
    elements=[1,2,3,4,5,6,7,8,9]
    def __init__(self,array=None,solution=None):
        if isinstance(array,type(None)):
            self.array=np.zeros((9,9),dtype=int)
        else:
            self.original=array.copy()
            self.array=array
            self.solution=solution
        
    def draw(self):
        for row in self.array:
            for column_element in row:
                if column_element:
                    print(column_element, end=" ")
                else:
                    print(" ",end=" ")
            print("")
    
    def get_empty(self):
        for row_index in range(len(self.array)):
            for column_index in range(len(self.array[0])):
                if not self.array[row_index][column_index]:
                    return row_index,column_index
        return False

    def is_legit(self,target_row_index,target_column_index,element):
        #check other occurence in row
        for column_index in range(len(self.array[target_row_index])):
            if self.array[target_row_index][column_index]==element and column_index!=target_column_index:
                return False

        #check other occurence in column
        for row_index in range(len(self.array)):
            if self.array[row_index][target_column_index]==element and row_index!=target_row_index:
                return False
    
        #count occurence in quadrant
        for row_index in range(target_row_index//3*3,target_row_index//3*3+3):
            for column_index in range(target_column_index//3*3,target_column_index//3*3+3):
                if self.array[row_index][column_index]==element and not(row_index==target_row_index and column_index==target_column_index):
                    return False
        return True


def choose_sudoku():
    sudokus=[]
    with open('sudokus_csv.txt') as f:
        for line in f.readlines():
            raw=line.strip().strip(',').replace('.','0')
            sudoku_list=[]
            for char in raw:
                sudoku_list.append(int(char))
            
            sudoku_array=np.array([sudoku_list])
            sudoku_array=np.reshape(sudoku_array,(9,9))
            sudokus.append(sudoku_array)
    return Sudoku(choice(sudokus))

sudoku=choose_sudoku()

sudoku1=np.array([
    [0,0,0,0,7,0,8,0,0],
    [0,0,0,0,3,2,0,9,0],
    [0,0,0,1,0,8,0,7,0],
    [1,3,0,0,0,9,6,0,0],
    [9,0,0,5,0,3,0,0,7],
    [0,0,4,6,0,0,0,3,1],
    [0,9,0,3,0,5,0,0,0],
    [0,8,0,7,9,0,0,0,0],
    [0,0,1,0,6,0,0,0,0]
])
sudoku1=Sudoku(sudoku1)

sudoku2=np.array([
    [0,5,1,0,4,0,9,7,0],
    [2,9,0,0,0,0,0,0,0],
    [0,0,6,3,0,0,0,2,0],
    [0,0,9,5,0,8,0,0,4],
    [0,0,0,0,6,0,0,0,0],
    [5,0,0,2,0,9,3,0,0],
    [0,2,0,0,0,5,1,0,0],
    [0,0,0,0,0,0,0,5,8],
    [0,7,5,0,8,0,6,4,0],
])
sudoku2=Sudoku(sudoku2)

sudoku3=np.array([
    [0,0,3,0,0,0,0,5,0],
    [0,7,0,0,0,8,0,0,9],
    [0,0,0,0,9,0,2,0,7],
    [4,0,0,1,0,0,5,0,6],
    [7,0,0,0,0,0,0,0,2],
    [5,0,0,0,0,6,0,0,8],
    [6,0,1,0,8,0,0,0,0],
    [8,0,0,7,0,0,0,9,0],
    [0,4,0,0,0,0,8,0,0]
])
sudoku3=Sudoku(sudoku3)

def solve_Sudoku(sudoku):
    if not isinstance(sudoku, Sudoku):
        sudoku=Sudoku(sudoku)

    if not sudoku.get_empty():
        sudoku.solution=Sudoku(sudoku.array)
        sudoku.array=sudoku.original
        return True
    
    else:
        target_row_index, target_column_index = sudoku.get_empty()
        for element in Sudoku.elements:
            if sudoku.is_legit(target_row_index,target_column_index,element):
                sudoku.array[target_row_index][target_column_index] = element

                if solve_Sudoku(sudoku):
                    return True
                sudoku.array[target_row_index][target_column_index]=0
    
    return False
  

if __name__ == "__main__":
    sudoku.draw()
    print("-----------------------------")
    solve_Sudoku(sudoku)
    sudoku.solution.draw()   