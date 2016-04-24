import os

################################################################
# changegreedy
# Greedy algorithm for coin change problem
# Naive since it may not be optimal
# Input: list V of coin values, amount A
# Output: returns list C of number of coins per value and
#   min number of coins to make amount
################################################################

def changegreedy(V, A):
    length = len(V)     # num of coin types
    C = [0] * length    # initialize return array, all counts are 0
    m = 0               # initialize coin count
    change = 0          # current change made with coins
    i = length - 1      # index of lists. V[i] corresponds to C[i]
                        # start with largest coin value
    while change < A:
        if(V[i] + change <= A):     # get largest possible coin value
            change += V[i]          # update change made
            C[i] += 1               # update coin count for i
            m += 1                  # update coin count
        else:
            i -= 1                  # move to next lower value coin

    return C, m

################################################################
# changedp
# Dynamic algorithm to determine coins needed for change
# Always optimal, every time.
# Input: list V of coin values, amount A
# Output: returns list C of number of coins per value and
#   min number of coins to make amount
################################################################

def changedp(V, A):

    C = []                          # array of min coins to reach change
    for i in range(len(V)):
        C.append(0)
    m = 0                           # min coins for change

    T = []                          # T table of values 0 - change
    D = []                          # V reference of coin denomination used for value
    for i in range(0, A + 1):
        T.append(float("inf"))      # initialize with inf, since unknown ceiling of coins for i change
        D.append(-1)                # initialize with -1, since coin index starts at 0
    T[0] = 0                        # no coins can equal 0 change

    for j in range(len(V)):
        for i in range(1, len(T)):
            if i >= V[j]:       # ensure that the change is not less than the denomination
                T[i] = min(T[i], T[i - V[j]] + 1)      # current combo or 1 coin of value j + num coins to equal i-j
                D[i] = j

    m = T[A]

    for i in range(T[A]):       # iterate through however many coins needed for change
        C[D[A]] += 1            # increment based on recorded denom at change index
        A -= V[D[A]]            # reduce change by that denomination

    return C, m

################################################################
# changeslow
# Divide and Conquer algorithm to determine coins needed for change
# Input: list of coin denominations, amount of change
# Output: returns list of coins used
#         number of coins to make amount
#
#           Uses a helper function
################################################################


def changeslow (coinValues, changeAmount):

    coinsUsed = [0]*len(coinValues)               # initializes the return list to 0 of all coin denominations
    change=[]                                     # store changeAmount in a list so that it is a mutable object
    change.append(changeAmount)
    changeSlowHelper(coinValues, change, coinsUsed)         # call helper function
    return coinsUsed, sum(coinsUsed)

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

################################################################
# input_output
# Iterates through functions to find differing results
# Input: input filename, names of functions
# Output: file with array of coins and min found.
################################################################

# file i/o
# references:
# http://stackoverflow.com/questions/1657299/how-do-i-read-two-lines-from-a-file-at-a-time-using-python
# http://stackoverflow.com/questions/3411771/multiple-character-replace-with-python
# http://forums.devshed.com/python-programming-11/convert-string-list-71857.html
# http://stackoverflow.com/questions/19334374/python-converting-a-string-of-numbers-into-a-list-of-int
# http://stackoverflow.com/questions/1038824/how-do-i-remove-a-substring-from-the-end-of-a-string-in-python

def input_output(inputFile, functions):
    # set up output file name
    if  inputFile.endswith(".txt"):
        outputFile = inputFile[:-4]
        outputFile += "change.txt"
    else:
        inputFile += ".txt"
        outputFile = inputFile[:-4]
        outputFile += "change.txt"

    # Attempts to delete the results file if it already exists
    # because when running the program multiple times
    # it will append to the file instead of producing a clean
    # set of results each time
    try:
        os.remove(outputFile)
    except OSError:
        pass

    sets = []
    f = open(inputFile, "r")
    while True:
        V = f.readline()
        if V:
            # remove erroneous chars, separate values with comma, convert string to int
            V = [int(val) for val in V.replace('[', '').replace(']', '').replace(' ', '').split(',') if val not in '\n']

        A = f.readline()
        if A:
            # remove newline char, convert string to int
            A = A.replace('\n', '')
            try:
                A = int(A)
            except ValueError:
                pass
        if not A: break

        # append V, A pair as tuple
        sets.append((V, A))

    for function in sorted(functions.items(), key=lambda e: e[1][1]):
        with open(outputFile, "a") as f:
            f.write("Algorithm " + function[0] + ":\n")

        print(function[0])

        for set in sets:
            V = set[0]
            A = set[1]
            coins = function[1][0](V, A)
            C = coins[0]
            m = coins[1]

            with open(outputFile, "a") as f:
                f.write("{0}\n{1}\n".format(C, m))


            print(C)
            print(m)

# main

# inputFilename = "Coin1.txt"
functions = {
    'Divide and Conquer': [changeslow, 1],
    'Greedy': [changegreedy, 2],
    'Dynamic': [changedp, 3]}

prompt = input("Please enter the input filename: ")       # prompt for user input filename
inputFilename = prompt
input_output(inputFilename, functions)
