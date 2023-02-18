# https://leetcode.com/problems/number-of-islands/?envType=study-plan&id=algorithm-ii
# 200. Number of Islands
# Medium
# 18.2K
# 411
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# go line by line, item by item
# if marked susha -> check left and up  -> if susha create link to other susha .. if new link -1 susha
# if susha -> check left and up -> mark as new susha +1
# check all links -> count number of islands 
class State:
    def __init__(self) -> None:
        self.links = set()
        self.islands = 0
        self.r = 0
        self.c = 0

def calc_soseds(r, c, grid, state):
    sosed = 0
    sosedup = 0

    if c > 0:
        sosed = int(grid[r][c-1])
    if r > 0:
        sosedup = int(grid[r-1][c])
    
    #print ("calc", sosed, sosedup)
    # sosed ne mojet bit' ne pomarkan 
    if sosed == 1:
        # or sosedup == 1:
        print("BUG!")
        exit(-1)

    if sosed == 0:
        return sosedup

    if sosedup == 0:
        return sosed 

    if sosed != sosedup:
        # link detected 
        link_detected(sosed, sosedup, state)

    return sosed

def link_detected(sosed, item, state):
    if (sosed, item) not in state.links:
        state.islands = state.islands - 1
        state.links.add((sosed, item))
        state.links.add((item, sosed))
        print ("link detected r=%d, c=%d isl=%d, so=%d, it=%d" % (state.r, state.c, state.islands, sosed, item))

def main(grid):
    raws = len(grid)
    if raws == 0:
        return 0
    columns = len(grid[0])

    state = State()
    susha_mark = 2
    
    for r in range (0, raws):
        for c in range (0, columns):
            state.r = r
            state.c = c

            item = int(grid[r][c])
            if item == 0:
                continue
            else:
                # susha detected 
                sosed = calc_soseds(r, c, grid, state)
                #print (r, c, sosed)

                if sosed == 0:
                    if item == 1:
                        # new susha

                        grid[r][c] = susha_mark
                        susha_mark = susha_mark + 1
                        state.islands = state.islands + 1
                        print ("new r=%d,c=%d,isl=%d" % (r, c, state.islands))
                else:
                    if item == 1:
                        grid[r][c] = sosed
                    else:
                        # Detected link of 2 islands 
                        link_detected(sosed, item, state)

    return state.islands

if __name__ == "__main__":
    # grid = [
    #     ["1","1","1","1","0"],
    #     ["1","1","0","1","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","0","0","0"]
    # ]

    # grid = [
    #     ["1","1","0","0","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","1","0","0"],
    #     ["0","0","0","1","1"]
    # ]

    grid = [
        # 0   1   2   3   4   5   6   7   8   9
        ["1","1","1","1","1","0","1","1","1","1"], # 0
        ["0","1","1","0","1","1","1","0","1","1"], # 1
        ["1","0","1","0","1","1","0","1","0","1"], # 2
        ["1","0","1","1","0","1","1","1","1","1"], # 3
        ["1","1","0","0","1","1","1","1","1","1"], # 4
        ["1","1","0","1","1","1","1","1","1","1"], # 5
        ["1","1","1","1","1","1","1","1","0","1"], # 6
        ["0","1","1","0","1","1","1","1","1","0"], # 7
        ["1","1","0","1","1","0","1","1","1","1"], # 8
        ["0","1","1","1","1","1","0","1","1","1"]  # 9
    ]
    print (main(grid))