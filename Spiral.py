#  File: Spiral.py

#  Description: Use two-dimentional lists to construct a spiral

#  Student's Name: Jadesola Jaiyesimi

#  Student's UT EID: jaj3847

#  Course Name: CS 313E

#  Unique Number: 50295

#  Date Created: February 14th, 2020

#  Date Last Modified: February 17th, 2020


#  Input: dim is a positive odd integer
#  Output: function returns a 2-D list of integers arranged in a spiral
import numpy as np

def create_spiral (dim):
    x_direction = [0, 1, 0, -1] #turn directions in spiral formation
    y_direction = [1, 0, -1, 0] 
    row, col, counter = 0, dim, 1
    grid = [[0 for i in range(dim)] for j in range(dim)] #create grid
    for i in range(dim + (dim + 1)):
            for j in range((dim + (dim - i)) // 2):
                    row += x_direction[i % 4] #choose direction
                    col -= y_direction[i % 4]
                    grid[row][col] = dim**2 + 1 - counter #print value in grid
                    counter += 1 #keeps count of number in array
    return grid
#  Input: grid a 2-D list containing a spiral of numbers
#         val is a number withing the range of numbers in
#         the grid
#  Output: sub-grid surrounding the parameter val in the grid
#          sub-grid could be 1-D or 2-D list
def sub_grid (grid, val):
    grid = np.array(grid)
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] == val:
                if x == 0 and y == 0:  #print 2x2 list CORNORS
                    return (grid [0:x+2 , 0:y+2])
                elif x == 0 and y != 0:
                    return(grid [x:x+2 ,y-1:y+2])
                elif y== 0 and x!=0:
                    return(grid [x-1:x+2 ,y:y+2])
                elif y == range(len(grid)) and x == range(len(grid)):
                    return (grid [x-2:x ,y-2:y])
                elif x - 1 == '':       #print 3x2 SIDE
                    return(grid [x:x+2 ,y-1:y+2])
                elif y - 1 == '':
                    return(grid [x+1:x+2 ,y:y+2])
                elif x + 1 == '':
                    return (grid [x:x+2 ,y-1:y+2])
                elif y + 1 == '':
                    new_grid = (grid [x-1:x+1 ,y-1:y])
                    return str(new_grid)
                else : #print 3x3 list NORMAL
                    return (grid [x-1:x+2 , y-1:y+2])
    
def main():
    dimension = int(input('Enter dimension: '))  # prompt user to enter dimension of grid
    if dimension%2 == 0:
        dimension += 1 
    spiral = int(input('Enter number in spiral: '))  # prompt user to enter value in grid
    if spiral > dimension**2:
        print('Number not in Range')
    else:
        spiral_grid = create_spiral(dimension)
        print(str(sub_grid(spiral_grid,spiral))) # print subgrid surrounding the value

if __name__ == "__main__":
  main()
