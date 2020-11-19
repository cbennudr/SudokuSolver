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
import SudokuCheckFuncs

unsolvedTestGrid = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]]
solvedTestGrid = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9]]

def backtrack(grid, rules):
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            #if cell is empty
            if grid[row][cell] == 0:
                #try values until one is found that works
                i = 0
                cellCorrect = False
                while not cellCorrect and i < 9:#for i in range(1, 10):
                    i+=1
                    tempGrid = grid[:][:]
                    tempGrid[row][cell] = i
                    #if value works, put it in the grid and continue on
                    if SudokuCheckFuncs.check(tempGrid, rules):  ####################this is always false rn because 0s are being looked at too
                        cellCorrect = True
                #if no values work 
                if tempGrid[row][cell] == 0:
                    #go to previously gotten cell and increaese it  until value works
                    tempGrid[row][cell] = -1

            else:
                continue
    
    return tempGrid
rules = ["normalSudokuRules"]
print(backtrack(unsolvedTestGrid, rules))
