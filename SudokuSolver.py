'''''''''''''''''
Sudoku Solver
Connor Bennudriti
11/18/20
'''''''''''''''''

'''''''''''''''''''''''
Backtracking:

Loop through cells in grid
If a cell is empty:
    Find a number that does not break the row, column, or box
    If there is no number that does not break the row, column, or box:
        Go to previous cell and increase it to the next possible value then continue on
    Else:
        Put in the lowest number (that hasnt been tried already) into that box and continue on to the next cell
Else:
    Skip the cell (because that means that it is one of the given digits)
'''''''''''''''''''''''
unsolvedTestGrid = 
            [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]
            ]

solvedTestGrid = 
            [
            [4, 3, 5, 2, 6, 9, 7, 8, 1],
            [6, 8, 2, 5, 7, 1, 4, 9, 3],
            [1, 9, 7, 8, 3, 4, 5, 6, 2],
            [8, 2, 6, 1, 9, 5, 3, 4, 7],
            [3, 7, 4, 6, 8, 2, 9, 1, 5],
            [9, 5, 1, 7, 4, 3, 6, 2, 8],
            [5, 1, 9, 3, 2, 6, 8, 7, 4],
            [2, 4, 8, 9, 5, 7, 1, 3, 6],
            [7, 6, 3, 4, 1, 8, 2, 5, 0]    
            ]

grid = [
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0], 
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0]
        ]

#list that will hold the currently selected rules
rules = []

#master function that will call specific check functions if their rule set is selected
def check(grid):
    global rules
    if (normalSudokuRules in rules):
        checkNormalSudoku()
        
#function to check the board using normal sudoku rules
def checkNormalSudoku(grid):
    print("Boxes: ", checkBoxes(grid))
    print("Rows: ", checkRows(grid))
    print("Columns: ", checkColumns(grid))
#functions to check parts of normal sudoku
def checkBoxes(grid):
    pass

def checkRows(grid):
    for row in grid:
        rowList = []
        for cell in row:
            if cell not in rowList:
                rowList.append(cell) 
            else:
                return False
    return True

def checkColumns(grid):
    for i in range(9):
        columnList = []
        for j in range(9):
            if grid[j][i] not in columnList:
                columnList.append(grid[j][i])
            else:
                return False
    return True

checkNormalSudoku(solvedTestGrid)
