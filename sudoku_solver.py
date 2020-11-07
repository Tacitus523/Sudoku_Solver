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

    def occupy_first(self,element):
        for row in self.array:
            for column_element in row:
                if not column_element:
                    column_element=0

    def is_solved(self):
        for row in self.array:
            for column_element in row:
                if not column_element:
                    return False
        if not self.is_legit():
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

def solve_Sudoku(array,row=0,column_element=0):
    if not isinstance(array, Sudoku):
        sudoku=Sudoku(array)
    elif isinstance(array, Sudoku):
        sudoku, array=array,array.array

    for element in Sudoku.elements:
        if not sudoku.array[row][column_element] and not array[row][column_element]:
            sudoku.array[row][column_element]=element
        elif column_element!=8:
            solve_Sudoku(sudoku,row,column_element+1)
        elif row!=8:
            solve_Sudoku(sudoku,row+1,0)

        
        if sudoku.is_legit():
            if column_element==4 and row==1:
                sudoku.draw()
            if column_element==8 and row==1:
                sudoku.draw()
            if column_element!=8:
                #print(f"next try at ({row},{column_element+1}) with {0}")
                if solve_Sudoku(sudoku,row,column_element+1):
                    return True
            elif row!=8:
                #print(f"next try at ({row},{column_element}) with {0}")
                if solve_Sudoku(sudoku,row+1,0):
                    return True
            
        
        if sudoku.is_solved():
            return True

        if not array[row][column_element]:
            sudoku.array[row][column_element]=0


if __name__ == "__main__":
    solve_Sudoku(sudoku_example)
    sudoku_example.draw()