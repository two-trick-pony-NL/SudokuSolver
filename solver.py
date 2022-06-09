#Representation of the puzzle to solve by pressing shift+enter the program will know that grid is the puzzle
"""
# Sudoku Solver! 🤓
This is my Sudoku puzzle solver. A simple script that solves sudoku puzzles in the blink of an eye. Inspired by this [video](https://www.youtube.com/watch?v=G_UYXzGuqvM)

#### How does it work:
0. Change the grid in the next section for the numbers in your puzzle (all the way down is an empty template)
1. Hit shift + enter to execute a block of code
2. Go block by block to get your answer
3. Each line tells you what the script does text after a # is a comment

Let's start by defining the puzzle: 
"""


grid = [[0,0,0,0,1,5,0,7,0],
        [0,0,0,0,0,0,5,8,1],
        [3,0,0,0,0,7,0,6,2],
        [0,9,0,0,0,0,0,5,0],
        [0,0,0,1,0,0,0,0,0],
        [0,7,6,0,0,0,0,1,0],
        [7,0,0,0,5,0,4,0,0],
        [0,4,5,3,0,0,7,0,8],
        [2,0,0,0,9,0,0,0,0]]


import numpy
print("This is the puzzle I attemt to solve: \n")
print(numpy.matrix(grid)) # let's print the sudoku puzzle using Numpy: 
print("\n")

"""
## Checking algorithm
Next up is a algorithm that checks whether a number in a certain place is allowed. 
It returns true if a number is allowed in a specific place, and False if it is not allowed. 
"""

def possible(y,x,n) : # defines a function  called possible, that takes a x and y coordinate and a number N that you'd like to check 
    global grid # look at the grid
    for i in range(0,9) : # try for all the numbers numbers 1 through 9
        if grid[y][i] == n : # If the number you are trying, exists in the y column then the number is False
            return False
    for i in range(0,9) : # try for all the numbers numbers 1 through 9
        if grid[i][x] == n : # If the number you are trying, exists in the x column then the number is False
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range (0,3) : #If the number you are trying exists in the square then the number is False
        for j in range(0,3) :
            if grid[y0+i][x0+j] == n :
                return False
    return True # if the number you are trying, is not in the row, or in the column and not in the square that number is allowed 

"""
## Let's see if that works! 🤖
The next cell is a helper function that allows us to test a position that we'd like to validate. It ensures that the algorithm we just wrote works properly. Simply call the function `Possible(y,x,n)` that we just defined and put the following information between the brackets: 
- first digit is the Y position of the square you want to try
- second digit is the X position of the square you want to try
- third digit is the number you would like to test and see if it is allowed
- Seperate with a comma 
- Press shift + enter to execute


As an example: try `possible(4,4,5)` if you want to try 5, in the center of your puzzle (row 5, column 5)
indexes in python start with 0 instead of 1 so it is always one less then you expect. 
"""
possible(0,2,9) 

"""
## The Solver 🧩
The next block defines the  solver function. It looks at the puzzle and will go over eacht block, checks if there is a valid number (using the checking algorithm we just wrote) and will replace the numbers in the puzzle as it finds correct answers. if it is done it will print the puzzle, using the Numpy tool we imported earlier. 
"""
# Writing the solver that recursively goes trough all options
# the solver replaces the options if a number is valid
def solve() : # defines a function called solve
    global grid # look at the puzzle 
    for y in range(9) : #go over all 9 rows
        for x in range(9) : #go over all 9 columns
            if grid[y][x]==0 : #if cell is 0 (empty)
                for n in range(1,10) : # Try the numbers 1-9
                    if possible(y,x,n) : # call the check algorithm we wrote before and try the X,Y coordinate with a number between 1-9
                        grid[y][x] = n #fill in the number in our puzzle that was found if the check algorithm returns true
                        solve() #continue with the next square
                        grid[y][x] = 0 #fill in a zero if the check algorithm returns false 
                return
    print("Here is the solution: \n")                
    print(numpy.matrix(grid)) # print with the numpy tool after we're done
    input("Hit enter to see if there is an alternative solutions available")
    

solve()