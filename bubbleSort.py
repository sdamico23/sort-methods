#LAB 14
#Due Date: 04/05/2019, 11:59PM
########################################
#                                      
# Name: Steve D'Amico
# Collaboration Statement: I worked alone.            
#
########################################


def bubbleSort(numList):
    '''
        Takes a list and returns 2 values
        1st returned value: a dictionary with the state of the list after each complete pass of bubble sort
        2nd returned value: the sorted list

        >>> bubbleSort([9,3,5,4,1,67,78])
        ({1: [3, 5, 4, 1, 9, 67, 78], 2: [3, 4, 1, 5, 9, 67, 78], 3: [3, 1, 4, 5, 9, 67, 78], 4: [1, 3, 4, 5, 9, 67, 78], 5: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
    '''
    # Your code starts here
    n = len(numList)
    dic = dict()
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if numList[j] > numList[j+1]:
                numList[j], numList[j+1] = numList[j+1], numList[j]
        dic[i+1] = numList[:]
    return dic, numList

