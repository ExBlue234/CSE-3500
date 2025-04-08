# Main Function below

def Largest_Sum(triangle_list:list[list[int]]): # Expects a triangle like format below
    return helper_Largest_Sum(i=0, j=0, cache={}, num_list=triangle_list)

def helper_Largest_Sum(i, j, cache, num_list):
    if i == len(num_list) - 1: # Reaches the base of the triangle
        return num_list[i][j] # Returns the value given current position
    if (i, j) in cache:
        return cache[(i, j)] # Precomputated result
    
    down_left = helper_Largest_Sum(i+1, j, cache, num_list) # Left recursion
    down_right = helper_Largest_Sum(i+1, j+1, cache, num_list) # Right recursion
    
    cache[(i, j)] = num_list[i][j] + max(down_left, down_right) # Goes down the adjacent path that has the greatest value
    
    return cache[(i, j)] # Returns current result

if __name__ == "__main__":
    triangle = [
    [2],
    [4, 1],
    [1, 2, 7],
    [8, 5, 9, 3]
    ]
    # Starting from 2, the top of this triangle
    
    print(Largest_Sum(triangle)) # 19 was the largest value produced after traversing adjacent paths (left or right) given any current location