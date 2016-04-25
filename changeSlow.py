



def changeslow (coinValues, changeAmount):

    ###########################################################################################
    #
    #   This function finds all possible coin combinations using brute force w/ recursion
    #
    #   PARAMETERS: coins(list) stores the current working solution, initially empty
    #               coinList(list) contains the coin denominations
    #               curCoin(int) variable to help with finding solutions
    #               total(int) - running total of current solution
    #               amount(int) - original change amount we are to find
    #               solutions(list) - a list that stores all valid solutions
    #
    #   Once a valid solution is found, it is added to the list of possible solutions
    #
    ###########################################################################################
    def changeHelper(coins, coinList, curCoin, total, amount, solutions):
        # A valid solution, add to solutions list, base case 1
        if total == amount:
            result = storeResult(coins, coinList)
            solutions.append(list(result))
        # not a valid solution, base case 2
        if total > amount:
            return

        for coin in coinList:
            if coin >= curCoin:
                # Copy the coins list, then add the current coin.
                copy = coins[:]
                copy.append(coin)
                changeHelper(copy, coinList, coin, total + coin, amount, solutions)

    ############################################################################################
    #
    #   this function formats the results of the valid solution
    #   PARAMETERS: coins (list) - individual denominations that make up a valid solution
    #               coinList (list) - coin denominations
    #
    #   RETURNS:    formatted list that has the quantity of the coin stored in the same index as that
    #               denomination in coinList
    ###########################################################################################
    def storeResult(coins, coinList):
        # diplays the quantity of each type of coin, matching the index of the coin input list
        coinTally = [0]*len(coinList)
        for coin in coinList:
            coinTally[coinList.index(coin)] = coins.count(coin)
        return coinTally


    # stores all valid solutions
    listOfSolutions = []

    # empty list to help with initial function call
    result = []

    # call helper funciton
    changeHelper(result, coinValues, 0, 0, changeAmount, listOfSolutions)

    # After all solutions found, find the optimal (fewest coins) solution
    fewestCoins = float("inf")
    indexOfFewest = -1
    for solution in listOfSolutions:
        if (sum(solution) < fewestCoins):
            fewestCoins = sum(solution)
            indexOfFewest = listOfSolutions.index(solution)

    return fewestCoins, listOfSolutions[indexOfFewest]









coins = [1,3,4,5]
amount = 4
print(changeslow(coins, amount))


#######################################################################################################
#
#   changeSlowHelper (list, list, list)
#
#   PARAMETERS: list of coin denominations
#               1 element list for change amount (list is used because it is a mutable object)
#               list to store the number of coins used
#
#   OUTPUT:     change[0] will be equal to 0
#               coinsUsed[] will store the quantities of each coin type used
#                   (for ex. if coinList=[1,5,10] and 7x 10 coins, 3x 5 coins, and 2x 1 coins were used
#                       coinsUsed would be [2,3,7]  )
#
#####################################################@@@@##############################################






