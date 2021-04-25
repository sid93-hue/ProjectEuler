"""Problem 31"""

def ways(n):
    """Returns number of ways total can be achieved using given coin denominations (dynamic programming) """
    coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]
    
    """ result array is 2D. First index for available coins and second index for total"""
    result = []
    
    """With 0 coins"""
    coloumn_array = []
    for i in range(0, n+1):
        coloumn_array.append(0)
    result.append(coloumn_array)
    
    """With 1 coins"""
    coloumn_array = []
    for i in range(0, n+1):
        coloumn_array.append(1)
    result.append(coloumn_array)

    """With remaining coins"""
    for row in range(2, len(coins)):
        coloumn_array = []
        for coloumn in range(0, n+1):
            if coloumn == 0 or coloumn == 1: 
                sum = 1
            else :
                new_coins = coloumn // coins[row]
                sum = result[row - 1][coloumn]
                for num_new_coins in range(1, new_coins + 1):
                    sum += result[row - 1][coloumn - (coins[row]* num_new_coins)]
            coloumn_array.append(sum)
        result.append(coloumn_array)
    
    return result[len(coins) - 1][n]

n = 200
print(f"ways({n}) = {ways(n)}")
