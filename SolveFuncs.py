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
import CheckFuncs

def backtrack(grid, rules):
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            #if cell is empty
            if grid[row][cell] == 0:
                #try values until one is found that works
                i = 0
                cellCorrect = False
                while not cellCorrect and i <= 9:
                    i+=1
                    #tempGrid = grid[:][:]
                    grid[row][cell] = i
                    #if value works, put it in the grid and continue on
                    if CheckFuncs.check(grid, rules):
                        print('cell gud: ', grid[row][cell])
                        cellCorrect = True
                #if no values work 
                if grid[row][cell] == 10:
                    #go to previously gotten cell and increaese it  until value works
                    grid[row][cell] = -1 

            else:
                continue
    
    return grid

class Solver:
    def __init__(self, grid, rules):
        self.grid = grid
        self.startingValIdxs = self.getStartingVals()
        self.curRowIdx = 0
        self.curColIdx = 0
        self.currentVal = self.grid[self.curRowIdx][self.curColIdx]
        
    def solve(self):
        self.solved = False
        while not self.solved:
            if self.getCurrentVal() == 0:
                #try values until one is found that works
                i = 0
                cellCorrect = False
                while not cellCorrect and i <= 9:
                    i+=1
                    self.grid[self.curRowIdx][self.curColIdx] = i
                    
                    #if value works, put it in the grid and continue on
                    if CheckFuncs.check(self.grid, rules):
                        cellCorrect = True
                #if no values work 
                if self.getCurrentVal() == 10:
                    print(self.getCurrentVal())
                    self.grid[self.curRowIdx][self.curColIdx] = 0
                    #go to previously gotten cell and increaese it  until value works
                    #self.getLastSolvedCell()
                    
                self.advance()
            else:
                self.advance()
    
        return self.grid 
    
    def incrementVal(self):
        self.grid[self.curRowIdx][self.curColIdx] += 1
    def getLastSolvedCell(self):
        onPrevCell = False
        while True:
            if self.curColIdx <= 0:
                self.curRowIdx -= 1
                self.curColIdx = 8
            else:
                self.curColIdx -= 1
            if (self.curRowIdx, self.curColIdx) not in self.startingValIdxs:
                self.currentVal = self.grid[self.curRowIdx][self.curColIdx]
                break
        return       
    def advance(self):
        #if self.curRowIdx <= 8 and self.curColIdx <= 8:
        if self.curColIdx >= 8:
            self.curRowIdx += 1
            self.curColIdx = 0
        else:
            self.curColIdx += 1
            
        if self.curRowIdx == 9:
            self.solved = True
            return
    def getCurrentVal(self):
        return self.grid[self.curRowIdx][self.curColIdx]
    def getStartingVals(self):
        startingValIdxs = []
        for row in range(len(self.grid)):
            for cell in range(len(self.grid[row])):
                if self.grid[row][cell] != 0:
                    startingValIdxs.append((row, cell))
        return startingValIdxs
    

rules = ["normalSudokuRules"]
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

s = Solver(unsolvedTestGrid, rules)
for l in s.solve():
    print(l)
# s.curRowIdx = 0
# s.curColIdx = 7
# print(s.curRowIdx, s.curColIdx)
# s.getLastSolvedCell()
# print(s.currentVal)
# print(s.curRowIdx, s.curColIdx)
# s.getLastSolvedCell()
# print(s.currentVal)
# print(s.curRowIdx, s.curColIdx)
