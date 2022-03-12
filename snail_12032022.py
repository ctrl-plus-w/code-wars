"""
Get the ring from the given interval in the matrix
"""
def get_ring(snail_map, mini, maxi):
    if mini == maxi:
        return [snail_map[mini][maxi]]
    
    # Reverse the array
    turned_snail_map = list(zip(*snail_map))
    
    """    
    1. Getting the top row (in the interval)
        a. Takes the first row in the interval
        b. Truncate the array to fit the interval (+1 to maxi bc goes to n-1)    
        
    2. Get the last column (in the interval) without it first and last element
        a. Get the last column of the turned matrix
        b. Truncate the array to fit the interval and remove one more element on each side of the array
        
    3. Get the last row (in the interval) reversed
        -> Same as Step 1 but for the last column of the interval
        c. Reverse the array
        
    4. Get the first column (in the interval) without the first and last element and reversed
        -> Same a Step 2 but for the first column of the interval
        c. Reverse the array
    """
    return [
        *snail_map[mini][mini:maxi+1],
        *turned_snail_map[maxi][mini+1:maxi],
        *snail_map[maxi][mini:maxi+1][::-1],
        *turned_snail_map[mini][mini+1:maxi][::-1],
    ]

"""
Snail function

see: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
"""
def snail(snail_map):
    if snail_map == [[]]:
        return []
    
    result = []
    
    mini = 0
    maxi = len(snail_map)-1
    
    while maxi-mini>=0:
        result += get_ring(snail_map, mini, maxi)
        mini += 1
        maxi -= 1
        
    return result