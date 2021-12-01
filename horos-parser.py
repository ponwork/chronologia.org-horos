# Script will parse the input OTVET.TXT file and find the possible solutions.
# 
# author: Yuri Ponomarev
# Github: https://github.com/ponwork/

import re
import linecache

# Working file's filename
fileName = 'OTVET.TXT'

# Open a file with the results
sourceFile = open(fileName) 

# String to find a solutions
solutionDelimiter = ' ----------------------------------------\n'

# String to find a solutions without Planets' shifts
sampleOrder = ' ORDER OF PLANETS IS THE SAME ++++++++++++++++++\n'

# Counter for the number of solutions without Planets' shifts
counterOrder = 0

# Total results
totalRes = 0

# Dictionary for the results (line number and distance)
resultsDic = {}

# Enumerating the file
enum = enumerate(sourceFile, start=1)

# Finding the results matching for no Planets shift criteria
for pos, line in enum:

    # check for the line that points solutions delimiter
    if line == solutionDelimiter:

        # Count delimiters
        totalRes+=1

    # check for the line that points to no Planet's shift solution
    if line == sampleOrder:

        # Get the string with the matched result
        resultString = linecache.getline(fileName, pos+2)

        # Get the value of the Distance
        resultValue = resultString[38:-4]

        # Add a string number with value to the dictionary
        resultsDic[pos+2] = resultValue

# Divide all the delimiters found by 2 to find the total number of solutions
totalRes = int(totalRes/2)

# Get the best solution (minimum number of the distance)
minDistanceLine = min(resultsDic, key=resultsDic.get)

# Print the statistics
print(f'\nTotal number of the solutions in the file: {totalRes}')
print(f'Total number of the solutions without Planets shift: {len(resultsDic)}\n')

# Print the result
print(f'Best solution with minimum distance:')
for line in range (minDistanceLine-9, minDistanceLine+2, 1):
    print(f'{linecache.getline(fileName, line)}', end='')