# Main function below

def Unique_coin_combos(list_coin:list[int]): # Expects a list of coins
    return helper_function_coin(sums={0}, visited=set(), num_list=list_coin)

def helper_function_coin(sums, visited, num_list):
    
    for coin in num_list: # Iterates through each coin
        for s in sums: # Iterates through sums
            visited.add(s + coin) # Given current s, add the current coin, creating a sum, only saves unique values
        sums.update(visited) # After all s have been exhausted, update sums
        
    sums.remove(0) # removes 0 as an temp value
    
    return sums # Returns all of the unique sum values coins from list_coin
        


if __name__ == "__main__":
    list_coin = [2, 4, 7]
    
    print(Unique_coin_combos(list_coin)) # Produces a set, containing {2, 4, 6, 7, 9, 11, 13}