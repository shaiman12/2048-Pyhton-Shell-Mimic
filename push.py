def push_up (grid):
    """merge grid values upwards"""
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if grid[j-1][k]==0 and grid[j][k]!=0:
                    grid[j-1][k]=grid[j][k]
                    grid[j][k]=0
    for i in range(1,4):
        for j in range(4):
            if grid[i][j]==grid[i-1][j] and grid[i][j]!=0:
                grid [i-1][j] = 2*(grid[i][j])
                grid[i][j] = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if grid[j-1][k] == 0 and grid[j][k]!=0:           
                        grid[j-1][k] = grid[j][k]
                        grid[j][k] = 0                    
                        
def push_down (grid):
    """merge grid values downwards"""
    for i in range(4):
        for j in range(4):
            for k in range(4): 
                if j < 3:
                    if grid[j+1][k] == 0 and grid[j][k]!=0:
                        grid[j+1][k] = grid[j][k]
                        grid[j][k] = 0
    for i in range(3,-1,-1):
        for j in range(4): 
            if i < 3:
                if grid[i][j] == grid[i+1][j] and grid[i][j]!=0:
                    grid [i+1][j] = (2 * grid[i][j])
                    grid[i][j] = 0
                    
    for i in range(4):
        for j in range(4):
            for k in range(4): 
                if j < 3:
                    if grid[j+1][k] == 0 and grid[j][k]!=0:
                        grid[j+1][k] = grid[j][k]
                        grid[j][k] = 0    
                                            
def push_left (grid):                           
    """merge grid values left"""
    for i in range (1,4):                       
        for j in range(4):                      
            for k in range(1,4):                
                if grid[j][k-1] == 0 and grid[j][k]!=0:
                    grid[j][k-1] = grid[j][k]
                    grid[j][k] = 0
    for i in range(4):                           
        for j in range(3):                      
            if grid[i][j] == grid[i][j+1] and grid[i][j]!=0:
                grid[i][j] = grid[i][j]*2
                grid[i][j+1] = 0
    for i in range(1,4):                        
        for j in range(4):                      
            for k in range(1,4):                
                if grid[j][k-1] == 0 and grid[j][k]!=0:
                    grid[j][k-1] = grid[j][k]
                    grid[j][k] = 0            

def push_right (grid):
    for i in range(4):
            for j in range(4):
                for k in range(4): 
                    if k < 3:
                        if grid[j][k+1] == 0 and grid[j][k]!=0:
                            grid[j][k+1] = grid[j][k]
                            grid[j][k] = 0
                            
    for i in range(4):
        for j in range(3,-1,-1): 
            if j < 3:
                if grid[i][j] == grid[i][j+1] and grid[i][j]!=0:
                    grid [i][j+1] = (2 * grid[i][j])
                    grid[i][j] = 0
                        
    for i in range(4):
        for j in range(4):
            for k in range(4): 
                if k < 3:
                    if grid[j][k+1] == 0 and grid[j][k]!=0:
                        grid[j][k+1] = grid[j][k]
                        grid[j][k] = 0    