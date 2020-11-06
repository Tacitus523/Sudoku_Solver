import numpy as np

class Sudoku:
    elements=[1,2,3,4,5,6,7,8,9]
    def __init__(self,array=None):
        if isinstance(array,type(None)):
            self.array=np.zeros((9,9),dtype=int)
        else:
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

sudoku=np.zeros((9,9),dtype=int)
sudoku_example=sudoku.copy()
sudoku_example[0,4]=7
sudoku_example[0,6]=8
sudoku_example[1,4]=3
sudoku_example[1,5]=2
sudoku_example[1,7]=9
sudoku_example[2,3]=1
sudoku_example[2,5]=8
sudoku_example[2,7]=7
sudoku_example[3,0]=1
sudoku_example[3,1]=3
sudoku_example[3,5]=9
sudoku_example[3,6]=6
sudoku_example[4,0]=9
sudoku_example[4,3]=5
sudoku_example[4,5]=3
sudoku_example[4,8]=7
sudoku_example[5,2]=4
sudoku_example[5,3]=6
sudoku_example[5,7]=3
sudoku_example[5,8]=1
sudoku_example[6,1]=9
sudoku_example[6,3]=3
sudoku_example[6,5]=5
sudoku_example[7,1]=8
sudoku_example[7,3]=7
sudoku_example[7,4]=9
sudoku_example[8,2]=1
sudoku_example[8,4]=6
sudoku_example=Sudoku(sudoku_example)

def solve_Sudoku(array):
    sudoku=Sudoku(array)
    

