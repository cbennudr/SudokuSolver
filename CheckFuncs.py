#master function that will call specific check functions if their rule set is selected
def check(grid, rules):
    if ("normalSudokuRules" in rules):
        checkNormalSudoku(grid) 

#function to check the board using normal sudoku rules
def checkNormalSudoku(grid):
    '''print("Boxes: ", checkBoxes(grid))
    print("Rows: ", checkRows(grid))
    print("Columns: ", checkColumns(grid))'''
    if checkBoxes(grid) and checkRows(grid) and checkColumns(grid):
        return True
    else:
        return False

#functions to check parts of normal sudoku
def checkBoxes(grid):
    boxList = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            boxList = [row[i:i+3] for row in grid[j:j+3]]
            vals = []
            for l in boxList:
                for val in l:
                    vals.append(val)
            
            if list(set(vals)) == sorted(vals):
                continue
            else:
                return False
    return True

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
