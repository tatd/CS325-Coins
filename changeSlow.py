coins = [1,5,10,15]
amount = 34


def changeslow (coinValues, changeAmount):

    coinsUsed = [0]*len(coinValues)               # initializes the return list to 0 of all coin denominations
    change=[]                                     # store changeAmount in a list so that it is a mutable object
    change.append(changeAmount)
    changeSlowHelper(coinValues, change, coinsUsed)         # call helper function



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


def changeSlowHelper(coinList, change, coinsUsed):
    for coin in reversed(coinList):
        if change[0] <= 0:
            return coinsUsed
        elif change[0]-coin >= 0:                               # if change > coin denomination
            result = change[0]-coin                             # subtract that denomination from the change amount
            change[0] = result                                  # store value back in list
            coinsUsed[coinList.index(coin)] += 1                # add 1 to the denomination of coin used
            changeSlowHelper(coinList, change, coinsUsed)       # recursively call with smaller change amount

    


changeslow(coins, amount)