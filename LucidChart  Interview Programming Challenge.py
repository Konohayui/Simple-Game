import sys
import re

# https://stackoverflow.com/questions/39681758/longest-sub-sequence-in-a-matrix
# http://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
# https://www.geeksforgeeks.org/dynamic-programming/#concepts
    
def find_subsequence(grid, i, j, check_points, path):
    
    # if a cell has seen, return its path length
    if (i, j) in check_points:
        return check_points[i, j]
    
    directions = [[0, 1], [0, -1],   # up, down
                  [-1, 0], [1, 0],   # left, right
                  [-1, 1], [1, 1],   # up left, up right
                  [-1, -1], [1, -1]] # down left, down right
    
    length = 1
    M, N = len(grid), len(grid[1])
    
    for move in directions:
        # update direction
        new_i, new_j = move[0] + i, move[1] + j
        if 0 <= new_i < M and 0 <= new_j < N:
            # check condiction and check repeat cells
            if abs(grid[new_i][new_j] - grid[i][j]) > 3 and (new_i, new_j) not in path:
                # add valid cell into path
                path.append((new_i, new_j))
                length = max(length, 1 + find_subsequence(grid, new_i, new_j, check_points, path))
        
    check_points[i, j] = length
    return length
	
def longest_subsequence(grid):
    
    """
    Take a rectangular grid of numbers and find the length
    of the longest sequence.
    Return the length as an integer.
    """
    # TODO: Complete this function
    
    if grid != []:
        # initialize
        longest_length = 0
        check_points = {}
        
        # size of the given grid
        M, N = len(grid), len(grid[1])
        
        # start searching
        for i in range(M): 
            for j in range(N):
                # initialize path
                path = []
                longest_length = max(find_subsequence(grid, i, j, check_points, path), longest_length)
        return longest_length
    
    else:
        return 0

def main():
#    dims = [int(i) for i in sys.stdin.readline().split()]
#    num_rows, num_cols = dims
#    grid = [[int(i) for i in sys.stdin.readline().split()] for _ in range(num_rows)]
    
    grid = [[1, 6, 2], 
            [8, 3, 7],
            [4, 9, 5]]

    grid2 = [[8, 2, 4],
             [0, 6, 1], 
             [3, 7, 9]]

    grid3 = [[4, 2, 4],
             [0, 3, 1], 
             [3, 7, 9]]

    print(longest_subsequence(grid))
    print("Answer is 9")

    print(longest_subsequence(grid2))
    print("Answer is 8")

    print(longest_subsequence(grid3))
    print("Answer is 6")
    
#    res = longest_subsequence(grid2)
#    print(str(res) + "\n")

if __name__ == "__main__":
    main()

	
	
