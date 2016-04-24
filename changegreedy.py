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

#main
'''
V = [1, 2, 4, 8]
A = 15
V2 = [1, 3, 7, 12]
A2 = 29
coins = changegreedy(V2, A2)

C = coins[0]
A = coins[1]

print("Algorithm changegreedy")
print(C)
print(A)
'''

# file i/o
# references:
# http://stackoverflow.com/questions/1657299/how-do-i-read-two-lines-from-a-file-at-a-time-using-python
# http://stackoverflow.com/questions/3411771/multiple-character-replace-with-python
# http://forums.devshed.com/python-programming-11/convert-string-list-71857.html
# http://stackoverflow.com/questions/19334374/python-converting-a-string-of-numbers-into-a-list-of-int
# http://stackoverflow.com/questions/1038824/how-do-i-remove-a-substring-from-the-end-of-a-string-in-python

# set up output file name
inputFile = "Coin1.txt"
if inputFile.endswith(".txt"):
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
        A = int(A)
    if not A: break

    # append V, A pair as tuple
    sets.append((V, A))

with open(outputFile, "a") as f:
    f.write("Algorithm changegreedy:\n")

print("\nFile contents: ", sets)
print("\n")
print("Algorithm changegreedy:")
for set in sets:
    V = set[0]
    A = set[1]
    coins = changegreedy(V, A)
    C = coins[0]
    m = coins[1]

    with open(outputFile, "a") as f:
        f.write("{0}\n{1}\n".format(C, m))

    print(C)
    print(m)