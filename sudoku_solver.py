import numpy as np

class Sudoku:
    elements=[1,2,3,4,5,6,7,8,9]
    def __init__(self,array=None):
        if isinstance(array,type(None)):
            self.array=np.zeros((9,9),dtype=int)
        else:
            self.original=array.copy()
            self.array=array
        
    def draw(self):
        for row in self.array:
            for column_element in row:
                if column_element:
                    print(column_element, end=" ")
                else:
                    print(" ",end=" ")
            print("")

    def is_legit(self):
        #count occurence in rows
        for element in Sudoku.elements:
            for row in self.array:
                count=np.count_nonzero(row == element)
                if count>1:
                    return False

        #count occurence in columns
        for element in Sudoku.elements:
            for column in self.array.T:
                count=np.count_nonzero(column == element)
                if count>1:
                    return False
    
        #count occurence in quadrant
        for row_index in range(0,9,3):
            array_slice=self.array[row_index:row_index+3]
            for column_index in range(0,9,3):
                quadrant=array_slice.T[column_index:column_index+3].T
                for element in Sudoku.elements:
                    count=np.count_nonzero(quadrant == element)
                    if count>1:
                        return False
        return True

    def legit_in(self,row,column,element):
        temp=self.array[row][column]
        self.array[row][column]=element
        if not self.is_legit():
            self.array[row][column]=temp
            return False
        return True

    def is_solved(self):
        for row in self.array:
            for column_element in row:
                if not column_element:
                    return False
        if not self.is_legit():
            return False
        return True
        
sudoku=np.array([
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
sudoku=Sudoku(sudoku)

sudoku=np.array([
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
sudoku=Sudoku(sudoku)

def solve_Sudoku(sudoku, row=0, column_element=0):
    if not isinstance(sudoku, Sudoku):
        sudoku=Sudoku(sudoku)
    
    
    if not sudoku.original[row][column_element]:
        for element in Sudoku.elements:
            if sudoku.legit_in(row,column_element,element):
                if column_element!=8:
                    if solve_Sudoku(sudoku,row,column_element+1):
                        return True
                elif row!=8:
                    if solve_Sudoku(sudoku,row+1,0):
                        return True  
            else:
                sudoku.array[row][column_element]=0
    else:
        if column_element!=8:
            if solve_Sudoku(sudoku,row,column_element+1):
                return True
        elif row!=8:
            if solve_Sudoku(sudoku,row+1,0):
                return True
        else:
            print("Highest field reached")     
                
    if sudoku.is_solved():
        sudoku.draw()
        return True
        


if __name__ == "__main__":
    Sudoku(sudoku.original).draw()
    solve_Sudoku(sudoku)