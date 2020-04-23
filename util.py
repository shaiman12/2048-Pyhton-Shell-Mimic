def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    for i in range(4):
        print("|",end="")
        for j in range(4):
            if grid[i][j] == 0:
                print("{0:<5}".format(" "), end="")   
            else:
                print("{0:<5}".format(grid[i][j]), end="")
        print("|")
    print("+--------------------+")
    
def check_lost (grid):
    """return True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""
    check1 = False
    check2 = False
    for i in range(4):
        for j in range(4):
            tester = grid[i][j]
            if j!=3:
                if tester == grid[i][j+1]:
                    check2 = True
            if i!=3:
                if tester == grid[i+1][j]:
                    check2 = True

            if grid[i][j] == 0:
                check1 = True
    if not check1 and not check2:
        return True
    else:
        return False

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    check = False
    for i in range(4):
        for j in range(4):
            if(grid[i][j]>=32):
                check = True
                break
    return check

def copy_grid (grid):
    """return a copy of the given grid"""
    from copy import deepcopy
    return deepcopy(grid)

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    tester = True
    for i in range(4):
        for j in range(4):
            if grid1[i][j]!=grid2[i][j]:
                tester = False
                break
    return tester
            