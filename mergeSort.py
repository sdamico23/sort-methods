#LAB 13
#Due Date: 11/18/2018, 11:59PM
########################################
#                                      
# Name:Collin Michaels
# Collaboration Statement:             
#
########################################

def merge(list1, list2):
	#write your code here
    newList = []
    z = 0
    y = 0
    while z < len(list1) and y < len(list2): #loop through lists and append them into newlist according to value
        if list1[z] < list2[y]:
            newList.append(list1[z])
            z += 1
        else:
            newList.append(list2[y])
            y += 1
    newList += list1[z:]
    newList += list2[y:]
    return newList

def mergeSort(numList):
	#write your code here
    if len(numList) <= 1:
        return numList
    midpt = len(numList)//2
    lefthalf = mergeSort(numList[:midpt])
    rightHalf = mergeSort(numList[midpt:])
    return merge(lefthalf,rightHalf)
