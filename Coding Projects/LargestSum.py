# Main Function below

def Largest_Sum(triangle_list):
    return helper_Largest_Sum(i=0, j=0, cache={}, num_list=triangle_list)

def helper_Largest_Sum(i, j, cache, num_list):
    if i == len(num_list) - 1: # reaches the base of the triangle
        return num_list[i][j]
    if (i, j) in cache:
        return cache[(i, j)] # precomputated result
    
    down_left = helper_Largest_Sum(i+1, j, cache, num_list)
    down_right = helper_Largest_Sum(i+1, j+1, cache, num_list)
    
    cache[(i, j)] = num_list[i][j] + max(down_left, down_right)
    
    return cache[(i, j)]

if __name__ == "__main__":
    triangle = [
    [2],
    [4, 1],
    [1, 2, 7],
    [8, 5, 9, 3]
    ]
    
    print(Largest_Sum(triangle))